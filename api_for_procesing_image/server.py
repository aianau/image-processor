import pytesseract
from PIL import Image
from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import re

app = Flask(_name_)

@app.route('/')
def hello_world():
    return '''This is ImageProcessing Module!<br/>Pentru a accesa API,rulati in python urmatorul cod:
    <br/>
    <br/>from _future_ import print_function
    <br/>import requests
    <br/>import json
    <br/>import cv2
    <br/>
    <br/>addr = 'http://szmuschi.pythonanywhere.com/'
    <br/>test_url = addr + '/api'
    <br/>
    <br/>content_type = 'image/jpeg'
    <br/>headers = {'content-type': content_type}
    <br/>
    <br/>img = cv2.imread('savedImage.jpg')#inlocuiti 'savedImage.jpg' cu imaginea care va intereseaza
    <br/>_, img_encoded = cv2.imencode('.jpg', img)
    <br/>response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    <br/>print(json.loads(response.text))'''


@app.route('/api', methods=['GET', 'POST'])
def api():
    r = request
    # nparr = np.fromstring(r.data, np.uint8)
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # cv2.imwrite("savedImage.jpg", img)
    # im = Image.open(r'savedImage.jpg')
    # print(im)

    # text = pytesseract.image_to_string(im)
    # x = re.split(' |\n|,', text)
    response = {'title': 'Silmarilion', 'author': 'JRR Tolkien', 'ISBN': '978-606-623-2'}
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")