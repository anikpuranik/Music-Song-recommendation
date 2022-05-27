import sqlite3
from config import Config

conn = sqlite3.connect(Config.database, check_same_thread=False)
cursor = conn.cursor()

class queries:
    def get_trending_songs_query():
        return '''SELECT SONG_ID, TITLE, ALBUM, ARTIST, YEAR FROM SONG_DATA WHERE 
                    YEAR = 2010 ORDER BY USER_COUNT LIMIT 12;'''
    
    def get_top_songs_by_year_query(year1, year2):
        return '''SELECT SONG_ID, TITLE, ALBUM, ARTIST, YEAR FROM SONG_DATA
                    WHERE YEAR BETWEEN {} AND {} ORDER BY USER_COUNT 
                    LIMIT 25;'''.format(year1, year2)

    def get_top_artist_query():
        return '''SELECT ARTIST FROM SONG_DATA GROUP BY ARTIST 
                    ORDER BY SUM(USER_COUNT) DESC LIMIT 12;'''
                
    def get_top_album_query():
        return '''SELECT ALBUM FROM SONG_DATA GROUP BY ALBUM 
                    ORDER BY SUM(USER_COUNT) DESC LIMIT 12;'''

    def get_top_songs_by_artist_query(artist):
        return '''SELECT SONG_ID, TITLE, ALBUM, ARTIST, YEAR FROM SONG_DATA 
                    WHERE ARTIST IN ("{}") ORDER BY USER_COUNT DESC 
                    LIMIT 20;'''.format(artist)
                
    def get_top_songs_by_album_query(album):
        return '''SELECT SONG_ID, TITLE, ALBUM, ARTIST, YEAR FROM SONG_DATA 
                    WHERE ALBUM IN ("{}") ORDER BY USER_COUNT DESC 
                    LIMIT 20;'''.format(album)
    
    def get_song_id_by_title_query(song_id):
        return '''SELECT song_id from song_data where title in ('{}');'''.format(song_id)

    def get_title_by_song_id_query(title):
        return '''SELECT TITLE from song_data 
                    where song_id in {};'''.format(title)    
    
    
    
    
    
    
    
    
    