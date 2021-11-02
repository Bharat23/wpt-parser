import re

from WPTParser.JSONParser.DataExtracter import DataExtracter

class ObjectListDataRegexExtracter(DataExtracter):

    def __init__(self):
        super().__init__()

    def extract(self, obj_list: list, key: str):
        """extract the keys of format [{key~value}]

        Keyword Arguments:
            obj_list {list} -- list of objects received from the previous key
            key {str} -- key that needs to be processed

        Returns:
            {} -- The found dict
        """
        try:
            key = key.replace(' ', '')
            dict_key, dict_value = key.split('~')
            for obj in obj_list:
                
                regex_dict_value = re.compile(dict_value)
                if dict_key in obj and re.search(regex_dict_value, obj[dict_key]):
                    return obj
            return None
        except Exception as ex:
            return None