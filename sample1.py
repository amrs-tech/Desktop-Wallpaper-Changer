import os
import ctypes
import urllib.request as u
import requests, random
from datetime import datetime as dt
import sys

i='1'
#arguments example= /home/user/Desktop/ day
arguments=sys.argv[1:]
path=arguments[0]
name=arguments[1]
path=path+name
try:
    day = dt.now().date()
    day = str(day)
    temp1 = int(day[-1])
    tnum = [9000,8900,8930,9010,8920,8970,8950]
    temp = 2*temp1 - 1
    t1 = random.choice(tnum)+temp
    i = str(t1)
    try:
        url = 'https://assets-natgeotv.fnghub.com/POD/'+i+'.jpg'

    except:
        print('Server Error !')
    # path = 'C:\\Users\\Sabi\\Downloads\\m\\pic_dtop\\'+day+'.jpg'
    file = u.urlretrieve(url,path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
except Exception as e:
    print('Some Technical issues !')

   