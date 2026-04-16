"""
AvaTax Software Development Kit for Python.

   Copyright 2022 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    Avalara E-Invoicing API
    An API that supports sending data for an E-Invoicing compliance use-case. 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    26.4.0
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

import re  # noqa: F401
import sys  # noqa: F401
import decimal

from Avalara.SDK.api_client import ApiClient, Endpoint as _Endpoint
from Avalara.SDK.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from datetime import date
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from Avalara.SDK.models.EInvoicing.V1.code_list_list_response import CodeListListResponse
from Avalara.SDK.models.EInvoicing.V1.code_list_response import CodeListResponse
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException
from Avalara.SDK.oauth_helper.AvalaraSdkOauthUtils import avalara_retry_oauth

class CodeListsApi(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("26.4.0")
        self.api_client = api_client
		
        self.get_code_list_endpoint = _Endpoint(
            settings={
                'response_type': (CodeListResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/codelists/{codelistId}',
                'operation_id': 'get_code_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'codelist_id',
                    'country_code',
                    'x_avalara_client',
                    'effective_date',
                    'sunset_date',
                ],
                'required': [
                    'avalara_version',
                    'codelist_id',
                    'country_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'avalara_version':
                        (str,),
                    'codelist_id':
                        (str,),
                    'country_code':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'effective_date':
                        (date,),
                    'sunset_date':
                        (date,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'codelist_id': 'codelistId',
                    'country_code': 'countryCode',
                    'x_avalara_client': 'X-Avalara-Client',
                    'effective_date': 'effectiveDate',
                    'sunset_date': 'sunsetDate',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'codelist_id': 'path',
                    'country_code': 'query',
                    'x_avalara_client': 'header',
                    'effective_date': 'query',
                    'sunset_date': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '1.6',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='EInvoicing'
        )
        self.get_code_list_list_endpoint = _Endpoint(
            settings={
                'response_type': (CodeListListResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/codelists',
                'operation_id': 'get_code_list_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'country_code',
                    'x_avalara_client',
                    'effective_date',
                    'sunset_date',
                    'count',
                    'count_only',
                    'top',
                    'skip',
                ],
                'required': [
                    'avalara_version',
                    'country_code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'avalara_version':
                        (str,),
                    'country_code':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'effective_date':
                        (date,),
                    'sunset_date':
                        (date,),
                    'count':
                        (str,),
                    'count_only':
                        (str,),
                    'top':
                        (int,),
                    'skip':
                        (int,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'country_code': 'countryCode',
                    'x_avalara_client': 'X-Avalara-Client',
                    'effective_date': 'effectiveDate',
                    'sunset_date': 'sunsetDate',
                    'count': '$count',
                    'count_only': '$countOnly',
                    'top': '$top',
                    'skip': '$skip',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'country_code': 'query',
                    'x_avalara_client': 'header',
                    'effective_date': 'query',
                    'sunset_date': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'top': 'query',
                    'skip': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '1.6',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='EInvoicing'
        )

    @avalara_retry_oauth(max_retry_attempts=2)
    def get_code_list(
        self,
        avalara_version,
        codelist_id,
        country_code,
        **kwargs
    ):
        """Retrieves a code list by ID for a specific country  # noqa: E501

        A Code List is a controlled set of predefined, standardized values used to populate specific fields in electronic documents (such as e-invoices). Each code has a stable, machine-readable identifier and a human-readable description. Code Lists are typically based on global standards (e.g., UN/CEFACT, ISO, EN16931) and may include jurisdiction-specific extensions or restrictions.<br><br>Code Lists are versioned, and each version may have defined effective and sunset dates to ensure that the correct set of allowable values is applied according to regulatory or jurisdictional requirements.<br><br>By default, the API returns only non-expired code list versions (versions where the sunset date has not passed). To retrieve expired versions or filter by specific date ranges, use the <code>effectiveDate</code> and <code>sunsetDate</code> query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_code_list(avalara_version, codelist_id, country_code, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            codelist_id (str): System-generated unique identifier of the code list definition. Typically a UUID used to reference this code list internally or via APIs.
            country_code (str): Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction this code list applies to.

        Keyword Args:
            x_avalara_client (str): Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\").. [optional]
            effective_date (date): Filter code list versions by effective date. Returns versions that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided.. [optional]
            sunset_date (date): Filter code list versions by sunset date. Returns versions that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired versions are returned.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CodeListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['avalara_version'] = avalara_version
        kwargs['codelist_id'] = codelist_id
        kwargs['country_code'] = country_code
        return self.get_code_list_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get_code_list_list(
        self,
        avalara_version,
        country_code,
        **kwargs
    ):
        """Returns a list of code lists for a specific country  # noqa: E501

        Get a list of code lists on the Avalara E-Invoicing platform for the specified country. By default, the API returns only non-expired code lists (code lists where the sunset date has not passed). To retrieve expired code lists or filter by specific date ranges, use the <code>effectiveDate</code> and <code>sunsetDate</code> query parameters.<br><br>A Code List is a controlled set of predefined, standardized values used to populate specific fields in electronic documents (such as e-invoices). Each code has a stable, machine-readable identifier and a human-readable description. Code Lists are typically based on global standards (e.g., UN/CEFACT, ISO, EN16931) and may include jurisdiction-specific extensions or restrictions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_code_list_list(avalara_version, country_code, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            country_code (str): Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction for which code lists should be returned.

        Keyword Args:
            x_avalara_client (str): Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\").. [optional]
            effective_date (date): Filter code lists by effective date. Returns code lists that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided.. [optional]
            sunset_date (date): Filter code lists by sunset date. Returns code lists that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired code lists are returned.. [optional]
            count (str): When set to true, the response body also includes the count of items in the collection.. [optional]
            count_only (str): When set to true, the response returns only the count of items in the collection.. [optional]
            top (int): The number of items to include in the result.. [optional]
            skip (int): The number of items to skip in the result.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CodeListListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        self.__verify_api_client(self.api_client)
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['avalara_version'] = avalara_version
        kwargs['country_code'] = country_code
        return self.get_code_list_list_endpoint.call_with_http_info(**kwargs)

