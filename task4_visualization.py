import pandas as pd
df=pd.read_csv('d:/trendpulse-Nanddanaa_Bobba/data/trends_analysed.csv')
import matplotlib.pyplot as plt
#here i am getting index of top 10 scores so i can get the title
top=df['score'].sort_values(ascending=False)[:10].index
#topt=df['score'].sort_values(ascending=False)[:10].values this gives values of scores not index 
top2=df['score'].sort_values(ascending=False)[:10] #only score row we get as a serialized  #direct top 10 values

##df1=df.sort_values(by='score',ascending=False)[:10] #all rows we get as a dataframe
#####plt.barh(df1['title'][:50],df1['score'])
#i want to all methods as a practice so i am doing in different way
plot1= plt.barh([df['title'].iloc[i][:50] for i in top], top2)
#then length less than 50
plt.xlabel('Score')
plt.ylabel('Title')
plt.title('Top 10 Stories by Score')
plt.savefig('d:/trendpulse-Nanddanaa_Bobba/outputs/chart1_top_stories.png')
plt.show()

#2
#plt.bar(df['category'].unique(), df['category'].value_counts())
#print("Categories:", df['category'].unique())
#print("Category Counts:", df['category'].value_counts())
#valuecounts give categgory and no of times it occured in descending but for i in value_counts give only value. 
#we have index, values, items()
value_counts=df['category'].value_counts() 
unique=df['category'].unique() #unique category 
#print(value_counts["technology"]) for i in value_counts: gives i means values not indexes 
# here x is unique catgories but y is count of x taken from unique to value_counts.
#value_counts[i] here i means category not value
#for i in value_counts give i is count

plot2=plt.bar(unique, [value_counts[i] for i in unique],color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.title('Number of Stories per Category')
plt.savefig('d:/trendpulse-Nanddanaa_Bobba/outputs/chart2_categories.png')
plt.show()


#3
plot3=plt.scatter(df['score'], df['num_comments'],color=df['is_popular'].map({True: 'green', False: 'red'}))
#all are easy but color we can do mapping because we are coloring bsed on different values in is_popular column
plt.xlabel('Score')
plt.ylabel('Number of Comments')
plt.title('Score vs Number of Comments (Green: Popular, Red: Not Popular)')
plt.savefig('d:/trendpulse-Nanddanaa_Bobba/outputs/chart3_scatter.png')

plt.show()

#this is for subplot here we need figsize becasue there should be no compression in image 
fig, axes = plt.subplots(1,3, figsize=(18, 6))
axes[0].barh([df['title'].iloc[i][:50] for i in top], top2)
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Title') 
axes[0].set_title('Top 10 Stories by Score')
axes[1].bar(unique, [value_counts[i] for i in unique],color=['blue', 'orange', 'green', 'red', 'purple'])
axes[1].set_xlabel('Category')
axes[1].set_ylabel('Number of Stories')
axes[1].set_title('Number of Stories per Category')
axes[2].scatter(df['score'], df['num_comments'],color=df['is_popular'].map({True: 'green', False: 'red'}))
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Comments')
axes[2].set_title('Score vs Number of Comments (Green: Popular, Red: Not Popular)')
plt.suptitle("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig('d:/trendpulse-Nanddanaa_Bobba/outputs/dashboard.png')
plt.show()

#print(df['category'].size)   === print(len(df['category'])) != df['category'].nunique() because nunique is for unique values count but size is total count of rows in that column