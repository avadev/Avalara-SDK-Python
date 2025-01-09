# Avalara.SDK.InteropApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_interop_document**](InteropApi.md#submit_interop_document) | **POST** /interop/documents | Submit a document


# **submit_interop_document**
> SubmitInteropDocument202Response submit_interop_document(document_type, interchange_type, avalara_version)

Submit a document

This API used by the interoperability partners to submit a document to  their trading partners in Avalara on behalf of their customers. 

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
    avalara_version = '1.2' # str | The HTTP Header meant to specify the version of the API intended to be used
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\" (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
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
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot; | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]
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
**202** | Document Accepted. This doesn&#39;t mean it is processed. This is just a transport ack. |  * X-Correlation-ID -  <br>  |
**400** | Bad/Invalid Request. |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

