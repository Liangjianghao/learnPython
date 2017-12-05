# -*- coding: utf-8 -*-

import os
import sysif os.path.isdir(path):
  print "it's a directory"
elif os.path.isfile(path):
  print "it's a normal file"
else:
  print "it's a special file (socket, FIFO, device file)"