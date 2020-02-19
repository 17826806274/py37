# -*- conding:utf-8 -*-
#Author:wzf
import schedule
import requests
import json
import time

def SendMessage_lunch():
    headers = {
        'content-type': 'application/json'
    }
    data = {"msgtype": "text","text": { "content": "中午好，大家准备用午膳吗？"}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6d72f882-46e3-4ca2-95a7-8980c0c2bfa4"
    requests.post(url=url, headers=headers, data=json.dumps(data))

def SendMessage_dinner():
    headers = {
        'content-type': 'application/json'
    }
    data = {"msgtype": "text","text": { "content": "大家好，晚上准备进食吗？"}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6d72f882-46e3-4ca2-95a7-8980c0c2bfa4"
    requests.post(url=url, headers=headers, data=json.dumps(data))
    #print('Send success')

schedule.every().day.at("11:00").do(SendMessage_lunch)
schedule.every().day.at("17:00").do(SendMessage_dinner)

while 1:
    schedule.run_pending()
    time.sleep(1)