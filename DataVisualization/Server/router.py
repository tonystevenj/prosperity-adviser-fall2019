# -*- coding: utf-8 -*-
from . controller import main, report
from .models.data.reviews import Reviews

def dispatch(app):
    app.add_url_rule('/', view_func=main.index, methods=['GET'])
    app.add_url_rule('/api/report/business', view_func=report.business, methods=['GET'])
    app.add_url_rule('/api/report/park', view_func=report.parks, methods=['GET'])
    @app.route('/api/report/review')
    def review():
        re = Reviews()
        re.load()
        re.get_id_according_to_redies()
        output = re.full_process()
        return str(output)