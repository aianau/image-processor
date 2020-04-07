import json
import cv2
import requests

addr = 'http://szmuschi.pythonanywhere.com/'
test_url = addr + '/api'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('savedImage.jpg')#inlocuiti 'savedImage.jpg' cu imaginea care va intereseaza
_, img_encoded = cv2.imencode('.jpg', img)
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
print(json.loads(response.text))