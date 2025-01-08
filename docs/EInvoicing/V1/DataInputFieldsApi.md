# Avalara.SDK.DataInputFieldsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_input_fields**](DataInputFieldsApi.md#get_data_input_fields) | **GET** /data-input-fields | Returns the mandatory and conditional invoice or creditnote input fields for different country mandates


# **get_data_input_fields**
> DataInputFieldsResponse get_data_input_fields(avalara_version)

Returns the mandatory and conditional invoice or creditnote input fields for different country mandates

This endpoint provides a list of required, conditional, and optional fields for each country mandate. You can use the <code>mandates</code> endpoint to retrieve all available country mandates. You can use the $filter query parameter to retrieve fields for a particular mandate

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import data_input_fields_api
from Avalara.SDK.model.forbidden_error import ForbiddenError
from Avalara.SDK.model.data_input_fields_response import DataInputFieldsResponse
from Avalara.SDK.model.internal_server_error import InternalServerError
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
    avalara_version = "1.0" # str | The HTTP Header meant to specify the version of the API intended to be used
    x_avalara_client = "John's E-Invoicing-API Client" # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    filter = "requiredFor/countryMandate eq AU-B2G-PEPPOL" # str | Filter by field name and value. This filter only supports <code>eq</code> and <code>contains</code>. Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. (optional)
    top = 10 # float | If nonzero, return no more than this number of results. Used with <code>$skip</code> to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 10 # float | If nonzero, skip this number of results before returning data. Used with <code>$top</code> to provide pagination for large datasets. (optional)
    count = "true" # bool | When set to true, the count of the collection is also returned in the response body (optional)
    count_only = "true" # bool | When set to true, only the count of the collection is returned (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns the mandatory and conditional invoice or creditnote input fields for different country mandates
        api_response = api_instance.get_data_input_fields(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DataInputFieldsApi->get_data_input_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the mandatory and conditional invoice or creditnote input fields for different country mandates
        api_response = api_instance.get_data_input_fields(avalara_version, x_avalara_client=x_avalara_client, filter=filter, top=top, skip=skip, count=count, count_only=count_only)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DataInputFieldsApi->get_data_input_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **filter** | **str**| Filter by field name and value. This filter only supports &lt;code&gt;eq&lt;/code&gt; and &lt;code&gt;contains&lt;/code&gt;. Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. | [optional]
 **top** | **float**| If nonzero, return no more than this number of results. Used with &lt;code&gt;$skip&lt;/code&gt; to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **float**| If nonzero, skip this number of results before returning data. Used with &lt;code&gt;$top&lt;/code&gt; to provide pagination for large datasets. | [optional]
 **count** | **bool**| When set to true, the count of the collection is also returned in the response body | [optional]
 **count_only** | **bool**| When set to true, only the count of the collection is returned | [optional]

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

