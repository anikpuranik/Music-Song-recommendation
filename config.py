class Config:
    dataset_path = "dataset"
    database = "data/song.db"
    co_occurance_path = "data/all_users_by_song"
    columns_rename = {'artist_name':'artist', 'release':'album', 'user_id':'user_count'}
    top_nav = ["ARTISTS", "ALBUMS"]
    
    decade_list = {"All time hits": (0, 2010), "Hit Last Decade": (2001,2010),
                    "Hit 2000s": (1991,2000), "Hit 90s": (1981, 1990),
                    "Hit 80s": (1971, 1980), "Hit 70s": (1961, 1970)
                    }

    charts_list = ["All time hits", "Hit Last Decade", "Hit 2000s", 
                    "Hit 90s", "Hit 80s", 'Hit 70s'
                    ]
                    
         