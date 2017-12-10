# -- coding: UTF-8 -- 
import requests
import json
from lxml import etree
import re

header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
res = requests.get("http://ow.thnuclub.com/").content
# selector = res.fromstring(res)
# hrefs=selector.xpath('//div[@class="search-item detail-width"]')
# https://k6i.github.io/0f/0fe61035b37beb3241d8150bc39d5179.mp3
result = re.findall(r'*/.(rm|mp3|wma)',res)



print result
# result=json.loads(res)
# print result

