from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:111111@localhost:3306/diet"
app.config['JSON_AS_ASCII'] = False

db.init_app(app)

from app import views, models, utils