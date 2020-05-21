from WPTParser.JSONParser.DataExtracter import DataExtracter

class KeyDataExtracter(DataExtracter):
    
    def __init__(self):
        super().__init__()

    def extract(self, obj: dict, key: str):
        return obj.get(key, None)