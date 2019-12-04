#from mailjet_rest import Client
import os, json, time
import requests

def sendEmail(subject,msg):
    api_key = '8ea797ff7e0a51160709410d31d496fc'
    api_secret = '9b467690c0203d0a541cc4a4c82a00d0'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
      {
        "From": {
          "Email": "dontsaybofa@gmail.com",
          "Name": "Joe"
        },
        "To": [
          {
            "Email": "guy7852314569@gmail.com",
            "Name": "Customer"
          }
        ],
        "Subject": subject,
        "TextPart": msg,
        "HTMLPart": msg,
        "CustomID": "AppGettingStartedTest"
      }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

#sendEmail("subject","message")

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=VTI&interval=5min&outputsize=fullapikey=BB7GVKBS5NX2R5KI



def getList():
    r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")
    data = r.json()
    data = data["Time Series (5min)"]
    # keys = data.keys()
    # keys.sort()
    # print(data[keys[-1]]["4. close"])
    # for x in keys:
    #     print(x + " " + data[x]["4. close"])
    return data

hourCounter = 1
while True:
    #sendEmail(str(hourCounter) + " hours elapsed","Hehe xd")
    data = getList()
    keys = data.keys()
    keys.sort()
    monthMax = 0
    weekMax = 0
    monthMin = 9999
    weekMin = 9999
    print(len(keys))
    for x in keys[:-1]:
        monthMax = max(data[x]["4. close"], monthMax)
        monthMin = min(data[x]["4. close"], monthMin)
    for x in keys[300:-1]:
        weekMax = max(data[x]["4. close"], weekMax)
        weekMin = min(data[x]["4. close"], weekMin)
    time.sleep(3600)
    hourCounter += 1
