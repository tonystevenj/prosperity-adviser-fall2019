# -*- coding: utf-8 -*-
import json
from flask import Response, request
from ..models import data
import numpy as np
from ..models.data import Business_Feature_Graph as bfg


def business():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    zipcode = request.args.get('zipcode')

    items = data.radius('Business', longitude, latitude, radius)
    result = {
        'open_count': 0,
        'close_count': 0,
        'total_earners': 0,
        'population': 0,
        'business': []
    }

    # 分析business数据
    for item in items:
        ret, exists = data.getItem('Business', item['key'])
        if exists:
            if ret['is_open'] == '1':
                result['open_count'] += 1
            else:
                result['close_count'] += 1
            result['business'].append({
                'business_id': ret['business_id'],
                'name': ret['name'],
                'is_open': ret['is_open'],
                'longitude': ret['longitude'],
                'latitude': ret['latitude'],
                'stars': ret['stars'],
                'review_count': ret['review_count']
            })

    # 分析population数据
    ret, exists = data.getItem('Population', zipcode)
    if exists:
        result['total_earners'] = ret['total_earners']
        result['population'] = ret['population']

    return Response(json.dumps(result), mimetype='application/json')


def reviews():
    category = request.args.get('category')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')
    # print("哈哈",category)
    IDs = data.radius('Business', longitude, latitude, radius)
    result_0 = []
    result_13 = []
    result_45 = []
    reviewInfo_closed = {
        'reviewAmount': 0,
        'businessAmount': 0,
    }
    reviewInfo_star13 = {
        'reviewAmount': 0,
        'businessAmount': 0,
    }
    reviewInfo_star45 = {
        'reviewAmount': 0,
        'businessAmount': 0,
    }
    # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
    for id in IDs:
        # print(id)
        ret, exists = data.getItem('Reviews', id['key'])
        ret2, exists2 = data.getItem('Business', id['key'])
        print(ret2)
        # print(exists, exists2)
        if exists and exists2:
            star = ret2['stars']
            # print(type(star))  # float
            isopen = ret2['is_open']
            # print("哈哈", type(isopen), isopen)  # int
            if float(isopen) == 0:
                result_0.append([id['key'], ret])
                reviewInfo_closed['reviewAmount'] += int(ret2['review_count'])
                reviewInfo_closed['businessAmount'] += 1
            else:
                if float(star) >= 4:
                    result_45.append([id['key'], ret])
                    reviewInfo_star45['reviewAmount'] += int(ret2['review_count'])
                    reviewInfo_star45['businessAmount'] += 1
                else:
                    result_13.append([id['key'], ret])
                    reviewInfo_star13['reviewAmount'] += int(ret2['review_count'])
                    reviewInfo_star13['businessAmount'] += 1
    # print(len(result_0), "呼呼")
    # print(len(result_13))
    # print(len(result_45))
    if category == 'closedinfo':
        return Response(json.dumps(reviewInfo_closed), mimetype='application/json')
    if category == 'star13info':
        return Response(json.dumps(reviewInfo_star13), mimetype='application/json')
    if category == 'star45info':
        return Response(json.dumps(reviewInfo_star45), mimetype='application/json')

    re, bool = data.getObj("Reviews")
    nparray = None
    if category == 'closed':
        nparray = np.array(result_0)
    elif category == 'star13':
        nparray = np.array(result_13)
    elif category == 'star45':
        nparray = np.array(result_45)
    if (len(nparray) == 0):
        return Response(json.dumps([["No data", 50], ["", 40]]), mimetype='application/json')
    output = re.full_process(nparray)  # 输入形式：(n,2)
    list_dic_out = []
    for i in range(len(output)):
        list_dic_out.append({'business_id': str(output[i, 0]),
                             'reviews': str(output[i, 1]),
                             'weights': str(output[i, 2])
                             })
    # return Response(json.dumps(list_dic_out), mimetype='application/json')

    # calculate top 10 words for whole region:
    whole_words = {}
    for i in range(len(output)):
        shop = output[i]
        for j in range(len(shop[1])):
            if shop[1][j] in whole_words:
                whole_words[shop[1][j]] += shop[2][j]
            else:
                whole_words[shop[1][j]] = shop[2][j]
        # whole_words: {food:0.231,mecian:0.3421,....}
    # sort dict(map) according to value
    # 这里牛皮，python真的比java省生命多了
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L), mimetype='application/json')


def parks():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    items = data.radius('Park', longitude, latitude, radius)
    result = []
    for item in items:
        ret, exists = data.getItem('Park', item['key'])
        if exists:
            result.append(ret)
    return Response(json.dumps(result), mimetype='application/json')
