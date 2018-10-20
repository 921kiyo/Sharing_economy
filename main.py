# GLOBALS
from GLOBALS import PRODUCT_LISTINGS

from flask import Flask, render_template, url_for, redirect, request \
    , flash, jsonify, make_response, session as login_session

app = Flask(__name__)

@app.route('/')
def hello_world():
#     # return render_template("/index.html", hello="Hello world!")
#     foo = [1,2,3]
#     return render_template("/index.html", outputs=foo)
#     # return 'Hello, World!'
    """
    Returns product listings for user homepage

    :return:
    """

    print(PRODUCT_LISTINGS)
    return render_template("/index.html", outputs=PRODUCT_LISTINGS)
    # foo = jsonify(PRODUCT_LISTINGS)
    # return jsonify(outputs=foo)
    


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)