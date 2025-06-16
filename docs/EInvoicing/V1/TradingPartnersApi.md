# Avalara.SDK.TradingPartnersApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_search_participants**](TradingPartnersApi.md#batch_search_participants) | **POST** /trading-partners/batch-searches | Creates a batch search and performs a batch search in the directory for participants in the background.
[**download_batch_search_report**](TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Download batch search results in a csv file.
[**get_batch_search_detail**](TradingPartnersApi.md#get_batch_search_detail) | **GET** /trading-partners/batch-searches/{id} | Get the batch search details for a given id.
[**list_batch_searches**](TradingPartnersApi.md#list_batch_searches) | **GET** /trading-partners/batch-searches | List all batch searches that were previously submitted.
[**search_participants**](TradingPartnersApi.md#search_participants) | **GET** /trading-partners | Returns a list of participants matching the input query.


# **batch_search_participants**
> BatchSearchParticipants202Response batch_search_participants(avalara_version, name, notification_email, file)

Creates a batch search and performs a batch search in the directory for participants in the background.

Handles batch search requests by uploading a file containing search parameters.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
BatchSearchParticipants202Response
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
    api_instance = trading_partners_api.TradingPartnersApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    name = 'Automotive Companies in London Search' # str | The human readable name given to this batch search.
    notification_email = 'user@example.com' # str | The email address of the user to whom the batch search completion notification must go to.
    file = None # bytearray | CSV file containing search parameters.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates a batch search and performs a batch search in the directory for participants in the background.
        api_response = api_instance.batch_search_participants(avalara_version, name, notification_email, file)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->batch_search_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a batch search and performs a batch search in the directory for participants in the background.
        api_response = api_instance.batch_search_participants(avalara_version, name, notification_email, file, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->batch_search_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **name** | **str**| The human readable name given to this batch search. |
 **notification_email** | **str**| The email address of the user to whom the batch search completion notification must go to. |
 **file** | [**bytearray**](bytearray.md)| CSV file containing search parameters. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**BatchSearchParticipants202Response**](BatchSearchParticipants202Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch search file accepted for processing the search. |  * X-Correlation-Id -  <br>  |
**400** | Invalid request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_batch_search_report**
> bytearray download_batch_search_report(avalara_version, id)

Download batch search results in a csv file.

Downloads the report for a specific batch search using the batch search ID.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
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
    api_instance = trading_partners_api.TradingPartnersApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    id = '2f5ea4b5-4dae-445a-b3e4-9f65a61eaa99' # str | The ID of the batch search whose report is to be downloaded.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Download batch search results in a csv file.
        api_response = api_instance.download_batch_search_report(avalara_version, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->download_batch_search_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download batch search results in a csv file.
        api_response = api_instance.download_batch_search_report(avalara_version, id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->download_batch_search_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **id** | **str**| The ID of the batch search whose report is to be downloaded. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful report download |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**404** | Report not found |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_batch_search_detail**
> BatchSearch get_batch_search_detail(avalara_version, id)

Get the batch search details for a given id.

This endpoint provides a detailed information for a specific batch search based on a given ID. It is ideal for tracking the progress of a previously initiated batch search operation.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
BatchSearch
BatchSearchListResponse
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
    api_instance = trading_partners_api.TradingPartnersApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    id = '2f5ea4b5-4dae-445a-b3e4-9f65a61eaa99' # str | The ID of the batch search that was submitted earlier.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Get the batch search details for a given id.
        api_response = api_instance.get_batch_search_detail(avalara_version, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->get_batch_search_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the batch search details for a given id.
        api_response = api_instance.get_batch_search_detail(avalara_version, id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->get_batch_search_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **id** | **str**| The ID of the batch search that was submitted earlier. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**BatchSearch**](BatchSearch.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the batch search details for a given id. |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**404** | Report not found |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_batch_searches**
> BatchSearchListResponse list_batch_searches(avalara_version)

List all batch searches that were previously submitted.

This endpoint provides a way to retrieve a comprehensive list of all batch search operations that have been previously submitted. This endpoint returns details about each batch search, such as their id, status, created date and associated metadata, allowing users to easily view past batch search requests. It's particularly useful for tracking the progress of a previously initiated batch search operations.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
BatchSearchListResponse
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
    api_instance = trading_partners_api.TradingPartnersApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    filter = 'name eq 'Batch_Search_Import_V4'' # str | Filter by field name and value. This filter only supports <code>eq</code> .The parameters supported is <code>name</code>.    Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided parameters. (optional)
    count = true # bool | When set to true, the count of the collection is included as @recordSetCount in the response body. (optional)
    top = '10' # str | If nonzero, return no more than this number of results. Used with <code>$skip</code> to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. (optional)
    skip = '10' # str | If nonzero, skip this number of results before returning data. Used with <code>$top</code> to provide pagination for large datasets. (optional)
    order_by = 'name desc' # str | The $orderBy query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # List all batch searches that were previously submitted.
        api_response = api_instance.list_batch_searches(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->list_batch_searches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all batch searches that were previously submitted.
        api_response = api_instance.list_batch_searches(avalara_version, x_avalara_client=x_avalara_client, filter=filter, count=count, top=top, skip=skip, order_by=order_by, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->list_batch_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **filter** | **str**| Filter by field name and value. This filter only supports &lt;code&gt;eq&lt;/code&gt; .The parameters supported is &lt;code&gt;name&lt;/code&gt;.    Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided parameters. | [optional]
 **count** | **bool**| When set to true, the count of the collection is included as @recordSetCount in the response body. | [optional]
 **top** | **str**| If nonzero, return no more than this number of results. Used with &lt;code&gt;$skip&lt;/code&gt; to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. | [optional]
 **skip** | **str**| If nonzero, skip this number of results before returning data. Used with &lt;code&gt;$top&lt;/code&gt; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| The $orderBy query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**BatchSearchListResponse**](BatchSearchListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of batch searches |  * X-Correlation-Id -  <br>  |
**400** | Bad request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_participants**
> DirectorySearchResponse search_participants(avalara_version, search)

Returns a list of participants matching the input query.

This endpoint provides a list of trading partners that match a specified input query. The search is performed based on various filters, search text, and other relevant parameters.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
DirectorySearchResponse
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
    api_instance = trading_partners_api.TradingPartnersApi(api_client)
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    search = 'Acme and 7726627177 or BMW' # str | Search by value supports logical AND and OR. Refer to [https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search) for more information on search. Search will be done over <code>name</code> and <code>identifier</code> parameters only.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    count = true # bool | When set to true, the count of the collection is included as @recordSetCount in the response body. (optional)
    filter = 'network eq 'Peppol' and country eq 'Australia'' # str | Filter by field name and value. This filter only supports <code>eq</code> .The parameters supported are <code>network</code>, <code>country</code>, <code>documentType</code>, <code>idType</code>.          Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided parameters. (optional)
    top = '10' # str | If nonzero, return no more than this number of results. Used with <code>$skip</code> to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. (optional)
    skip = '10' # str | If nonzero, skip this number of results before returning data. Used with <code>$top</code> to provide pagination for large datasets. (optional)
    order_by = 'name desc' # str | The $orderBy query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns a list of participants matching the input query.
        api_response = api_instance.search_participants(avalara_version, search)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->search_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of participants matching the input query.
        api_response = api_instance.search_participants(avalara_version, search, x_avalara_client=x_avalara_client, count=count, filter=filter, top=top, skip=skip, order_by=order_by, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->search_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **search** | **str**| Search by value supports logical AND and OR. Refer to [https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search) for more information on search. Search will be done over &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;identifier&lt;/code&gt; parameters only. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **count** | **bool**| When set to true, the count of the collection is included as @recordSetCount in the response body. | [optional]
 **filter** | **str**| Filter by field name and value. This filter only supports &lt;code&gt;eq&lt;/code&gt; .The parameters supported are &lt;code&gt;network&lt;/code&gt;, &lt;code&gt;country&lt;/code&gt;, &lt;code&gt;documentType&lt;/code&gt;, &lt;code&gt;idType&lt;/code&gt;.          Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided parameters. | [optional]
 **top** | **str**| If nonzero, return no more than this number of results. Used with &lt;code&gt;$skip&lt;/code&gt; to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. | [optional]
 **skip** | **str**| If nonzero, skip this number of results before returning data. Used with &lt;code&gt;$top&lt;/code&gt; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| The $orderBy query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**DirectorySearchResponse**](DirectorySearchResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Correlation-Id -  <br>  |
**400** | Bad request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

