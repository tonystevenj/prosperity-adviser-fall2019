import pandas as pd

titles = ['user_id', 'gender', 'age', 'occupation', 'zip']
reviews = pd.read_csv('Data/review_Phoenix.csv', sep='::', header=None,
                      names=titles, engine='python')
print(reviews[0:10])
