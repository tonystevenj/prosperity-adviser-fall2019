import pandas as pd


def processToMiddata(fPath, toName="midData"):
    reviews = pd.read_csv(fPath, sep=',', header=None, engine='python')
    reviews.columns = reviews.iloc[0]
    new3 = reviews.drop(0)
    new3.reset_index(drop=True, inplace=True)
    new4 = new3.drop(['review_id', 'cool', 'useful', 'user_id', 'funny', 'date', 'stars'], axis=1)
    new5 = new4.groupby('business_id').agg(lambda x: '&'.join(set(x))).reset_index()
    for i in range(len(new5)):
        new5[i:i+1].to_csv(f'midDataes_Single/{new5.iloc[i,0]}.csv')
# processToMiddata('Data/review_Phoenix.csv')

# # test   .agg(lambda x: '&'.join(set(x))
# print(type('&'))
# str1="I am stevenJ"
# print(set(str1))
# out='&'.join(set(str1))
# print(out)
#
# strs=[]
# str01 = "this restrant is bad"
# str02 = "Food is dilecious"
# set1 = set(strs)
# print(len(set1))
# set1.add(str01)
# print(str01 in set1)
# print(set1)
# print("*******************")
# print(set(str01))
# print(set(str02))
# print(type(set(strs)))
# print(type(set(str01)))

# test 2 .agg(lambda x: '&'.join(set(x))
# 了解到python的内置函数list()，是通过调用__iterable__函数实现之后（原理和print调用tostring是一样的）
# 回来看刚才的实验：为什么我输入 strs 到set(x)里面就不能正常输出，原来是类型的问题，
# .agg(lambda x: '&'.join(set(x))这里的x很可能传入的是series类型，所以他有值，我没有
# pd.Series.__iter__()这个函数是定义了的，继承自父类 base.IndexOpsMixin

str01 = "this restrant is bad"
str02 = "Food is dilecious"
series_3=pd.Series([str01,str02])
print(set(series_3))
print(type(series_3))
# 果然如此！ list就不行！
list01=[str01,str02]
print(set(list01))

# 瓜皮，list也可以，原来是我刚才没有在创建的list里面加入元素，我是瓜皮：
# strs=[]
# str01 = "this restrant is bad"
# str02 = "Food is dilecious"
# set1 = set(strs)    这里strs本来就是空的，怎么输出嘛！