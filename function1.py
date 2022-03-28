import pandas as pd

def function_1(dataframe):
    dataframe.sort_values(by=['retweetCount'], inplace=True, ascending=False)
    selection = dataframe[['content', 'retweetCount']]
    print(selection.head(10))
