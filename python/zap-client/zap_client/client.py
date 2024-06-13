import http.client
import json
import typing

from .api_key import ApiKey
from .exceptions import *

__all__ = ['Client']


class Client:
    def __init__(
            self, *,
            api_key: ApiKey, host: str, port: int = None, secure: bool = True
    ):
        self.__api_key = api_key
        self.__host = host
        self.__port = port
        self.__secure = secure

    def __get_connection(self) -> http.client.HTTPConnection:
        if self.__secure:
            return http.client.HTTPSConnection(
                host=self.__host, port=self.__port
            )
        else:
            return http.client.HTTPConnection(
                host=self.__host, port=self.__port
            )

    def __request(
            self,
            method: str,
            path: str,
            body: str = None,
            headers: dict[str, str] = None,
            transform_response: typing.Callable = None,
    ):
        connection = self.__get_connection()

        if headers is None:
            headers = {}

        url = self.__url_for_path(path)

        try:
            connection.request(
                body=body,
                headers={
                    **self.__api_key.signature_headers(
                        body=body,
                        method=method,
                        url=url
                    ),
                    **headers
                },
                method=method,
                url=url,
            )

            if transform_response is None:
                return connection.getresponse()
            else:
                return transform_response(connection.getresponse())
        finally:
            connection.close()

    def __url_for_path(self, path: str):
        url = 'https' if self.__secure else 'http'
        url += f'://{self.__host}'

        if self.__port is not None:
            url += f':{self.__port}'

        return url + path

    def create_account(self, attributes: dict):
        return self.__request(
            'POST',
            '/api/v1/accounts',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def create_calendar_resource(self, attributes: dict):
        return self.__request(
            'POST',
            '/api/v1/calendar-resources',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def create_distribution_list(self, attributes: dict):
        return self.__request(
            'POST',
            '/api/v1/distribution-lists',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def destroy_account(self, id: str):
        self.__request('DELETE', f'/api/v1/accounts/{id}')

    def destroy_calendar_resource(self, id: str):
        self.__request('DELETE', f'/api/v1/calendar-resources/{id}')

    def destroy_distribution_list(self, id: str):
        self.__request('DELETE', f'/api/v1/distribution-lists/{id}')

    def get_account(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/accounts/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_accounts(self, *, page: int = None):
        if page is None:
            path = '/api/v1/accounts'
        else:
            path = f'/api/v1/accounts/?page={page}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )['data']

    def get_calendar_resource(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/calendar-resources/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_calendar_resources(self):
        return self.__request(
            'GET',
            '/api/v1/calendar-resources',
            transform_response=_parse_response
        )['data']

    def get_class_of_service(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/classes-of-service/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_classes_of_service(self):
        return self.__request(
            'GET',
            '/api/v1/classes-of-service',
            transform_response=_parse_response
        )['data']

    def get_distribution_list(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/distribution-lists/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_distribution_lists(self):
        return self.__request(
            'GET',
            '/api/v1/distribution-lists',
            transform_response=_parse_response
        )['data']

    def get_domain(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/domains/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_domains(self):
        return self.__request(
            'GET',
            '/api/v1/domains',
            transform_response=_parse_response
        )['data']

    def update_account(self, id: str, attributes: dict):
        return self.__request(
            'PUT',
            f'/api/v1/accounts/{id}',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def update_calendar_resource(self, id: str, attributes: dict):
        return self.__request(
            'PUT',
            f'/api/v1/calendar-resources/{id}',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def update_distribution_list(self, id: str, attributes: dict):
        return self.__request(
            'PUT',
            f'/api/v1/distribution-lists/{id}',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )


def _parse_response(response: http.client.HTTPResponse):
    if response.status in range(200, 300):
        return json.load(response)
    elif response.status == 429:
        raise RateLimitExceededException()
    elif response.headers.get_content_type() == 'text/plain':
        raise Exception(
            f'{response.status} {response.reason} {response.read().decode()}'
        )
    else:
        raise Exception(f'{response.status} {response.reason}')


def _parse_response_with_none_on_not_found(response: http.client.HTTPResponse):
    if response.status != 404:
        return _parse_response(response)
