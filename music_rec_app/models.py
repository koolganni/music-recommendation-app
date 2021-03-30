from music_rec_app import db

class MyMusic(db.Model):
    __tablename__ = 'mymusic'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), primary_key=True) 


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    private_user = db.Column(db.Integer, nullable=False) # 피드에 저장(공개) 여부

    tracks = db.relationship('Track', secondary='mymusic')


class Track(db.Model):
    __tablename__ = 'track'

    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    release_year = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    preview_url = db.Column(db.String)
    image_url = db.Column(db.String)
    explicit = db.Column(db.Integer)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Float)

    users = db.relationship('User', secondary='mymusic')
