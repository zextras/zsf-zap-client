from . import configuration, request


class Zap:
    def __init__(self):
        self.configuration = configuration.Configuration()

    def load_config(self, filepath):
        self.configuration.load(filepath)

    def get(self, path, headers=None, params=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        url = f"{self.configuration.get_baseurl()}{path}"
        if params != {}:
            params_string = '&'.join([f"{key}={value}" for key, value in params.items()])
            url = f"{url}?{params_string}"

        req = request.Request(url, 'GET', headers, None, self.configuration)
        return req.execute()

    def post(self, path, body, headers=None):
        if headers is None:
            headers = {}

        url = f"{self.configuration.get_baseurl()}{path}"
        req = request.Request(url, 'POST', headers, body, self.configuration)
        return req.execute()

    def patch(self, path, body, headers=None):
        if headers is None:
            headers = {}

        url = f"{self.configuration.get_baseurl()}{path}"
        req = request.Request(url, 'PATCH', headers, body, self.configuration)
        return req.execute()

    def delete(self, path, headers=None):
        if headers is None:
            headers = {}

        url = f"{self.configuration.get_baseurl()}{path}"
        req = request.Request(url, 'DELETE', headers, None, self.configuration)
        return req.execute()