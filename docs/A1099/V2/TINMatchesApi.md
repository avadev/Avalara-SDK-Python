# Avalara.SDK.TINMatchesApi

All URIs are relative to *https://api-ava1099.edge.qa.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perform_real_time_tin_match**](TINMatchesApi.md#perform_real_time_tin_match) | **POST** /tin-matches/$real-time | Perform real time TIN Match


# **perform_real_time_tin_match**
> RealTimeTinMatchResponse perform_real_time_tin_match(avalara_version)

Perform real time TIN Match

Perform real time TIN Match.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import tin_matches_api
RealTimeTinMatchRequest
RealTimeTinMatchResponse
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
    api_instance = tin_matches_api.TINMatchesApi(api_client)
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '86993e01-0897-4667-b8f3-bac8c0081c4c' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    real_time_tin_match_request = {"tinType":"BUSINESS","tin":"94-2765439","name":"Acme Corporation"} # RealTimeTinMatchRequest | Required data to perform TIN match (optional)
    # example passing only required values which don't have defaults set
    try:
        # Perform real time TIN Match
        api_response = api_instance.perform_real_time_tin_match(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->perform_real_time_tin_match: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Perform real time TIN Match
        api_response = api_instance.perform_real_time_tin_match(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, real_time_tin_match_request=real_time_tin_match_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->perform_real_time_tin_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **real_time_tin_match_request** | [**RealTimeTinMatchRequest**](RealTimeTinMatchRequest.md)| Required data to perform TIN match | [optional]

### Return type

[**RealTimeTinMatchResponse**](RealTimeTinMatchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TIN match result (matched or rejected) |  -  |
**400** | Bad request (e.g. invalid field values) |  -  |
**401** | Authentication failed |  -  |
**429** | Usage limit exceeded (10,000 successful calls per 24 hours) |  -  |
**403** | Authorization failed (lack of permissions or product not purchased) |  -  |
**503** | IRS Service is not available. Client should retry later. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

