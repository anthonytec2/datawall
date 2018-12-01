from mongoengine import *
import company
import json


class Contract(Document):
    name = StringField(max_length=200, primary_key=True)
    content = StringField(max_length=2000000)
    status = StringField()
    companies = ListField(ReferenceField(
        company.Company, reverse_delete_rule=CASCADE))


def _get_contract(contract_name):
    found_contracts = Contract.objects(name=contract_name)
    if len(found_contracts) == 0:
        return None
    else:
        return found_contracts[0]


def _get_all_contracts():
    found_contracts = Contract.objects
    return found_contracts


def _get_contracts_of_company(company_name):
    found_contracts = Contract.objects
    return [contract for contract in found_contracts
            if company_name in [company.name for company in contract.companies]]


def _create_contract(contract_name, proposer_name, content, status, companies):
    if content is None:
        content = ""
    found_contract = _get_contract(contract_name)
    if found_contract is not None:
        return None
    found_proposer = company._get_company(proposer_name)
    if found_proposer is None:
        return None
    else:
        new_contract = Contract(name=contract_name,
                                content=content,
                                status=status,
                                companies=[proposer_name])
        new_contract.save()
        return new_contract


def _remove_contract(contract_name):
    found_contract = _get_contract(contract_name)
    if found_contract is None:
        return 0
    else:
        found_contract.delete()
        return 1


'''
TODO: cannot use found_contract.update_one, should be some problems in query method
'''


def _remove_company_from_contract(contract_name, company_name):
    found_contract = _get_contract(contract_name)
    if found_contract is None:
        return 0
    found_company = company._get_company(company_name)
    if found_company is None:
        return 0
    company_names_list = [c.name for c in found_contract.companies]
    if found_company.name not in company_names_list:
        return 0
    Contract.objects(name=contract_name).update_one(
        pull__companies=found_company)

    return 1


def _insert_company_to_contract(contract_name, company_name):
    found_contract = _get_contract(contract_name)
    if found_contract is None:
        return 0
    found_company = company._get_company(company_name)
    if found_company is None:
        return 0
    company_names_list = [c.name for c in found_contract.companies]
    if found_company.name in company_names_list:
        return 0
    Contract.objects(name=contract_name).update_one(
        push__companies=found_company)
    return 1


def _to_dict(contract):
    return {
        "name": contract.name,
        "content": contract.content,
        "status": contract.status,
        "companies": [c.name for c in contract.companies]
    }


def _jsonify(contract):
    return json.dumps(_to_dict(contract))
