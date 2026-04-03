import pandas as pd
df=pd.read_json('d:/trendpulse-Nanddanaa_Bobba/data/trends_20240115.json',lines=True)
#here used lines=True because I have a json file with multiple dictionaries
print(f"Loaded {len(df)} stories from data/trends_20240115.json")
df.drop_duplicates(subset='post_id', inplace=True)
#dropping duplicates means dropping entire row where post_id is duplicated
print(f"After removing duplicates: {len(df)}")
df = df[(df['post_id'].isna() == False) & (df['title'].isna() == False) & (df['score'].isna() == False)]
#we have dropna with subset but I want to go with filtering 
print(f"After removing nulls: {len(df)}")
df['score'] = df['score'].astype('int')
df['num_comments'] = df['num_comments'].fillna(0).astype('int')
# as scores and num_comments should be integers, but astype is not inplace so we need to reassign back 
df = df[df['score']>=5]
#we are filtering the less scores 
print(f"After removing low scores: {len(df)}")
#here main thing is we need str because strip is string method but df['title'] is serialize wheree we cant apply strip so str makes to apply strip to element wise 
df['title'] = df['title'].str.strip()
print("The number of rows remaining after cleaning:", len(df))
#saving to csv file
df.to_csv('d:/trendpulse-Nanddanaa_Bobba/data/trends_clean.csv', index=False)
print(f"Saved {len(df)} rows to data/trends_clean.csv")
print("Stories per category:")
#groupby is to group and used size 
print(df.groupby('category').size())
#here both are same but value_counts only for one column and sort descening and size for multiple column with groupby and no default sorting 
print(df['category'].value_counts())
