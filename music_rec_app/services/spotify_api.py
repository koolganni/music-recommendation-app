import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '비공개'
client_secret = '비공개'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
