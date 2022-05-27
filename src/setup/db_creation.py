# importing libraries
import numpy as np
import pandas as pd
import os
import sqlite3
from config import Config

# loading data
def run():
    print("Loading Data...")
    path = Config.dataset_path
    data1 = pd.read_csv(os.path.join(path,"song_data.csv"))
    data1.drop_duplicates(inplace=True)

    data2 = pd.read_csv(os.path.join(path,"app_data.csv"))
    data2.drop_duplicates(inplace=True)

    # addition data
    user_count = data2.groupby(["song_id"]).agg({'user_id':'count'}).reset_index()
    user_count.sort_values(by="user_id", ascending=False)

    song_data = pd.merge(data1, user_count, on="song_id")
    song_data.rename(columns=Config.columns_rename, inplace=True)
    
    # creating connection
    print("Creating Database...")
    conn = sqlite3.connect(Config.database)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS song_data (song_id text, title text, release text, artist text, 
                year integer, user_count integer);''')
    song_data.to_sql('song_data', conn, if_exists='replace', index = False)

    cur.execute('''CREATE TABLE IF NOT EXISTS app_data (user_id text, song_id text, listen_count integer);''')
    conn.commit()
    data2.to_sql('app_data', conn, if_exists='replace', index = False)
