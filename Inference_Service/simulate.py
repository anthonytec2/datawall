import numpy as np
import json
import requests

data = {
        "User":"Citi",
	    "Data":[1,2,3,16000,16000,16000,7]
        }
    
data_json = json.dumps(data)

request =requests.post("35.243.211.120:5000/inf", json=data)
print(request.text)