import json
import threading
import time
import unittest
import requests
from flask_restful import Resource
from app import flaskAppInstance

SERVER_URL = "http://192.168.99.100:5000"

class TestAPI(Resource):
    def get(self):
        def start_and_init_server(app):
            flaskAppInstance.run(threaded=True)
        server_thread = threading.Thread(target=start_and_init_server, args=(flaskAppInstance, ))
        n = 5
        request_threads = []
        try:
            server_thread.start()
            r = requests.get(url = SERVER_URL)
            
            def post_data():
                r = requests.post(url = SERVER_URL)
            for i in range(n):
                t = threading.Thread(target=post_data)
                request_threads.append(t)
                t.start()
            all_done = False
            while not all_done:
                all_done = True
                for t in request_threads:
                    if t.is_alive():
                        all_done = False
                        time.sleep(1)
            r = requests.get(url = SERVER_URL)
            print(r.json())
        except Exception:
            print('Something went horribly wrong!')