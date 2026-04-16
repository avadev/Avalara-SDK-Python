# Avalara.SDK.ReportsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report**](ReportsApi.md#download_report) | **GET** /reports/{reportId}/$download | Returns a pre-signed download URL for a report
[**get_report_by_id**](ReportsApi.md#get_report_by_id) | **GET** /reports/{reportId}/status | Retrieves a report by its unique ID
[**get_reports**](ReportsApi.md#get_reports) | **GET** /reports | Returns a list of reports


# **download_report**
> ReportDownloadResponse download_report(avalara_version, report_id)

Returns a pre-signed download URL for a report

Returns a pre-signed URL to download the report file when it is available. If the report has not yet been generated, a 404 (not found) is returned.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import reports_api
ReportDownloadResponse
ForbiddenError
NotFoundError
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
    api_instance = reports_api.ReportsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    report_id = 'report_id_example' # str | The unique ID for this report as returned in a GET /reports response.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns a pre-signed download URL for a report
        api_response = api_instance.download_report(avalara_version, report_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->download_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a pre-signed download URL for a report
        api_response = api_instance.download_report(avalara_version, report_id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->download_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **report_id** | **str**| The unique ID for this report as returned in a GET /reports response. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]

### Return type

[**ReportDownloadResponse**](ReportDownloadResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a pre-signed URL to download the report. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Report not found or not yet available for download. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_report_by_id**
> ReportItem get_report_by_id(avalara_version, report_id)

Retrieves a report by its unique ID

Retrieves a specific report by its unique identifier. Returns complete report details including metadata, status, and associated information.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import reports_api
BadRequest
ForbiddenError
NotFoundError
ReportItem
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
    api_instance = reports_api.ReportsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    report_id = 'report_id_example' # str | The unique ID for this report as returned in a GET /reports response.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieves a report by its unique ID
        api_response = api_instance.get_report_by_id(avalara_version, report_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->get_report_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a report by its unique ID
        api_response = api_instance.get_report_by_id(avalara_version, report_id, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->get_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **report_id** | **str**| The unique ID for this report as returned in a GET /reports response. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]

### Return type

[**ReportItem**](ReportItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report found and returned successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Report not found. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_reports**
> ReportListResponse get_reports(avalara_version)

Returns a list of reports

Retrieves all reports with optional filtering, paging, and sorting. Results are filtered by tenant. Supports OData-style filtering using the $filter parameter. Use $top and $skip for paging; when more results exist, the response includes @nextLink to fetch the next page. Default sort order is by report generation date (descending).

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import reports_api
BadRequest
ReportListResponse
ForbiddenError
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
    api_instance = reports_api.ReportsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
    filter = 'status eq 'COMPLETED'' # str | OData-style filter expression. Supports operators: eq, ne, gt, ge, lt, le, like, ilike, contains. Examples: status eq 'COMPLETED', reportGenerateDate gt '2025-11-01', transactionIds contains 'TXN-2025-001' (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    count = 'true' # str | When set to true, the response body also includes the count of items in the collection. (optional)
    count_only = 'false' # str | When set to true, the response returns only the count of items in the collection. (optional)
    orderby = 'reportGenerateDate desc' # str | OData-style orderby expression. Format: 'field asc' or 'field desc'. Default: reportGenerateDate desc (optional) if omitted the server will use the default value of 'reportGenerateDate desc'
    # example passing only required values which don't have defaults set
    try:
        # Returns a list of reports
        api_response = api_instance.get_reports(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->get_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of reports
        api_response = api_instance.get_reports(avalara_version, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id, filter=filter, top=top, skip=skip, count=count, count_only=count_only, orderby=orderby)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ReportsApi->get_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]
 **filter** | **str**| OData-style filter expression. Supports operators: eq, ne, gt, ge, lt, le, like, ilike, contains. Examples: status eq &#39;COMPLETED&#39;, reportGenerateDate gt &#39;2025-11-01&#39;, transactionIds contains &#39;TXN-2025-001&#39; | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]
 **count** | **str**| When set to true, the response body also includes the count of items in the collection. | [optional]
 **count_only** | **str**| When set to true, the response returns only the count of items in the collection. | [optional]
 **orderby** | **str**| OData-style orderby expression. Format: &#39;field asc&#39; or &#39;field desc&#39;. Default: reportGenerateDate desc | [optional] if omitted the server will use the default value of 'reportGenerateDate desc'

### Return type

[**ReportListResponse**](ReportListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reports retrieved successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

