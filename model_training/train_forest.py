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
    model = XGBClassifier(tree_method='gpu_exact', objective='binary:logistic',
                          n_estimators=300, scale_pos_weight=weights, n_jobs=6)
    if name == 'citi':
        model.fit(X_train, y_train, eval_metric=['auc'])
    else:
        model.fit(X_train, y_train, eval_metric=['auc'])
    y_pred = model.predict(X_test)
    get_results(y_pred, y_test)
    model.save_model(f'{name}.model')
    return model


def main():
    init()
    gcpdata.init_demo()
    
    for i in range(3):
        if i == 0:
            print(Fore.RED+'--------CITI----DATA----TRAINING----------------------')
            citi_X_train, citi_y_train, citi_X_test, citi_y_test=grab_data(i)
            train(citi_X_train, citi_y_train, citi_X_test, citi_y_test, i)
            del citi_X_train, citi_y_train, citi_X_test, citi_y_test
        elif i == 1:
            print(Fore.GREEN+'--------JPM----DATA----TRAINING----------------------')
            jpm_X_train, jpm_y_train, jpm_X_test, jpm_y_test=grab_data(i)
            train(jpm_X_train, jpm_y_train, jpm_X_test, jpm_y_test, i)
        elif i == 2:
            print(Fore.BLUE+'--------BOA----DATA----TRAINING----------------------')
            boa_X_train, boa_y_train, boa_X_test, boa_y_test=grab_data(i)
            model = train(boa_X_train, boa_y_train, boa_X_test, boa_y_test, i)


if __name__ == '__main__':
    main()
