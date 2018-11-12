
import sys
from flask import Flask
from pymongo import MongoClient
from mongoengine import *
import utils
import json

app = Flask(__name__)
ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"    
DB_NAME = "datawall"
connect(db = DB_NAME, host = ADDRESS)

class Company(Document):
    name = StringField(max_length=200, primary_key = True)
class Contract(Document):
    name = StringField(max_length=200, primary_key = True)
    companies = ListField(ReferenceField(Company, reverse_delete_rule=CASCADE))

@app.route("/")
def home():
    print "[in home]"
    return "created app! "

# CRUD to the company database:
# create new company
# companyName, contractName
@app.route("/company/new/<company_name>", methods = ["PUT"])
def create_company(company_name):
    print "[in create_company]"
    found_companies = Company.objects(name = company_name)
    if len(found_companies) > 0:
        print "company existed"
        return "Already existed"
    company = Company(name = company_name)
    company.save()
    return company_name

@app.route("/company/<company_name>", methods = ["GET"])
def get_company(company_name):
    print "[in get_company]"
    found_companies = Company.objects(name = company_name)
    if len(found_companies) > 1:
        print "more than one companies found"
        return "Too many found"
    elif len(found_companies) == 0:
        return "Found Nothing"
    else:
        return found_companies[0].name

@app.route("/company/<company_name>/remove", methods = ["PUT"])
def remove_company(company_name):
    # delete from companies collection
    Company.objects(name = company_name).delete()
    return "deleted"

# CRUD to the contract database
# create new contract
@app.route("/contract/new/<contract_name>", methods = ["POST"])
def create_contract(contract_name):
    print "[in create_contract]" 
    found_contracts = Contract.objects(name = contract_name)
    if len(found_contracts) >= 1:
        return "Already existed"
    else:
        new_contract = Contract(name = contract_name, companies = [])
        new_contract.save()
        return "New contract created"

@app.route("/contract/<contract_name>", methods = ["GET"])
def get_contract(contract_name):
    print "[in get_contract]"
    found_contracts = Contract.objects(name = contract_name)
    if len(found_contracts) == 0:
        return "Nothing found"
    else:
        return found_contracts.name

@app.route("/contract/contract_name>/remove", methods = ["PUT"])
def remove_contract(contract_name):
    Contract.objects(name = contract_name).delete()
    return "deleted"

@app.route("/contract/<contract_name>/remove_company/<company_name>", methods = ["PUT"])
def remove_company_from_contract(contract_name, company_name):
    found_contracts = Contract.objects(name = contract_name)
    if len(found_contracts) == 0:
        return "Contract not found"
    found_companies = Company.objects(name = company_name)
    if len(company_name) == 0:
        return "Company not found"
    else:
        found_contracts[0].update_one(pull__companies = found_companies[0])
        return "Company removed from contract"

@app.route("/contract/<contract_name>/insert_company/<company_name>", methods = ["PUT"])
def insert_company_to_contract(contract_name, company_name):
    found_contracts = Contract.objects(name = contract_name)
    if len(found_contracts) == 0:
        return "Contract not found"
    found_companies = Company.objects(name = company_name)
    if len(company_name) == 0:
        return "Company not found"
    else:
        found_contracts[0].update_one(push__companies = found_companies[0])
        return "Company inserted to contract"