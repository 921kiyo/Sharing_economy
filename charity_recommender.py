"""
Recommendation system for suggesting a charity

1. get user information
"""

import pandas as pd
from math import sqrt
from GLOBALS import DATABASE_URL
from models import User

def get_demographic_similarity(df, user_id):

    # Scale columns
    df["sex"] = df["sex"].apply(lambda x: 1 if x == "M" else 0)
    df["age"] = (df["age"] - df["age"].min()) / (df["age"].max() - df["age"].min())
    df["haversine_distance"] = (df["haversine_distance"] - df["haversine_distance"].min()) / (df["haversine_distance"].max() - df["haversine_distance"].min())

    # Get user column
    user = df[df["id"] == user_id]

    df["similarity"] = 0
    # Calculates using euclidean distance
    for col in df.columns:
        df["similarity"] += (df[col] - user[col]) * (df[col] - user[col])

    df["similarity"] = df["similarity"].apply(lambda x: sqrt(x))

    return df["similarity"].tolist()


def recommend(user_id):
    """
    Recommend something using user id

    :param user_id:
    :return:
    """

    df = pd.read_sql(DATABASE_URL, index_col="id", columns=["sex", "age", "haversine_distance"])

    k = 5
    similarity = get_demographic_similarity(df, user_id)
    similarity = similarity.sort()[::-1]

    users = similarity[1:1 + k]

    # Get the charities then select the most common
    charity_counts = {}
    for user in users:
        charity_counts.ad









