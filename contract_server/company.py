from mongoengine import *

class Company(Document):
    name = StringField(max_length=200, primary_key = True)

def _create_company(company_name):
    found_companies = _get_company(company_name)
    if found_companies is not None:
        return None
    company = Company(name = company_name)
    company.save()
    return company

def _get_company(company_name):
    found_companies = Company.objects(name = company_name)
    if len(found_companies) == 0:
        return None
    else:
        return found_companies[0]

def _remove_company(company_name):
    found_company = _get_company(company_name)
    if found_company is None:
        return 0
    else:
        found_company.delete()
        return 1
        
def _jsonify(company):
    return company.name