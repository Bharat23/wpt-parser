# TODO: ADD support for array type fields while parsing eg: data.Median.[0].value
import re

from WPTParser.Constants import RegexConstants
from WPTParser.JSONParser.KeyDataExtracter import KeyDataExtracter
from WPTParser.JSONParser.ListDataExtracter import ListDataExtracter
from WPTParser.JSONParser.ObjectListDataExtracter import ObjectListDataExtracter

class JSONParser():

    def __init__(self, json: dict = {}):
        self.json = json
        self.picked_json = {}

    def pick(self, key: str = None, keys: list = [], key_delimiter: str = '.'):
        """Extract key from provided JSON object and returns new object of specified keys

        Keyword Arguments:
            key {str} -- A single key that needs to be extracted (default: {None})
            keys {list} -- A list of keys that needs to be extracted (default: {[]})
            key_delimiter {str} -- JSON object level separator used in the keys provided (default: {'.'})

        Returns:
            JSONParser -- object of JSONParser to allow functional chaining
        """
        if key is not None:
            final_obj = self._recursive_find(self.json, key.split(key_delimiter), 0)
            self.picked_json[key] = final_obj
        elif len(keys) > 0:
            for key in keys:
                final_obj = self._recursive_find(self.json, key.split(key_delimiter), 0)
                self.picked_json[key] = final_obj
        return self

    def _recursive_find(self, obj: dict = {}, level_list: list = [], index: int = 0):
        """recursively find and extract the requested keys

        Keyword Arguments:
            obj {dict} -- object on which extraction needs to be done (default: {{}})
            level_list {list} -- list of key depth (default: {[]})
            index {int} -- index of the level list (default: {0})

        Returns:
            [type] -- The request value/dict/list
        """
        try:
            key, extracter = self._process_key(level_list[index])
            current_level_obj = extracter.extract(obj, key)
            if index == (len(level_list) - 1):
                return current_level_obj
            else:
                if current_level_obj is not None:
                    return self._recursive_find(current_level_obj, level_list, index + 1)
                else:
                    return None
        except Exception as ex:
            print('error', ex)
            return None

    def _process_key(self, key: str):
        """processes the key to make it usable for extraction and decides extraction type

        Arguments:
            key {str} -- the key which needs to extracted

        Returns:
            str, DataExtracter -- the key which needs to be extracted and Extracter object based on type of Extraction needed
        """
        extracter = KeyDataExtracter()
        if re.match(RegexConstants.INDEXED_ARRAY, key):
            key = int(re.findall(RegexConstants.INDEXED_ARRAY, key)[0])
            extracter = ListDataExtracter()
        elif re.match(RegexConstants.DICT_ARRAY_SEARCH, key):
            key = re.findall(RegexConstants.DICT_ARRAY_SEARCH, key)[0]
            extracter = ObjectListDataExtracter()
        return key, extracter


    def remove(self, key: str = None, keys: list = []):
        # TODO: Add remove key functionality
        pass

    def exec(self):
        """fetches the final object with extracted keys and their values

        Returns:
            dict -- the dictionary with final extracted values
        """
        return self.picked_json
