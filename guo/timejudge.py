# -*- coding: utf-8 -*-
import os
import eyed3

def main():
    mp3 = u'/Volumes/my/丑娘娘/丑娘娘4.mp3'
 
    xx = eyed3.load(mp3)
 
    print(u'时长为：{}秒'.format(xx.info.time_secs))

def findAll(path):
 	# for filename in os.listdir(path):
 	# 	# print filename
	 #    mp3 = u'%s/%s'%(path,filename)
 
  #   	xx = eyed3.load(mp3)
 
		# print(u'时长为：{}秒'.format(xx.info.time_secs))


    mp3 = u'/Volumes/my/丑娘娘/丑娘娘4.mp3'
 
    xx = eyed3.load(mp3)
 
    print(u'时长为：{}秒'.format(xx.info.time_secs))

if __name__ == '__main__':
    findAll('/Volumes/my/你要')
    


