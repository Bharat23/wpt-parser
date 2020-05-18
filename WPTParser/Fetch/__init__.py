import requests

class Fetch():

    def json(self, test_id='200205_GV_35399987e1bf158adebe02183f590b17'):
        # api rejects the request with unauthorized if user-agent header not set
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        url = 'https://wpt1.speedcurve.com/jsonResult.php?test={0}'.format(test_id)
        json_data = requests.get(url, headers = headers)
        json_data = json_data.json()
        return json_data