import os, sys
from ID3 import *
files = os.listdir(os.getcwd())
for f in files:
  x = os.path.splitext(f)
  if x[1] == '.mp3':
    n = x[0].split(' - ')
    author = n[0]
    title = n[1]
    id3info = ID3(f)
    id3info['ARTIST'] = author
    id3info['TITLE'] = title
    print f+' id3 tagged.'
print 'Done!'