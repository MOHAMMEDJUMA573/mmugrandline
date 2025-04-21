from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '249c7b64dccfa1f5f3e8970d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes