import os
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Using "Web Archive Machine" (Billboard's page is now generated with JavaScript)
BILLBOARD_URL = "https://web.archive.org/web/20190920223214/https://www.billboard.com/charts/hot-100/2010-01-09"

response = requests.get(BILLBOARD_URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

songs = soup.find_all(name="span", class_="chart-list-item__title-text")
songs_titles = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
for song in songs_titles:
    result = sp.search(q=f"track:{song} year:2010", type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped")

PLAYLIST_ID: object = sp.user_playlist_create(user=user_id, public=False, name=f"2010-01-09 BillBoard-100")['id']

sp.playlist_add_items(PLAYLIST_ID, song_uris)