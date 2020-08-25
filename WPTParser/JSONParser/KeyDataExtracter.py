from WPTParser.JSONParser.DataExtracter import DataExtracter

class KeyDataExtracter(DataExtracter):
    
    def __init__(self):
        super().__init__()

    def extract(self, obj: dict, key: str):
        try:
            return obj.get(key, None)
        except Exception as ex:
            return None