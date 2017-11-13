# -- coding: UTF-8 -- 
import sys
import os
import os.path
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url='http://ic.snssdk.com/neihan/video/playback/?video_id=55846cb1d2dd43b2be1773137b2e6f66&quality=origin&line=0&is_gif=0&device_platform=iphone'
title='12'
path='/Volumes/my/内涵段子/魔术视频/%s.mp4'%title
urllib.urlretrieve(url, path)    
