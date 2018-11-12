from mongoengine import *
from contract import Contract

class Company(Document):
    name = StringField(max_length=200, required = True)
    contracts = ListField(ReferenceField(Contract), required = True)