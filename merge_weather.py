import pandas as pd
from datetime import datetime
import numpy as np
import collections



def load_data(file):

    df = pd.read_csv(file, sep=',', header=0, parse_dates=[0])
    return df


def match_dates():

    metrorail_data = load_data('metrorail.csv')
    weather_data = load_data('weather.csv')

    print metrorail_data
    print weather_data

    # for index1, row1 in weather_data.iterrows():
    #     weather_row = row1['DATE'].to_pydatetime()
    #
    #     for index, row in metrorail_data.iterrows():
    #
    #         if row['Date'].to_pydatetime() == weather_row:
    #             metrorail_data.assign(weather_row)

    result = pd.merge(left=metrorail_data,right=weather_data, left_on='Date', right_on='DATE')

    result.to_csv('blah.csv')
match_dates()

