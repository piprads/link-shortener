from flask import Flask 

from .extensions import db
from .routes import short

def create_app(config_file='settings.py'):
    # Initialize the app
    app = Flask(__name__)

    # Load the config file
    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(short)

    return app