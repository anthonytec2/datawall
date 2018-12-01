import sys
from flask import Flask, request
from pymongo import MongoClient
from mongoengine import *
import company
import contract
import contract_content
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


ADDRESS = "mongodb://datawall:datawall123@ds159273.mlab.com:59273/datawall"
DB_NAME = "datawall"
connect(db=DB_NAME, host=ADDRESS)


@app.route("/")
@cross_origin()
def home():
    return "created app! "


@app.route("/company/new", methods=["POST"])
@cross_origin()
def create_company():
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    found_company = company._create_company(company_name)
    if found_company is None:
        return "insertion failed"
    else:
        return company._jsonify(found_company)


@app.route("/company/<company_name>", methods=["GET"])
@cross_origin()
def get_company(company_name):
    found_company = company._get_company(company_name)
    if found_company is None:
        return "company not found"
    else:
        return company._jsonify(found_company)


@app.route("/company/<company_name>/contracts", methods=["GET"])
@cross_origin()
def get_company_contracts(company_name):
    found_contracts = contract._get_contracts_of_company(company_name)
    contracts_info = json.dumps({
        "company": company_name,
        "contracts": [contract._to_dict(c) for c in found_contracts]
    })
    return contracts_info


@app.route("/company/remove", methods=["PUT"])
@cross_origin()
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


@app.route("/contract/new", methods=["POST"])
@cross_origin()
def create_contract():
    # get the name of company that proposes it
    try:
        proposer_name = request.args["proposer"]
        contract_name = request.args["contract_name"]
        content_dict = {k: v for k, v in request.args.items()
                        if not k in ["proposer", "contract_name", "content"]}
    except:
        return "Not enough parameters in request"
    content = contract_content.Content(content_dict)
    content_text = content.to_str()
    new_contract = contract._create_contract(contract_name=contract_name,
                                             proposer_name=proposer_name,
                                             content=content_text,
                                             status="pending",
                                             companies=[proposer_name])
    if new_contract is None:
        return "Contract creation failed"
    else:
        return contract._jsonify(new_contract)


@app.route("/contract/<contract_name>", methods=["GET"])
@cross_origin()
def get_contract(contract_name):
    found_contract = contract._get_contract(contract_name)
    if found_contract is None:
        return "Contract not found"
    else:
        return contract._jsonify(found_contract)


@app.route("/contract/all", methods=["GET"])
@cross_origin()
def get_all_contracts():
    found_contracts = contract._get_all_contracts()
    return json.dumps({
        "contracts": [contract._to_dict(c) for c in found_contracts]
    })


@app.route("/contract/remove", methods=["PUT"])
@cross_origin()
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


@app.route("/contract/<contract_name>/remove", methods=["PUT"])
@cross_origin()
def remove_company_from_contract(contract_name):
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    removed = contract._remove_company_from_contract(
        contract_name, company_name)
    if removed:
        return "company %s removed from %s" % (company_name, contract_name)
    else:
        return "failure to remove %s from %s" % (company_name, contract_name)


@app.route("/contract/<contract_name>/insert", methods=["PUT"])
@cross_origin()
def insert_company_to_contract(contract_name):
    try:
        company_name = request.args["company_name"]
    except:
        return "Not enough parameter in request"
    inserted = contract._insert_company_to_contract(
        contract_name, company_name)
    if inserted:
        return "company %s inserted to %s" % (company_name, contract_name)
    else:
        return "failure to insert %s to %s" % (company_name, contract_name)


@app.route("/script", methods=["GET"])
@cross_origin()
def get_script_from_contract():
    return json.dumps(
        {
            "status": 1,
            "script": '''print 'YOUR MACHINE IS LOCKED' ''',
            "bucket_list":
            [
                {
                    "company_name": "Citi",
                    "bucket_info":
                    [
                        {
                            "bucket_name": "beardless bucket",
                            "bucket_key": "key to beard"
                        }
                    ]
                },
                {
                    "company_name": "JPM",
                    "bucket_info":
                    [
                        {
                            "bucket_name": "toxic bucket",
                            "bucket_key": "key to BBQ"
                        }
                    ]
                },
            ]
        })
    # try:
    #     contract_name = request.args["contract_name"]
    # except:
    #     return "Not enough parameter in request"
    # found_contract = contract._get_contract(contract_name)
    # if found_contract is None:
    #     return ""
    # else:
    #     return found_contract.content
