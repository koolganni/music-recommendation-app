from flask import Blueprint, render_template, request, redirect
from music_rec_app import db
from music_rec_app.models import Track, User, MyMusic

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/feed/')
@bp.route('/feed/<int:user_id>')
def feed(user_id=None):
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        return render_template('my_music.html', tracks=user.tracks, username=user.username)
    
    users = User.query.all()
    return render_template('feed.html', users=users)


@bp.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('user_join.html')

    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if user:
        return "이미 있는 username 입니다. 뒤돌아가 다시 작성해주세요."
    
    # 새로운 유저 추가
    new_user = User(username=username, private_user=0)
    db.session.add(new_user)
    db.session.commit()

    return genre(username=username)


@bp.route('/genre')
def genre(username=None):
    genres = [
        {'genre': 'pop', 'url': 'https://i.scdn.co/image/ab67616d0000b273e6f407c7f3a0ec98845e4431', 'name': '팝'},
        {'genre': 'k-pop', 'url': 'https://i.scdn.co/image/ab67616d0000b2730fdd9fc8745ed9185dc95873', 'name': 'K-POP'},
        {'genre': 'hiphop', 'url': 'https://i.scdn.co/image/ab67616d0000b273a4af7eb20f13592b228c6c82', 'name': '힙합'},
        {'genre': 'r&b', 'url': 'https://i.scdn.co/image/ab67616d0000b27312a76d1b13ef07188f7dfbc9', 'name': 'R&B'},
        {'genre': 'indie', 'url': 'https://i.scdn.co/image/ab67616d0000b273f69775359d3d6f87a7d4f33f', 'name': '인디'},
        {'genre': 'fork-acoustic', 'url': 'https://i.scdn.co/image/ab67616d0000b273cd5f66ec071620298c747963', 'name': '포크/어쿠스틱'},
        {'genre': 'dance-electronic', 'url': 'https://i.scdn.co/image/ab67616d0000b2734eb176d91cebd3d84346acec', 'name': '댄스/일렉트로닉'},
        {'genre': 'jazz', 'url': 'https://i.scdn.co/image/ab67616d0000b273cf1a31bd900aee2d866c0807', 'name': '재즈'},
        {'genre': 'soul', 'url': 'https://i.scdn.co/image/ab67616d0000b2736f9e6abbd6fa43ac3cdbeee0', 'name': '소울'},
        {'genre': 'classic', 'url': 'https://i.scdn.co/image/ab67616d0000b2735f38431d036be50439043b08', 'name': '클래식'},
        {'genre': 'metal', 'url': 'https://i.scdn.co/image/ab67616d0000b27375e6375e11550746705a9645', 'name': '메탈'},
        {'genre': 'alternative', 'url': 'https://i.scdn.co/image/ab67616d0000b2736ebb479c2160fa31c39061bc', 'name': '얼터너티브'}
    ]
    return render_template('genre_choice.html', username=username, genres=genres)


@bp.route('/genre_choice', methods=['POST'])
def genre_choice():
    genre = request.form['genre']
    username = request.form['username']
    tracks = Track.query.filter_by(genre=genre).all()

    return render_template('track_choice.html', tracks=tracks, username=username)


@bp.route('/track_choice', methods=['POST'])
def track_choice():
    track_id = request.form['track_id']
    username = request.form['username']
    user_id = User.query.filter_by(username=username).first().id

    # 유저-노래 MyMusic 에 추가
    new_mymuic = MyMusic(user_id=user_id, track_id=track_id)
    db.session.add(new_mymuic)
    db.session.commit()

    return '', 204
