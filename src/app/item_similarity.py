import pickle
import pandas as pd
from config import Config

all_users_by_song = pickle.load(open(Config.co_occurance_path, "rb"))

def recommend_song(target_song_id):
    corr_mat = dict()
    all_songs = all_users_by_song.keys()
    user_of_target_song = all_users_by_song[target_song_id]
    
    for ind, song_id in enumerate(all_songs):
        user_by_song_id =  all_users_by_song[song_id]
        score = len(user_of_target_song.intersection(user_by_song_id))

        if score > 0:
            score = score/len(user_of_target_song.union(user_by_song_id))
        else:
            score = 0
        corr_mat[song_id] = score
        
    data = sorted(corr_mat.items(), key=lambda item: item[1], reverse=True)[1:13]
    data = pd.DataFrame(data)
    return tuple(data[0])
