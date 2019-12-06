import pandas as pd


def business_top_features(bdata_selected, restaurant_group):
    # bdata = pd.read_csv(input_csv)
    # bdata_selected = bdata[bdata.apply(lambda x: x['business_id'] in business_id_lst, axis=1)]
    if restaurant_group == 1:
        bdata_group = bdata_selected.loc[(bdata_selected['stars'].astype(float).fillna(0.0) >= 4) & (
            bdata_selected['is_open'] == '1')]
        feature = {'food_type': 0.0872, 'attributes.NoiseLevel': 0.0574, 'attributes.RestaurantsPriceRange2': 0.0568,
                   'attributes.RestaurantsDelivery': 0.0458, 'attributes.Alcohol': 0.0406, 'attributes.RestaurantsGoodForGroups': 0.0393,
                   'attributes.WiFi': 0.0385, 'attributes.RestaurantsReservations': 0.0373, 'attributes.RestaurantsTableService': 0.037,
                   'attributes.OutdoorSeating': 0.037}
    elif restaurant_group == 2:
        bdata_group = bdata_selected.loc[(bdata_selected['stars'].astype(float).fillna(0.0) < 4) & (
            bdata_selected['is_open'] == '1')]
        feature = {'casual': 0.1134, 'food_type': 0.0869, 'attributes.Alcohol': 0.0866, 'attributes.WiFi': 0.0581, 'attributes.Caters': 0.0502,
                   'attributes.NoiseLevel': 0.0473, 'attributes.OutdoorSeating': 0.0472, 'attributes.BikeParking': 0.0466, 'lot': 0.041,
                   'attributes.RestaurantsGoodForGroups': 0.0406}
    else:
        bdata_group = bdata_selected.loc[(bdata_selected['is_open'] == '0')]
        feature = {'food_type': 0.1075, 'attributes.NoiseLevel': 0.0589, 'attributes.Alcohol': 0.0581, 'attributes.RestaurantsPriceRange2': 0.0577,
                   'attributes.OutdoorSeating': 0.0509, 'attributes.Caters': 0.0502, 'attributes.WiFi': 0.0463, 'attributes.HasTV': 0.0454,
                   'attributes.BikeParking': 0.0445, 'attributes.RestaurantsGoodForGroups': 0.0439}
    bgraphdata = top_features(feature, bdata_group)
    return bgraphdata


def top_features(feature_lst, df):
    common_values = []
    for x in feature_lst:
        values = df[x].value_counts()
        if len(values) == 0:
            continue
        valueTmp = {}
        valuekeys = values.keys().tolist()
        valuecounts = values.tolist()
        if "attributes." in x:
            name_value = x[x.find('.') + 1:]
        else:
            name_value = x
        count = 0
        total = 0.0
        for i in range(len(valuekeys)):
            if count > 4 or valuekeys[i] == '' or valuekeys[i] == 'None':
                continue
            count += 1
            valueTmp[valuekeys[i]] = round(
                valuecounts[i] * 100.0 / len(df[x]), 2)
            total += valueTmp[valuekeys[i]]
        if total < 100:
            valueTmp['other'] = round(100 - total, 2)

        common_values.append(
            {"name": name_value, "value": feature_lst[x], "data": valueTmp})
    return common_values


def Business_Feature_Graph_Old(input_file, processed_csv, restaurant_group):
    # input_file: the json file with business id
    # input_file='F:/Yan/courses/CAP5768/project/data/star45.json'

    # processed_csv: business data file after processing
    # processed_csv='F:/Yan/courses/CAP5768/project/Phoenix_Restaurant/business_Phoenix_Restaurant_processed.csv'

    # restaurant_group: 1 for restaurants with stars>=4 and open; 2 for restaurants with stars less than 1 and open
    # 3 for closed restaurants
    # restaurant_group = 1

    bdata0 = pd.read_json(input_file)
    bids = list(bdata0['business_id'])
    graphdata = business_top_features(processed_csv, bids, restaurant_group)
    return graphdata


def Business_Feature_Graph(business_list, restaurant_group):
    bdata = pd.DataFrame.from_dict(business_list)
    graphdata = business_top_features(bdata, restaurant_group)
    return graphdata
