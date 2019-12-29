# -*- coding: utf-8 -*-
from . controller import main, report

def dispatch(app):
    app.add_url_rule('/', view_func=main.index, methods=['GET'])
    app.add_url_rule('/api/report/business', view_func=report.business, methods=['GET'])
    app.add_url_rule('/api/report/park', view_func=report.parks, methods=['GET'])
    app.add_url_rule('/api/report/reviews', view_func=report.reviews, methods=['GET'])
    app.add_url_rule('/api/report/feature', view_func=report.feature, methods=['GET'])
    app.add_url_rule('/api/report/table', view_func=report.table, methods=['GET'])
    app.add_url_rule('/api/report/score', view_func=report.score, methods=['GET'])
    app.add_url_rule('/api/report/score_data', view_func=report.score_data, methods=['GET'])
    app.add_url_rule('/api/report/crime', view_func=report.crime, methods=['GET'])
    app.add_url_rule('/api/report/pop_age', view_func=report.pop_age, methods=['GET'])
