from market import db, bcrypt, login_manager
from flask_login import login_user
from flask_login import UserMixin 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=58), nullable=False, unique=True)
    pass_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plaintext_password):
        self.pass_hash = bcrypt.generate_password_hash(plaintext_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.pass_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'

    def buy(self, user):
        # Ensure the user has enough funds and update their budget
        if user.budget >= self.price:
            self.owner = user.id
            user.budget -= self.price
            db.session.commit()  # Ensure the changes are saved
        else:
            raise ValueError("Insufficient funds to purchase the item")

    def sell(self, user):
        """Handles selling the item, removes owner, and adds to user's budget"""
        self.owner = None
        user.budget += self.price
        db.session.commit()  # Ensure the changes are committed

    def can_purchase(self, user):
        # Ensure user has enough budget to purchase the item
        return user.budget >= self.price  # `user.budget` should be the correct reference

