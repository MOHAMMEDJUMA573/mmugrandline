from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '249c7b64dccfa1f5f3e8970d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"  # Redirects to login if user is not logged in
login_manager.login_message_category = "info"

from market import routes
