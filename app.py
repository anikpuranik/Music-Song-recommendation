from flask import Flask, render_template, request
import webbrowser 
from src.app import functions as f
from config import Config

app = Flask(__name__)

# loading initial data
top_charts_list, top_artist_list, top_album_list, trending_songs = f.load_list()
top_nav = Config.top_nav
# browsser
print("Opening Browser...")
webbrowser.open_new("http://127.0.0.1:8080/") 

@app.route("/", methods=['GET', 'POST'])
def home():
    
    if request.method == "POST":
        pass
    
    return render_template("home.html", top_charts_list = top_charts_list, 
                           trending_songs = trending_songs,
                           top_artist_list = top_artist_list, 
                           top_album_list = top_album_list
                           )

@app.route("/list/<parameter>")
def show_list(parameter):
    print(parameter)
    
    if parameter == "artists":
        list_item = top_artist_list
    elif parameter == "albums":
        list_item = top_album_list
    elif parameter == "trending":
        list_item = trending_songs
        
        return render_template("display_list.html", list_type=parameter.upper(),
                               list_item=list_item
                               )
        
    return render_template(
    "display_song.html", list_type=parameter.upper(),
    nav_bar=top_nav, list_item=list_item
    )

@app.route("/list1/<trending>")
def display_trend(trending):
    print(trending)
    top_songs = f.get_similar_song(trending)
    return render_template("display_song.html", list_type=trending.upper(),
                           list_item=top_songs
                           )

@app.route("/list2/<chart>")
def display_chart(chart):
    print(chart)
    top_songs = f.get_top_songs_by_chart(chart)
    return render_template(
                            "display_list.html", list_type=chart,
                            list_item=top_songs
                            )

@app.route("/artist/<artist>")
def display_artist(artist):
    print(artist)
    top_songs = f.get_top_songs_by_artist(artist)
    return render_template(
                            "display_list.html", list_type=artist,
                            list_item=top_songs
                            )

@app.route("/album/<album>")
def display_album(album):
    print(album)
    top_songs = f.get_top_songs_by_album(album)
    return render_template(
                            "display_list.html", list_type=album,
                            list_item=top_songs
                            )

if __name__ == '__main__':
    app.run(port=8080)
