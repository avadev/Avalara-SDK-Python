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
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from Avalara.SDK.models.EInvoicing.V1.report_download_response import ReportDownloadResponse
from Avalara.SDK.models.EInvoicing.V1.report_item import ReportItem
from Avalara.SDK.models.EInvoicing.V1.report_list_response import ReportListResponse
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException
from Avalara.SDK.oauth_helper.AvalaraSdkOauthUtils import avalara_retry_oauth

class ReportsApi(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("26.4.0")
        self.api_client = api_client
		
        self.download_report_endpoint = _Endpoint(
            settings={
                'response_type': (ReportDownloadResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/reports/{reportId}/$download',
                'operation_id': 'download_report',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'report_id',
                    'x_avalara_client',
                    'x_correlation_id',
                ],
                'required': [
                    'avalara_version',
                    'report_id',
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
                    'report_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'report_id': 'reportId',
                    'x_avalara_client': 'X-Avalara-Client',
                    'x_correlation_id': 'X-Correlation-ID',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'report_id': 'path',
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
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='EInvoicing'
        )
        self.get_report_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (ReportItem,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/reports/{reportId}/status',
                'operation_id': 'get_report_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'report_id',
                    'x_avalara_client',
                    'x_correlation_id',
                ],
                'required': [
                    'avalara_version',
                    'report_id',
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
                    'report_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'x_correlation_id':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'report_id': 'reportId',
                    'x_avalara_client': 'X-Avalara-Client',
                    'x_correlation_id': 'X-Correlation-ID',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'report_id': 'path',
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
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='EInvoicing'
        )
        self.get_reports_endpoint = _Endpoint(
            settings={
                'response_type': (ReportListResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/einvoicing/reports',
                'operation_id': 'get_reports',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'x_avalara_client',
                    'x_correlation_id',
                    'filter',
                    'top',
                    'skip',
                    'count',
                    'count_only',
                    'orderby',
                ],
                'required': [
                    'avalara_version',
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
                    'x_avalara_client':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'filter':
                        (str,),
                    'top':
                        (int,),
                    'skip':
                        (int,),
                    'count':
                        (str,),
                    'count_only':
                        (str,),
                    'orderby':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'x_avalara_client': 'X-Avalara-Client',
                    'x_correlation_id': 'X-Correlation-ID',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'count': '$count',
                    'count_only': '$countOnly',
                    'orderby': '$orderby',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'x_avalara_client': 'header',
                    'x_correlation_id': 'header',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'count': 'query',
                    'count_only': 'query',
                    'orderby': 'query',
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
    def download_report(
        self,
        avalara_version,
        report_id,
        **kwargs
    ):
        """Returns a pre-signed download URL for a report  # noqa: E501

        Returns a pre-signed URL to download the report file when it is available. If the report has not yet been generated, a 404 (not found) is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_report(avalara_version, report_id, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            report_id (str): The unique ID for this report as returned in a GET /reports response.

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
            ReportDownloadResponse
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
        kwargs['report_id'] = report_id
        return self.download_report_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get_report_by_id(
        self,
        avalara_version,
        report_id,
        **kwargs
    ):
        """Retrieves a report by its unique ID  # noqa: E501

        Retrieves a specific report by its unique identifier. Returns complete report details including metadata, status, and associated information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_report_by_id(avalara_version, report_id, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").
            report_id (str): The unique ID for this report as returned in a GET /reports response.

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
            ReportItem
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
        kwargs['report_id'] = report_id
        return self.get_report_by_id_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get_reports(
        self,
        avalara_version,
        **kwargs
    ):
        """Returns a list of reports  # noqa: E501

        Retrieves all reports with optional filtering, paging, and sorting. Results are filtered by tenant. Supports OData-style filtering using the $filter parameter. Use $top and $skip for paging; when more results exist, the response includes @nextLink to fetch the next page. Default sort order is by report generation date (descending).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_reports(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): Header that specifies the API version to use (for example \"1.6\").

        Keyword Args:
            x_avalara_client (str): Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\").. [optional]
            x_correlation_id (str): Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\").. [optional]
            filter (str): OData-style filter expression. Supports operators: eq, ne, gt, ge, lt, le, like, ilike, contains. Examples: status eq 'COMPLETED', reportGenerateDate gt '2025-11-01', transactionIds contains 'TXN-2025-001'. [optional]
            top (int): The number of items to include in the result.. [optional]
            skip (int): The number of items to skip in the result.. [optional]
            count (str): When set to true, the response body also includes the count of items in the collection.. [optional]
            count_only (str): When set to true, the response returns only the count of items in the collection.. [optional]
            orderby (str): OData-style orderby expression. Format: 'field asc' or 'field desc'. Default: reportGenerateDate desc. [optional] if omitted the server will use the default value of 'reportGenerateDate desc'
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
            ReportListResponse
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
        return self.get_reports_endpoint.call_with_http_info(**kwargs)

