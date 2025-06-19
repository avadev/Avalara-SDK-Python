# Avalara.SDK.MandatesApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mandate_data_input_fields**](MandatesApi.md#get_mandate_data_input_fields) | **GET** /mandates/{mandateId}/data-input-fields | Returns document field information for a country mandate, a selected document type, and its version
[**get_mandates**](MandatesApi.md#get_mandates) | **GET** /mandates | List country mandates that are supported by the Avalara E-Invoicing platform


# **get_mandate_data_input_fields**
> List[MandateDataInputField] get_mandate_data_input_fields(avalara_version, mandate_id, document_type, document_version)

Returns document field information for a country mandate, a selected document type, and its version

This endpoint provides document field details and the optionality of fields (required, conditional, optional) of different documents supported by the country mandate. Use the GET <code>/mandates</code> endpoint to retrieve all available country mandates, their supported document types and supported versions. You can use the `documentType` and `documentVersion` query parameters to retrieve the input fields for a particular document type and document version.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import mandates_api
BadRequest
MandateDataInputField
ForbiddenError
NotFoundError
InternalServerError
from pprint import pprint
    
# Define configuration object with parameters specified to your application.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    client_id='<Your Avalara Identity Client Id>'
    client_secret='<Your Avalara Identity Client Secret>'
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mandates_api.MandatesApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    mandate_id = 'AD-B2G-PEPPOL' # str | The unique ID for the mandate that was returned in the GET /einvoicing/mandates response body
    document_type = 'ubl-invoice' # str | Select the documentType for which you wish to view the data-input-fields (You may obtain the supported documentTypes from the GET /mandates endpoint)
    document_version = '2.1' # str | Select the document version of the documentType (You may obtain the supported documentVersion from the GET /mandates endpoint)
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a fingerprint. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns document field information for a country mandate, a selected document type, and its version
        api_response = api_instance.get_mandate_data_input_fields(avalara_version, mandate_id, document_type, document_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling MandatesApi->get_mandate_data_input_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns document field information for a country mandate, a selected document type, and its version
        api_response = api_instance.get_mandate_data_input_fields(avalara_version, mandate_id, document_type, document_version, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling MandatesApi->get_mandate_data_input_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **mandate_id** | **str**| The unique ID for the mandate that was returned in the GET /einvoicing/mandates response body |
 **document_type** | **str**| Select the documentType for which you wish to view the data-input-fields (You may obtain the supported documentTypes from the GET /mandates endpoint) |
 **document_version** | **str**| Select the document version of the documentType (You may obtain the supported documentVersion from the GET /mandates endpoint) |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a fingerprint. | [optional]

### Return type

[**List[MandateDataInputField]**](MandateDataInputField.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_mandates**
> MandatesResponse get_mandates(avalara_version)

List country mandates that are supported by the Avalara E-Invoicing platform

This endpoint offers a list of country mandates supported by the Avalara E-Invoicing API.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import mandates_api
ForbiddenError
MandatesResponse
NotFoundError
InternalServerError
from pprint import pprint
    
# Define configuration object with parameters specified to your application.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    client_id='<Your Avalara Identity Client Id>'
    client_secret='<Your Avalara Identity Client Secret>'
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mandates_api.MandatesApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a fingerprint. (optional)
    filter = 'countryMandate eq DE-B2G-PEPPOL' # str | Filter by field name and value. This filter only supports <code>eq</code> and <code>contains</code>. Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. (optional)
    top = 10 # decimal.Decimal | If nonzero, return no more than this number of results. Used with <code>$skip</code> to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 10 # decimal.Decimal | If nonzero, skip this number of results before returning data. Used with <code>$top</code> to provide pagination for large datasets. (optional)
    count = true # bool | When set to true, the count of the collection is also returned in the response body. (optional)
    count_only = true # bool | When set to true, only the count of the collection is returned (optional)
    # example passing only required values which don't have defaults set
    try:
        # List country mandates that are supported by the Avalara E-Invoicing platform
        api_response = api_instance.get_mandates(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling MandatesApi->get_mandates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List country mandates that are supported by the Avalara E-Invoicing platform
        api_response = api_instance.get_mandates(avalara_version, x_avalara_client=x_avalara_client, filter=filter, top=top, skip=skip, count=count, count_only=count_only)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling MandatesApi->get_mandates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a fingerprint. | [optional]
 **filter** | **str**| Filter by field name and value. This filter only supports &lt;code&gt;eq&lt;/code&gt; and &lt;code&gt;contains&lt;/code&gt;. Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. | [optional]
 **top** | **decimal.Decimal**| If nonzero, return no more than this number of results. Used with &lt;code&gt;$skip&lt;/code&gt; to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **decimal.Decimal**| If nonzero, skip this number of results before returning data. Used with &lt;code&gt;$top&lt;/code&gt; to provide pagination for large datasets. | [optional]
 **count** | **bool**| When set to true, the count of the collection is also returned in the response body. | [optional]
 **count_only** | **bool**| When set to true, only the count of the collection is returned | [optional]

### Return type

[**MandatesResponse**](MandatesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

