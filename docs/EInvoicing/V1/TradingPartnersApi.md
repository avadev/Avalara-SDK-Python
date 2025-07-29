# Avalara.SDK.TradingPartnersApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_search_participants**](TradingPartnersApi.md#batch_search_participants) | **POST** /trading-partners/batch-searches | Handles batch search requests by uploading a file containing search parameters.
[**create_trading_partner**](TradingPartnersApi.md#create_trading_partner) | **POST** /trading-partners | Creates a new trading partner.
[**create_trading_partners_batch**](TradingPartnersApi.md#create_trading_partners_batch) | **POST** /trading-partners/batch | Creates a batch of multiple trading partners.
[**delete_trading_partner**](TradingPartnersApi.md#delete_trading_partner) | **DELETE** /trading-partners/{id} | Deletes a trading partner using ID.
[**download_batch_search_report**](TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Downloads batch search results in a csv file.
[**get_batch_search_detail**](TradingPartnersApi.md#get_batch_search_detail) | **GET** /trading-partners/batch-searches/{id} | Returns the batch search details using ID.
[**list_batch_searches**](TradingPartnersApi.md#list_batch_searches) | **GET** /trading-partners/batch-searches | Lists all batch searches that were previously submitted.
[**search_participants**](TradingPartnersApi.md#search_participants) | **GET** /trading-partners | Returns a list of participants matching the input query.
[**update_trading_partner**](TradingPartnersApi.md#update_trading_partner) | **PUT** /trading-partners/{id} | Updates a trading partner using ID.


# **batch_search_participants**
> BatchSearchParticipants202Response batch_search_participants(avalara_version, name, notification_email, file)

Handles batch search requests by uploading a file containing search parameters.

This endpoint creates a batch search and performs a batch search in the directory for participants in the background.

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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    name = 'Automotive Companies in London Search' # str | A <b>human-readable</b> name for the batch search.
    notification_email = 'user@example.com' # str | The email address to which a notification will be sent once the batch search is complete.
    file = None # bytearray | CSV file containing search parameters.  Input Constraints: - Maximum file size: 1 MB - File Header: Must be less than 500 KB - Total number of lines (including header): Must be 101 or fewer
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Handles batch search requests by uploading a file containing search parameters.
        api_response = api_instance.batch_search_participants(avalara_version, name, notification_email, file)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->batch_search_participants: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Handles batch search requests by uploading a file containing search parameters.
        api_response = api_instance.batch_search_participants(avalara_version, name, notification_email, file, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->batch_search_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **name** | **str**| A &lt;b&gt;human-readable&lt;/b&gt; name for the batch search. |
 **notification_email** | **str**| The email address to which a notification will be sent once the batch search is complete. |
 **file** | [**bytearray**](bytearray.md)| CSV file containing search parameters.  Input Constraints: - Maximum file size: 1 MB - File Header: Must be less than 500 KB - Total number of lines (including header): Must be 101 or fewer |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
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

# **create_trading_partner**
> CreateTradingPartner201Response create_trading_partner(avalara_version, trading_partner)

Creates a new trading partner.

This endpoint creates a new trading partner with the provided details. The request body must include the necessary information as defined in the `TradingPartner` schema.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
CreateTradingPartner201Response
TradingPartner
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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    trading_partner = {"name":"Pineapple Labs ltd","network":"","registrationDate":"2024-01-01T00:00:00.000Z","identifiers":[{"name":"urn:avalara:systems:des:directory:participant:identifiers:peppolparticipantid","displayName":"","value":"9930:de112233445"}],"addresses":[{"line1":"Line 1","line2":"Line 2","city":"Brisbane","state":"Queensland","country":"Australia","postalCode":"4000"}],"supportedDocumentTypes":[{"name":"","value":"busdox-docid-qns::urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1","supportedByTradingPartner":true,"supportedByAvalara":true,"extensions":[]}],"consents":{"listInAvalaraDirectory":true},"extensions":[]} # TradingPartner | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates a new trading partner.
        api_response = api_instance.create_trading_partner(avalara_version, trading_partner)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->create_trading_partner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new trading partner.
        api_response = api_instance.create_trading_partner(avalara_version, trading_partner, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->create_trading_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **trading_partner** | [**TradingPartner**](TradingPartner.md)|  |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**CreateTradingPartner201Response**](CreateTradingPartner201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The trading partner has been successfully created. |  * X-Correlation-Id -  <br>  |
**400** | Bad request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**409** | Conflict |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_trading_partners_batch**
> CreateTradingPartnersBatch200Response create_trading_partners_batch(avalara_version, create_trading_partners_batch_request)

Creates a batch of multiple trading partners.

This endpoint creates multiple trading partners in a single batch request. It accepts an array of trading partners and processes them synchronously. Supports a maximum of 100 records or 1 MB request payload. The batch is processed atomically and partial success is not allowed.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
CreateTradingPartnersBatch200Response
CreateTradingPartnersBatchRequest
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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    create_trading_partners_batch_request = {"value":[{"name":"Pineapple Labs ltd","network":"","registrationDate":"2024-01-01T00:00:00.000Z","identifiers":[{"name":"urn:avalara:systems:des:directory:participant:identifiers:peppolparticipantid","displayName":"","value":"9930:de112233445"}],"addresses":[{"line1":"Line 1","line2":"Line 2","city":"Brisbane","state":"Queensland","country":"Australia","postalCode":"4000"}],"supportedDocumentTypes":[{"name":"","value":"busdox-docid-qns::urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1","supportedByTradingPartner":true,"supportedByAvalara":true,"extensions":[]}],"consents":{"listInAvalaraDirectory":true},"extensions":[]}]} # CreateTradingPartnersBatchRequest | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates a batch of multiple trading partners.
        api_response = api_instance.create_trading_partners_batch(avalara_version, create_trading_partners_batch_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->create_trading_partners_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a batch of multiple trading partners.
        api_response = api_instance.create_trading_partners_batch(avalara_version, create_trading_partners_batch_request, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->create_trading_partners_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **create_trading_partners_batch_request** | [**CreateTradingPartnersBatchRequest**](CreateTradingPartnersBatchRequest.md)|  |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**CreateTradingPartnersBatch200Response**](CreateTradingPartnersBatch200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch processing completed |  * X-Correlation-Id -  <br>  |
**400** | Bad request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**409** | Conflict |  * X-Correlation-Id -  <br>  |
**413** | ContentTooLarge |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_trading_partner**
> delete_trading_partner(avalara_version, id)

Deletes a trading partner using ID.

This endpoint deletes an existing trading partner identified by the provided ID.

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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    id = 'id_example' # str | The ID of the trading partner which is being deleted.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Deletes a trading partner using ID.
        api_instance.delete_trading_partner(avalara_version, id)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->delete_trading_partner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a trading partner using ID.
        api_instance.delete_trading_partner(avalara_version, id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->delete_trading_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **id** | **str**| The ID of the trading partner which is being deleted. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Trading partner deleted successfully. |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**404** | NotFound |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_batch_search_report**
> bytearray download_batch_search_report(avalara_version, id)

Downloads batch search results in a csv file.

This endpoint downloads the report for a specific batch search using the batch search ID. It returns a CSV file containing up to 1,000 query results.

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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    id = '2f5ea4b5-4dae-445a-b3e4-9f65a61eaa99' # str | The ID of the batch search for which the report should be downloaded.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Downloads batch search results in a csv file.
        api_response = api_instance.download_batch_search_report(avalara_version, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->download_batch_search_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Downloads batch search results in a csv file.
        api_response = api_instance.download_batch_search_report(avalara_version, id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->download_batch_search_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **id** | **str**| The ID of the batch search for which the report should be downloaded. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
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
**200** | Successful report download  Output Constraints: - Maximum of 1000 query results returned in the CSV |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**404** | Report not found |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_batch_search_detail**
> BatchSearch get_batch_search_detail(avalara_version, id)

Returns the batch search details using ID.

This endpoint returns detailed information for a specific batch search using the provided ID. It is useful for tracking the status and progress of a previously initiated batch search operation.

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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    id = '2f5ea4b5-4dae-445a-b3e4-9f65a61eaa99' # str | The ID of the batch search that was submitted earlier.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns the batch search details using ID.
        api_response = api_instance.get_batch_search_detail(avalara_version, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->get_batch_search_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the batch search details using ID.
        api_response = api_instance.get_batch_search_detail(avalara_version, id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->get_batch_search_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **id** | **str**| The ID of the batch search that was submitted earlier. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
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
**200** | The batch search details for a given ID. |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**404** | Report not found |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_batch_searches**
> BatchSearchListResponse list_batch_searches(avalara_version)

Lists all batch searches that were previously submitted.

This endpoint retrieves a list of all batch search operations that have been previously submitted. It returns details such as the batch search ID, status, creation date, and associated metadata. It is useful for tracking the progress of a previously initiated batch search operations.

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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    filter = 'name eq 'Batch_Search_Import_V4'' # str | Filters the results by field name. Only the <code>eq</code> operator and the name field is supported. For more information, refer to [AvaTax filtering guide](https://developer.avalara.com/avatax/filtering-in-rest/). (optional)
    count = true # bool | When set to <code>true</code>, returns the total count of matching records included as <code>@recordSetCount</code> in the response body. (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    order_by = 'name desc' # str | The <code>$orderBy</code> query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Lists all batch searches that were previously submitted.
        api_response = api_instance.list_batch_searches(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->list_batch_searches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lists all batch searches that were previously submitted.
        api_response = api_instance.list_batch_searches(avalara_version, x_avalara_client=x_avalara_client, filter=filter, count=count, top=top, skip=skip, order_by=order_by, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->list_batch_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **filter** | **str**| Filters the results by field name. Only the &lt;code&gt;eq&lt;/code&gt; operator and the name field is supported. For more information, refer to [AvaTax filtering guide](https://developer.avalara.com/avatax/filtering-in-rest/). | [optional]
 **count** | **bool**| When set to &lt;code&gt;true&lt;/code&gt;, returns the total count of matching records included as &lt;code&gt;@recordSetCount&lt;/code&gt; in the response body. | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]
 **order_by** | **str**| The &lt;code&gt;$orderBy&lt;/code&gt; query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. | [optional]
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
> SearchParticipants200Response search_participants(avalara_version, search)

Returns a list of participants matching the input query.

This endpoint retrieves a list of trading partners that match the specified search criteria. It supports filtering, search text, and other relevant query parameters to narrow down the results.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
SearchParticipants200Response
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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    search = 'Acme and 7726627177 or BMW' # str | Search by value supports logical <code>AND</code> / <code>OR</code> operators. Search is performed only over the name and identifier value fields. For more information, refer to [Query options overview - OData.](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search).
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    count = true # bool | When set to <code>true</code>, returns the total count of matching records included as <code>@recordSetCount</code> in the response body. (optional)
    filter = 'network eq 'Peppol' and country eq 'Australia'' # str | Filters the results using the <code>eq</code> operator. Supported fields: <code>network</code>, <code>country</code>, <code>documentType</code>, <code>idType</code>. For more information, refer to [AvaTax filtering guide](https://developer.avalara.com/avatax/filtering-in-rest/). (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    order_by = 'name desc' # str | The <code>$orderBy</code> query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. (optional)
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
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **search** | **str**| Search by value supports logical &lt;code&gt;AND&lt;/code&gt; / &lt;code&gt;OR&lt;/code&gt; operators. Search is performed only over the name and identifier value fields. For more information, refer to [Query options overview - OData.](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview#search). |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **count** | **bool**| When set to &lt;code&gt;true&lt;/code&gt;, returns the total count of matching records included as &lt;code&gt;@recordSetCount&lt;/code&gt; in the response body. | [optional]
 **filter** | **str**| Filters the results using the &lt;code&gt;eq&lt;/code&gt; operator. Supported fields: &lt;code&gt;network&lt;/code&gt;, &lt;code&gt;country&lt;/code&gt;, &lt;code&gt;documentType&lt;/code&gt;, &lt;code&gt;idType&lt;/code&gt;. For more information, refer to [AvaTax filtering guide](https://developer.avalara.com/avatax/filtering-in-rest/). | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]
 **order_by** | **str**| The &lt;code&gt;$orderBy&lt;/code&gt; query parameter specifies the field and sorting direction for ordering the result set. The value is a string that combines a field name and a sorting direction (asc for ascending or desc for descending), separated by a space. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**SearchParticipants200Response**](SearchParticipants200Response.md)

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

# **update_trading_partner**
> UpdateTradingPartner200Response update_trading_partner(avalara_version, id, trading_partner)

Updates a trading partner using ID.

This endpoint updates the details of an existing trading partner specified by the provided ID. It performs a full update, and the request body must include all required fields.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import trading_partners_api
UpdateTradingPartner200Response
TradingPartner
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
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    id = 'id_example' # str | The ID of the trading partner which is being updated.
    trading_partner = {"name":"Pineapple Labs ltd","registrationDate":"2024-01-01T00:00:00.000Z","identifiers":[{"name":"urn:avalara:systems:des:directory:participant:identifiers:peppolparticipantid","displayName":"","value":"9930:de112233445"}],"address":[{"line1":"Line 1","line2":"Line 2","city":"Brisbane","state":"Queensland","country":"Australia","postalCode":"4000"}],"supportedDocumentTypes":[{"name":"","value":"busdox-docid-qns::urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1","supportedByTradingPartner":true,"supportedByAvalara":true,"extensions":[]}],"consents":{"listInAvalaraDirectory":true},"extensions":[]} # TradingPartner | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Updates a trading partner using ID.
        api_response = api_instance.update_trading_partner(avalara_version, id, trading_partner)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->update_trading_partner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a trading partner using ID.
        api_response = api_instance.update_trading_partner(avalara_version, id, trading_partner, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TradingPartnersApi->update_trading_partner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **id** | **str**| The ID of the trading partner which is being updated. |
 **trading_partner** | [**TradingPartner**](TradingPartner.md)|  |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**UpdateTradingPartner200Response**](UpdateTradingPartner200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The trading partner has been successfully created. |  -  |
**400** | Bad request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**404** | NotFound |  * X-Correlation-Id -  <br>  |
**409** | Conflict |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

