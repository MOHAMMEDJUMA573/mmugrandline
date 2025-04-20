from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)  # <-- fixed here
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"Item: {self.name}"

@app.route("/")
@app.route("/Home")
def home_page():
    visitor_ip = request.remote_addr
    with open("visits.log", "a") as f:
        f.write(f"{datetime.now()} - {visitor_ip}\n")
    return render_template("home.html")

"""@app.route("/about/<username>")
def about_page(username):
    return f"<h1> This is the about page of {username} </h1>" """
# About route
@app.route("/about_gl")
def about_page():
    return render_template("about.html")
# Market route
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
# Contact route
@app.route("/contact")
def contact_page():
    return render_template("contact.html")
#Blog route
@app.route("/blog")
def blog_page():
    return render_template("blog.html")
#Login route
@app.route("/login")
def login_page():
    return render_template("login.html")
#Login route
@app.route("/register")
def register_page():
    return render_template("register.html")
#logging in route
@app.route("/logging")
def logging_page():
    return render_template("not.html")