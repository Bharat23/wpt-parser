from WPTParser.JSONParser.DataExtracter import DataExtracter

class KeyDataExtracter(DataExtracter):
    
    def __init__(self):
        super().__init__()

    def extract(self, obj: any, key: str):
        try:
            if isinstance(obj, dict):
                return obj.get(key, None)
            elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], dict):
                extracted_list = []
                for obj_in_list in obj:
                    extracted_list.append(obj_in_list.get(key, None))
                return extracted_list
        except Exception as ex:
            return None