from market import app, db
from flask import render_template, redirect, url_for, flash, request, get_flashed_messages
from datetime import datetime 
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user



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
@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    items = Item.query.filter_by(owner=None).all()
    owned_items = Item.query.filter_by(owner=current_user.id).all()
    purchase_forms = {item.id: PurchaseItemForm() for item in items}
    selling_form = SellItemForm()

    if request.method == 'POST':
        purchased_item_id = request.form.get('purchased_item')
        if purchased_item_id:
            try:
                item_id = int(purchased_item_id)
                item = Item.query.get(item_id)
                
                # Check if the item exists and if the user can purchase it
                if item and item.can_purchase(current_user):
                    item.buy(current_user)
                    flash(f"Successfully purchased {item.name}!", category='success')
                else:
                    flash("Not enough balance or invalid item.", category='danger')
            except Exception as e:
                flash(f"Something went wrong: {str(e)}", category='danger')

        sold_item = request.form.get('sold_item')
        if sold_item:
            s_item_object = Item.query.filter_by(name=sold_item).first()
            if s_item_object and current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name}!", category='success')
            else:
                flash(f"Could not sell {sold_item}.", category='danger')

        return redirect(url_for('market_page'))

    return render_template(
        'market.html',
        items=items,
        purchase_forms=purchase_forms,
        owned_items=owned_items,
        selling_form=selling_form
    )

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
        login_user(user_to_create)
        flash(f"@{user_to_create.username} Account created successfully!", category="success")
        return redirect(url_for("login_page"))   
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')    
    return render_template("register.html", form=form)
@app.route('/mypeople')
def users_page():
    users = User.query.all()
    return render_template('not.html', users=users)
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/mypeople/dashbord')
@login_required
def admin_dashboard():
    users = User.query.all()
    items = Item.query.all()
    return render_template('admin_dashboard.html', users=users, items=items)
