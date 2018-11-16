from pymongo import MongoClient
from mongoengine import *
class User(Document):
    user = StringField(max_length=200, required=True)
    payout=FloatField(required=True)
    num_inf=FloatField(required=True)

ADDRESS = "mongodb://datawall:datawall1@ds255403.mlab.com:55403/inf-node"    
DB_NAME = "datawall"
client=connect(db = DB_NAME, host = ADDRESS)
db = client[DB_NAME]

def set_zero():
    User.objects(user='citi').update_one(payout=0)
    User.objects(user='jpm').update_one(payout=0)
    User.objects(user='boa').update_one(payout=0)
    User.objects(user='datawall').update_one(payout=0)

if __name__=='__main__':
    set_zero()