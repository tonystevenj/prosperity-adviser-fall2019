# -*- coding: utf-8 -*-
import json
from flask import Response, request
from ..models import data
import numpy as np
from ..models.data import Business_Feature_Graph as bfg
import math
import pandas as pd


def business():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    zipcode = request.args.get('zipcode')

    items = data.radius('Business', longitude, latitude, radius)
    result = {
        'open_count': 0,
        'stars45': 0,
        'stars03': 0,
        'close_count': 0,
        'median_earnings': 0,
        'population': 0,
        'business': []
    }

    # 分析business数据
    for item in items:
        ret, exists = data.getItem('Business', item['key'])
        if exists:
            if ret['is_open'] == '1':
                result['open_count'] += 1
                if float(ret['stars']) >= 4:
                    result['stars45'] += 1
                else:
                    result['stars03'] += 1
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
        result['median_earnings'] = ret['median_earnings']
        result['population'] = ret['population']

    return Response(json.dumps(result), mimetype='application/json')

import datetime as d
def reviews():
    print("进入review")
    print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    category = request.args.get('category')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')
    # print("哈哈",category)
    IDs = data.radius('Business', longitude, latitude, radius)
    print("redius反应时间")
    print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
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
        # print(exists, exists2)
        if exists and exists2:
            star = ret2['stars']
            # print(type(star))  # float
            isopen = ret2['is_open']
            # print("哈哈", type(isopen), isopen)  # int
            if float(isopen) == 0:
                result_0 .append(ret)
                reviewInfo_closed['reviewAmount'] += int(ret2['review_count'])
                reviewInfo_closed['businessAmount'] += 1
            else:
                if float(star) >= 4:
                    result_45 .append(ret)
                    reviewInfo_star45['reviewAmount'] += int(
                        ret2['review_count'])
                    reviewInfo_star45['businessAmount'] += 1
                else:
                    result_13 .append(ret)
                    reviewInfo_star13['reviewAmount'] += int(
                        ret2['review_count'])
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
    result=[['closed'," ".join(result_0)],['star 1 3'," ".join(result_13)],['star 4 5'," ".join(result_45)]]
    nparray = None

    # if category == 'closed':
    #     nparray = np.array(result_0)
    # elif category == 'star13':
    #     nparray = np.array(result_13)
    # elif category == 'star45':
    #     nparray = np.array(result_45)
    if category == "reviewsfeature":
        nparray = np.array(result)
        # print(nparray.shape)
    if (len(nparray) == 0):
        return Response(json.dumps([["No data", 50], ["", 40]]), mimetype='application/json')
    print("数据准备完成")
    print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    # try:
    output = re.full_process(nparray)  # 输入形式：(n,2)
    # except Exception as e:
    #     print("reviews api", e)
    #     return Response(json.dumps([["No data", 50], ["", 40]]), mimetype='application/json')
    print("TF-IDF时间")
    print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    # list_dic_out = []
    # for i in range(len(output)):
    #     list_dic_out.append({'category': str(output[i, 0]),
    #                          'reviews': str(output[i, 1]),
    #                          'weights': str(output[i, 2])
    #                          })
    # print("字典输出时间")
    #
    # print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    # return Response(json.dumps(list_dic_out), mimetype='application/json')

    # do iterative TF-IDF:
    allinfodict={}
    print(output)
    print(output[0, 1])
    print(output[0, 1][0])
    for i in range(len(output)):
        for j in range(len(output[i, 1])):
            if str(output[i,1][j]) in allinfodict:
                allinfodict[str(output[i,1][j])][i]=int(output[i, 2][j]*100)
            else:
                allinfodict[str(output[i,1][j])]=[0,0,0]
                allinfodict[str(output[i,1][j])][i]=int(output[i, 2][j]*100)
    terms=[]
    matrix=[]
    for key in allinfodict:
        terms.append(key)
        matrix.append(allinfodict[key])
    matrix=np.array(matrix).T.tolist()
    print('呱呱',matrix[0])
    print('呱呱',matrix[1])
    print('呱呱',matrix[2])
    def steven_tf_idf(matrix, terms):
        # matrix: (3,5), 表示三个文档，5个words
        # terms: len=5, 表示5个words
        # 算法参考:https://stackoverflow.com/questions/36966019/how-aretf-idf-calculated-by-the-scikit-learn-tfidfvectorizer
        matrixnew = np.array(matrix)
        print("哈哈", matrixnew)
        output = np.zeros(matrixnew.shape)
        if len(matrixnew.T) != len(terms):
            print("lenth do not match!")
            return
        ducomentsnum = len(matrixnew)
        linesums = []
        for i in range(len(matrixnew)):
            linesum = 0
            for num in matrixnew[i]:
                linesum += num
            linesums.append(linesum)

        # 包含词条w的文档数
        ducomentsnumwithWs = []
        tem = matrixnew.T
        for i in range(len(tem)):
            ducomentsnumwithW = 0
            for j in range(len(tem[i])):
                if tem[i][j] != 0:
                    ducomentsnumwithW += 1
            ducomentsnumwithWs.append(ducomentsnumwithW)

        # 找最大的tf:
        maxlinetfs = []
        for i in range(len(matrixnew)):
            tem = 0
            for j in range(len(matrixnew[i])):
                tf = matrixnew[i][j] / linesums[i]
                tem = max(tf, tem)
            maxlinetfs.append(tem)

        # 计算tf-idf
        for i in range(len(matrixnew)):
            for j in range(len(matrixnew[i])):
                tf = (matrixnew[i][j] / linesums[i]) / maxlinetfs[i]
                idf = math.log((ducomentsnum + 1) / (ducomentsnumwithWs[j] + 1), math.e) + 1
                output[i][j] = tf * idf
        return output

    second_tf_idf=steven_tf_idf(matrix,terms)

    termslist=[]
    # 排序:
    for k in range(3):
        for i in range(len(second_tf_idf[k])):
            reviews=terms.copy()
            weight=second_tf_idf[k]
            # 冒泡排序:
            for i in range(len(weight)-1):
                for j in range(len(weight)-1):
                    if weight[i]<weight[i+1]:
                        tem = weight[i]
                        weight[i] = weight[i+1]
                        weight[i+1]=tem

                        tem2 = reviews[i]
                        reviews[i] = reviews[i + 1]
                        reviews[i + 1] = tem2
            termslist.append(reviews)
    labels = ['closed', 'star13', 'star45']
    list_dic_out = []
    for i in range(len(second_tf_idf)):
        list_dic_out.append({'category': str(labels[i]),
                             'reviews': str(termslist[i]),
                             'weights': str(second_tf_idf[i])
                             })
    print("字典输出时间")
    print(d.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    return Response(json.dumps(list_dic_out), mimetype='application/json')


    # # calculate top 10 words for whole region:
    # whole_words = {}
    # for i in range(len(output)):
    #     shop = output[i]
    #     for j in range(len(shop[1])):
    #         if shop[1][j] in whole_words:
    #             whole_words[shop[1][j]] += shop[2][j]
    #         else:
    #             whole_words[shop[1][j]] = shop[2][j]
    #     # whole_words: {food:0.231,mecian:0.3421,....}
    # # sort dict(map) according to value
    # # 这里牛皮，python真的比java省生命多了
    # L = sorted(whole_words.items(), key=lambda item: item[1], reverse=True)
    # # if u want top 20. then change the number below to 20
    # return Response(json.dumps(L), mimetype='application/json')


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


def feature():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    category = request.args.get('category')

    items = data.radius('Business', longitude, latitude, radius)

    dataTmp = []
    group = None

    for item in items:
        ret, exists = data.getItem('Business', item['key'])
        if category == 'closed' and ret['is_open'] == '0':
            group = 3
            dataTmp.append(ret)
        if category == 'star45' and ret['is_open'] == '1' and float(ret['stars']) >= 4:
            group = 1
            dataTmp.append(ret)
        elif category == 'star13' and ret['is_open'] == '1' and float(ret['stars']) > 0 and float(ret['stars']) < 4:
            group = 2
            dataTmp.append(ret)
    try:
        response = bfg.Business_Feature_Graph(dataTmp, group)
    except Exception as e:
        print('feature api', e)
        response = []
    return Response(json.dumps(response), mimetype='application/json')


def table():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    result = {
        'business': [],
        'park': [],
        'school': [],
        'pride': [],
        'hospital': [],
        'rail': [],
    }

    # business数据
    items = data.radius('Business', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('Business', item['key'])
        ret['distance'] = item['distance']
        result['business'].append(ret)

    # park数据
    items = data.radius('Park', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('Park', item['key'])
        ret['distance'] = item['distance']
        result['park'].append(ret)

    # school数据
    items = data.radius('School', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('School', item['key'])
        ret['distance'] = item['distance']
        result['school'].append(ret)

    # Hospital数据
    items = data.radius('Hospital', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('Hospital', item['key'])
        ret['distance'] = item['distance']
        result['hospital'].append(ret)

    # Pride数据
    items = data.radius('Pride', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('Pride', item['key'])
        ret['distance'] = item['distance']
        result['pride'].append(ret)

    # Rail数据
    items = data.radius('Rail', longitude, latitude, radius)
    for item in items:
        ret, exists = data.getItem('Rail', item['key'])
        ret['distance'] = item['distance']
        result['rail'].append(ret)

    return Response(json.dumps(result), mimetype='application/json')


def score():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = int(request.args.get('radius'))
    area_size = math.pi * radius * radius
    park_percentage = float(request.args.get('park_percentage'))
    school_percentage = float(request.args.get('school_percentage'))
    pride_percentage = float(request.args.get('pride_percentage'))
    hospital_percentage = float(request.args.get('hospital_percentage'))
    rail_percentage = float(request.args.get('rail_percentage'))
    salary_percentage = float(request.args.get('salary_percentage'))
    population_percentage = float(request.args.get('population_percentage'))
    zipcode = request.args.get('zipcode')
    # convert 5 percentage into 100% in total:
    sum = park_percentage + school_percentage + pride_percentage + \
          hospital_percentage + rail_percentage + salary_percentage + population_percentage
    park_percentage = park_percentage / sum
    school_percentage = school_percentage / sum
    pride_percentage = pride_percentage / sum
    hospital_percentage = hospital_percentage / sum
    rail_percentage = rail_percentage / sum
    salary_percentage = salary_percentage / sum
    population_percentage = population_percentage / sum
    result = 0

    maxdata = {
        'park': 1.201385924,
        'school': 5.815748132,
        'pride': 2.31007695,
        'hospital': 0.340240332,
        'rail': 0.373340781,
        'salary': 61968,
        'population': 70008
    }

    def calculateScore(current, max):
        if current > max:
            return 1
        return current / max

    # park数据
    items = data.radius('Park', longitude, latitude, radius)
    park_score = calculateScore(len(items) / area_size, maxdata['park'])
    result += park_score * park_percentage

    # school数据
    items = data.radius('School', longitude, latitude, radius)
    School_score = calculateScore(len(items) / area_size, maxdata['school'])
    result += School_score * school_percentage

    # Hospital数据
    items = data.radius('Hospital', longitude, latitude, radius)
    Hospital_score = calculateScore(
        len(items) / area_size, maxdata['hospital'])
    result += Hospital_score * hospital_percentage

    # Pride数据
    items = data.radius('Pride', longitude, latitude, radius)
    Pride_score = calculateScore(len(items) / area_size, maxdata['pride'])
    result += Pride_score * pride_percentage

    # Rail数据
    items = data.radius('Rail', longitude, latitude, radius)
    Rail_score = calculateScore(len(items) / area_size, maxdata['rail'])
    result += Rail_score * rail_percentage

    # salary数据
    ret, exists = data.getItem('Population', zipcode)
    median_earnings = 0
    population = 0
    if exists:
        median_earnings = ret['median_earnings']
        population = ret['population']

    result += (median_earnings / maxdata['salary']) * salary_percentage
    # population数据
    result += (population / maxdata['population']) * population_percentage
    # print(salary_percentage)
    # print(population_percentage)
    # print((median_earnings / maxdata['salary']) * salary_percentage)
    # print((population/maxdata['population'])*population_percentage)
    return Response(json.dumps(result), mimetype='application/json')


def score_data():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = int(request.args.get('radius'))
    zipcode = request.args.get('zipcode')

    result = {
        'park': {
            'sum': 0,
            'max': 1.201385924
        },
        'school': {
            'sum': 0,
            'max': 5.815748132
        },
        'pride': {
            'sum': 0,
            'max': 2.31007695
        },
        'hospital': {
            'sum': 0,
            'max': 0.340240332
        },
        'rail': {
            'sum': 0,
            'max': 0.373340781
        },
        'salary': {
            'sum': 0,
            'max': 61968},
        'population': {
            'sum': 0,
            'max': 70008
        }
    }

    # park数据
    items = data.radius('Park', longitude, latitude, radius)
    result['park']['sum'] = len(items)

    # school数据
    items = data.radius('School', longitude, latitude, radius)
    result['school']['sum'] = len(items)

    # Hospital数据
    items = data.radius('Hospital', longitude, latitude, radius)
    result['hospital']['sum'] = len(items)

    # Pride数据
    items = data.radius('Pride', longitude, latitude, radius)
    result['pride']['sum'] = len(items)

    # Rail数据
    items = data.radius('Rail', longitude, latitude, radius)
    result['rail']['sum'] = len(items)

    # salary数据
    ret, exists = data.getItem('Population', zipcode)
    median_earnings = 0
    population = 0
    if exists:
        result['salary']['sum'] = ret['median_earnings']
        result['population']['sum'] = ret['population']

    return Response(json.dumps(result), mimetype='application/json')


def crime():
    zipcode = request.args.get('zipcode')
    result = {}
    ret, exists = data.getItem('Crime', zipcode)
    if exists:
        for i in ret:
            # http://dmcoders.com/2018/03/10/python-pandasdatatime/#%E4%B8%89%E6%9C%80%E5%90%8E%E4%BD%BF%E7%94%A8%E7%AE%80%E4%BE%BF%E5%87%BD%E6%95%B0resample%E8%BF%9B%E8%A1%8C%E5%88%86%E7%BB%84%E8%81%9A%E5%90%88%E8%BF%90%E7%AE%97%E7%AD%89%E6%93%8D%E4%BD%9C
            pdData = pd.DataFrame.from_dict(ret[i])
            pdData['occurred on'] = pd.to_datetime(pdData['occurred on'])
            pdData = pdData.set_index('occurred on', drop=True)
            pdData['value'] = 1
            df2 = pdData.resample('M')['value'].sum()
            tmpJSON = df2.to_json()
            tmpDict = json.loads(tmpJSON)
            result[i] = tmpDict

    return Response(json.dumps(result), mimetype='application/json')
