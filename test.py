# -*- coding:utf-8 -*-
import requests
import bs4

res = requests.get('http://www.runoob.com/')
res.raise_for_status()
res.encoding='utf-8'
bs = bs4.BeautifulSoup(res.text,"html5lib")
div = bs.select('h4')
str(div)
print(div[4])