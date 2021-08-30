"""Seed file to make sample data for db"""
from models import db
from app import app

db.drop_all()
db.create_all()