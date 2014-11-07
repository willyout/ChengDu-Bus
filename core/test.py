# -*- coding: utf-8 -*-
import pyquery

BUS_URL = 'http://www.basbus.cn/m/line?id={0}'
BUS_URL_REVERSE = 'http://www.basbus.cn/m/line?id={0}&t=2'

UA_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20100101 Firefox/15.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn,en-us;q=0.7,en;q=0.3',
    'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

page = pyquery.PyQuery(BUS_URL.format('1'), headers=UA_HEADER)

texts = page('.buslineinfo')
print type(texts)
print page('.headinfo').text().split(' ')[1]
print page('.leftspan01').text()
print page('.leftspan02').text()
print page('.rightspan01').text()
# print page('.rightspan02').text()


for t in texts('ul'):
    a = pyquery.PyQuery(t)
    print a('.li_01').text()
    print a('.yuanicon').text()
    print a('p').text()


