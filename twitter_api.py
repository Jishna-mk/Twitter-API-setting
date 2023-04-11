import tweepy
import configparser
import pandas as pd

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
followers_list=api.get_followers(screen_name="pipedrive",count=200)
# printfollowers_list[0]['next_cursor'])
# print(lenfollowers_list))
# printfollowers_list[0].name)

columns=['User']
data=[]

for tweet in followers_list:
    data.append([ tweet.name])

df=pd.DataFrame(data,columns=columns)

df.to_csv('tweets.csv')




