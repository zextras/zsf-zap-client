import hashlib
import time

__all__ = ['ApiKey']


class ApiKey:
    def __init__(self, id: str, secret: str):
        self.__id = id
        self.__secret = secret

    def sign(self, *, body=None, method, timestamp, url):
        if body is None:
            body = ''

        return hashlib.sha256(
            f'{self.__secret}|{timestamp}|{method}|{url}|{body}'.encode()
        ).hexdigest()

    def signature_headers(self, *, body=None, method, timestamp=None, url):
        if timestamp is None:
            timestamp = int(time.time() * 1000)

        return {
            'X-ZAP-API-Key': self.__id,
            'X-ZAP-Signature': self.sign(
                body=body, method=method, timestamp=timestamp, url=url
            ),
            'X-ZAP-Timestamp': timestamp,
        }
