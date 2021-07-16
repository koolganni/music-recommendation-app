from music_rec_app import db
from music_rec_app.models import Track, User, MyMusic
from settings import *
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cdist
import numpy as np
import pandas as pd

cols = ['popularity', 'explicit', 'danceability',
       'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']


def get_mean_vector(df_mymusic):
    mymusic_matrix = np.array(df_mymusic[cols])
    return np.mean(mymusic_matrix, axis=0)


# Contents(Item) based 추천 (유사도 metric : 코사인 거리)
def recommend_track(track_id_list=None, num_of_track=10):
    # 전체 음악
    df_tracks = pd.read_sql_table('track', DEV_DB_URI)
    # df_tracks = pd.read_csv(DEV_CSV_URI)
    df_tracks.drop_duplicates(subset=['spotify_id'], inplace=True)

    # 유저 마이 뮤직
    # queryset = Track.query.filter(Track.id.in_(tuple(track_id_list)))
    # df_mymusic = pd.read_sql(queryset.statement, queryset.session.bind)
    df_mymusic = df_tracks[(df_tracks['id'].isin(track_id_list))]

    mymusic_center = get_mean_vector(df_mymusic)
    distances = cdist(mymusic_center.reshape(1,-1), df_tracks[cols], 'cosine')
    index = list(np.argsort(distances)[:, :num_of_track][0])

    recommended_tracks = df_tracks.iloc[index].to_dict(orient='records')

    return recommended_tracks
