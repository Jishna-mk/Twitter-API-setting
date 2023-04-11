import tweepy
import configparser
import pandas as pd
from datetime import datetime,date,timedelta
import json
import csv
import pandas as pandasForSortingCSV
  



config=configparser.ConfigParser()
config.read('config.ini')
api_key= config['twitter']['api_key']
api_key_secret=config['twitter']['api_key_secret']

access_token=config['twitter']['access_token']
access_token_secret=config['twitter']['access_token_secret']

#authentication
auth=tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api= tweepy.API(auth)
limit=1000
followers_list=tweepy.Cursor(api.get_followers,screen_name="pipedrive",count=200).items(1000)




columns=['User','Time','Location','Description']
data=[]
val = {}

for tweet in followers_list:
    data.append([ tweet.name,tweet.created_at,tweet.location,tweet.description])




# newlist = []
# for fname in followers_list:
#     newlist.append([fname.name,fname.created_at,fname.location,fname.desciption])

df=pd.DataFrame(data,columns=columns)

df.to_csv('twitter.csv')    

# import csv

# fields = ['User','Time','Location','Description']
# rows = newlist

# with open("twee.csv", 'w') as csvfile: 
#     # creating a csv writer object 
    
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(fields) 
        
#     # writing the data rows 
#     csvwriter.writerows(rows)

# import pandas as pandasForSortingCSV
  
# # assign dataset
# csvData = pandasForSortingCSV.read_csv("twee.csv")
                                         
# # displaying unsorted data frame
# print("\nBefore sorting:")
# print(csvData)
  
# # sort data frame
# csvData.sort_values(csvData.columns[0], 
#                     axis=0,
#                     inplace=True)
  
# # displaying sorted data frame
# print("\nAfter sorting:")
# print(csvData)        