from flask_login import UserMixin


from ext import db,login_manager


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(),nullable=False, default="default_photo.jpg")

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

def __init__(self,Username,Password,Role="Admin"):
    self.Username = Username
    self.Password = Password
    self.Role = Role

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


