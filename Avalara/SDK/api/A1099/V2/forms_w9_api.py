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

    Avalara 1099 & W-9 API Definition
    ## 🔐 Authentication  Use **username/password** or generate a **license key** from: *Avalara Portal → Settings → License and API Keys*.  [More on authentication methods](https://developer.avalara.com/avatax-dm-combined-erp/common-setup/authentication/authentication-methods/)  [Test your credentials](https://developer.avalara.com/avatax/test-credentials/)  ## 📘 API & SDK Documentation  [Avalara SDK (.NET) on GitHub](https://github.com/avadev/Avalara-SDK-DotNet#avalarasdk--the-unified-c-library-for-next-gen-avalara-services)  [Code Examples – 1099 API](https://github.com/avadev/Avalara-SDK-DotNet/blob/main/docs/A1099/V2/Class1099IssuersApi.md#call1099issuersget) 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    25.7.2
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
from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import Optional, Union
from typing_extensions import Annotated
from Avalara.SDK.models.A1099.V2.iw9_form_data_models_one_of import IW9FormDataModelsOneOf
from Avalara.SDK.models.A1099.V2.paginated_w9_forms_model import PaginatedW9FormsModel
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException
from Avalara.SDK.oauth_helper.AvalaraSdkOauthUtils import avalara_retry_oauth

class FormsW9Api(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("25.7.2")
        self.api_client = api_client
		
        self.create_w9_form_endpoint = _Endpoint(
            settings={
                'response_type': (IW9FormDataModelsOneOf,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms',
                'operation_id': 'create_w9_form',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                    'iw9_form_data_models_one_of',
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
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'iw9_form_data_models_one_of':
                        (IW9FormDataModelsOneOf,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                    'iw9_form_data_models_one_of': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.delete_w9_form_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms/{id}',
                'operation_id': 'delete_w9_form',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.get_w9_form_endpoint = _Endpoint(
            settings={
                'response_type': (IW9FormDataModelsOneOf,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms/{id}',
                'operation_id': 'get_w9_form',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.list_w9_forms_endpoint = _Endpoint(
            settings={
                'response_type': (PaginatedW9FormsModel,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms',
                'operation_id': 'list_w9_forms',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'filter',
                    'top',
                    'skip',
                    'order_by',
                    'count',
                    'x_correlation_id',
                    'x_avalara_client',
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
                    'filter':
                        (str,),
                    'top':
                        (int,),
                    'skip':
                        (int,),
                    'order_by':
                        (str,),
                    'count':
                        (bool,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'filter': '$filter',
                    'top': '$top',
                    'skip': '$skip',
                    'order_by': '$orderBy',
                    'count': 'count',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
                    'count': 'query',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.send_w9_form_email_endpoint = _Endpoint(
            settings={
                'response_type': (IW9FormDataModelsOneOf,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms/{id}/$send-email',
                'operation_id': 'send_w9_form_email',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.update_w9_form_endpoint = _Endpoint(
            settings={
                'response_type': (IW9FormDataModelsOneOf,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms/{id}',
                'operation_id': 'update_w9_form',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                    'iw9_form_data_models_one_of',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'iw9_form_data_models_one_of':
                        (IW9FormDataModelsOneOf,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                    'iw9_form_data_models_one_of': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )
        self.upload_w9_files_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/w9/forms/{id}/attachment',
                'operation_id': 'upload_w9_files',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                    'file',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'avalara_version':
                        (str,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'file':
                        (bytearray,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                    'file': 'file',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                    'file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'avalara-version': '2.0',
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            required_scopes='',
            microservice='A1099'
        )

    @avalara_retry_oauth(max_retry_attempts=2)
    def create_w9_form(
        self,
        avalara_version,
        **kwargs
    ):
        """Create a W9/W4/W8 form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_w9_form(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            iw9_form_data_models_one_of (IW9FormDataModelsOneOf): Form to be created. [optional]
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
            IW9FormDataModelsOneOf
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
        return self.create_w9_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def delete_w9_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Delete a form  # noqa: E501

        Delete a form  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_w9_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Id of the form to delete
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
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
            None
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
        kwargs['id'] = id
        kwargs['avalara_version'] = avalara_version
        return self.delete_w9_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get_w9_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Retrieve a W9/W4/W8 form  # noqa: E501

        Retrieve a W9/W4/W8 form  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_w9_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Id of the form
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
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
            IW9FormDataModelsOneOf
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
        kwargs['id'] = id
        kwargs['avalara_version'] = avalara_version
        return self.get_w9_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def list_w9_forms(
        self,
        avalara_version,
        **kwargs
    ):
        """List W9/W4/W8 forms.  # noqa: E501

        List W9/W4/W8 forms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_w9_forms(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): API version

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve. For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>.. [optional]
            top (int): If nonzero, return no more than this number of results. Used with skip to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional] if omitted the server will use the default value of 10
            skip (int): If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets.. [optional] if omitted the server will use the default value of 0
            order_by (str): A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC.. [optional]
            count (bool): When true, returns a @recordSetCount in the result set. [optional]
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
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
            PaginatedW9FormsModel
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
        return self.list_w9_forms_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def send_w9_form_email(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Sends a W9 email request to a vendor/payee  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_w9_form_email(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The ID of the W9/W4/W8 form.
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
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
            IW9FormDataModelsOneOf
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
        kwargs['id'] = id
        kwargs['avalara_version'] = avalara_version
        return self.send_w9_form_email_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def update_w9_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Update a W9/W4/W8 form  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_w9_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Id of the form to update
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            iw9_form_data_models_one_of (IW9FormDataModelsOneOf): Form to be updated. [optional]
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
            IW9FormDataModelsOneOf
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
        kwargs['id'] = id
        kwargs['avalara_version'] = avalara_version
        return self.update_w9_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def upload_w9_files(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Upload files for a W9/W4/W8 form  # noqa: E501

        Upload files for a W9/W4/W8 form  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_w9_files(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Id of the form
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            file (bytearray): [optional]
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
            str
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
        kwargs['id'] = id
        kwargs['avalara_version'] = avalara_version
        return self.upload_w9_files_endpoint.call_with_http_info(**kwargs)

