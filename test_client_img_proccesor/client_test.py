import json
import os
import time
import cv2
import psutil
import requests

class TestApi:
    def __init__(self):
        self.URL ='http://szmuschi.pythonanywhere.com/'

    def test_request(self, image_path):

        start_time = time.time()
        process = psutil.Process(os.getpid())
        addr =self.URL
        test_url = addr + '/api'
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}

        img = cv2.imread('imgs/'+image_path)#inlocuiti 'savedImage.jpg' cu imaginea care va intereseaza
        _, img_encoded = cv2.imencode('.jpg', img)
        response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        print(json.loads(response.text))
        print("--- %s seconds ---" % (time.time() - start_time))
        print("---", process.memory_info().rss / 1000, "kilobytes")  # in bytes

if __name__ == '__main__':
    test_api = TestApi()

    test_api.test_request('cover.jpg')
    print("expected: Anthem by Ayn Rand /n")
    test_api.test_request('cover1.jpg')
    print("expected: Pride and Prejudice by jane asutin /n")
    test_api.test_request('cover2.jpg')
    print("expected: the greatest treasure bu marius oelsching /n")
    test_api.test_request('cover3.jpg')
    print("expected: the happy lemon/n")
    test_api.test_request('cover4.jpg')
    print("expected: the book title by author name/n")
    test_api.test_request('cover5.jpg')
    print("expected: the crying book by heather christle /n")
    test_api.test_request('cover7.jpg')
    print("expected: red queen /n")