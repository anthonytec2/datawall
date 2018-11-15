import json

class Content:
    def __init__(self, content_dict):
        try:
            self.content_text = json.dumps(content_dict)
            # sequential?
            self.train_type = content_dict["train_type"]
            # [NOT CLEAR]
            self.monitor_type = content_dict["monitor_type"]
            # GCP IO info
            self.io_ip = content_dict["io_ip"]
            # malicious data detection 
            self.malicious_detect = content_dict["malicious_detect"]
            # model definition. may be loaded from ONNX
            self.model_structure = content_dict["model_structure"]
            # required participants
            self.required_participants = content_dict["required_participants"]
        except:
            print "Not enough params to build contract content"
    
    def to_str(self):
        return self.content_text
    
    