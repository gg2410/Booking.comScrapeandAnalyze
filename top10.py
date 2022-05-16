import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv



columns = ['Average Polarity Score']
data = pd.read_csv('Lab3\HotelListFinal.csv', skiprows=41, nrows=20, usecols=columns)
sec_cols = ['Hotel-Name', 'Average Polarity Score']
data2 = pd.read_csv('Lab3\HotelListFinal.csv', skiprows=41, nrows=20, usecols=sec_cols)

data_list = data['Average Polarity Score'].tolist()
sort_l = sorted(data_list)

data2_dict = data2.to_dict()

print(data2_dict)
print('\n', '\n')
print(sort_l[20:9:-1])

