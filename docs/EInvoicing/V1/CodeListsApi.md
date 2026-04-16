# Avalara.SDK.CodeListsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_list**](CodeListsApi.md#get_code_list) | **GET** /codelists/{codelistId} | Retrieves a code list by ID for a specific country
[**get_code_list_list**](CodeListsApi.md#get_code_list_list) | **GET** /codelists | Returns a list of code lists for a specific country


# **get_code_list**
> CodeListResponse get_code_list(avalara_version, codelist_id, country_code)

Retrieves a code list by ID for a specific country

A Code List is a controlled set of predefined, standardized values used to populate specific fields in electronic documents (such as e-invoices). Each code has a stable, machine-readable identifier and a human-readable description. Code Lists are typically based on global standards (e.g., UN/CEFACT, ISO, EN16931) and may include jurisdiction-specific extensions or restrictions.<br><br>Code Lists are versioned, and each version may have defined effective and sunset dates to ensure that the correct set of allowable values is applied according to regulatory or jurisdictional requirements.<br><br>By default, the API returns only non-expired code list versions (versions where the sunset date has not passed). To retrieve expired versions or filter by specific date ranges, use the <code>effectiveDate</code> and <code>sunsetDate</code> query parameters.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import code_lists_api
BadRequest
ForbiddenError
NotFoundError
CodeListResponse
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
    api_instance = code_lists_api.CodeListsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    codelist_id = 'ab123343-3432-423c-ac3f-53453scs9999' # str | System-generated unique identifier of the code list definition. Typically a UUID used to reference this code list internally or via APIs.
    country_code = 'FR' # str | Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction this code list applies to.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    effective_date = 'Tue Dec 31 16:00:00 PST 2024' # date | Filter code list versions by effective date. Returns versions that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided. (optional)
    sunset_date = 'Wed Dec 30 16:00:00 PST 2026' # date | Filter code list versions by sunset date. Returns versions that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired versions are returned. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieves a code list by ID for a specific country
        api_response = api_instance.get_code_list(avalara_version, codelist_id, country_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CodeListsApi->get_code_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a code list by ID for a specific country
        api_response = api_instance.get_code_list(avalara_version, codelist_id, country_code, x_avalara_client=x_avalara_client, effective_date=effective_date, sunset_date=sunset_date)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CodeListsApi->get_code_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **codelist_id** | **str**| System-generated unique identifier of the code list definition. Typically a UUID used to reference this code list internally or via APIs. |
 **country_code** | **str**| Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction this code list applies to. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **effective_date** | **date**| Filter code list versions by effective date. Returns versions that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided. | [optional]
 **sunset_date** | **date**| Filter code list versions by sunset date. Returns versions that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired versions are returned. | [optional]

### Return type

[**CodeListResponse**](CodeListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Code list not found. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_code_list_list**
> CodeListListResponse get_code_list_list(avalara_version, country_code)

Returns a list of code lists for a specific country

Get a list of code lists on the Avalara E-Invoicing platform for the specified country. By default, the API returns only non-expired code lists (code lists where the sunset date has not passed). To retrieve expired code lists or filter by specific date ranges, use the <code>effectiveDate</code> and <code>sunsetDate</code> query parameters.<br><br>A Code List is a controlled set of predefined, standardized values used to populate specific fields in electronic documents (such as e-invoices). Each code has a stable, machine-readable identifier and a human-readable description. Code Lists are typically based on global standards (e.g., UN/CEFACT, ISO, EN16931) and may include jurisdiction-specific extensions or restrictions.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import code_lists_api
BadRequest
ForbiddenError
CodeListListResponse
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
    api_instance = code_lists_api.CodeListsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    country_code = 'FR' # str | Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction for which code lists should be returned.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    effective_date = 'Tue Dec 31 16:00:00 PST 2024' # date | Filter code lists by effective date. Returns code lists that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided. (optional)
    sunset_date = 'Wed Dec 30 16:00:00 PST 2026' # date | Filter code lists by sunset date. Returns code lists that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired code lists are returned. (optional)
    count = 'true' # str | When set to true, the response body also includes the count of items in the collection. (optional)
    count_only = 'false' # str | When set to true, the response returns only the count of items in the collection. (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns a list of code lists for a specific country
        api_response = api_instance.get_code_list_list(avalara_version, country_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CodeListsApi->get_code_list_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of code lists for a specific country
        api_response = api_instance.get_code_list_list(avalara_version, country_code, x_avalara_client=x_avalara_client, effective_date=effective_date, sunset_date=sunset_date, count=count, count_only=count_only, top=top, skip=skip)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CodeListsApi->get_code_list_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **country_code** | **str**| Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction for which code lists should be returned. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **effective_date** | **date**| Filter code lists by effective date. Returns code lists that are effective on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, defaults to the current date. sunsetDate is required when effectiveDate is provided. | [optional]
 **sunset_date** | **date**| Filter code lists by sunset date. Returns code lists that have not yet sunset on or before this date. Format: YYYY-MM-DD (ISO 8601). If not specified, only non-expired code lists are returned. | [optional]
 **count** | **str**| When set to true, the response body also includes the count of items in the collection. | [optional]
 **count_only** | **str**| When set to true, the response returns only the count of items in the collection. | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]

### Return type

[**CodeListListResponse**](CodeListListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

