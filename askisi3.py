import urllib.request #προσθηκη βιβλιοθηκης
import json #προσθηκη βιβλιοθηκης
import datetime
from datetime import date, timedelta
import requests as req
import array

x = datetime.datetime.now() #σημερινή ημερομηνία
month=x.month #σημερινός μήνας
year=x.year #σημερινό έτος
day=x.strftime("%d") #σημερινή ημέρα
day1=1
month=int(month)    #metatroph se integer
year=int(year)
day=int(day)
#'str' object has no attribute 'year'
#loop for the dates
#print(month)
pinar=[]
for i in range (1,day+1): #τρέχον μήνας
    if x.month>=10:
        m=x.month
    else: #x.month<10
        m='0'+str(x.month) #url
    if day1>=10:
        d=str(day1)

    else:
        d='0'+str(day1) #url
    day1=day1+1
    #print(year,m,d) #hmeromhnia pou allazei


    #852886
    #url="https://api.opap.gr/draws/v3.0/1100/draw-date/{}-{}-{}/{}-{}-{}".format(year,m,d,year,m,d) #στατιστικα
    #print(url)
    #t=draw["drawId"]
    #for draw in data["content"]:
    if d=="01":
        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)  # η τελευταία ημέρα του προηγούμενου μήνα
        #print(last_day_of_prev_month)
        url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}".format(last_day_of_prev_month, last_day_of_prev_month)
        #print(url)
        resp = req.get(url)
        html=resp.text #response
        data=json.loads(html)
        i=0
        for draw in data["content"]:
            if i==0:
                t = draw["drawId"]
                #print (t)
                id=t+1
                i=i+1
    else:
        id=id+180
    url1 = "https://api.opap.gr/draws/v3.0/1100/{}".format(id)
    resp1 = req.get(url1)
    html1 = resp1.text  # response
    data1 = json.loads(html1)
    t = data1["winningNumbers"]["list"] #array
    for j in range(0,81):
        pinar.append(0) #pinakas gia to poses fores emfanisthke enas arithmos,periexei 80 mhdenika
    for i in range(0,20):
        #print(t[i]) #apotelesmata απο winningNumbers της πρωτης κληρωσης της ημερας του τρεχοντος μηνα
        for j in range (1,81):
            if t[i]==j:
                pinar[j]=pinar[j]+1 #αυξανεται η εμφανιση του συγκεκριμενου αριθμου
                #print (pinar[j],j) #τυπώνει πόσες φορές εμφανιζεται ο καθε αριθμος
sum=0
apot=0
for i in range (1,81):
    sum=sum+pinar[i]
for i in range(1,81):
    print ("Ο ΑΡΙΘΜΟΣ",i,"ΕΜΦΑΝΙΣΤΗΚΕ",(pinar[i]/sum)*100,"%")
    apot=apot+(pinar[i]/sum)*100
print (int(apot)) #100% ελεγχος για σωστα αποτελεσματα στα στατιστικα
