# Avalara.SDK.InteropApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_interop_document**](InteropApi.md#submit_interop_document) | **POST** /interop/documents | Submit a document


# **submit_interop_document**
> SubmitInteropDocument202Response submit_interop_document(document_type, interchange_type, avalara_version)

Submit a document

Upload documents on behalf of interoperability partners and submit them to trading partners through the Avalara platform.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import interop_api
SubmitInteropDocument202Response
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
    api_instance = interop_api.InteropApi(api_client)
    document_type = 'document_type_example' # str | Type of the document being uploaded. Partners will be configured in Avalara system to send only certain types of documents.
    interchange_type = 'interchange_type_example' # str | Type of interchange (codes in Avalara system that uniquely identifies a type of interchange). Partners will be configured in Avalara system to send documents belonging to certain types of interchanges.
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
    file_name = None # bytearray | The file to be uploaded (e.g., UBL XML, CII XML). (optional)
    # example passing only required values which don't have defaults set
    try:
        # Submit a document
        api_response = api_instance.submit_interop_document(document_type, interchange_type, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling InteropApi->submit_interop_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit a document
        api_response = api_instance.submit_interop_document(document_type, interchange_type, avalara_version, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id, file_name=file_name)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling InteropApi->submit_interop_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**| Type of the document being uploaded. Partners will be configured in Avalara system to send only certain types of documents. |
 **interchange_type** | **str**| Type of interchange (codes in Avalara system that uniquely identifies a type of interchange). Partners will be configured in Avalara system to send documents belonging to certain types of interchanges. |
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]
 **file_name** | [**bytearray**](bytearray.md)| The file to be uploaded (e.g., UBL XML, CII XML). | [optional]

### Return type

[**SubmitInteropDocument202Response**](SubmitInteropDocument202Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Document accepted for processing. Returns the interchange ID and acceptance message. This is a transport acknowledgment; processing occurs asynchronously. |  * X-Correlation-ID -  <br>  |
**400** | Bad request. The request is invalid or contains missing or incorrect parameters. |  * X-Correlation-ID -  <br>  |
**401** | Unauthorized. |  * X-Correlation-ID -  <br>  |
**403** | Forbidden. |  * X-Correlation-ID -  <br>  |
**500** | Internal server error. |  * X-Correlation-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

