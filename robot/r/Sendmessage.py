 #-*- coding: UTF-8 -*-
import requests
import json
import time,datetime

def SendMessage():
    headers = {
        'content-type': 'application/json'
    }
    data = {"msgtype": "text","text": { "content": "吃饭吗？"}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e20c25ef-15a8-484f-ac8d-b082bbb04902"
    #requests.post(url=url, headers=headers, data=json.dumps(data))
    print('Send success')

