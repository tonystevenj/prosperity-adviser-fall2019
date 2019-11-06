import pandas as pd


def processToMiddata(fPath, toName="midData"):
    reviews = pd.read_csv(fPath, sep=',', header=None, engine='python')
    reviews.columns = reviews.iloc[0]
    new3 = reviews.drop(0)
    new3.reset_index(drop=True, inplace=True)
    new4 = new3.drop(['review_id', 'cool', 'useful', 'user_id', 'funny', 'date', 'stars'], axis=1)
    new5 = new4.groupby('business_id').agg(lambda x: '&'.join(set(x)))

    for i in range(41):
        new5[100*i:100*(i+1)].to_csv(f'midDataes/{toName}{i}.csv')
