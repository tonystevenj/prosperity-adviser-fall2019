# -*- coding: utf-8 -*-
from flask import Flask
from . import router


def run():
    app = Flask(__name__)
    router.dispatch(app)
    app.run(host='localhost', port=8080, debug=True)
