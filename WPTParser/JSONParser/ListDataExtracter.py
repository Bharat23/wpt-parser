from WPTParser.JSONParser.DataExtracter import DataExtracter

class ListDataExtracter(DataExtracter):

    def __init__(self):
        super().__init__()

    def extract(self, list: list, index: int):
        try:
            return list[index]
        except KeyError as ex:
            return None