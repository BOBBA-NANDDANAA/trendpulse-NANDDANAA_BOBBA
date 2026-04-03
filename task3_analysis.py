import pandas as pd
df=pd.read_csv('d:/trendpulse-Nanddanaa_Bobba/data/trends_clean.csv')
#loading csv into dataframe.
print("Loaded data:", df.shape)
#used df.shape to find the number of rows and columns 
print("\nFirst 5 rows:\n",df.head())
#see wheather data loaded properly or not.
print("Average score: ", df['score'].mean())
print("Average comments: ", df['num_comments'].mean())
#using pandas we calculated mean 
print("\n--- NumPy Stats ---")
#using numpy we calculate and also in numpy we can do 

import numpy as np
avg=np.mean(df['score'])

print("Mean score: ", avg)
#median
print("Median score: ", np.median(df['score']))      
#std
#max score
print("Std deviation: ", np.std(df['score']))

print("Max score: ", np.max(df['score']))
print("Min score: ", np.min(df['score']),"\n")
#using numpy only to find the category where most stories is becasue in that section asked to use numpy
#without return_counts=False we don't get counts we get only unique categories

category, counts= np.unique(df['category'], return_counts=True)
#argmin is used to find the index of max so we can use that index to find category name to print
max_index=np.argmax(counts)
print("Most stories in: ", category[max_index])
#most commented story so here we get the index where maximum value fro num_comments
index=np.argmax(df['num_comments'])
#taken title
title=df.iloc[index, 0]
#taken comment_count used iloc because i know the index not label
comment_count=df.iloc[index, 3]
print("Most commented story: ", title, "-", comment_count,"\n")
#adding new columns and pandas do element wise internally 
df['engagement'] = df['num_comments']/(df['score'] + 1)
df['is_popular'] = df['score'] > avg
print("First five rows just for test:")
print(df.head())
df.to_csv('d:/trendpulse-Nanddanaa_Bobba/data/trends_analysed.csv', index=False)
print("\nSaved to data/trends_analysed.csv")