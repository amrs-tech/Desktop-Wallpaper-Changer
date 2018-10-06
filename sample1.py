import os
import ctypes
import urllib.request as u
import requests, random
from datetime import datetime as dt

download_directory = os.path.join('.', 'pic_dtop')
if not os.path.exists(download_directory):
    os.mkdir(download_directory)

i='1'

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
    path = os.path.join(download_directory, '{day}.jpg'.format(day=day))
    file = u.urlretrieve(url,path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
except Exception as e:
    print('Some Technical issues !')

   