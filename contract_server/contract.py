from mongoengine import *
from company import Company

class Contract(Document):
    name = StringField(max_length=200, required = True)
    companies = ListField(ReferenceField(Company), required = True)