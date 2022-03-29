import pandas as pd

def function_1(dataframe):
    dataframe.sort_values(by=['retweetCount'], inplace=True, ascending=False)
    selection = dataframe[['tweetUrl', 'retweetCount']]
    print(selection.head(10))
