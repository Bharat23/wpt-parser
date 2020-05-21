from WPTParser.JSONParser.DataExtracter import DataExtracter

class ObjectListDataExtracter(DataExtracter):

    def __init__(self):
        super().__init__()

    def extract(self, obj_list: list, key: str):
        key = key.replace(' ', '')
        dict_key, dict_value = key.split('=')
        for obj in obj_list:
            if obj.get(dict_key, None) is not None and obj.get(dict_key) == dict_value:
                return obj
        return None