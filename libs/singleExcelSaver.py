import pandas as pd

def save(df, filename):

    '''

    :param df: pandas dataframe
    :param filename: end with .xlsx
    :return: None
    '''

    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, "sheet1")
    writer.save()
