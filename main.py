# GLOBALS
from GLOBALS import DATABASE_URL, CONTRIBUTION_PERC

# Populate database
import fill_database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Charity

from flask import Flask, render_template, url_for, redirect, request \
    , flash, jsonify, make_response, session as login_session

app = Flask(__name__)

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
def home():
    """
    Mercari all products homepage

    :return:
    """
    products = session.query(Product).all()

    # TODO: Change html
    return render_template("/index.html", outputs=products)


@app.route("/user/<int:user_id>", methods=["GET", "POST"])
def user_home(user_id):
    """
    Returns product listings for user homepage. Applies the donate.

    :return:
    """

    if request.method == "GET":
        # Returns the list of products by the user
        user_products = session.query(Product).filter_by(user_id=user_id)
        all_charities = session.query(Charity).all()
        return render_template("/index.html", products=user_products, charities=all_charities)

    if request.method == "POST":
        # Updates donation
        charity_id = request.form["charity_id"]
        user = session.query(User).filter_by(id=user_id).first()
        charity = session.query(Charity).filter_by(id=charity_id).first()

        # Toggled Off / On
        if charity_id is None:
            user.donating = False
            charity_id.num_donators = charity.num_donators - 1
            flash("sad", "failure")
        else:
            user.donating = True
            user.charity_id = charity_id
            charity.num_donators = charity.num_donators + 1
            flash('Thank you for much for helping our charity partner!!', 'success')

        session.commit()

@app.route("/charity")
@app.route("/charity/<int:charity_id>")
def charity_home(charity_id=None):
    """
    Returns the details of the charity.

    :return: dependent on request
    """

    if charity_id is None:
        return jsonify(outputs=session.query(Charity).all())
    
    charity = session.query(Charity).filter_by(charity_id).first()
    return jsonify(outputs=charity)


@app.route("/product/<int:product_id>")
def show_product(product_id):
    """
    Gets product detail on the user page, posts a new product

    :return: json
    """
    product = session.query(Product).filter_by(id=product_id).first()
    # if product is None:
    #     return jsonify(output=False, error="Product does not exist")  #TODO: Confirm format
    # product = jsonify(output=product.serialize)
    
    return jsonify(outputs=product)
    # return render_template("product.html", product=product)
    

@app.route("/buy")
def buy_product(product_id):
    """
    Implements the buy product functionality. If a donation has been applied will take 3% of the price and put it towards
    the product.

    :return: Void
    """

    product = session.query(Product).filter_by(id=product_id).first()

    if product.sold:
        return jsonify(output=False, error="Product has already been sold")
    else:
        product.sold = True

    user_id = product.user_id
    user = session.query(User).filter_by(id=user_id).first()

    if user.donating:
        # Donate 3% of total price (product + shipping)
        user.total_donated = user.total_donated + (product.price + product.shipping) * CONTRIBUTION_PERC
        print("Total donated to date is", user.total_donated)

    session.commit()

    return jsonify(output=True)


if __name__ == '__main__':

    # Populate the product
    fill_database.add_users()
    fill_database.add_products()

    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)