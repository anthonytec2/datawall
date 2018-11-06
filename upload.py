# coding: utf-8

from google.cloud import datastore
import pandas as pd

LOCAL_FNAME = "data/data.csv"
ENTITY_KIND = "bank"
KEY_FNAME = "key.json"

def create_client(key_file):
    return datastore.Client.from_service_account_json(key_file)

'''
add one entity to GCP
'''
def add_entity(client, entity_kind, sample):
    key = client.key(entity_kind)

    new_entity = datastore.Entity(key)

    new_entity.update(sample)

    client.put(new_entity)

    return new_entity.key

'''
read data from local file and transform into json format
'''
def load_local(fname):
    data = pd.read_csv(fname)
    return data

def transform_upload_data(data):
    properties = list(data.columns)
    json_list = []
    num_samples = data.shape[0]
    for i in range(num_samples):
        if i > 20:
            break
        if i % 10 == 0:
            print "processed %d of %d"%(i+1, num_samples)
        json_dict = {properties[j]:data.iloc[i, j] for j in range(len(properties))}
        entity_key = add_entity(client, ENTITY_KIND, json_dict)

client = create_client(KEY_FNAME)
data = load_local(LOCAL_FNAME)


transform_upload_data(data)


def list_banks(client):
    query = client.query(kind='bank')
    query.order = ['amount']
    return list(query.fetch())