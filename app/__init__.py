""" Application """
import os
from flask import Flask
from config import config
from models import connect_db

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    connect_db(app)
    return app

