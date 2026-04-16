# Avalara.SDK.DataInputFieldsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_input_fields**](DataInputFieldsApi.md#get_data_input_fields) | **GET** /data-input-fields | Returns the optionality of document fields for different country mandates


# **get_data_input_fields**
> DataInputFieldsResponse get_data_input_fields(avalara_version)

Returns the optionality of document fields for different country mandates

This endpoint returns a list of required, conditional, and optional fields for each country mandate. Use the mandates endpoint to retrieve all available country mandates. Use the $filter query parameter to retrieve fields for a specific mandate.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import data_input_fields_api
DataInputFieldsResponse
ForbiddenError
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
    api_instance = data_input_fields_api.DataInputFieldsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    filter = 'requiredFor/countryMandate eq AU-B2G-PEPPOL' # str | Filter by field name and value. This filter supports only eq and contains. For more information, refer to the Avalara filtering guide. (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    count = true # bool | When set to true, the response body also includes the count of items in the collection. (optional)
    count_only = true # bool | When set to true, the response returns only the count of items in the collection. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns the optionality of document fields for different country mandates
        api_response = api_instance.get_data_input_fields(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DataInputFieldsApi->get_data_input_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the optionality of document fields for different country mandates
        api_response = api_instance.get_data_input_fields(avalara_version, x_avalara_client=x_avalara_client, filter=filter, top=top, skip=skip, count=count, count_only=count_only)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DataInputFieldsApi->get_data_input_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **filter** | **str**| Filter by field name and value. This filter supports only eq and contains. For more information, refer to the Avalara filtering guide. | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]
 **count** | **bool**| When set to true, the response body also includes the count of items in the collection. | [optional]
 **count_only** | **bool**| When set to true, the response returns only the count of items in the collection. | [optional]

### Return type

[**DataInputFieldsResponse**](DataInputFieldsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a DataInputFieldsResponse object containing the data input fields and their optionality for the requested mandate. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

