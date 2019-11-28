# -*- coding: utf-8 -*-
from . controller import main, report

def dispatch(app):
    app.add_url_rule('/', view_func=main.index, methods=['GET'])
    app.add_url_rule('/api/report/business', view_func=report.business, methods=['GET'])
    app.add_url_rule('/api/report/park', view_func=report.parks, methods=['GET'])
    app.add_url_rule('/api/report/reviews0', view_func=report.reviews0, methods=['GET'])
    app.add_url_rule('/api/report/reviews13', view_func=report.reviews13, methods=['GET'])
    app.add_url_rule('/api/report/reviews45', view_func=report.reviews45, methods=['GET'])