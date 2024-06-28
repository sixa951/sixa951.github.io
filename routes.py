from flask import Flask, render_template,redirect, request

from os import path

from flask_login import login_user,logout_user

import forms
from models import Product,User
from forms import RegistrationForm, ProductForm, LoginForm
from ext import app, db





@app.route('/')
def home():
    Products = Product.query.all()
    return render_template("index.html", products=Products, role="guest")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
      new_user = User(username=form.username.data, password=form.password.data)

      db.session.add(new_user)
    db.session.commit()
    return render_template("register.html", form=form)



@app.route('/help')
def help():
    return render_template("help.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)

    return render_template("product_details.html", product=product)




@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            login_user(user)
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route('/sale')
def sale():
    return render_template("sale.html")


@app.route('/create_product', methods=["GET", "POST"])
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data)

        image = form.img.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)

        new_product.img = image.filename

        db.session.add(new_product)
        db.session.commit()
        return redirect("/")
    return render_template("create_product.html", form=form)



@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)

    db.session.delete(product)
    db.session.commit()

    return redirect("/")


# აქ მოგივა ნივთები და შეგიძლია დათაბეისში შეინახო (ან რაც გინდა ის უქნა)
@app.route('/checkout', methods=['POST'])
def checkout():
    cart_items = request.json
    print(cart_items)

    return {"success": True} # ესეც შეგიძლია შეცვალო და render_tempate() გამოიყენო