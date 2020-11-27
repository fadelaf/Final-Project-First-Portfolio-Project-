import pickle

from pandas import DataFrame, get_dummies
import pandas as pd

model = pickle.load(open('final.sav','rb'))
encode_columns = pickle.load(open('x_colomn.sav','rb'))


def prediction_data(data):
    df = pd.DataFrame(data, index=[0])
    df = pd.get_dummies(df)
    df = df.reindex(columns=encode_columns, fill_value = 0)
    hasil = model.predict(df)
    return (hasil[0])