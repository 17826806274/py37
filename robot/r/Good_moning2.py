# -*- conding:utf-8 -*-
#Author:wzf

import re
from bs4 import BeautifulSoup
import requests
import random
import json
import schedule
import time

    #爬虫下载soup
def good_moning_spider():
    url = 'https://www.wowoqq.com/juzi/zaoanxinyu.html'
    res = requests.get(url)
    res1 = res.content.decode("utf-8")
    soup = BeautifulSoup(res1,'html.parser')
    return soup


def good_moning_text():
    soup = good_moning_spider()
    good_moning_html = str(soup.find_all(attrs={'class' : 'artCon'}))
    good_moning_html = re.sub('\d', '',good_moning_html)
    good_moning_html = re.sub('\.', '', good_moning_html)
    good_moning_html = re.sub('、', '', good_moning_html)
    good_moning_html = re.sub(' ', '', good_moning_html)
    res_good_moning = r'<p>\r\n\t([.\s\S]*?)</p>'
    text = re.findall(res_good_moning,good_moning_html)
    #for a in range(2,len(text)):
    return text

def SendMessage(text):
    headers = {
        'content-type': 'application/json'
    }
    content = time.strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')+'\n'+ '\n'+text
    data = {"msgtype": "text","text": { "content":content}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9a4528f1-12b7-458f-ae99-9c21a3055d79"
    requests.post(url=url, headers=headers, data=json.dumps(data))
    #print(content)

    #post 文字
def post_moning(text):
    number = random.randint(1,len(text)-1)
    SendMessage(text[number])


text = good_moning_text()

schedule.every().day.at("09:00").do(post_moning,text)

while 1:
    schedule.run_pending()
    time.sleep(1)


