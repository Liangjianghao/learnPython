# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
try:
    import requests
    import pytesseract
    from PIL import Image
except ImportError:
    raise SystemExit('cuole');
# addr = raw_input()
image = Image.open('/Users/l/Desktop/img/image_code.png')
# image.show()
vcode = pytesseract.image_to_string(image)
print vcode