# https://blog.csdn.net/liuxuejiang158blog/article/details/31360765

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import csr_matrix
import numpy as np
import math

# 自己写的版本:输入term和term矩阵,输出tf-idf
def steven_tf_idf(matrix,terms):
    # matrix: (3,5), 表示三个文档，5个words
    # terms: len=5, 表示5个words
    # 算法参考:https://stackoverflow.com/questions/36966019/how-aretf-idf-calculated-by-the-scikit-learn-tfidfvectorizer
    matrixnew=np.array(matrix)
    print("哈哈",matrixnew)
    output = np.zeros(matrixnew.shape)
    if len(matrixnew.T)!=len(terms):
        print("lenth do not match!")
        return
    ducomentsnum=len(matrixnew)
    linesums=[]
    for i in range(len(matrixnew)):
        linesum=0
        for num in matrixnew[i]:
            linesum+=num
        linesums.append(linesum)


    #包含词条w的文档数
    ducomentsnumwithWs =[]
    tem = matrixnew.T
    for i in range(len(tem)):
        ducomentsnumwithW = 0
        for j in range(len(tem[i])):
            if tem[i][j]!=0:
                ducomentsnumwithW+=1
        ducomentsnumwithWs.append(ducomentsnumwithW)

    #找最大的tf:
    maxlinetfs=[]
    for i in range(len(matrixnew)):
        tem = 0
        for j in range(len(matrixnew[i])):
            tf=matrixnew[i][j]/linesums[i]
            tem = max(tf,tem)
        maxlinetfs.append(tem)


    # 计算tf-idf
    for i in range(len(matrixnew)):
        for j in range(len(matrixnew[i])):
            tf=(matrixnew[i][j]/linesums[i])/maxlinetfs[i]
            idf=math.log((ducomentsnum+1)/(ducomentsnumwithWs[j]+1),math.e)+1
            output[i][j]=tf*idf
    return output
corpus = ['This is the first document.',
          'This is the second second document.',
          'And the third one.',
          'Is this the first document?', ]
corpus = ['This is a string','This is another string','TFIDF computation calculation','TfIDF is the product of TF and IDF']
if __name__ == "__main__":
    from nltk.corpus import stopwords
    stop = stopwords.words('english')
    vectorizer = CountVectorizer(stop_words=stop)  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    matrix=vectorizer.fit_transform(corpus)
    tfidf = transformer.fit_transform(matrix)  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

    """"""
    newweight= steven_tf_idf(matrix.toarray(),word)
    """"""
    print(newweight)
    print("***************")
    print(weight)
    print(word)
    # for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    #     print (u"-------这里输出第",i,u"类文本的词语tf-idf权重------")
    #     for j in range(len(word)):
    #         print (word[j], weight[i][j])
