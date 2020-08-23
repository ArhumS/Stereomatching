# random.stereogram

import numpy as np
import cv2
import sys
import os
import random

def makerandom(width, height, square=8,color = 255):
   a = np.zeros((height,width,3), np.uint8)
   for h in range(0,height/square):
    for w in range(0,width/square):
      if random.random() < 0.5:
         c = color
      else:
         c = 8
      for hh in range(square):
         for ww in range(square):
           a[square*h+hh,square*w+ww] = c
   return a

#------x-------#

a = makerandom(512,512,color = 255)
b=  makerandom(256,256,color = 128)
c = makerandom(128,128,color = 128)
left = np.copy(a)
right = np.copy(a)
left[256-128:256+128,256-128+16:256+128+16]=b
right[256-128:256+128,256-128:256+128]=b

left[256-64:256+64,256-64+24:256+64+24]=c
right[256-64:256+64,256-64:256+64]=c

z= np.concatenate((left, right),axis = 0)
cv2.imshow('z',z)
cv2.waitKey()


