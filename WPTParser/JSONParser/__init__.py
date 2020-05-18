class JSONParser():

    def __init__(self, json: dict = {}):
        self.json = json
        self.picked_json = {}

    def pick(self, key: str = None, keys: list = [], key_delimiter: str = '.'):
        if key is not None:
            final_obj = self._recursive_find(self.json, key.split(key_delimiter), 0)
            self.picked_json[key] = final_obj
        elif len(keys) > 0:
            for key in keys:
                final_obj = self._recursive_find(self.json, key.split(key_delimiter), 0)
                self.picked_json[key] = final_obj
        return self

    def _recursive_find(self, obj: dict = {}, level_list: list = [], index: int = 0):
        if index == (len(level_list) - 1):
            return obj.get(level_list[index], None)
        else:
            current_level_obj = obj.get(level_list[index], None)
            if current_level_obj is not None:
                return self._recursive_find(current_level_obj, level_list, index + 1)
            else:
                return None

    def remove(self, key: str = None, keys: list = []):
        pass

    def exec(self):
        return self.picked_json
