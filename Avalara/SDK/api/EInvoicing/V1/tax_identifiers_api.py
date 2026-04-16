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
from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_request import TaxIdentifierRequest
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_response import TaxIdentifierResponse
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_schema_by_country200_response import TaxIdentifierSchemaByCountry200Response
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException
from Avalara.SDK.oauth_helper.AvalaraSdkOauthUtils import avalara_retry_oauth

class TaxIdentifiersApi(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("26.4.0")
        self.api_client = api_client
		
        self.tax_identifier_schema_by_country_endpoint = _Endpoint(
            settings={
                'response_type': (TaxIdentifierSchemaByCountry200Response,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/tax-identifiers/schema',
                'operation_id': 'tax_identifier_schema_by_country',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'country_code',
                    'x_avalara_client',
                    'x_correlation_id',
                    'type',
                ],
                'required': [
                    'avalara_version',
                    'country_code',
                ],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "&#39;request&#39;": 'request',
                        "&#39;response&#39;": 'response'
                    },
                },
                'openapi_types': {
                    'avalara_version':
                        (str,),
                    'country_code':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'country_code': 'countryCode',
                    'x_avalara_client': 'X-Avalara-Client',
                    'x_correlation_id': 'X-Correlation-ID',
                    'type': 'type',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'country_code': 'query',
                    'x_avalara_client': 'header',
                    'x_correlation_id': 'header',
                    'type': 'query',
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
        self.validate_tax_identifier_endpoint = _Endpoint(
            settings={
                'response_type': (TaxIdentifierResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/tax-identifiers/validate',
                'operation_id': 'validate_tax_identifier',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'tax_identifier_request',
                    'x_avalara_client',
                    'x_correlation_id',
                ],
                'required': [
                    'avalara_version',
                    'tax_identifier_request',
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
                    'tax_identifier_request':
                        (TaxIdentifierRequest,),
                    'x_avalara_client':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'x_avalara_client': 'X-Avalara-Client',
                    'x_correlation_id': 'X-Correlation-ID',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'tax_identifier_request': 'body',
                    'x_avalara_client': 'header',
                    'x_correlation_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '1.6',
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            required_scopes='',
            microservice='EInvoicing'
        )

    @avalara_retry_oauth(max_retry_attempts=2)
    def tax_identifier_schema_by_country(
        self,
        avalara_version,
        country_code,
        **kwargs
    ):
        """Returns the tax identifier request and response schema for a specific country.  # noqa: E501

        Returns the tax identifier request and response schema for a specific country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tax_identifier_schema_by_country(avalara_version, country_code, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            country_code (str): Two-letter ISO 3166 country code for which to retrieve the schema (for example \"DE\").

        Keyword Args:
            x_avalara_client (str): Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\").. [optional]
            x_correlation_id (str): Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\").. [optional]
            type (str): Specifies which schema to return: \"request\" to receive the request validation schema or \"response\" to receive the response validation schema.. [optional]
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
            TaxIdentifierSchemaByCountry200Response
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
        return self.tax_identifier_schema_by_country_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def validate_tax_identifier(
        self,
        avalara_version,
        tax_identifier_request,
        **kwargs
    ):
        """Validates a tax identifier.  # noqa: E501

        This endpoint verifies whether a given tax identifier is valid and properly formatted according to the rules of the applicable country or tax system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_tax_identifier(avalara_version, tax_identifier_request, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            tax_identifier_request (TaxIdentifierRequest):

        Keyword Args:
            x_avalara_client (str): Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\").. [optional]
            x_correlation_id (str): Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\").. [optional]
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
            TaxIdentifierResponse
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
        kwargs['tax_identifier_request'] = tax_identifier_request
        return self.validate_tax_identifier_endpoint.call_with_http_info(**kwargs)

