# Avalara.SDK.TINMatchesApi

All URIs are relative to *https://api.sbx.avalara.com/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bulk_tin_match**](TINMatchesApi.md#get_bulk_tin_match) | **GET** /tin-matches/$bulk/{id} | Get bulk TIN match details
[**get_bulk_tin_match_results**](TINMatchesApi.md#get_bulk_tin_match_results) | **GET** /tin-matches/$bulk/{id}/results | List bulk TIN match results
[**perform_real_time_tin_match**](TINMatchesApi.md#perform_real_time_tin_match) | **POST** /tin-matches/$real-time | Perform real time TIN Match
[**submit_bulk_tin_match**](TINMatchesApi.md#submit_bulk_tin_match) | **POST** /tin-matches/$bulk | Submit bulk TIN match


# **get_bulk_tin_match**
> BulkTinMatchResponse get_bulk_tin_match(id, avalara_version)

Get bulk TIN match details

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import tin_matches_api
BulkTinMatchResponse
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
    id = 'id_example' # str | The bulk ID
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'df30781a-da37-45b3-be01-d835e5d0ad8b' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Get bulk TIN match details
        api_response = api_instance.get_bulk_tin_match(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->get_bulk_tin_match: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get bulk TIN match details
        api_response = api_instance.get_bulk_tin_match(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->get_bulk_tin_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The bulk ID |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**BulkTinMatchResponse**](BulkTinMatchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulk TIN match details |  -  |
**401** | Authentication failed |  -  |
**404** | Bulk not found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bulk_tin_match_results**
> PaginatedQueryResultModelBulkTinMatchResultItemResponse get_bulk_tin_match_results(id, avalara_version)

List bulk TIN match results

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import tin_matches_api
PaginatedQueryResultModelBulkTinMatchResultItemResponse
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
    id = 'id_example' # str | The bulk ID
    avalara_version = '2.0.0' # str | API version
    filter = 'filter_example' # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 56 # int | If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. (optional)
    skip = 56 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional)
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | If true, return the global count of elements in the collection. (optional)
    count_only = True # bool | If true, return ONLY the global count of elements in the collection.  It only applies when count=true. (optional)
    x_correlation_id = '98367ed4-44bb-4254-a388-ec2e63ac293e' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # List bulk TIN match results
        api_response = api_instance.get_bulk_tin_match_results(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->get_bulk_tin_match_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List bulk TIN match results
        api_response = api_instance.get_bulk_tin_match_results(id, avalara_version, filter=filter, top=top, skip=skip, order_by=order_by, count=count, count_only=count_only, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->get_bulk_tin_match_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The bulk ID |
 **avalara_version** | **str**| API version |
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see &lt;a href&#x3D;\&quot;https://developer.avalara.com/avatax/filtering-in-rest/\&quot;&gt;Filtering in REST&lt;/a&gt;. | [optional]
 **top** | **int**| If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. | [optional]
 **count** | **bool**| If true, return the global count of elements in the collection. | [optional]
 **count_only** | **bool**| If true, return ONLY the global count of elements in the collection.  It only applies when count&#x3D;true. | [optional]
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**PaginatedQueryResultModelBulkTinMatchResultItemResponse**](PaginatedQueryResultModelBulkTinMatchResultItemResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TIN match responses |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |
**404** | Bulk not found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

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
    x_correlation_id = '7d625954-787a-4153-8365-45cef8288be1' # str | Unique correlation Id in a GUID format (optional)
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

# **submit_bulk_tin_match**
> BulkTinMatchAcceptedResponse submit_bulk_tin_match(avalara_version)

Submit bulk TIN match

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import tin_matches_api
BulkTinMatchRequest
BulkTinMatchAcceptedResponse
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
    x_correlation_id = '3f051c64-117a-46f1-b9b5-324064394c6a' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    bulk_tin_match_request = {"items":[{"referenceId":"ACME0001","tinType":"BUSINESS","tin":"94-2765439","name":"Acme Corporation"},{"referenceId":"123JD","tinType":"INDIVIDUAL","tin":"543-45-6789","name":"John Doe"}]} # BulkTinMatchRequest | Required TIN collection to perform bulk TIN match (optional)
    # example passing only required values which don't have defaults set
    try:
        # Submit bulk TIN match
        api_response = api_instance.submit_bulk_tin_match(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->submit_bulk_tin_match: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit bulk TIN match
        api_response = api_instance.submit_bulk_tin_match(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, bulk_tin_match_request=bulk_tin_match_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TINMatchesApi->submit_bulk_tin_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **bulk_tin_match_request** | [**BulkTinMatchRequest**](BulkTinMatchRequest.md)| Required TIN collection to perform bulk TIN match | [optional]

### Return type

[**BulkTinMatchAcceptedResponse**](BulkTinMatchAcceptedResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted submission, indicating it will be processed later and where to get results from |  -  |
**400** | Bad request (e.g. invalid field values) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

