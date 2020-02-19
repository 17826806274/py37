 #-*- coding: UTF-8 -*-
import requests
import json
import time,datetime
import schedule

def SendMessage():
    headers = {
        'content-type': 'application/json'
    }
    data = {"msgtype": "text","text": { "content": "抗击疫情，众志成城！"}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9a4528f1-12b7-458f-ae99-9c21a3055d79"
    requests.post(url=url, headers=headers, data=json.dumps(data))

schedule.every().day.at("22:59").do(SendMessage)

while 1:
    schedule.run_pending()
    time.sleep(1)
