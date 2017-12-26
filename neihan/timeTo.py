# coding:utf-8

import sys
import os
import time 


dt = "2016-05-05 20:28:54"

# #转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# #转换成时间戳
timestamp = time.mktime(timeArray)

print timestamp
print time.time()
maxtime=time.time()
maxtime=maxtime-2
print maxtime
url='http://is.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=9&count=30&level=6&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
print url

86400