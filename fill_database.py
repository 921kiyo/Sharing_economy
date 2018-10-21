
from GLOBALS import DATABASE_URL, PRODUCT_LISTINGS, CHARITY_INFO, USERS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product, User, Charity

from math import radians, asin, cos, sin, sqrt

engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def haversine(lon1, lat1):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon2 = 0
    lat2 = 0

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def add_users():
    for person in USERS:
        print("Adding", person)
        user = User(name=person["name"],
                    age=person["age"],
                    sex=person["sex"],
                    country=person["country"],
                    city=person["city"],
                    haversine_distance=haversine(person["longitude"], person["latitude"]),
                    donating=person["donating"]
                    )

        session.add(user)

    session.commit()


def add_products():
    for person in PRODUCT_LISTINGS:
        for product in PRODUCT_LISTINGS[person]:
            print("Adding", product["name"], "for", person)

            user = session.query(User).filter_by(name=person).first()
            p = Product(name=product["name"],
                        user_id=user.id,
                        description=product["description"],
                        image=product["url"],
                        price=product["price"],
                        size=product["size"],
                        condition=product["condition"],
                        shipping=product["shipping_cost"]
                        )

            session.add(p)

    session.commit()


def add_charities():
    for charity in CHARITY_INFO:

        c = Charity(name=charity["name"],
                    mission=charity["mission"],
                    url=charity["url"])

        if charity.get("url") is not None and charity.get("url") != "":
            c.url = charity["url"]

        session.add(c)

    session.commit()


if __name__ == "__main__":

    print("Adding users")
    add_users()

    print("Adding products")
    add_products()

    print("Adding charities")
    add_charities()





