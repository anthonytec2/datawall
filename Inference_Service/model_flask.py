from flask import Flask, request
import numpy as np
import json
from google.cloud import storage
import pickle
import os
from sklearn.preprocessing import LabelEncoder
from pymongo import MongoClient
from mongoengine import *
import socket
import sys
ADDRESS = "mongodb://datawall:datawall1@ds255403.mlab.com:55403/inf-node"    
DB_NAME = "datawall"
connect(db = DB_NAME, host = ADDRESS)
app = Flask(__name__)
client = storage.Client.from_service_account_json('/home/abisulco/key.json')
bucket = client.get_bucket('traina-data')
blob = bucket.blob('model.pb')
blob.download_to_filename('model.pb')
file = open('model.pb', 'rb')
model, data_info  = pickle.load(file)
file.close()
os.remove('model.pb')

@app.route('/', methods = ["GET"])
def home():
    return "you are at the homepage"

@app.route('/inf', methods = ["POST"])
def runmodel():
    parsed_data = request.get_json()
    print(parsed_data)
    user=parsed_data['User']
    input_data=parsed_data['Data']
    print('USER:', user)
    print('Data: ', input_data)
    model._le = LabelEncoder().fit([0, 1])    
    return str(model.predict(np.expand_dims(np.array(input_data),0)))

def calculate_payout(User, percent_dict, base_cost = 10000):
    comp_part = []
    comp_dw = 0
    for participant in percent_dict:
        if participant != User:
            comp_part.append((participant, (.985 * base_cost * percent_dict[participant] * (1-percent_dict[User])**2) / (1-percent_dict[User])))
            comp_dw += (.015 * base_cost * percent_dict[participant] * (1-percent_dict[User])**2) / (1-percent_dict[User])
    cost = base_cost * (1 - percent_dict[User])**2
    return cost, comp_dw, comp_part
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)