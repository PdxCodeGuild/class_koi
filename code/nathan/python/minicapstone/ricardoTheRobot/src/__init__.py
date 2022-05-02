from flask import Flask
import os
from src.database import db
from src.database import Challenge
from src.build_db import import_challenges
from src.api import api

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

    db.app=app
    db.init_app(app)
    app.register_blueprint(api)

    @app.route('/')
    def index():
        return 'Hello'
    
    return app
