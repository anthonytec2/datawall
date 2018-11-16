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
from mongo import *
app = Flask(__name__)
client = storage.Client.from_service_account_json('/home/abisulco/key.json')
bucket = client.get_bucket('traina-data')
blob = bucket.blob('model.pb')
blob.download_to_filename('model.pb')
file = open('model.pb', 'rb')
model, percent_dict = pickle.load(file)
file.close()
os.remove('model.pb')


@app.route('/', methods=["GET"])
def home():
    return "you are at the homepage"


@app.route('/inf', methods=["POST"])
def runmodel():
    parsed_data = request.get_json()
    print(parsed_data)
    user = parsed_data['User'].lower()
    input_data = parsed_data['Data']
    print('USER:', user)
    print('Data: ', input_data)
    percent_dict={'boa':.33, 'jpm':.33, 'citi':.33}
    print(calculate_payout(user, percent_dict))
    cost, comp_dw, comp_part=calculate_payout(user, percent_dict)
    update_user(user, cost, comp_dw, comp_part)
    model._le = LabelEncoder().fit([0, 1])
    return str(model.predict(np.expand_dims(np.array(input_data), 0)))


def update_user(usera, cost, comp_dw, comp_part):
    new_payout = User.objects(user=usera)[0].payout-cost
    new_inf = User.objects(user=usera)[0].num_inf+1
    User.objects(user=usera.lower()).update_one(
        payout=new_payout, num_inf=new_inf)
    new_pat_dw=User.objects(user='datawall')[0].payout+comp_dw
    User.objects(user='datawall').update_one(payout=new_pat_dw)
    for userb in comp_part:
        new_payout = User.objects(user=userb[0].lower())[0].payout+userb[1]
        User.objects(user=userb[0].lower()).update_one(payout=new_payout)
    
def calculate_payout(requestor, percent_dict, base_cost=2):
    comp_part = []
    comp_dw = 0
    for participant in percent_dict:
        if not participant == requestor:
            print((.985 * base_cost * percent_dict[participant] * (
                1-percent_dict[requestor])**2) / (1-percent_dict[requestor]))
            comp_part.append((participant, (.985 * base_cost * percent_dict[participant] * (
                1-percent_dict[requestor])**2) / (1-percent_dict[requestor])))
            comp_dw += (.015 * base_cost * percent_dict[participant] * (
                1-percent_dict[requestor])**2) / (1-percent_dict[requestor])
    cost = base_cost * (1 - percent_dict[requestor])**2
    return cost, comp_dw, comp_part


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
