#Importing libraries
import pandas as pd
from tqdm import tqdm
import sqlite3
import pickle
from config import Config

def get_users_by_song_id(data, song_id):
    return  set(data['user_id'][data['song_id']==song_id])

def run():
   # making connections
   print("Loading data from databsae...")
   conn = sqlite3.connect(Config.database)
   cur = conn.cursor()
   query = cur.execute("Select * from app_data;")
   app_data = cur.fetchall()
   data = pd.DataFrame(app_data)
   data.rename(columns={0:"user_id", 1:'song_id', 2:'listen_count'}, inplace=True)
   all_songs = list(data["song_id"].unique())
   
   # Creating Co-occurance matrix
   print("Creating Co-occurance matrix...")
   all_users_of_song = dict()
   for song_id in all_songs:
      all_users_of_song[song_id] = get_users_by_song_id(data, song_id)
              
   print("Saving File...")
   pickle.dump(all_users_of_song, open(Config.co_occurance_path, "wb"))
    
