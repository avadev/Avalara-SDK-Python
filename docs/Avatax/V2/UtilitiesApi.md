# Avalara.SDK.UtilitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_my_subscriptions**](UtilitiesApi.md#list_my_subscriptions) | **GET** /avatax/utilities/subscriptions | List all services to which the current user is subscribed
[**ping**](UtilitiesApi.md#ping) | **GET** /avatax/utilities/ping | Tests connectivity and version of the service


# **list_my_subscriptions**
> SubscriptionModelFetchResult list_my_subscriptions()

List all services to which the current user is subscribed

Returns the list of all subscriptions enabled for the currently logged in user.                This API will return an error if it is called with invalid authentication credentials.                This API is intended to help you determine whether you have the necessary subscription to use certain API calls  within AvaTax.  You can examine the subscriptions returned from this API call to look for a particular product  or subscription to provide useful information to the current user as to whether they are entitled to use  specific features of AvaTax.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import utilities_api
from Avalara.SDK.model.subscription_model_fetch_result import SubscriptionModelFetchResult
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
    api_instance = utilities_api.UtilitiesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all services to which the current user is subscribed
        api_response = api_instance.list_my_subscriptions(x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling UtilitiesApi->list_my_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**SubscriptionModelFetchResult**](SubscriptionModelFetchResult.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **ping**
> PingResultModel ping()

Tests connectivity and version of the service

Check connectivity to AvaTax and return information about the AvaTax API server.                This API is intended to help you verify that your connection is working.  This API will always succeed and will  never return a error.  It provides basic information about the server you connect to:                * `version` - The version number of the AvaTax API server that responded to your request.  The AvaTax API version number is updated once per month during Avalara's update process.  * `authenticated` - A boolean flag indicating whether or not you sent valid credentials with your API request.  * `authenticationType` - If you provided valid credentials to the API, this field will tell you whether you used Bearer, Username, or LicenseKey authentication.  * `authenticatedUserName` - If you provided valid credentials to the API, this field will tell you the username of the currently logged in user.  * `authenticatedUserId` - If you provided valid credentials to the API, this field will tell you the user ID of the currently logged in user.  * `authenticatedAccountId` - If you provided valid credentials to the API, this field will contain the account ID of the currently logged in user.                This API helps diagnose connectivity problems between your application and AvaTax; you may call this API even  if you do not have verified connection credentials.  If this API fails, either your computer is not connected to  the internet, or there is a routing problem between your office and Avalara, or the Avalara server is not available.  For more information on the uptime of AvaTax, please see [Avalara's AvaTax Status Page](https://status.avalara.com/).  ### Security Policies  * This API may be called without providing authentication credentials. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import utilities_api
from Avalara.SDK.model.ping_result_model import PingResultModel
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
    api_instance = utilities_api.UtilitiesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Tests connectivity and version of the service
        api_response = api_instance.ping(x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling UtilitiesApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**PingResultModel**](PingResultModel.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

