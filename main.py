# GLOBALS
from GLOBALS import PRODUCT_LISTINGS, CHARITY_INFO

from flask import Flask, render_template, url_for, redirect, request \
    , flash, jsonify, make_response, session as login_session

app = Flask(__name__)

@app.route("/")
def user_home():
    """
    Returns product listings for user homepage

    :return:
    """

    print(PRODUCT_LISTINGS)
    return jsonify(data=PRODUCT_LISTINGS)


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


@app.route("/buy")
def buy_product(seller, product_id):
    """
    Implements the buy product functionality. If a donation has been applied will take 3% of the price and put it towards
    the product.

    :return: -
    """

    # Database lookup
    # Look up product id
    # TODO: Update after creating database models

    user = user_table[seller]
    if user.donating == True:
        # Donate 3%
        product = product_table[product_id]
        charity_table["price"] += product.price * 0.03

    return









if __name__ == '__main__':
    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)