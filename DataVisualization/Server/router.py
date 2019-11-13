# -*- coding: utf-8 -*-
from . controller import main, report

def dispatch(app):
    app.add_url_rule('/', view_func=main.index, methods=['GET'])
    app.add_url_rule('/api/report', view_func=report.report, methods=['GET'])
