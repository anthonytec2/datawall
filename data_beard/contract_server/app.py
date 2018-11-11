from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def init():
    ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"    
    client = MongoClient(ADDRESS)
    db = client.datawall
    cols = db.list_collection_names()
    return "created app!"+cols[1]
# from flask import Flask
# # from pymongo import MongoClient

# app = Flask(__name__)

# @app.route("/")
# def init():
#     # load database
#     # client = build_connection(ADDRESS)
#     # ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"     
#     print "server built"

# # def build_connection(address):
# #     client = MongoClient(address)
# #     return client