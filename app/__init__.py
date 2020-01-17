from flask import Flask
from config import Config
from app.db.connector import Connector

app = Flask(__name__)
app.config.from_object(Config)
connector = Connector()

from app import routes