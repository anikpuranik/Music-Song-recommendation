import pandas as pd
from src.app.db import cursor, queries
from src.app.item_similarity import recommend_song
from config import Config

# loading the data
def load_list():
    trending_songs = get_trending_songs()
    top_artists = get_top_artists()
    top_albums = get_top_albums()    
    return Config.charts_list, top_artists, top_albums, trending_songs

def get_trending_songs():
    query = queries.get_trending_songs_query()
    cursor.execute(query)
    top_songs = cursor.fetchall()
    top_songs = format_table(top_songs)
    return top_songs

def get_top_artists():
    query = queries.get_top_artist_query()
    cursor.execute(query)
    top_artists = cursor.fetchall()
    top_artists = format_series(top_artists)
    return top_artists

def get_top_albums():
    query = queries.get_top_album_query()
    cursor.execute(query)
    top_songs = cursor.fetchall()
    top_songs = format_series(top_songs)
    return top_songs

def get_top_songs_by_chart(chart):
    year1, year2 = Config.decade_list[chart]
    query = queries.get_top_songs_by_year_query(year1, year2)
    cursor.execute(query)
    top_songs = cursor.fetchall()
    top_songs = format_table(top_songs)
    return top_songs

def get_top_songs_by_artist(artist):
    query = queries.get_top_songs_by_artist_query(artist)
    cursor.execute(query)
    top_songs = cursor.fetchall()
    top_songs = format_table(top_songs)
    return top_songs

def get_top_songs_by_album(album):
    query = queries.get_top_songs_by_album_query(album)
    cursor.execute(query)
    top_songs = cursor.fetchall()
    top_songs = format_table(top_songs)
    return top_songs

def get_similar_song(title):
    query = queries.get_song_id_by_title_query(title)
    cursor.execute(query)
    song_id = cursor.fetchone()
    
    top_song_ids = recommend_song(*song_id)
    
    query = queries.get_title_by_song_id_query(top_song_ids)
    cursor.execute(query)
    query_result = cursor.fetchall()
    top_songs = format_series(query_result)
    
    return top_songs

def format_table(query_result):
    lis = []
    for i in query_result:
        lis.append([*i])
    return lis

def format_series(query_result):
    lis = []
    for i in query_result:
        lis.append(*i)
    return lis
    

 








