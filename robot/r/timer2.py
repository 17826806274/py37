# -*- conding:utf-8 -*-
#Author:wzf
#2020年2月7日 更新版
#发送时间修改为：每周一到周六


import schedule
import requests
import json
import time

def conten(eat_conten):

    eat1 = eat_conten
    return eat1

def SendMessage_lunch():
    headers = {
        'content-type': 'application/json'
    }
    data = {"msgtype": "text","text": { "content": "中午好，大家准备用午膳吗？"}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6d72f882-46e3-4ca2-95a7-8980c0c2bfa4"
    #requests.post(url=url, headers=headers, data=json.dumps(data))

def SendMessage_dinner():
    headers = {
        'content-type': 'application/json'
    }
    #data = {"msgtype": "text","text": { "content": "大家好，晚上准备进食吗？"}}
    data_test= {"msgtype": "text", "text": {"content": conten('erwer')}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6d72f882-46e3-4ca2-95a7-8980c0c2bfa4"
    #requests.post(url=url, headers=headers, data=json.dumps(data))
    print(data_test)



SendMessage_dinner()


'''
schedule.every().monday.at("11:00").do(SendMessage_lunch)
schedule.every().tuesday.at("11:00").do(SendMessage_lunch)
schedule.every().wednesday.at("11:00").do(SendMessage_lunch)
schedule.every().thursday.at("11:00").do(SendMessage_lunch)
schedule.every().friday.at("11:00").do(SendMessage_lunch)
schedule.every().saturday.at("11:00").do(SendMessage_lunch)
schedule.every().monday.at("17:00").do(SendMessage_dinner)
schedule.every().tuesday.at("17:00").do(SendMessage_dinner)
schedule.every().wednesday.at("17:00").do(SendMessage_dinner)
schedule.every().thursday.at("17:00").do(SendMessage_dinner)
schedule.every().friday.at("17:00").do(SendMessage_dinner)
schedule.every().saturday.at("17:00").do(SendMessage_dinner)

while 1:
    schedule.run_pending()
'''
