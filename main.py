# GLOBALS
from GLOBALS import PRODUCT_LISTINGS

from flask import Flask, render_template, url_for, redirect, request \
    , flash, jsonify, make_response, session as login_session

app = Flask(__name__)

@app.route("/")
def hello_world():
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


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)