# -*- conding:utf-8 -*-
#Author:wzf

import re
from bs4 import BeautifulSoup
import requests
import time
import random

def spider_gushi(gushi_number):
    url = 'https://www.gushimi.org/gushi/'+ str(gushi_number) + '.html'
    res = requests.get(url)
    res1 = res.content.decode("utf-8")
    soup = BeautifulSoup(res1,'html.parser')
    gushi_title_html = str(soup.find_all(attrs={'class' : 'box_title'}))
    #print(gushi_title_html)
    res_title = r'<h2>(.*?)</h2>'
    gushi_title = re.findall(res_title,gushi_title_html)
    print(gushi_title[0])

def number_add(a):
    a += 1
    spider_gushi(a)

for a in range(2,100):
    spider_gushi(random.randint(0,99999))
    time.sleep(2)