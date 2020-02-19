# -*- conding:utf-8 -*-
#Author:wzf
import re
from bs4 import BeautifulSoup
import requests
import random
import json
import schedule
import time

def spider_tangshi300shou_soup(gushi_number):
    url = 'https://www.gushimi.org/gushi/tangshisanbaishou/index_'+ str(gushi_number) +'.html'
    res = requests.get(url)
    res1 = res.content.decode("utf-8")
    soup = BeautifulSoup(res1,'html.parser')
    return soup

def gushi_title(soup):
    gushi_title_html = str(soup.find_all(attrs={'class' : 'news_title'}))
    res_title = r'html">(.*?)</a'
    gushi_title_list = re.findall(res_title,gushi_title_html)
    random_number = random.randint(1, len(gushi_title_list)-1)
    gushi_title ='《'+ gushi_title_list[random_number] + '》'
    return gushi_title,random_number

def gushi_summy(soup,random_number):
    gushi_summy_html = str(soup.find_all(attrs={'class' : 'news_summy'}))
    res_summy = r'html">(.*?)</a'
    gushi_summy = re.findall(res_summy,gushi_summy_html)
    return ('作者：'+ gushi_summy[random_number] )


def gushi_text(soup,radom_number):
    gushi_text_html = str(soup.find_all(attrs={'class': 'news_text'}))
    res_text1 =r'text"><p>([.\s\S]*?)</p>'
    gushi_text_list = re.findall(res_text1, gushi_text_html)
    #print(gushi_text_list)
    gushi_text = gushi_text_list[radom_number]
    #print(gushi_text)
    #gushi_text = re.sub(r'。', '。\n', gushi_text_list[3])
    #print(gushi_text_huanhang)
    return gushi_text


def gushi():
    page_number = random.randint(2,7)
    soup = spider_tangshi300shou_soup(page_number)
    title,random_number = gushi_title(soup)
    summy = gushi_summy(soup,random_number)
    text = gushi_text(soup,random_number)
    #print(title)
    #print(summy)
    #print(text)
    return title,summy,text


def SendMessage_gushi(title,summy,text):
    headers = {
        'content-type': 'application/json'
    }
    content_gushi = title+'\n'+summy+'\n'+text +'\n'+'\n'+'嗨！小朋友，你知道这首诗表达了诗人什么样的情感吗？'
    data = {"msgtype": "text","text": { "content": content_gushi}}
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6d72f882-46e3-4ca2-95a7-8980c0c2bfa4"
    requests.post(url=url, headers=headers, data=json.dumps(data))

def post_gushi():
    title,summy,text = gushi()
    SendMessage_gushi(title,summy,text)


schedule.every().day.at("08:59").do(post_gushi)

while 1:
    schedule.run_pending()
    time.sleep(1)
