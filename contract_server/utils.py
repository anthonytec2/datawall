import json

def mongo_obj_to_json(obj):
    obj["_id"] = str(obj["_id"])
    return json.dumps(obj)