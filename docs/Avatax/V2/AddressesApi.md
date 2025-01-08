# Avalara.SDK.AddressesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_address_post**](AddressesApi.md#resolve_address_post) | **POST** /avatax/addresses/resolve | Retrieve geolocation information for a specified address


# **resolve_address_post**
> AddressResolutionModel resolve_address_post()

Retrieve geolocation information for a specified address

Resolve an address against Avalara's address-validation system.  If the address can be resolved, this API  provides the latitude and longitude of the resolved location.  The value 'resolutionQuality' can be used  to identify how closely this address can be located.  If the address cannot be clearly located, use the  'messages' structure to learn more about problems with this address.  This is the same API as the GET /avatax/addresses/resolve endpoint.  Both verbs are supported to provide for flexible implementation.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AutoAddress. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import addresses_api
from Avalara.SDK.model.address_validation_info import AddressValidationInfo
from Avalara.SDK.model.address_resolution_model import AddressResolutionModel
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
    api_instance = addresses_api.AddressesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = AddressValidationInfo(
        line1="2000 Main Street",
        text_case="Upper",
        line2="line2_example",
        line3="line3_example",
        city="Irvine",
        region="CA",
        country="US",
        postal_code="92614",
        latitude=3.14,
        longitude=3.14,
    ) # AddressValidationInfo | The address to resolve (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve geolocation information for a specified address
        api_response = api_instance.resolve_address_post(x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AddressesApi->resolve_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**AddressValidationInfo**](AddressValidationInfo.md)| The address to resolve | [optional]

### Return type

[**AddressResolutionModel**](AddressResolutionModel.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

