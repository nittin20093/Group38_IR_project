# -*- coding: utf-8 -*-
"""Ranking system(IR Project)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l90rt4CAp8VKMMx_CmtRavAxHQS92EjF
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
import ast

nltk.download('vader_lexicon')
skywalker = SentimentIntensityAnalyzer()

df=pd.read_csv("/content/drive/MyDrive/IR_Project/goa_hotels_details_final.csv")
x=df["reviews"].to_dict()
score=[]
for i in x:
  res = ast.literal_eval(x[i])
  jedi=pd.DataFrame.from_dict(res, orient='columns')
  jedi["Review_Heading"]=jedi["Review_Heading"].str.replace('”','')
  jedi["Review"] = jedi[['Review_Heading', 'Review_Body']].agg(' '.join, axis=1)
  jedi['sentiment'] = jedi['Review'].apply(lambda x: skywalker.polarity_scores(x)['compound'])
  jedi = jedi.astype({'Review_Rating':'float'})
  result = jedi['Review_Rating'].multiply(jedi['sentiment'], axis="index")
  f=result.mean()
  score.append(f)
df['Score'] = score

df=df.drop(['Unnamed: 0.1'], axis=1)
df=df.drop(['Unnamed: 0'], axis=1)
df=df.drop(['overall_rating'], axis=1)
column_to_move = df.pop("Score")
df.insert(4, "Score", column_to_move)

Sith =df.sort_values('Score', ascending=False) #ranking of hotels according to score
Sith.head()

sith.shape

from google.colab import files
Sith.to_csv('BasicRankedHotels.csv', sep='\t', index=False,header=True)
files.download('BasicRankedHotels.csv')