import bson
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

app: Flask = Flask(__name__)
#our initial form page
@app.route('/')
def index():
    return "Hi!"