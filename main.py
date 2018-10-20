# GLOBALS
from GLOBALS import PRODUCT_LISTINGS, CHARITY_INFO, DATABASE_URL

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
def user_home():
    """
    Returns product listings for user homepage

    :return:
    """

    print(PRODUCT_LISTINGS)
    return render_template("/index.html", outputs=PRODUCT_LISTINGS)
    # foo = jsonify(PRODUCT_LISTINGS)
    # return jsonify(outputs=foo)
    

@app.route("/donate")
def apply_donation():
    """
    Updates the user's 'donating' status in the user database table

    :return:
    """

    # Update database
    pass

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
@app.route("/user<int:user_id>/product/", methods=['GET', 'POST'])
def user_product(user_id):
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
    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)