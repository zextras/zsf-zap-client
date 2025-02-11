import http.client
import json
import typing
import urllib.parse

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

        try:
            connection.request(
                body=body,
                headers={
                    **self.__api_key.signature_headers(
                        body=body,
                        method=method,
                        url=self.__url_for_path(path)
                    ),
                    **headers
                },
                method=method,
                url=self.__url_for_path(path),
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

        if self.__port is not None and (
                self.__secure == False and self.__port != 80 or
                self.__secure == True and self.__port != 443
        ):
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

    def find_by_email_address(self, email_address: str):
        params = urllib.parse.urlencode({'name': email_address})

        path = f'/api/v1/search/by-email-address?{params}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response_with_none_on_not_found
        )

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
        )

    def get_calendar_resource(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/calendar-resources/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_calendar_resources(self, page: int = None):
        if page is None:
            path = '/api/v1/calendar-resources'
        else:
            path = f'/api/v1/calendar-resources/?page={page}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

    def get_class_of_service(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/classes-of-service/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_classes_of_service(self, page: int = None):
        if page is None:
            path = '/api/v1/classes-of-service'
        else:
            path = f'/api/v1/classes-of-service/?page={page}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

    def get_distribution_list(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/distribution-lists/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_distribution_lists(self, page: int = None):
        if page is None:
            path = '/api/v1/distribution-lists'
        else:
            path = f'/api/v1/distribution-lists/?page={page}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

    def get_domain(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/domains/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_domains(self, page: int = None):
        if page is None:
            path = '/api/v1/classes-of-service'
        else:
            path = f'/api/v1/classes-of-service/?page={page}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

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
