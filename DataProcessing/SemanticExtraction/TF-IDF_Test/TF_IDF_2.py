# https://blog.csdn.net/baimafujinji/article/details/51476117

from sklearn.feature_extraction.text import TfidfVectorizer
# Documentation: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

text1 = "Python is a 2000 made-for-TV horror movie directed by Richard \
Clabaugh. The film features several cult favorite actors, including William \
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy, \
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the \
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean \
Whalen. The film concerns a genetically engineered snake, a python, that \
escapes and unleashes itself on a small town. It includes the classic final\
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles, \
 California and Malibu, California. Python was followed by two sequels: Python \
 II (2002) and Boa vs. Python (2004), both also made-for-TV films."

text2 = "Python, from the Greek word (πύθων/πύθωνας), is a genus of \
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are \
recognised.[2] A member of this genus, P. reticulatus, is among the longest \
snakes known."

text3 = "The Colt Python is a .357 Magnum caliber revolver formerly \
manufactured by Colt's Manufacturing Company of Hartford, Connecticut. \
It is sometimes referred to as a \"Combat Magnum\".[1] It was first introduced \
in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued \
Colt Python targeted the premium revolver market segment. Some firearm \
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy \
Thompson, Renee Smeets and Martin Dougherty have described the Python as the \
finest production revolver ever made."
corpus = ['This is the first document.',
      'This is the second second document.',
      'And the third one.',
      'Is this the first document?',
          ]
# corpus[1]=text1
# corpus[2]=text2

"""
Question，Oct 29
如果把所有的名词搞定去就太多了，有没有方法筛选我们需要的词

"""
from nltk.corpus import stopwords
stop = stopwords.words('english')
stopwords = {'english','is','and','the','this'}
vectorizer = TfidfVectorizer(min_df=1,stop_words= stop)
# vectorizer = TfidfVectorizer(min_df=1)
vectorizer.fit_transform(corpus)
out1=vectorizer.get_feature_names()
out2=vectorizer.fit_transform(corpus).toarray()
print(out1)
print(out2)
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
vectorizer.vocabulary={'first': 1, 'document': 0, 'second': 3, 'third': 4, 'one': 2}
