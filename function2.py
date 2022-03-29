
def function_2(dataframe):
    selection = dataframe.value_counts(['userId'])
    print(selection.head(10))