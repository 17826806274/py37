# -*- coding:utf-8 -*-
import requests
import bs4
import re
import time


res = requests.get('http://www.runoob.com/')
res.raise_for_status()
res.encoding='utf-8'
bs = bs4.BeautifulSoup(res.text,"html5lib")
h4_list = bs.select('h4')

rex1 = "(?<=【).*?(?=】)"

def write_file(txt):
    f1 = open('web4.txt','a',encoding='utf8')
    f1.write(txt)
    f1.close()

def local_time():
    return(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


#write_file('\n'+str(h4_list))
for h4 in bs.find_all('h4'):
    matchobj = re.match(r'【',h4.string)
    if matchobj:
        #print(h4.string)
        time1 = local_time()
        write_file(time1 +' '+ h4.string + '\n' )




#get_text 循环
'''
for i in h4_list:
    print(i.get_text())
'''

