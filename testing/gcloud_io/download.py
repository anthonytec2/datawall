# coding: utf-8

from google.cloud import datastore
import pandas as pd

ENTITY_KIND = "bank"
KEY_FNAME = "key.json"

def create_client(key_file):
    return datastore.Client.from_service_account_json(key_file)


def list_banks(client):
    query = client.query(kind='bank')
    # query.order = ['amount']
    return list(query.fetch())

client = create_client(KEY_FNAME)

query_result = list_banks(client)
print query_result[0]
