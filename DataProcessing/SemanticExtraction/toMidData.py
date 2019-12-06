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
