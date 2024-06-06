import hashlib
import json
import time
import http.client


class Request:
    def __init__(self, url, method, headers, body, configuration):
        self.request = None
        self.timestamp = None
        self.configuration = configuration
        self.url = url
        self.method = method
        self.headers = headers
        if body is None:
            self.body = ''
        else:
            self.body = body

    def get_timestamp(self):
        self.timestamp = int(time.time() * 1000)

    def get_signature(self):
        return hashlib.sha256(f'{self.configuration.APISECRET}|{self.timestamp}|{self.method}|{self.url}|{self.body}'.encode()).hexdigest()

    def execute(self):
        connection = http.client.HTTPConnection(host='localhost', port=3000)

        self.get_timestamp()

        try:
            headers = {**self.headers, **{
                'Content-Type': 'application/json',
                'X-ZAP-API-Key': self.configuration.APIKEY,
                'X-ZAP-Signature': self.get_signature(),
                'X-ZAP-Timestamp': str(self.timestamp),
            }}

            connection.request(self.method, self.url, self.body, headers)

            response = connection.getresponse()
            return self.do_response(response)

        finally:
            connection.close()

    def do_response(self, response):
        if response.status == 200:
            decode = response.read().decode()
            return json.loads(decode)
        else:
            return None
