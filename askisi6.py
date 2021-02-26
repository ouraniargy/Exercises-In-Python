#API key:
#Cuuk87UE8l2jekC06C4vwV3Qz
#API key secret:
#psJz1UMXqM29QwDyTiSpMmhRxKadyhJ1RmN4lKWE2BP6jEPt26

import tweepy
import webbrowser
import time
import pandas as pd

consumer_key = "Cuuk87UE8l2jekC06C4vwV3Qz"
consumer_secret_key = "psJz1UMXqM29QwDyTiSpMmhRxKadyhJ1RmN4lKWE2BP6jEPt26"

callback_uri = "oob" #https://cfe.sh/twitter/callback
auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key,callback_uri)
redirect_url = auth.get_authorization_url()
print (redirect_url)
webbrowser.open(redirect_url)

#patame authorize app
user_pint_input = input("What's the pin value?")
print (user_pint_input)
auth.get_access_token(user_pint_input)
print(auth.access_token,auth.access_token_secret)
#the accesstoken and the accesstokensecret are always the same

api = tweepy.API(auth,wait_on_rate_limit=True)
me = api.me()
my_timline = api.home_timeline()

user = api.get_user("code")
user_timeline = user.timeline()
user_timeline_status_obj = user_timeline[0]
status_obj_id = user_timeline[0].id
status_obj_screen_name = user_timeline_status_obj.user.screen_name
status_obj_url = f"https://twitter.com/{status_obj_screen_name}/status/{status_obj_id}"
status_obj = api.get_status("1363497742396497928")
status_obj.text

other_user = input("give me user:")
maxword1 = pow(-10,9)
maxword2 = pow(-10,9)
maxword3 = pow(-10,9)
maxword4 = pow(-10,9)
maxword5 = pow(-10,9)
longestword1 = ""
longestword2 = ""
longestword3 = ""
longestword4 = ""
longestword5 = ""
minword1 = 10000
minword2 = 10000
minword3 = 10000
minword4 = 10000
minword5 = 10000
smallestword1 = ""
smallestword2 = ""
smallestword3 = ""
smallestword4 = ""
smallestword5 = ""
for i,status in enumerate(tweepy.Cursor(api.user_timeline,screen_name=other_user).items(10)):
    print (i,status.text)
    text = status.text
    res = text.split()
    print (res)
    print (len(text))   #poses lekseis exei to post
    for word in res:
        print(word,len(word))
        if len(word)>=maxword1:
            maxword1=len(word)
            longestword1 = word
        if len(word)>=maxword2 and word!=longestword1:
            maxword2=len(word)
            longestword2 = word
        if len(word)>=maxword3 and word!=longestword1 and word!=longestword2:
            maxword3=len(word)
            longestword3 = word
        if len(word)>=maxword4 and word!=longestword1 and word!=longestword2 and word!=longestword3:
            maxword4=len(word)
            longestword4 = word
        if len(word)>=maxword5 and word!=longestword1 and word!=longestword2 and word!=longestword3 and word!=longestword4:
            maxword5=len(word)
            longestword5 = word
        if len(word) <= minword1:
            minword1=len(word)
            smallestword1= word
        if len(word) <= minword2 and smallestword1!=word:
            minword2 = len(word)
            smallestword2 = word
        if len(word) <= minword3 and smallestword2!= word and smallestword1!= word:
            minword3 = len(word)
            smallestword3 = word
        if len(word) <= minword4 and smallestword3!=word and smallestword2!= word and smallestword1!= word:
            minword4=len(word)
            smallestword4 = word
        if len(word) <= minword5 and smallestword4!=word and smallestword3!= word and smallestword2!= word and smallestword1!= word:
            minword5=len(word)
            smallestword5 = word
print ("Oi megalyteres lekseis pou emfanizontai einai: ", longestword1,longestword2,longestword3,longestword4,longestword5)
print ("Oi mikroteres lekseis pou emfanizontai einai: ",smallestword1,smallestword2,smallestword3,smallestword4,smallestword5)

#status.text is the post




