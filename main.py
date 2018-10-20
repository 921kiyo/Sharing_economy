# GLOBALS
from GLOBALS import PRODUCT_LISTINGS, CHARITY_INFO, DATABASE_URL

# Populate database
import fill_database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product

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
    return render_template("/index.html", outputs=PRODUCT_LISTINGS)


@app.route("/user/<int:user_id>", methods=["GET", "POST"])
def user_home(user_id):
    """
    Returns product listings for user homepage. Applies the donate.

    :return:
    """

    if request.method == "GET":
        # Returns the list of products by the user
        all_products = session.query(Product).filter_by(user_id=user_id)
        return render_template("/index.html", outputs=all_products)


    if request.method == "POST":
        # Updates donation
        user = session.query(User).filter_by(id=user_id).first()
        user.donating = not user.donating
        session.commit()

        if user.donating:
            flash('Thank you for much for helping our charity partner!!', 'success')
        else:
            flash("sad", "failure")


    return render_template("/index.html", outputs=PRODUCT_LISTINGS)
    # foo = jsonify(PRODUCT_LISTINGS)
    # return jsonify(outputs=foo)



@app.route("/catalog/tshirts")
def show_catalog():
    pass

@app.route("/charity", methods=["GET"])
def charity_home():
    """
    Returns the details of the charity. These include:

    Video / IMAGE
    Description of cause
    total funds raised

    :return: dependent on request
    """

    # Assumes data is available in the database
    # TODO: Error handling
    if request.method == "GET":
        return jsonify(output=CHARITY_INFO)


# TODO: Confirm the structure
@app.route("/product/<int:product_id>", methods=['GET'])
def user_product(product_id):
    """
    Gets product detail on the user page, posts a new product

    :return: json
    """

    if request.method == "GET":
        product_id = request.params.get("product_id")
        product = session.query(Product).filter_by(id=product_id).first()
        if product is None:
            return jsonify(output=False, error="Product does not exist")  #TODO: Confirm format

        return jsonify(output=product)

    elif request.method == "POST":
        new_product = Product(name=request.form["name"],
                                user_id=user_id,
                                description=request.form["description"],
                                image=request.form["image"],
                                price=request.form["price"],
                                condition=request.form["condition"],
                                category=request.form["category"]
        )

        if request.form["size"]:
            new_product.size = request.form["size"]

        if request.form["shipping"]:
            new_product.shipping = request.form["shipping"]

        session.add(new_product)
        session.commit()

        print("New product added")

        product = session.query(Product).filter_by(name=request.form["name"])
        return jsonify(output=product.id)

@app.route("/product/<int:product_id>")
def show_product(product_id):
    # product = session.query(Product).filter_by(id=product_id).one()
    product = {
            "name": "Water T-shirt",
            "url": "https://cdn.shopify.com/s/files/1/0209/1522/products/t-shirts-water-t-shirt-1_grande.jpg?v=1527120370",
            "seller_id": 1,
            "description": "Beautiful T-shirt with a water logo on it.",
            "image": 1,  # Dummy
            "price": 26,  # Dollars
            "categories": ["apparel", "boys"],
            "condition": "good",  # Should this be an integer
            "size": "XL",
            "shipping_cost": 0
        }
    return render_template("item.html", product=product)
    


@app.route("/buy")
def buy_product(product_id):
    """
    Implements the buy product functionality. If a donation has been applied will take 3% of the price and put it towards
    the product.

    :return: Void
    """

    contribution_perc = 0.03
    product = session.query(Product).filter_by(id=product_id).first()

    if product.sold:
        return jsonify(output=False, error="Product has already been sold")
    else:
        product.sold = True

    user_id = product.user_id
    user = session.query(User).filter_by(id=user_id).first()

    if user.donating:
        # Donate 3% of total price (product + shipping)
        user.total_donated = user.total_donated + (product.price + product.shipping) * contribution_perc
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