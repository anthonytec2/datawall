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
from google.cloud import storage


def split(X, y, equal=False, prob_list=[.2, .5]):
    if equal:
        sss = StratifiedShuffleSplit(n_splits=3, test_size=0.1, random_state=0)
        j = 0
        for train_index, test_index in sss.split(X, y):
            if j == 0:
                citi_X_train, citi_X_test = X[train_index], X[test_index]
                citi_y_train, citi_y_test = y[train_index], y[test_index]
            elif j == 1:
                jpm_X_train, jpm_X_test = X[train_index], X[test_index]
                jpm_y_train, jpm_y_test = y[train_index], y[test_index]
            elif j == 2:
                boa_X_train, boa_X_test = X[train_index], X[test_index]
                boa_y_train, boa_y_test = y[train_index], y[test_index]
            j += 1
    else:
        X, y = shuffle(X, y, random_state=0)
        num_elem_one = int(len(y) * prob_list[0])
        num_elem_two = int(len(y) * prob_list[1])
        citiX = X[:num_elem_one]
        jpmX = X[num_elem_one:num_elem_one+num_elem_two]
        boaX = X[num_elem_one+num_elem_two:]
        citiy = y[:num_elem_one]
        jpmy = y[num_elem_one:num_elem_one+num_elem_two]
        boay = y[num_elem_one+num_elem_two:]
        citi_X_train, citi_X_test, citi_y_train, citi_y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        jpm_X_train, jpm_X_test, jpm_y_train, jpm_y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        boa_X_train, boa_X_test, boa_y_train, boa_y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        print(citiX.shape, citiy.shape)
        np.savetxt("citi.csv", np.concatenate(
            (citi_X_train, np.expand_dims(citi_y_train, 1)), 1), delimiter=",")
        print(jpmX.shape, jpmy.shape)
        np.savetxt("jpm.csv", np.concatenate(
            (jpm_X_train, np.expand_dims(jpm_y_train, 1)), 1), delimiter=",")
        print(boaX.shape, boay.shape)
        np.savetxt("boa.csv", np.concatenate(
            (boa_X_train, np.expand_dims(boa_y_train, 1)), 1), delimiter=",")

        X_test = np.vstack([citi_X_test, jpm_X_test, boa_X_test])
        y_test = np.hstack([citi_y_test, jpm_y_test, boa_y_test])
        np.savetxt("test.csv", np.concatenate(
            (X_test, np.expand_dims(y_test, 1)), 1), delimiter=",")

        client = storage.Client.from_service_account_json(
            '/home/abisulco/key.json')
        bucket_boa = client.get_bucket('boa-data')
        bucket_jpm = client.get_bucket('jpm-data')
        bucket_citi = client.get_bucket('cit-data')
        bucket_test = client.get_bucket('traina-data')
        blob_boa = bucket_boa.blob('boa.csv')
        blob_jpm = bucket_jpm.blob('jpm.csv')
        blob_citi = bucket_citi.blob('citi.csv')
        blob_test = bucket_test.blob('test.csv')
        blob_boa.upload_from_filename(filename='boa.csv')
        blob_jpm.upload_from_filename(filename='jpm.csv')
        blob_citi.upload_from_filename(filename='citi.csv')
        blob_test.upload_from_filename(filename='test.csv')

    print('--------------Data Split---------------')
    print(f'Total data size {len(y)}')
    print(f'Citi: {len(citiy)/len(y)}')
    print(f'JPM: {len(jpmy)/len(y)}')
    print(f'BOA: {len(boay)/len(y)}')
    return citi_X_train, citi_X_test, citi_y_train, citi_y_test, jpm_X_train, jpm_X_test, jpm_y_train, jpm_y_test, boa_X_train, boa_X_test, boa_y_train, boa_y_test


def init_demo():
    load_data = torch.load('../data/data.pt')
    X = load_data["X"]
    y = load_data["y"]
    p1 = np.random.uniform(0, .6)
    p2 = np.random.uniform(0, 1-p1-.2)
    citi_X_train, citi_X_test, citi_y_train, citi_y_test, jpm_X_train, jpm_X_test, jpm_y_train, jpm_y_test, boa_X_train, boa_X_test, boa_y_train, boa_y_test = split(
        X, y, equal=False, prob_list=[p1, p2])
    print('Data Sucessfully Uploaded')


if __name__ == '__main__':
    init_demo()
