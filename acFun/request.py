# -- coding: UTF-8 -- 
import requests
import json

header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
res = requests.get("https://apipc.app.acfun.cn/v2/videos/4116972",headers=header_dict).content
result=json.loads(res)
print result['vdata']['videos'][0]['videoId']


# 快速看完一局韩服王者斗殴局