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

    def create_signature(self, organization_id: str, attributes: dict):
        return self.__request(
            'POST',
            f'/api/v1/organizations/{organization_id}/signatures',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def create_signature_link(self, signature_id: str, attributes: dict):
        return self.__request(
            'POST',
            f'/api/v1/signatures/{signature_id}/links',
            json.dumps(attributes),
            {'Content-Type': 'application/json'},
            transform_response=_parse_response
        )

    def deploy_signature_link(self, signature_id: str, id: str):
        return self.__request(
            'POST',
            f'/api/v1/signatures/{signature_id}/links/{id}/deploy'
        )

    def deploy_signature_links(self, signature_id: str):
        return self.__request(
            'POST',
            f'/api/v1/signatures/{signature_id}/links/all/deploy'
        )

    def destroy_account(self, id: str):
        self.__request('DELETE', f'/api/v1/accounts/{id}')

    def destroy_calendar_resource(self, id: str):
        self.__request('DELETE', f'/api/v1/calendar-resources/{id}')

    def destroy_distribution_list(self, id: str):
        self.__request('DELETE', f'/api/v1/distribution-lists/{id}')

    def destroy_signature(self, id: str):
        self.__request('DELETE', f'/api/v1/signatures/{id}')

    def destroy_signature_link(self, id: str):
        self.__request('DELETE', f'/api/v1/signature-links/{id}')

    def get_account(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/accounts/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_accounts(
            self,
            *,
            domain_id: str = None,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if domain_id is not None:
            path = f'/api/v1/domains/{domain_id}/accounts'
        elif organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/accounts'
        else:
            path = '/api/v1/accounts'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

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

    def get_calendar_resources(
            self,
            *,
            domain_id: str = None,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if domain_id is not None:
            path = f'/api/v1/domains/{domain_id}/calendar-resources'
        elif organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/calendar-resources'
        else:
            path = '/api/v1/calendar-resources'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

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

    def get_classes_of_service(
            self,
            *,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/classes-of-service'
        else:
            path = '/api/v1/classes-of-service'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

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

    def get_distribution_lists(
            self,
            *,
            domain_id: str = None,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if domain_id is not None:
            path = f'/api/v1/domains/{domain_id}/distribution-lists'
        elif organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/distribution-lists'
        else:
            path = '/api/v1/distribution-lists'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

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

    def get_domains(
            self,
            *,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/domains'
        else:
            path = '/api/v1/domains'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

    def get_signature(self, id: str):
        return self.__request(
            'GET',
            f'/api/v1/signatures/{id}',
            transform_response=_parse_response_with_none_on_not_found
        )

    def get_signature_links(
            self,
            *,
            items: int = None,
            metadata_only: bool = False,
            page: int = None,
            organization_id: str = None,
            signature_id: str = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if signature_id is not None:
            path = f'/api/v1/signatures/{signature_id}/links'
        elif organization_id is not None:
            path = f'/api/v1/organizations/{organization_id}/signature-links'
        else:
            path = '/api/v1/signature-links'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

        return self.__request(
            'GET',
            path,
            transform_response=_parse_response
        )

    def get_signatures(
            self,
            *,
            items: int = None,
            metadata_only: bool = False,
            organization_id: str = None,
            page: int = None
    ):
        params = {}

        if items is not None:
            params['items'] = items

        if metadata_only:
            params['metadata_only'] = 1

        if page is not None:
            params['page'] = page

        if organization_id is None:
            path = '/api/v1/signatures'
        else:
            path = f'/api/v1/organizations/{organization_id}/signatures'

        if len(params) > 0:
            path += f'?{urllib.parse.urlencode(params)}'

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

    def update_signature(self, id: str, attributes: dict):
        return self.__request(
            'PUT',
            f'/api/v1/signatures/{id}',
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

    return None
