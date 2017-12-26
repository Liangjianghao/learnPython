# -- coding: UTF-8 -- 
# import mp3play, time
import os
from pygame import mixer 
import time
# filename = "1.mp3"
# clip = mp3play.load(filename)
# clip.play()
# os.system('paplay 1.mp3')
# clip = mp3play.load('1.mp3')
# clip.play()
# time.sleep(10)   #定义播放时间，如果没有这句话，是听不到声音的。
# clip.stop()


def playMusci():
	
	mixer.init()
	# mixer.music.load('/Users/l/Desktop/learnPython/acFun/2.mp3')
	mixer.music.load('1.mp3')
	mixer.music.play()
	time.sleep(1)