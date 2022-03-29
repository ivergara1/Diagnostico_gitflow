import pandas as pd

def function_3(dataframe):
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe['date_d'] = dataframe['date'].dt.to_period('D')
    selection = dataframe.value_counts(['date_d'])
    print(selection.head(10))