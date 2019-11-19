# -*- coding: utf-8 -*-
import json
from flask import Response, request
from ..models import data


def business():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    items = data.radius('Business', latitude, longitude, radius)
    result = []

    for item in items:
        ret, exists = data.getItem('Business', item['business_id'])
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

def parks():
    pass
    # latitude = request.args.get('latitude')
    # longitude = request.args.get('longitude')
    # radius = request.args.get('radius')
    #
    # park = Park()
    # items = park.radius(latitude, longitude, radius)
    # result = []
    # for item in items:
    #     ret, exists = park.getItem(item['name'])
    #     if exists:
    #         result.append(ret)
    # return Response(json.dumps(result), mimetype='application/json')

