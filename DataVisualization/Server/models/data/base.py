from ...models.dao import redisDao

# 对象寄存
objMap = {}
# 数据寄存
dataMap = {}
# redis
redis = redisDao.connect()


def regObj(obj):
    """ 注册数据处理对象
        Args:
            obj: 数据处理对象
        Return: Object
    """
    objMap[getObjName(obj)] = obj
    dataMap[getObjName(obj)] = {}


def getObj(name):
    """ 获取对象
        Args:
            name: 数据处理对象的类名
        Return: Object
    """
    if name in objMap:
        return objMap[name], True
    return None, False


def getObjName(obj):
    """ 获取对象名称
        Args:
            obj: 数据处理对象
        Return: String
    """
    return obj.__class__.__name__


def radius(name, longitude, latitude, radius, unit='mi'):
    """ 获取地点半径内的数据
        Args:
            name: 类名，比如Business
            longitude: 精度
            latitude: 纬度
            radius: 半径
            unit: 单位，默认mi英里
        Return: list
    """
    result = []
    geoList = redis.georadius('afrss_'+name, longitude=longitude, latitude=latitude, radius=radius,
                              unit=unit, withdist=True, withcoord=False, withhash=False, count=None,
                              sort='ASC', store=None, store_dist=None)
    for item in geoList:
        result.append({
            'business_id': item[0].decode('utf-8'),
            'distance': item[1],
        })
    return result


def getItem(name, key):
    """ 获取数据
        Args:
            name: 类名，比如Business
            key: 唯一标识
        Return: dict
    """
    if name in dataMap and key in dataMap[name]:
        return dataMap[name][key], True
    return None, False


def getItems(name, keys):
    """ 批量获取数据
        Args:
            name: 类名，比如Business
            keys: list 唯一标识
        Return: dict
    """
    result = {}
    for key in keys:
        data, exists = getItem(name, key)
        if exists:
            result[key] = data
        else:
            result[key] = None
    return result


def setItem(name, key, item):
    """ 设置数据
        Args:
            name: 类名，比如Business
            key: 唯一标识
            item: 数据
        Return: bool
    """
    if name in dataMap:
        dataMap[name][key] = item
        return True
    return False


def setItems(name, items):
    """ 批量设置数据
        Args:
            name: 类名，比如Business
            items: dict 数据
        Return: bool
    """
    if name in dataMap:
        for key in items:
            setItem(name, key, items[key])
    return False


def setGeoItems(name, items):
    """ 批量设置地理位置数据
        Args:
            name: 类名，比如Business
            items: dict 数据
        Return: 成功写入的个数
    """
    split = 1000 * 3
    count = 0
    valueInput = []
    i = 0
    for key in items:
        valueInput.append(items[key]['longitude'])
        valueInput.append(items[key]['latitude'])
        valueInput.append(key)
        i += 1
        if i == split:
            count += redis.geoadd('afrss_'+name, *valueInput)
            valueInput = []
            i = 0
    if len(valueInput) > 0:
        count += redis.geoadd('afrss_'+name, *valueInput)
    return count


def load(service):
    """ 加载数据
        Args:
            service: bool 运行类型，True为服务形式运行，False为脚本形式运行初始化
    """
    for name in objMap:
        items, geoItems = objMap[name].load()
        if service and items and len(items) > 0:
            status = setItems(name, items)
            print('Data load: [{}] has {} items load successed'.format(
                name, len(items)))
        if not service and geoItems and len(geoItems) > 0:
            count = setGeoItems(name, geoItems)
            print('Data load: [{}] has {} geo items load successed'.format(
                name, count))
