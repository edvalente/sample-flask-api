import requests

class Client:

    def __init__(self, host='localhost', port='5000'):
        self.host = host
        self.port = port
        if 'local' in host:
            self.host = '127.0.0.1'
        self.base_url = 'http://' + self.host + ':' + self.port

    def get_score(self, pk):
        url = self.base_url + '/get/' + str(pk)
        response = requests.post(url=url)
        pass

    def update_data(self, dir):
        pass

    def foo(self):
        url = self.base_url + '/'
        response = requests.get(url)
        return response.json()