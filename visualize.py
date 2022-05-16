import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [10.00, 6.50]
plt.rcParams["figure.autolayout"] = True
plt.ylabel('Average Polarity Scores')
plt.xlabel('Comment Ratings')

columns = ["OverallRating", "AveragePolarityScore"]
data = pd.read_csv('Lab3\HotelListFinal.csv', usecols=columns, skiprows=41, nrows=20)

a, b = np.polyfit(data.OverallRating, data.AveragePolarityScore, 1)
plt.plot(data.OverallRating, a*data.OverallRating+b, color='red', linestyle='--', linewidth=2)


plt.scatter(data.OverallRating, data.AveragePolarityScore)
plt.show()

