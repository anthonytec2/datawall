import sys
from flask import Flask, request
from pymongo import MongoClient
from mongoengine import *
import company
import contract
import utils
import json

app = Flask(__name__)
ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"    
DB_NAME = "datawall"
connect(db = DB_NAME, host = ADDRESS)

@app.route("/")
def home():
    print "[in home]"
    return "created app! "

@app.route("/company/new", methods = ["POST"])
def create_company():
    print "[in create_company]"
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    found_company = company._create_company(company_name)
    if found_company is None:
        return "insertion failed"
    else:
        return company._jsonify(found_company)


@app.route("/company/<company_name>", methods = ["GET"])
def get_company(company_name):
    print "[in get_company]"
    found_company = company._get_company(company_name)
    if found_company is None:
        return "company not found"
    else:
        return company._jsonify(found_company)

@app.route("/company/remove", methods = ["PUT"])
def remove_company():
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    # delete from companies collection
    deleted = company._remove_company(company_name)
    if deleted:
        return "deleted"
    else:
        return "company not found"

# CRUD to the contract database
@app.route("/contract/new", methods = ["POST"])
def create_contract():
    print "[in create_contract]"
    # get the name of company that proposes it
    try:
        proposer_name = request.args["proposer"]
        contract_name = request.args["contract_name"]
        content = request.args["content"]
    except:
        return "Not enough parameters in request"
    new_contract = contract._create_contract(contract_name = contract_name, 
                                             proposer_name = proposer_name, 
                                             content = content, 
                                             status = "pending", 
                                             companies = [proposer_name])
    if new_contract is None:
        return "Contract creation failed"
    else:
        return contract._jsonify(new_contract)
    
    

@app.route("/contract/<contract_name>", methods = ["GET"])
def get_contract(contract_name):
    print "[in get_contract]"
    found_contract = contract._get_contract(contract_name)
    if found_contract is None:
        return "Contract not found"
    else:
        return contract._jsonify(found_contract)

@app.route("/contract/remove", methods = ["PUT"])
def remove_contract():
    try:
        contract_name = request.args["contract_name"]
    except:
        return "Not enough parameter in request"
    removed = contract._remove_contract(contract_name)
    if removed:
        return "deleted"
    else:
        return "Contract not found"

@app.route("/contract/<contract_name>/remove", methods = ["PUT"])
def remove_company_from_contract(contract_name):
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    removed = contract._remove_company_from_contract(contract_name, company_name)
    if removed:
        return "company %s removed from %s" % (company_name, contract_name)
    else:
        return "failure to remove %s from %s" % (company_name, contract_name)


@app.route("/contract/<contract_name>/insert", methods = ["PUT"])
def insert_company_to_contract(contract_name):
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    inserted = contract._insert_company_to_contract(contract_name, company_name)
    if inserted:
        return "company %s inserted to %s" % (company_name, contract_name)
    else:
        return "failure to insert %s to %s" % (company_name, contract_name)

@app.route("/script", methods = ["GET"])
def get_script_from_contract():
    try:
        contract_name = request.args["contract_name"]
    except:
        return "Not enough parameter in request"
