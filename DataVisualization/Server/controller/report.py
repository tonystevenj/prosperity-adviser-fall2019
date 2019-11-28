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


def reviews0():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    IDs = data.radius('Business', latitude, longitude, radius)
    result_0 = []

    for id in IDs:  # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
        ret, exists = data.getItem('Reviews', id['key'])
        ret2, exists2 = data.getItem('Business', id['key'])
        if exists and exists2:
            star = ret2['stars']
            # print( type(star))  # float
            isopen = ret2['is_open']
            #print("哈哈",type(isopen)) # int
            if isopen == 0:
                result_0.append([id['key'], ret])
    re, bool = data.getObj("Reviews")
    nparray = np.array(result_0)
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
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)  # 这里牛皮，python真的比java省生命多了
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L), mimetype='application/json')
def reviews13():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    IDs = data.radius('Business', latitude, longitude, radius)
    result_13 = []

    for id in IDs:  # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
        ret, exists = data.getItem('Reviews', id['key'])
        ret2, exists2 = data.getItem('Business', id['key'])
        if exists and exists2:
            star = ret2['stars']
            # print( type(star))  # float
            isopen = ret2['is_open']
            #print("哈哈",type(isopen)) # int
            if isopen != 0 and star <4:
                result_13.append([id['key'], ret])
    re, bool = data.getObj("Reviews")
    nparray = np.array(result_13)
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
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)  # 这里牛皮，python真的比java省生命多了
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L), mimetype='application/json')
def reviews45():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    IDs = data.radius('Business', latitude, longitude, radius)
    result_45 = []

    for id in IDs:  # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
        ret, exists = data.getItem('Reviews', id['key'])
        ret2, exists2 = data.getItem('Business', id['key'])
        if exists and exists2:
            star = ret2['stars']
            # print( type(star))  # float
            isopen = ret2['is_open']
            #print("哈哈",type(isopen)) # int
            if isopen != 0 and star >=4:
                result_45.append([id['key'], ret])
    re, bool = data.getObj("Reviews")
    nparray = np.array(result_45)
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
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)  # 这里牛皮，python真的比java省生命多了
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L), mimetype='application/json')
def reviews_backup(category):
    category = 'closed'
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')

    IDs = data.radius('Business', latitude, longitude, radius)
    result_0 = []
    result_13 = []
    result_45 = []

    for id in IDs:  # print(id) : {'key': '_iEl9sCLsvXEFHUWPvgsAg', 'distance': 0.0082}
        ret, exists = data.getItem('Reviews', id['key'])
        ret2, exists2 = data.getItem('Business', id['key'])
        if exists and exists2:
            star = ret2['stars']
            # print( type(star))  # float
            isopen = ret2['is_open']
            #print("哈哈",type(isopen)) # int
            if isopen == 0:
                result_0.append([id['key'], ret])
            else:
                if star >=4:
                    result_45.append([id['key'], ret])
                else:
                    result_13.append([id['key'], ret])
    re, bool = data.getObj("Reviews")
    if category== 'closed':
        nparray = np.array(result_0)
    elif category== 'star13':
        nparray = np.array(result_13)
    elif category== 'star45':
        nparray = np.array(result_45)
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
    L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)  # 这里牛皮，python真的比java省生命多了
    # if u want top 20. then change the number below to 20
    return Response(json.dumps(L), mimetype='application/json')

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
