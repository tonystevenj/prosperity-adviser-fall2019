# -*- coding: utf-8 -*-
from flask import Flask
from . import router


def run():
    app = Flask(__name__)
    router.dispatch(app)
    app.run(host='0.0.0.0', port=8080, debug=True)
