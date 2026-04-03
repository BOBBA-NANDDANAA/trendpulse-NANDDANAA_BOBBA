import requests
import time
from datetime import datetime
import json 

headers = {"User-Agent": "TrendPulse/1.0"}
#as per problem we need header so taken

try:
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json",headers=headers)
    #first response to read the story id's
    list1 = response.json()[:500] #response.json gives it as list  i have seen type(list1) as list and taken only first 500 
    response2 = {} #dumpy dictionary used to store each story id data like story id: {data of that story id}
    for i in list1:
        try:
            response3 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json",headers=headers)
            #this response3 takes only data of id i
            #and this data is used in resonse 
            response2[i] = response3.json()
        except Exception as e:
            #exception check because program shouldnot crash
            print(f"Failed to fetch story {i}: {e}")
            continue
#taking all categories into category dictionary with key as category and values as list
    categories = {
        "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
        "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
        "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
        "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
        "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
    }

    
    category={}
    #taken new dummy dictionary category where my goal is category as key and list of story id they are belong to that category 
    for cat, keywords in categories.items():
        list2=[]
        #empty list to store story id of that category we need to empty it for each category 
        for key, value in response2.items():
            title = str(value.get('title')).lower() #it handles no title condition without giving error
            if any(k.lower() in title for k in keywords):
                list2.append(key)
                #stored entire for that category key
        category[cat]=list2
        time.sleep(2)

    extracted_fields={}
    count=0
#another dummy dictionary to store the extracted fields 
    for key, value in category.items():
        for i in value[:26]:
            extracted_fields['post_id']=response2[i]['id']
            extracted_fields['title']=response2[i]['title']
            extracted_fields['category']=key
            extracted_fields['score']=response2[i]['score']
            extracted_fields['num_comments']=response2[i].get('descendants')
            extracted_fields['author']=response2[i].get('by')
            extracted_fields['collected_at']=str(datetime.now()) #json takes string, booleans, numbers, lists, dict, null, boolean but no date time so changing it to string 
            #after that opened a file in appending mode and dump make dict to json string and store in file f
            with open("d:/trendpulse-Nanddanaa_Bobba/data/trends_20240115.json","a") as f:
                json.dump(extracted_fields,f)
                #as last i need to print count of storing in json i used it
                count+=1
                f.write("\n")
    
    print(f"Collected {count} stories.\nSaved to data/trends_20240115.json\n")


except Exception as e:
    print("Error:", e) 