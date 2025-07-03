# Avalara.SDK.Jobs1099Api

All URIs are relative to *https://api-ava1099.eta.sbx.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](Jobs1099Api.md#get_job) | **GET** /1099/jobs/{id} | Retrieves information about the job


# **get_job**
> JobResult get_job(id, avalara_version)

Retrieves information about the job

Retrieves information about the job

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import jobs1099_api
JobResult
ErrorResponse
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
    api_instance = jobs1099_api.Jobs1099Api(api_client)
    id = 'id_example' # str | Job id obtained from other API responses, like `/1099/bulk-upsert`.
    avalara_version = '2.0' # str | API version
    x_correlation_id = '479c98ac-f5b2-438f-9e24-c8999d2d332e' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieves information about the job
        api_response = api_instance.get_job(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Jobs1099Api->get_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves information about the job
        api_response = api_instance.get_job(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Jobs1099Api->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job id obtained from other API responses, like &#x60;/1099/bulk-upsert&#x60;. |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**JobResult**](JobResult.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

