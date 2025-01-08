# Avalara.SDK.DefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_entity_use_codes**](DefinitionsApi.md#list_entity_use_codes) | **GET** /avatax/definitions/entityusecodes | Retrieve the full list of Avalara-supported entity use codes
[**list_nexus**](DefinitionsApi.md#list_nexus) | **GET** /avatax/definitions/nexus | Retrieve the full list of Avalara-supported nexus for all countries and regions.


# **list_entity_use_codes**
> EntityUseCodeModelFetchResult list_entity_use_codes()

Retrieve the full list of Avalara-supported entity use codes

Returns the full list of Avalara-supported entity use codes.  Entity/Use Codes are definitions of the entity who is purchasing something, or the purpose for which the transaction  is occurring.  This information is generally used to determine taxability of the product.  In order to facilitate correct reporting of your taxes, you are encouraged to select the proper entity use codes for  all transactions that are exempt.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import definitions_api
from Avalara.SDK.model.entity_use_code_model_fetch_result import EntityUseCodeModelFetchResult
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
    api_instance = definitions_api.DefinitionsApi(api_client)
    filter = "$filter_example" # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* validCountries (optional)
    top = 1 # int | If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 1 # int | If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets. (optional)
    order_by = "$orderBy_example" # str | A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the full list of Avalara-supported entity use codes
        api_response = api_instance.list_entity_use_codes(filter=filter, top=top, skip=skip, order_by=order_by, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DefinitionsApi->list_entity_use_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).&lt;br /&gt;*Not filterable:* validCountries | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.  Used with &#x60;$skip&#x60; to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data.  Used with &#x60;$top&#x60; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format &#x60;(fieldname) [ASC|DESC]&#x60;, for example &#x60;id ASC&#x60;. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**EntityUseCodeModelFetchResult**](EntityUseCodeModelFetchResult.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_nexus**
> NexusModelFetchResult list_nexus()

Retrieve the full list of Avalara-supported nexus for all countries and regions.

Returns the full list of all Avalara-supported nexus for all countries and regions.                This API is intended to be useful if your user interface needs to display a selectable list of nexus.

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import definitions_api
from Avalara.SDK.model.nexus_model_fetch_result import NexusModelFetchResult
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
    api_instance = definitions_api.DefinitionsApi(api_client)
    filter = "$filter_example" # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxTypeGroup, taxAuthorityId, taxName, parameters, taxableNexus (optional)
    top = 1 # int | If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 1 # int | If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets. (optional)
    order_by = "$orderBy_example" # str | A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the full list of Avalara-supported nexus for all countries and regions.
        api_response = api_instance.list_nexus(filter=filter, top=top, skip=skip, order_by=order_by, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DefinitionsApi->list_nexus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).&lt;br /&gt;*Not filterable:* streamlinedSalesTax, isSSTActive, taxTypeGroup, taxAuthorityId, taxName, parameters, taxableNexus | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.  Used with &#x60;$skip&#x60; to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data.  Used with &#x60;$top&#x60; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format &#x60;(fieldname) [ASC|DESC]&#x60;, for example &#x60;id ASC&#x60;. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**NexusModelFetchResult**](NexusModelFetchResult.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

