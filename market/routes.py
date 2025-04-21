from market import app
from flask import render_template, request
from datetime import datetime 
from market.models import Item

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