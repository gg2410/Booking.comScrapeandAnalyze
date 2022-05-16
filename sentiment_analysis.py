from turtle import pos
import nltk 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


data = pd.read_csv('Lab3\Hotel_List.csv')

sentiments = SentimentIntensityAnalyzer()


positive_scores = [sentiments.polarity_scores(i)["pos"] for i in data["Comment_Text"]]
negative_scores = [sentiments.polarity_scores(i)["neg"] for i in data["Comment_Text"]]
neutral_scores = [sentiments.polarity_scores(i)["neu"] for i in data["Comment_Text"]]
compound = [sentiments.polarity_scores(i)["compound"] for i in data["Comment_Text"]]


csv_scores_dict = {'Positive Scores': positive_scores, 'Negative Scores': negative_scores , 'Neutral Scores': neutral_scores, 'Compound Scores': compound}
new_csv = pd.DataFrame(csv_scores_dict)
new_csv.to_csv('Vaibhav_Hotel_Scores.csv', mode='a')


"""x = sum(positive_scores)
y = sum(negative_scores)
z = sum(neutral_scores)

avg = (x+y+z)/3

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive")
    elif (b>a) and (b>c):
        print("Negative")
    else:
        print("Neutral")
sentiment_score(x, y, z)
print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)

print("Mean Score: ", avg)
"""