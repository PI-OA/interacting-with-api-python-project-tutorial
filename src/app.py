import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
print("CLIENT_ID:", client_id)
print("CLIENT_SECRET:", client_secret)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

#2YZyLoL8N0Wb9xBt1NhZWg



# obtener mejores canciones del artista
results = spotify.artist_top_tracks("2YZyLoL8N0Wb9xBt1NhZWg")
print("results:", results)  # Depuración: ver toda la respuesta
print("Cantidad de tracks:", len(results.get('tracks', [])))  # Depuración: ver cuántos tracks hay


songs = []

for track in results['tracks']:
    songs.append({"name":track['name'],
                 "popularity":track ['popularity'],
                 "duracion_min":track['duration_ms']/60000})
    
print(songs)

df = pd.DataFrame(songs)
print(df)