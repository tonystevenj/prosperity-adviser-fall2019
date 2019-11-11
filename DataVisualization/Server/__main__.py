# -*- coding: utf-8 -*-
if __name__ == '__main__':
    from flask import Flask, request, render_template
    from .librarys import env
    from .models.data.business import Business

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/api/report', methods=['GET'])
    def report():
        business = Business()
        business.load()
        lat = request.args.get('lat')
        lng = request.args.get('lng')
        return '{}   {}'.format(lat, lng)

    app.run(host='0.0.0.0', port=8080, debug=True)
