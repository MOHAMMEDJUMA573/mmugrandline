from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/Home")
def home_page():
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
    return render_template("market.html")
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
@app.route("/logging")
def logging_page():
    return render_template("not.html")