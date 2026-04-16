# Avalara.SDK.DocumentsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_document**](DocumentsApi.md#download_document) | **GET** /documents/{documentId}/$download | Returns a copy of the document
[**fetch_documents**](DocumentsApi.md#fetch_documents) | **POST** /documents/$fetch | Fetch the inbound document from a tax authority
[**get_document_list**](DocumentsApi.md#get_document_list) | **GET** /documents | Returns a summary of documents for a date range
[**get_document_status**](DocumentsApi.md#get_document_status) | **GET** /documents/{documentId}/status | Checks the status of a document
[**submit_document**](DocumentsApi.md#submit_document) | **POST** /documents | Submits a document to Avalara E-Invoicing API


# **download_document**
> bytearray download_document(avalara_version, accept, document_id)

Returns a copy of the document

Downloads the document when it is available. Specify the output format in the Accept header. Returns 404 if the file has not been created.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import documents_api
BadDownloadRequest
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    accept = 'application/pdf' # str | Header that specifies the MIME type of the returned document.
    document_id = 'document_id_example' # str | The unique documentId returned in the POST /documents response body.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
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
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **accept** | **str**| Header that specifies the MIME type of the returned document. |
 **document_id** | **str**| The unique documentId returned in the POST /documents response body. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]

### Return type

**bytearray**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the document content in the format specified by the Accept header. |  * Content-type -  <br>  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | A document for the specified ID was not found. |  -  |
**406** | Unsupported document format was requested in the Accept header. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fetch_documents**
> DocumentFetch fetch_documents(avalara_version, fetch_documents_request)

Fetch the inbound document from a tax authority

Retrieves an inbound document. Provide key-value pairs as request parameters. Supported parameters vary by tax authority and country.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import documents_api
FetchDocumentsRequest
DocumentFetch
ForbiddenError
InternalServerError
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
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    fetch_documents_request = Avalara.SDK.FetchDocumentsRequest() # FetchDocumentsRequest | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    # example passing only required values which don't have defaults set
    try:
        # Fetch the inbound document from a tax authority
        api_response = api_instance.fetch_documents(avalara_version, fetch_documents_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->fetch_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch the inbound document from a tax authority
        api_response = api_instance.fetch_documents(avalara_version, fetch_documents_request, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->fetch_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **fetch_documents_request** | [**FetchDocumentsRequest**](FetchDocumentsRequest.md)|  |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]

### Return type

[**DocumentFetch**](DocumentFetch.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response from the inbound document fetch endpoint. Contains the platform documentId for status checks and downloads, the returned status (e.g. Accepted), and eventDateTime when the document was accepted. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_document_list**
> DocumentListResponse get_document_list(avalara_version)

Returns a summary of documents for a date range

Returns a list of document summaries with a processing date within the specified date range.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import documents_api
BadRequest
DocumentListResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date for documents to return. Defaults to the previous month. Format: \"YYYY-MM-DDThh:mm:ss\". (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End date for documents to return. Defaults to the current date. Format: \"YYYY-MM-DDThh:mm:ss\". (optional)
    flow = 'out' # str | Optional filter for document direction: issued uses \"out\" and received uses \"in\". (optional)
    count = 'true' # str | When set to true, the response body also includes the count of items in the collection. (optional)
    count_only = 'false' # str | When set to true, the response returns only the count of items in the collection. (optional)
    filter = 'id eq 52f60401-44d0-4667-ad47-4afe519abb53' # str | Filter by field name and value. This filter supports only eq. For more information, refer to the Avalara filtering guide. (optional)
    include = 'events' # str | When set to `events`, each document in the response includes its events array. Omit this parameter or use any other value to exclude events from the response. (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
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
        api_response = api_instance.get_document_list(avalara_version, x_avalara_client=x_avalara_client, start_date=start_date, end_date=end_date, flow=flow, count=count, count_only=count_only, filter=filter, include=include, top=top, skip=skip)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **start_date** | **datetime**| Start date for documents to return. Defaults to the previous month. Format: \&quot;YYYY-MM-DDThh:mm:ss\&quot;. | [optional]
 **end_date** | **datetime**| End date for documents to return. Defaults to the current date. Format: \&quot;YYYY-MM-DDThh:mm:ss\&quot;. | [optional]
 **flow** | **str**| Optional filter for document direction: issued uses \&quot;out\&quot; and received uses \&quot;in\&quot;. | [optional]
 **count** | **str**| When set to true, the response body also includes the count of items in the collection. | [optional]
 **count_only** | **str**| When set to true, the response returns only the count of items in the collection. | [optional]
 **filter** | **str**| Filter by field name and value. This filter supports only eq. For more information, refer to the Avalara filtering guide. | [optional]
 **include** | **str**| When set to &#x60;events&#x60;, each document in the response includes its events array. Omit this parameter or use any other value to exclude events from the response. | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]

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
**200** | Returns a collection of document summaries for the specified date range. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_document_status**
> DocumentStatusResponse get_document_status(avalara_version, document_id)

Checks the status of a document

Uses the documentId from the POST /documents response body to return the current status of a document.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import documents_api
DocumentStatusResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    document_id = 'document_id_example' # str | The unique documentId returned in the POST /documents response body.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
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
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **document_id** | **str**| The unique documentId returned in the POST /documents response body. |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]

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
**200** | Returns the current status for the specified documentId. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | A document for the specified ID was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **submit_document**
> DocumentSubmitResponse submit_document(avalara_version, metadata, data)

Submits a document to Avalara E-Invoicing API

When a UBL document is sent to this endpoint, it generates a document in the required format as mandated by the specified country. Additionally, it initiates the workflow to transmit the generated document to the relevant tax authority, if necessary.<br><br>The response from the endpoint contains a unique document ID, which can be used to request the status of the document and verify if it was successfully accepted at the destination.<br><br>Furthermore, the unique ID enables the download of a copy of the generated document for reference purposes.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import documents_api
DocumentSubmissionError
DocumentSubmitResponse
SubmitDocumentMetadata
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
    api_instance = documents_api.DocumentsApi(api_client)
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    metadata = Avalara.SDK.SubmitDocumentMetadata() # SubmitDocumentMetadata | 
    data = None # object | The document to be submitted, as indicated by the metadata fields 'dataFormat' and 'dataFormatVersion'
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
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
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **metadata** | [**SubmitDocumentMetadata**](SubmitDocumentMetadata.md)|  |
 **data** | [**object**](object.md)| The document to be submitted, as indicated by the metadata fields &#39;dataFormat&#39; and &#39;dataFormatVersion&#39; |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]

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
**201** | Returns a unique documentId for the submitted document. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

