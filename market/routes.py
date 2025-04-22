from market import app, db
from flask import render_template, redirect, url_for, flash, request, get_flashed_messages
from datetime import datetime 
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user


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
@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Success You are logged in as {attempted_user.username}",category='success')
            return redirect(url_for('market_page'))
        else: 
            flash(f"username and password mismatch! Please try Again!", category='danger')
        
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data) 
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("login_page"))   
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')    
    return render_template("register.html", form=form)
#logging in route
@app.route("/logging")
def logging_page():
    return render_template("not.html")