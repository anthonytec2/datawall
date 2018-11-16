import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedShuffleSplit
import argparse
from colorama import Fore, Back, Style
from colorama import init
from sklearn.utils import shuffle
import gcpdata
from google.cloud import storage
import os
import pickle
import socket
import sys
def get_results(y_pred, y_test):
    number_flagged_right = np.sum(y_pred[y_test == 1] == 1)
    number_flagged_wrong = np.sum(y_test == 1)-number_flagged_right
    number_null_right = np.sum(y_pred[y_test == 0] == 0)
    number_null_wrong = np.sum(y_test == 0)-number_null_right
    print(f'Flagged Right: {number_flagged_right}')
    print(f'Flagged Wrong: {number_flagged_wrong}')
    print(f'Null Right: {number_null_right}')
    print(f'Null Wrong: {number_null_wrong}')


def train(X_train, y_train, X_test, y_test, i):
    if i == 0:
        name = 'citi'
    elif i == 1:
        name = 'jpm'
    else:
        name = 'boa'
    weights = (y_train == 0).sum()/(1.0 * (y_train == 1).sum())
    model = XGBClassifier(tree_method='gpu_hist', objective='binary:logistic',
                          n_estimators=300, scale_pos_weight=weights, n_jobs=6)
    if name == 'citi':
        model.fit(X_train, y_train, eval_metric=['auc'])
    else:
        model.fit(X_train, y_train, eval_metric=['auc'])
    y_pred = model.predict(X_test)
    get_results(y_pred, y_test)
    model.save_model(f'{name}.model')
    return model

def grab_data(i, client):
    if i==-1:
        print('Downloading Training Data')
        bucket = client.get_bucket('traina-data')
        blob = bucket.blob('test.csv')
        blob.download_to_filename('test.csv')
        data = np.genfromtxt('test.csv', delimiter=',')
        X=data[:,0:7]
        y=data[:,7]
        os.remove("test.csv")
    elif i==0:
        print('Downloading Citi Data')
        bucket = client.get_bucket('cit-data')
        blob = bucket.blob('citi.csv')
        blob.download_to_filename('citi.csv')
        data = np.genfromtxt('citi.csv', delimiter=',')
        X=data[:,0:7]
        y=data[:,7]
        os.remove("citi.csv")
    elif i==1:
        print('Downloading JPM Data')
        bucket = client.get_bucket('jpm-data')
        blob = bucket.blob('jpm.csv')
        blob.download_to_filename('jpm.csv')
        data = np.genfromtxt('jpm.csv', delimiter=',')
        X=data[:,0:7]
        y=data[:,7]
        os.remove("jpm.csv")
    elif i==2:
        print('Downloading BOA Data')
        bucket = client.get_bucket('boa-data')
        blob = bucket.blob('boa.csv')
        blob.download_to_filename('boa.csv')
        data = np.genfromtxt('boa.csv', delimiter=',')
        X=data[:,0:7]
        y=data[:,7]
        os.remove("boa.csv")
    return X, y

def export_model( amnt_data, client):
    model = XGBClassifier()
    model.load_model('boa.model')
    output = open('model.pb', 'wb')
    pickle.dump([model, amnt_data], output)
    output.close()
    bucket_test = client.get_bucket('traina-data') 
    blob_test = bucket_test.blob('model.pb')
    blob_test.upload_from_filename(filename='model.pb')
    os.remove('model.pb')
    print(Fore.GREEN+'Exported Model Sucessfully')
    return
def send_signal_infnode():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('35.243.211.120', 10000)
    print('Connecting to port')
    sock.connect(server_address)
    sock.close()
def main():
    client = storage.Client.from_service_account_json('/home/abisulco/key.json')
    '''
    init()
    gcpdata.init_demo()
    client = storage.Client.from_service_account_json('/home/abisulco/key.json')
    X_test, y_test=grab_data(-1, client)
    amnt_data={}
    for i in range(3):
        if i == 0:
            print(Fore.RED+'--------CITI----DATA----TRAINING----------------------')
            citi_X_train, citi_y_train=grab_data(i, client)
            amnt_data['citi']=len(citi_y_train)
            train(citi_X_train, citi_y_train, X_test, y_test, i)
            del citi_X_train, citi_y_train
        elif i == 1:
            print(Fore.GREEN+'--------JPM----DATA----TRAINING----------------------')
            jpm_X_train, jpm_y_train=grab_data(i, client)
            amnt_data['jpm']=len(jpm_y_train)
            train(jpm_X_train, jpm_y_train, X_test, y_test, i)
            del jpm_X_train, jpm_y_train
        elif i == 2:
            print(Fore.BLUE+'--------BOA----DATA----TRAINING----------------------')
            boa_X_train, boa_y_train=grab_data(i, client)
            amnt_data['boa']=len(boa_X_train)
            model = train(boa_X_train, boa_y_train, X_test, y_test, i)
            del boa_X_train, boa_y_train
        '''
    print('Model Finshed Training Begining Export')
    export_model({'boa':555, 'jpm':333, 'citi':1111}, client)
    send_signal_infnode()
if __name__ == '__main__':
    main()
