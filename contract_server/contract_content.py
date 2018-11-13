class Content:
    def __init__(self, train_type, 
                monitor_type, 
                io_ip, 
                malicious_detect, 
                model_structure):
        # sequential?
        self.train_type = train_type
        # [NOT CLEAR]
        self.monitor_type = monitor_type
        # GCP IO info
        self.io_ip = io_ip
        # malicious data detection 
        self.malicious_detect = malicious_detect
        # model definition. may be loaded from ONNX
        self.model_structure = model_structure
        # required participants
        self.required_participants = None
    
    