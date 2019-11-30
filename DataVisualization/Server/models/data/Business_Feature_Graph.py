import pandas as pd


def business_top_features(input_csv, business_id_lst, restaurant_group):
    bdata = pd.read_csv(input_csv)
    bdata_selected = bdata[bdata.apply(lambda x: x['business_id'] in business_id_lst, axis=1)]
    if restaurant_group == 1:
        bdata_group = bdata_selected.loc[(bdata_selected['stars'] >= 4) & (bdata_selected['is_open'] == 1)]
        feature = ['food_type', 'attributes.NoiseLevel', 'attributes.RestaurantsPriceRange2',
                   'attributes.RestaurantsDelivery', 'attributes.Alcohol', 'attributes.RestaurantsGoodForGroups',
                   'attributes.WiFi', 'attributes.RestaurantsReservations', 'attributes.RestaurantsTableService',
                   'attributes.OutdoorSeating']
    elif restaurant_group == 2:
        bdata_group = bdata_selected.loc[(bdata_selected['stars'] < 4) & (bdata_selected['is_open'] == 1)]
        feature = ['casual', 'food_type', 'attributes.Alcohol', 'attributes.WiFi', 'attributes.Caters',
                   'attributes.NoiseLevel', 'attributes.OutdoorSeating', 'attributes.BikeParking', 'lot',
                   'attributes.RestaurantsGoodForGroups']
    else:
        bdata_group = bdata_selected.loc[(bdata_selected['is_open'] == 0)]
        feature = ['food_type', 'attributes.NoiseLevel', 'attributes.Alcohol', 'attributes.RestaurantsPriceRange2',
                   'attributes.OutdoorSeating', 'attributes.Caters', 'attributes.WiFi', 'attributes.HasTV',
                   'attributes.BikeParking', 'attributes.RestaurantsGoodForGroups']
    bgraphdata = top_features(feature, bdata_group)
    return bgraphdata


def top_features(feature_lst, df):
    common_values = []
    for x in feature_lst:
        values = df[x].value_counts()
        if values is not None:
            valuekeys = values.keys().tolist()
            valuecounts = values.tolist()
            if "attributes." in x:
                name_value = x[x.find('.') + 1:] + ' - ' + str(valuekeys[0])
            else:
                name_value = x + ' - ' + str(valuekeys[0])
            prctvalue = valuecounts[0] * 1.0 / len(df[x])
            common_values.append([name_value, prctvalue])
    return common_values


def Business_Feature_Graph(input_file, processed_csv, restaurant_group):
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
