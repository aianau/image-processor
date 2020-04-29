import json
import cv2
import requests
import time
import os
import psutil
from glob import glob

img_mask = 'imgs/*.jpg'
img_names = glob(img_mask)

process = psutil.Process(os.getpid())
addr = 'http://szmuschi.pythonanywhere.com/'
test_url = addr + '/api'

content_type = 'image/jpg'
headers = {'content-type': content_type}
for fn in img_names:
    start_time = time.time()
    img = cv2.imread(fn, 0)  #inlocuiti 'savedImage.jpg' cu imaginea care va intereseaza
    _, img_encoded = cv2.imencode('.jpg', img)
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    print(json.loads(response.text))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("---", process.memory_info().rss/1000, "kilobytes")    # in bytes
