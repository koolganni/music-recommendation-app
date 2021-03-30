from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)

    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)

    from music_rec_app.views import main_views, user_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
