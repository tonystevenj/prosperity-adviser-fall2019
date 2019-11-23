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

    IDs = data.radius('Business', latitude, longitude, radius)
    result = []

    for id in IDs: # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
        ret, exists = data.getItem('Reviews', id['key'])
        if exists:
            result.append([id['key'],ret])
    re,bool = data.getObj("Reviews")
    nparray = np.array(result)
    output = re.full_process(nparray) #输入形式：(n,2)
    list_dic_out = []
    for i in range(len(output)):
        list_dic_out.append({'business_id': str(output[i,0]),
                             'reviews':str(output[i,1]),
                             'weights':str(output[i,2])
                             })
    # return Response(json.dumps(list_dic_out), mimetype='application/json')

    # calculate top 10 words for whole region:
    whole_words={}
    for i in range(len(output)):
        shop = output[i]
        for j in range(len(shop[1])):
            if shop[1][j] in whole_words:
                whole_words[shop[1][j]] += shop[2][j]
            else:
                whole_words[shop[1][j]] = shop[2][j]
        # whole_words: {food:0.231,mecian:0.3421,....}
    # sort dict(map) according to value
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True) # 这里牛皮，python真的比java省生命多了
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L[:10]), mimetype='application/json')

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
