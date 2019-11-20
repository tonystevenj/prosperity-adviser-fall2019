# -*- coding: utf-8 -*-
import json
from flask import Response, request
from ..models import data
import numpy as np
def business():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    items = data.radius('Business', latitude, longitude, radius)
    result = []

    for item in items:
        ret, exists = data.getItem('Business', item['key'])
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

def reviews():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    items = data.radius('Business', latitude, longitude, radius)
    result = set()

    for item in items:
        ret, exists = data.getItem('Business', item['key'])
        if exists:
            result.add(ret['business_id'])

    finaloutput = []
    re = data.base.re
    for i in range(len(re.data)):
        if re.data[i,0] in result:
            finaloutput.append([re.data[i,0],re.data[i,1]])
    nparray = np.array(finaloutput)
    # print(nparray.shape)
    output = re.full_process(nparray.T)
    # print(output.shape)
    list_dic_out = []
    for i in range(len(output)):
        list_dic_out.append({'business_id': str(output[i,0]),
                             'reviews':str(output[i,1])
                             })
    # print(type(list_dic_out[0]))
    return Response(json.dumps(list_dic_out), mimetype='application/json')

def parks():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')
    items = data.radius('Park', latitude, longitude, radius)
    result = []
    for item in items:
        ret, exists = data.getItem('Park', item['key'])
        if exists:
            result.append(ret)
    return Response(json.dumps(result), mimetype='application/json')
