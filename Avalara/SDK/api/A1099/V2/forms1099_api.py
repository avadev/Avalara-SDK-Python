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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from Avalara.SDK.models.A1099.V2.bulk_upsert1099_forms_request import BulkUpsert1099FormsRequest
from Avalara.SDK.models.A1099.V2.form1099_list import Form1099List
from Avalara.SDK.models.A1099.V2.form1099_proccess_result import Form1099ProccessResult
from Avalara.SDK.models.A1099.V2.get1099_form200_response import Get1099Form200Response
from Avalara.SDK.models.A1099.V2.i_create_form1099_request import ICreateForm1099Request
from Avalara.SDK.models.A1099.V2.i_update_form1099_request import IUpdateForm1099Request
from Avalara.SDK.models.A1099.V2.update1099_form200_response import Update1099Form200Response
from Avalara.SDK.exceptions import ApiTypeError, ApiValueError, ApiException
from Avalara.SDK.oauth_helper.AvalaraSdkOauthUtils import avalara_retry_oauth

class Forms1099Api(object):

    def __init__(self, api_client):
        self.__set_configuration(api_client)
    
    def __verify_api_client(self,api_client):
        if api_client is None:
            raise ApiValueError("APIClient not defined")
    
    def __set_configuration(self, api_client):
        self.__verify_api_client(api_client)
        api_client.set_sdk_version("25.7.2")
        self.api_client = api_client
		
        self.bulk_upsert1099_forms_endpoint = _Endpoint(
            settings={
                'response_type': (Form1099ProccessResult,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms/$bulk-upsert',
                'operation_id': 'bulk_upsert1099_forms',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'dry_run',
                    'x_correlation_id',
                    'x_avalara_client',
                    'bulk_upsert1099_forms_request',
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
                    'dry_run':
                        (bool,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                    'bulk_upsert1099_forms_request':
                        (BulkUpsert1099FormsRequest,),
                },
                'attribute_map': {
                    'avalara_version': 'avalara-version',
                    'dry_run': 'dryRun',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'dry_run': 'query',
                    'x_correlation_id': 'header',
                    'x_avalara_client': 'header',
                    'bulk_upsert1099_forms_request': 'body',
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
        self.create1099_form_endpoint = _Endpoint(
            settings={
                'response_type': (Get1099Form200Response,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms',
                'operation_id': 'create1099_form',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                    'i_create_form1099_request',
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
                    'i_create_form1099_request':
                        (ICreateForm1099Request,),
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
                    'i_create_form1099_request': 'body',
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
        self.delete1099_form_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms/{id}',
                'operation_id': 'delete1099_form',
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
        self.get1099_form_endpoint = _Endpoint(
            settings={
                'response_type': (Get1099Form200Response,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms/{id}',
                'operation_id': 'get1099_form',
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
        self.get1099_form_pdf_endpoint = _Endpoint(
            settings={
                'response_type': (Update1099Form200Response,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms/{id}/pdf',
                'operation_id': 'get1099_form_pdf',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'mark_edelivered',
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
                    'mark_edelivered':
                        (bool,),
                    'x_correlation_id':
                        (str,),
                    'x_avalara_client':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'avalara_version': 'avalara-version',
                    'mark_edelivered': 'markEdelivered',
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'id': 'path',
                    'avalara_version': 'header',
                    'mark_edelivered': 'query',
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
        self.list1099_forms_endpoint = _Endpoint(
            settings={
                'response_type': (Form1099List,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms',
                'operation_id': 'list1099_forms',
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
                    'x_correlation_id': 'X-Correlation-Id',
                    'x_avalara_client': 'X-Avalara-Client',
                },
                'location_map': {
                    'avalara_version': 'header',
                    'filter': 'query',
                    'top': 'query',
                    'skip': 'query',
                    'order_by': 'query',
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
        self.update1099_form_endpoint = _Endpoint(
            settings={
                'response_type': (Update1099Form200Response,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/1099/forms/{id}',
                'operation_id': 'update1099_form',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'avalara_version',
                    'x_correlation_id',
                    'x_avalara_client',
                    'i_update_form1099_request',
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
                    'i_update_form1099_request':
                        (IUpdateForm1099Request,),
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
                    'i_update_form1099_request': 'body',
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

    @avalara_retry_oauth(max_retry_attempts=2)
    def bulk_upsert1099_forms(
        self,
        avalara_version,
        **kwargs
    ):
        """Creates or updates multiple 1099 forms.  # noqa: E501

        This endpoint allows you to create or update multiple 1099 forms.  You can use one of the following payload structures:                **Form 1099-MISC:**  ```json  {     \"formType\": \"1099-MISC\",     \"forms\": [         {             \"IssuerId\": \"123456\",             \"IssuerReferenceId\": \"REF123\",             \"IssuerTin\": \"12-3456789\",             \"TaxYear\": 2023,             \"ReferenceId\": \"FORM123456\",             \"RecipientName\": \"John Doe\",             \"RecipientTin\": \"987-65-4321\",             \"TinType\": \"IEN\",             \"RecipientSecondName\": \"Jane Doe\",             \"Address\": \"123 Main Street\",             \"Address2\": \"Apt 4B\",             \"City\": \"New York\",             \"State\": \"NY\",             \"Zip\": \"10001\",             \"RecipientEmail\": \"john.doe@email.com\",             \"AccountNumber\": \"ACC123456\",             \"OfficeCode\": \"NYC01\",             \"SecondTinNotice\": false,             \"RecipientNonUsProvince\": \"\",             \"CountryCode\": \"US\",             \"Rents\": 12000.00,             \"Royalties\": 5000.00,             \"OtherIncome\": 3000.00,             \"FishingBoatProceeds\": 0.00,             \"MedicalHealthCarePayments\": 15000.00,             \"SubstitutePayments\": 1000.00,             \"CropInsuranceProceeds\": 0.00,             \"GrossProceedsPaidToAttorney\": 7500.00,             \"FishPurchasedForResale\": 0.00,             \"FedIncomeTaxWithheld\": 5000.00,             \"Section409ADeferrals\": 0.00,             \"ExcessGoldenParachutePayments\": 0.00,             \"NonqualifiedDeferredCompensation\": 0.00,             \"PayerMadeDirectSales\": false,             \"FatcaFilingRequirement\": false,             \"StateAndLocalWithholding\": {               \"StateTaxWithheld\": 2500.00,               \"LocalTaxWithheld\": 1000.00,               \"State\": \"NY\",               \"StateIdNumber\": \"NY123456\",               \"Locality\": \"New York City\",               \"StateIncome\": 35000.00,               \"LocalIncome\": 35000.00             }         }     ]  }  ```                **Form 1099-NEC:**  ```json  {    \"formType\": \"1099-NEC\",    \"forms\": [      {        \"issuerID\": \"180337282\",        \"issuerReferenceId\": \"ISS123\",        \"issuerTin\": \"12-3000000\",        \"taxYear\": 2024,        \"referenceID\": \"REF-002\",        \"recipientName\": \"Jane Smith\",        \"recipientSecondName\": \"\",        \"recipientTin\": \"987-65-4321\",        \"tinType\": \"IEN\",        \"address\": \"123 Center St\",        \"address2\": \"\",        \"city\": \"Santa Monica\",        \"state\": \"CA\",        \"zip\": \"90401\",        \"countryCode\": \"US\",        \"recipientNonUsProvince\": \"\",        \"recipientEmail\": \"\",        \"accountNumber\": \"\",        \"officeCode\": \"\",        \"secondTinNotice\": false,        \"nonemployeeCompensation\": 123.45,        \"payerMadeDirectSales\": false,        \"federalIncomeTaxWithheld\": 12.34,        \"stateAndLocalWithholding\": {          \"state\": \"CA\",          \"stateIdNumber\": \"123123123\"          \"stateIncome\": 123.45,          \"stateTaxWithheld\": 12.34,          \"locality\": \"Santa Monica\",          \"localityIdNumber\": \"456456\",          \"localTaxWithheld\": 12.34          \"localIncome\": 50000.00         },        \"federalEFile\": true,        \"postalMail\": true,        \"stateEFile\": true,        \"tinMatch\": true,        \"addressVerification\": true       }     ]   }  ```  For the full version of the payload and its schema details, refer to the Swagger schemas section.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_upsert1099_forms(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): API version

        Keyword Args:
            dry_run (bool): . [optional] if omitted the server will use the default value of False
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            bulk_upsert1099_forms_request (BulkUpsert1099FormsRequest): . [optional]
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
            Form1099ProccessResult
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
        return self.bulk_upsert1099_forms_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def create1099_form(
        self,
        avalara_version,
        **kwargs
    ):
        """Creates a 1099 form.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create1099_form(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            i_create_form1099_request (ICreateForm1099Request): [optional]
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
            Get1099Form200Response
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
        return self.create1099_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def delete1099_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Deletes a 1099 form.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete1099_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): The unique identifier of the desired form to delete.
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
        return self.delete1099_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get1099_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Retrieves a 1099 form.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get1099_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
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
            Get1099Form200Response
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
        return self.get1099_form_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def get1099_form_pdf(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Retrieves the PDF file for a single 1099 by form id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get1099_form_pdf(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): 
            avalara_version (str): API version

        Keyword Args:
            mark_edelivered (bool): The parameter for marked e-delivered. [optional]
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
            Update1099Form200Response
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
        return self.get1099_form_pdf_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def list1099_forms(
        self,
        avalara_version,
        **kwargs
    ):
        """Retrieves a list of 1099 forms based on query parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list1099_forms(avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            avalara_version (str): API version

        Keyword Args:
            filter (str): A filter statement to identify specific records to retrieve. For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>.    Collections support filtering only on certain fields. An attempt to filter on an unsupported field will receive a 400 Bad Request response.    Supported filtering fields are as follows:        issuerId      issuerReferenceId      taxYear      addressVerificationStatus - possible values are: unknown, pending, failed, incomplete, unchanged, verified      createdAt      edeliveryStatus - possible values are: sent, unscheduled, bad_verify, bad_verify_limit, scheduled, bounced, accepted      email      federalEfileStatus - possible values are: unscheduled, scheduled, sent, corrected_scheduled, accepted, corrected, corrected_accepted, held      recipientName      mailStatus - possible values are: sent, unscheduled, pending, delivered      referenceId      tinMatchStatus - possible values are: none, pending, matched, failed      type - possible values are: 940, 941, 943, 944, 945, 1042, 1042-S, 1095-B, 1095-C, 1097-BTC, 1098, 1098-C, 1098-E, 1098-Q, 1098-T, 3921, 3922, 5498, 5498-ESA, 5498-SA, 1099-MISC, 1099-A, 1099-B, 1099-C, 1099-CAP, 1099-DIV, 1099-G, 1099-INT, 1099-K, 1099-LS, 1099-LTC, 1099-NEC, 1099-OID, 1099-PATR, 1099-Q, 1099-R, 1099-S, 1099-SA, T4A, W-2, W-2G, 1099-HC      updatedAt      validity - possible values are: true, false. [optional]
            top (int): If nonzero, return no more than this number of results.     Used with skip to provide pagination for large datasets.     Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.. [optional] if omitted the server will use the default value of 10
            skip (int): If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets.. [optional] if omitted the server will use the default value of 0
            order_by (str): A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example issuerReferenceId ASC.    Supported sorting fields are:         issuerReferenceId       taxYear       createdAt       recipientName      updatedAt. [optional]
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
            Form1099List
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
        return self.list1099_forms_endpoint.call_with_http_info(**kwargs)

    @avalara_retry_oauth(max_retry_attempts=2)
    def update1099_form(
        self,
        id,
        avalara_version,
        **kwargs
    ):
        """Updates a 1099 form.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update1099_form(id, avalara_version, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):
            avalara_version (str): API version

        Keyword Args:
            x_correlation_id (str): Unique correlation Id in a GUID format. [optional]
            x_avalara_client (str): Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) .. [optional]
            i_update_form1099_request (IUpdateForm1099Request): [optional]
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
            Update1099Form200Response
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
        return self.update1099_form_endpoint.call_with_http_info(**kwargs)

