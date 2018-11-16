
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
import subprocess
import mongo
def wait_for_signal():
    print('Waiting For Signal')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 10000)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('Waiting for Connection')
        connection, client_address = sock.accept()
        break
    connection.close()

if __name__=="__main__":
    mongo.set_zero()
    wait_for_signal()
    client = storage.Client.from_service_account_json('/home/abisulco/key.json')
    bucket = client.get_bucket('traina-data')
    blob = bucket.blob('model.pb')
    blob.download_to_filename('model.pb')
    print('Connected Starting Server')
    proc = subprocess.Popen(['python3' ' /home/abisulco/datawall/Inference_Service/model_flask.py'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)
    while True:
        output = proc.stdout.readline()
        if output == '' and proc.poll() is not None:
            break
        if output:
            print(output.strip())
    print(proc.communicate())