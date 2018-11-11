from flask import Flask
from pymongo import MongoClient
from flask import request
import utils

app = Flask(__name__)
ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"    
DB_NAME = "datawall"
client = MongoClient(ADDRESS)
db = client[DB_NAME]
TABLE_LIST = ["contracts", "companys"]

'''
TABLE DEFINITIONS:
companies:
 company_name
 contract_list:[contractID1, contractID2, ...]

contracts:
 contract_name
 contract_content
 company_list:[companyID1, companyID2, ...]
'''

@app.route("/")
def home():
    print "in home"
    return "created app! "

# CRUD to the company database:
# create new company
# companyName, contractName
@app.route("/company/new/<string:company_name>", methods = ["PUT"])
def create_company(company_name):
    print "[in crate_company]"
    company_collection = db["companies"]
    existed_company = list(company_collection.find({"companyName":company_name}))
    if len(existed_company) > 0:
        print "length of query result is %d"%len(existed_company)
        return "%s already existed" % company_name
    company_collection.insert_one({"companyName": company_name, "contractList": []})
    return "created company: " + company_name

@app.route("/company/<company_name>", methods = ["GET"])
def get_company(company_name):
    print "[in get_company]"
    company_collection = db["companies"]
    companies_found = list(company_collection.find({"companyName":company_name}))
    if len(companies_found) == 0:
        return "Not found"
    else:
        assert len(companies_found) == 1
        return utils.mongo_obj_to_json(companies_found[0])

@app.route("/company/remove", methods = ["PUT"])
def remove_company():
    # delete from companies collection
    # delete from contracts
    pass

@app.route("/company/<company_name>/insert_contract/<contract_name>", methods = ["PUT"])
def insert_contract_to_company(company_name, contract_name):

    pass

@app.route("/company/<company_name>/remove_contract/<contract_name>", methods = ["PUT"])
def remove_contract_from_company(company_name, contract_name):
    pass

# CRUD to the contract database
# create new contract
@app.route("/contract/new", methods = ["POST"])
def crate_contract():
    pass

@app.route("/contract/<contract_name>", methods = ["GET"])
def get_contract(company_name):
    pass

@app.route("contract/<contract_name>")
def remove_contract(contract_name):
    pass

@app.route("contract/<contract_name>/remove_company/<company_name>", methods = ["PUT"])
def remove_company_from_contract(contract_name, company_name):
    pass
@app.route("/contract/<contract_name>/insert_company/<company_name>", methods = ["PUT"])
def insert_company_to_contract(contract_name, company_name):
    pass