from flask import Blueprint, render_template, request, redirect
from music_rec_app import db
from music_rec_app.models import Track, User, MyMusic
from music_rec_app.services.recommender import recommend_track

bp = Blueprint('user', __name__)

@bp.route('/recommend', methods=['POST'])
def recommend():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    tracks = user.tracks
    track_id_list = []
    for track in tracks:
        track_id_list.append(track.id)
    # 추천 API
    recommended_tracks = recommend_track(track_id_list=track_id_list)
    return render_template('recommend.html', tracks=recommended_tracks, username=username)
