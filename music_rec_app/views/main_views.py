from flask import Blueprint, render_template, request
from music_rec_app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
