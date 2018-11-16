import numpy as np
import json
import requests
import random
import time
while True:
    data = {
            "User": random.choice(['citi', 'jpm', 'boa']),
            "Data": [1,random.randint(1,3),random.randint(1,1000000000), random.randint(1,1000000000),random.randint(1,1000000000),random.randint(1,1000000000),random.randint(1,1000000000)]
            }
    request =requests.post("http://35.243.211.120:5000/inf", json=data)
    time.sleep(.1)
    print(request.text)
