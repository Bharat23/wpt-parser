class WPTParser:

    def __init__(self):
        self._BASE_WPT_URI = 'https://www.webpagetest.org'

    def WPT_URI(self, wpt_uri: str = None):
        if wpt_uri is not None:
            self._BASE_WPT_URI = wpt_uri
        return self._BASE_WPT_URI