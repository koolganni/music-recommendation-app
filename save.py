from music_rec_app.services.spotify_api import *
from settings import *
from genre_playlist import *
import psycopg2

host = DEV_DB_HOST
username = DEV_DB_USERNAME
password = DEV_DB_PASSWORD
database = DEV_DB_DATABASE

connection = psycopg2.connect(
    host=host,
    user=username,
    password=password,
    database=database
)

try:
    # 데이터베이스 연결 
    cursor = connection.cursor()
    
    # 테이블 생성
    cursor.execute(
        """
        DROP TABLE IF EXISTS mymusic;
        DROP TABLE IF EXISTS track;
        DROP TABLE IF EXISTS users;
        CREATE TABLE track (
            id INT PRIMARY KEY,
            spotify_id VARCHAR,
            name VARCHAR, 
            artist VARCHAR,
            genre VARCHAR, 
            release_year VARCHAR, 
            popularity INT,
            preview_url VARCHAR, 
            image_url VARCHAR, 
            explicit INT,
            danceability FLOAT, 
            energy FLOAT,
            key INT, 
            loudness FLOAT, 
            mode INT, 
            speechiness FLOAT,
            acousticness FLOAT, 
            instrumentalness FLOAT, 
            liveness FLOAT,
            valence FLOAT, 
            tempo FLOAT, 
            duration_ms FLOAT
        );
        CREATE TABLE users (
            id INT PRIMARY KEY,
            username VARCHAR,
            private_user INT
        );
        CREATE TABLE mymusic (
            user_id INT NOT NULL,
            track_id INT NOT NULL,
            PRIMARY KEY (user_id, track_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE,
            FOREIGN KEY (track_id) REFERENCES track(id) ON UPDATE CASCADE
        );
        """
    )
    
    # 데이터 옮기기
    idx = 0
    for playlist in genre_playlist:
      results = sp.user_playlist_tracks("spotify", playlist[1])
      for item in results['items']:
          track = item['track']

          spotify_id = track['id']

          name = track['name'].replace("'", "`")
          artist = track['artists'][0]['name'].replace("'", "`")
          genre = playlist[0].replace("'", "`")

          release_year = int(track['album']['release_date'].split('-')[0])
          popularity = track['popularity']
          preview_url = ''
          if track['preview_url'] is not None:
            preview_url = track['preview_url']
          image_url = track['album']['images'][0]['url']
          explicit = int(track['explicit'])

          features = sp.audio_features(spotify_id)[0]
          if features is None:
            continue
          danceability = features['danceability']
          energy = features['energy']
          key = features['key']
          loudness = features['loudness']
          mode = features['mode']
          speechiness = features['speechiness']
          acousticness = features['acousticness']
          instrumentalness = features['instrumentalness']
          liveness = features['liveness']
          valence = features['valence']
          tempo = features['tempo']
          duration_ms = features['duration_ms']

          new_track = (idx, spotify_id, str(name), str(artist),
                      str(genre), release_year, popularity,
                      preview_url, image_url, explicit,
                      danceability, energy,
                      key, loudness, mode, speechiness,
                      acousticness, instrumentalness, liveness,
                      valence, tempo, duration_ms)
          
          cursor.execute(
              f"""
              INSERT INTO track(id, spotify_id, name, artist,
                      genre, release_year, popularity,
                      preview_url, image_url, explicit,
                      danceability, energy,
                      key, loudness, mode, speechiness,
                      acousticness, instrumentalness, liveness,
                      valence, tempo, duration_ms)
              VALUES {new_track}
              """
          )
          connection.commit() # 데이터베이스 업데이트
          idx += 1
except Exception as e:
    print(e)

connection.close()
