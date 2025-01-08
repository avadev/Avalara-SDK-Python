# Avalara.SDK.DocumentsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_document**](DocumentsApi.md#download_document) | **GET** /documents/{documentId}/$download | Returns a copy of the document
[**get_document_list**](DocumentsApi.md#get_document_list) | **GET** /documents | Returns a summary of documents for a date range
[**get_document_status**](DocumentsApi.md#get_document_status) | **GET** /document/{documentId}/status | Checks the status of a document
[**submit_document**](DocumentsApi.md#submit_document) | **POST** /documents | Submits a document to Avalara E-Invoicing API


# **download_document**
> file_type download_document(avalara_version, accept, document_id)

Returns a copy of the document

When the document is available, use this endpoint to download it as text, XML, or PDF. The output format needs to be specified in the Accept header and it will vary depending on the mandate. If the file has not yet been created, then status code 404 (not found) is returned.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import documents_api
from Avalara.SDK.model.not_found_error import NotFoundError
from Avalara.SDK.model.bad_download_request import BadDownloadRequest
from Avalara.SDK.model.forbidden_error import ForbiddenError
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = "1.0" # str | The HTTP Header meant to specify the version of the API intended to be used
    accept = "application/pdf" # str | This header indicates the MIME type of the document
    document_id = "2022-01-008572" # str | The unique ID for this document that was returned in the POST /einvoicing/document response body
    x_avalara_client = "John's E-Invoicing-API Client" # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns a copy of the document
        api_response = api_instance.download_document(avalara_version, accept, document_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a copy of the document
        api_response = api_instance.download_document(avalara_version, accept, document_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **accept** | **str**| This header indicates the MIME type of the document |
 **document_id** | **str**| The unique ID for this document that was returned in the POST /einvoicing/document response body |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]

### Return type

**file_type**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-type -  <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | A document for the specified ID was not found. |  -  |
**406** | Unsupported document format was requested in the Accept header |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_document_list**
> DocumentListResponse get_document_list(avalara_version)

Returns a summary of documents for a date range

Get a list of documents on the Avalara E-Invoicing platform that have a processing date within the specified date range.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import documents_api
from Avalara.SDK.model.forbidden_error import ForbiddenError
from Avalara.SDK.model.document_list_response import DocumentListResponse
from Avalara.SDK.model.bad_request import BadRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = "1.0" # str | The HTTP Header meant to specify the version of the API intended to be used
    x_avalara_client = "John's E-Invoicing-API Client" # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Start date of documents to return. This defaults to the previous month. (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | End date of documents to return. This defaults to the current date. (optional)
    flow = "out" # str | Optionally filter by document direction, where issued = `out` and received = `in` (optional)
    count = "true" # str | When set to true, the count of the collection is also returned in the response body (optional)
    count_only = "false" # str | When set to true, only the count of the collection is returned (optional)
    filter = "id eq 2023-02-000016" # str | Filter by field name and value. This filter only supports <code>eq</code> . Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided startDate and endDate. If no startDate or endDate is provided, defaults will be assumed. (optional)
    top = 10 # float | If nonzero, return no more than this number of results. Used with <code>$skip</code> to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. (optional)
    skip = "10" # str | If nonzero, skip this number of results before returning data. Used with <code>$top</code> to provide pagination for large datasets. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns a summary of documents for a date range
        api_response = api_instance.get_document_list(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a summary of documents for a date range
        api_response = api_instance.get_document_list(avalara_version, x_avalara_client=x_avalara_client, start_date=start_date, end_date=end_date, flow=flow, count=count, count_only=count_only, filter=filter, top=top, skip=skip)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **start_date** | **datetime**| Start date of documents to return. This defaults to the previous month. | [optional]
 **end_date** | **datetime**| End date of documents to return. This defaults to the current date. | [optional]
 **flow** | **str**| Optionally filter by document direction, where issued &#x3D; &#x60;out&#x60; and received &#x3D; &#x60;in&#x60; | [optional]
 **count** | **str**| When set to true, the count of the collection is also returned in the response body | [optional]
 **count_only** | **str**| When set to true, only the count of the collection is returned | [optional]
 **filter** | **str**| Filter by field name and value. This filter only supports &lt;code&gt;eq&lt;/code&gt; . Refer to [https://developer.avalara.com/avatax/filtering-in-rest/](https://developer.avalara.com/avatax/filtering-in-rest/) for more information on filtering. Filtering will be done over the provided startDate and endDate. If no startDate or endDate is provided, defaults will be assumed. | [optional]
 **top** | **float**| If nonzero, return no more than this number of results. Used with &lt;code&gt;$skip&lt;/code&gt; to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 200 records. | [optional]
 **skip** | **str**| If nonzero, skip this number of results before returning data. Used with &lt;code&gt;$top&lt;/code&gt; to provide pagination for large datasets. | [optional]

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_document_status**
> DocumentStatusResponse get_document_status(avalara_version, document_id)

Checks the status of a document

Using the unique ID from POST /einvoicing/documents response body, request the current status of a document.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import documents_api
from Avalara.SDK.model.not_found_error import NotFoundError
from Avalara.SDK.model.forbidden_error import ForbiddenError
from Avalara.SDK.model.document_status_response import DocumentStatusResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = "1.0" # str | The HTTP Header meant to specify the version of the API intended to be used
    document_id = "2022-01-008572" # str | The unique ID for this document that was returned in the POST /einvoicing/documents response body
    x_avalara_client = "John's E-Invoicing-API Client" # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    # example passing only required values which don't have defaults set
    try:
        # Checks the status of a document
        api_response = api_instance.get_document_status(avalara_version, document_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Checks the status of a document
        api_response = api_instance.get_document_status(avalara_version, document_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **document_id** | **str**| The unique ID for this document that was returned in the POST /einvoicing/documents response body |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]

### Return type

[**DocumentStatusResponse**](DocumentStatusResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | A document for the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **submit_document**
> DocumentSubmitResponse submit_document(avalara_version, metadata, data)

Submits a document to Avalara E-Invoicing API

For both e-invoices and credit notes, when a document is sent to this endpoint, it generates an invoice or credit note in the required format as mandated by the specified country. Additionally, it initiates the workflow to transmit the generated document to the relevant tax authority, if necessary.<br><br>The response from the endpoint contains a unique document ID, which can be used to request the status of the document and verify if it was successfully accepted at the destination.<br><br>Furthermore, the unique ID enables the download of a copy of the e-invoice or credit note for reference purposes.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import documents_api
from Avalara.SDK.model.document_submission_error import DocumentSubmissionError
from Avalara.SDK.model.forbidden_error import ForbiddenError
from Avalara.SDK.model.submit_document_metadata import SubmitDocumentMetadata
from Avalara.SDK.model.document_submit_response import DocumentSubmitResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = "1.0" # str | The HTTP Header meant to specify the version of the API intended to be used
    metadata = SubmitDocumentMetadata(
        workflow_id="partner-einvoicing",
        data_format="ubl-invoice",
        data_format_version="2.1",
        country_code="SA",
        country_mandate="SA-Phase1-B2B",
    ) # SubmitDocumentMetadata | 
    data = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | The document to be submitted, as indicated by the metadata fields 'dataFormat' and 'dataFormatVersion'
    x_avalara_client = "John's E-Invoicing-API Client" # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    # example passing only required values which don't have defaults set
    try:
        # Submits a document to Avalara E-Invoicing API
        api_response = api_instance.submit_document(avalara_version, metadata, data)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->submit_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submits a document to Avalara E-Invoicing API
        api_response = api_instance.submit_document(avalara_version, metadata, data, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->submit_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **metadata** | [**SubmitDocumentMetadata**](SubmitDocumentMetadata.md)|  |
 **data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| The document to be submitted, as indicated by the metadata fields &#39;dataFormat&#39; and &#39;dataFormatVersion&#39; |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]

### Return type

[**DocumentSubmitResponse**](DocumentSubmitResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

