# -*- coding: utf-8 -*-
import json
from flask import Response, request
from ..models.data.business import Business


def report():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    business = Business()
    items = business.radius(latitude, longitude, radius)
    result = []

    for item in items:
        ret, exists = business.getItem(item['business_id'])
        if exists:
            result.append({
                'business_id': ret['business_id'],
                'name': ret['name'],
                'latitude': ret['latitude'],
                'longitude': ret['longitude'],
                'stars': ret['stars'],
                'review_count': ret['review_count'],
            })
    return Response(json.dumps(result), mimetype='application/json')
