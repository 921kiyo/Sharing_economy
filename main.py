# GLOBALS
from GLOBALS import DATABASE_URL, CONTRIBUTION_PERC

# Populate database
import fill_database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Charity

from flask import Flask, render_template, url_for, redirect, request \
    , flash, jsonify, make_response, session as login_session

from flask_sqlalchemy_session import flask_scoped_session

import pandas as pd
from math import radians, cos, sin, asin, sqrt


app = Flask(__name__)

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# session = DBSession()
session = flask_scoped_session(sessionmaker(bind=engine))


def get_demographic_similarity(df, user_id):
    # Scale columns
    df["sex"] = df["sex"].apply(lambda x: 1 if x.lower() == "m" else 0)
    df["age"] = (df["age"] - df["age"].min()) / (df["age"].max() - df["age"].min())
    df["haversine_distance"] = (df["haversine_distance"] - df["haversine_distance"].min()) / (
                df["haversine_distance"].max() - df["haversine_distance"].min())

    # Get user column
    user = df[df["id"] == user_id]

    print(user)

    df["similarity"] = 0
    # Calculates using euclidean distance
    for col in df.columns:
        if col != "similarity":
            print(("attribute", col, "df", df[col], "user val", user[col].iloc[0]))
            df["similarity"] += (df[col] - user[col].iloc[0]) * (df[col] - user[col].iloc[0])

    df["similarity"] = df["similarity"].apply(lambda x: sqrt(x))

    similarity = df[["id", "similarity"]]
    similarity = similarity.sort_values(by=["similarity"], ascending=True)

    return similarity


def recommend(user_id):
    """
    Recommends a charity to the user id

    :param user_id:
    :return:
    """

    df = pd.read_sql_table(table_name="user", con=DATABASE_URL, columns=["id", "sex", "age", "haversine_distance"])
    print(df)

    k = 5
    similarity = get_demographic_similarity(df, user_id)

    # Get the charities then select the most common

    print("similarity df", similarity)
    charity_counts = {}
    for row in range(1, 1 + k):  # Start from 1 as first row is user itself with distance of 0
        try:
            user_id = int(similarity["id"].iloc[row])
            print("user_id", user_id, type(user_id))
            u = session.query(User).filter_by(id=user_id).first()
            if u.charity_id is not None:
                charity_counts[u.charity_id] = charity_counts.get(u.charity_id, 0) + 1
        except IndexError:
            break

    # Sort and get top 1

    print("charity counts", charity_counts)
    if not charity_counts:  # If empty
        return None

    best_charity_id = max(charity_counts, key=charity_counts.get)
    return best_charity_id

@app.route("/")
def home():
    # """
    # Mercari all products homepage

    # :return:
    # """
    products = session.query(Product).all()

    # # TODO: Change html
    return render_template("/index.html", products=products)


@app.route("/user/<int:user_id>", methods=["GET", "POST"])
def user_home(user_id):
    """
    Returns product listings for user homepage. Applies the donate.
    :return:
    """
    # UPDATE donation
    if request.method == "POST":
        # Updates donation
        
        user = session.query(User).filter_by(id=user_id).first()
        # Toggled Off / On
        if "charity_radio" in request.form:
            charity_id = request.form["charity_radio"]
            user = session.query(User).filter_by(id=user_id).first()
            charity = session.query(Charity).filter_by(id=charity_id).first()

            user.donating = True
            user.charity_id = charity_id
            # charity.num_donators = charity.num_donators + 1
            flash('Thank you for much for helping our charity partner!!', 'success')

        else:
            charity = session.query(Charity).filter_by(id=user.charity_id).first()
            user.donating = False
            # charity_id.num_donators = charity.num_donators - 1
            flash("Sad you are leaving the donation", "error")            
        session.commit()

    # Returns the list of products by the user
    user_products = session.query(Product).filter_by(user_id=user_id)
    all_charities = session.query(Charity).all()
    print("ALL CHARITY ", all_charities)
    user = session.query(User).filter_by(id=user_id).first()
    rec_id = recommend(user_id)
    print("recommended id", rec_id)
    rec = session.query(Charity).filter_by(id=rec_id).first()
    for c in all_charities:
        print(c.name)
    return render_template("/user.html", products=user_products, user=user, charities=all_charities, recommend_charity=rec)

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
    seller = session.query(User).filter_by(id=product.user_id).first()
    # if product is None:
    #     return jsonify(output=False, error="Product does not exist")  #TODO: Confirm format
    # product = jsonify(output=product.serialize)

    return render_template("product.html", product=product, seller=seller)
    

@app.route("/buy/<int:product_id>", methods=["POST"])
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
        donation = (product.price + product.shipping) * CONTRIBUTION_PERC
        user.total_donated = user.total_donated + donation

        charity = session.query(Charity).filter_by(id=user.charity_id).first()
        charity.amount_raised = charity.amount_raised + donation

        print("Total donated to date is", user.total_donated, "to", charity.name)

    session.commit()
    flash('Purchase complete. Thank you so much!', 'success')

    products = session.query(Product).all()
    return render_template("/index.html", outputs=products)


if __name__ == '__main__':

    # Populate the product
    fill_database.add_users()
    fill_database.add_products()
    fill_database.add_charities()

    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)