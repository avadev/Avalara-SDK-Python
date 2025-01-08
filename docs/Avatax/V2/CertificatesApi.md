# Avalara.SDK.CertificatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_certificate_image**](CertificatesApi.md#download_certificate_image) | **GET** /avatax/companies/{companyId}/certificates/{id}/attachment | Download an image for this certificate
[**upload_certificate_image**](CertificatesApi.md#upload_certificate_image) | **POST** /avatax/companies/{companyId}/certificates/{id}/attachment | Upload an image or PDF attachment for this certificate


# **download_certificate_image**
> file_type download_certificate_image(company_id, id)

Download an image for this certificate

Download an image or PDF file for this certificate.                This API can be used to download either a single-page preview of the certificate or a full PDF document.  To retrieve a preview image, set the `$type` parameter to `Jpeg` and the `$page` parameter to `1`.                A certificate is a document stored in either AvaTax Exemptions or CertCapture.  The certificate document  can contain information about a customer's eligibility for exemption from sales or use taxes based on  criteria you specify when you store the certificate.  To view or manage your certificates directly, please  log onto the administrative website for the product you purchased.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)
    company_id = 1 # int | The unique ID number of the company that recorded this certificate
    id = 1 # int | The unique ID number of this certificate
    page = 1 # int | If you choose `$type`=`Jpeg`, you must specify which page number to retrieve. (optional)
    type = "Pdf" # str | The data format in which to retrieve the certificate image (optional) if omitted the server will use the default value of "Pdf"
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Download an image for this certificate
        api_response = api_instance.download_certificate_image(company_id, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertificatesApi->download_certificate_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download an image for this certificate
        api_response = api_instance.download_certificate_image(company_id, id, page=page, type=type, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertificatesApi->download_certificate_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that recorded this certificate |
 **id** | **int**| The unique ID number of this certificate |
 **page** | **int**| If you choose &#x60;$type&#x60;&#x3D;&#x60;Jpeg&#x60;, you must specify which page number to retrieve. | [optional]
 **type** | **str**| The data format in which to retrieve the certificate image | [optional] if omitted the server will use the default value of "Pdf"
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

**file_type**

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_certificate_image**
> str upload_certificate_image(company_id, id, file)

Upload an image or PDF attachment for this certificate

Upload an image or PDF attachment for this certificate.                Image attachments can be of the format `PDF`, `JPEG`, `TIFF`, or `PNG`.  To upload a multi-page image, please  use the `PDF` data type.                A certificate is a document stored in either AvaTax Exemptions or CertCapture.  The certificate document  can contain information about a customer's eligibility for exemption from sales or use taxes based on  criteria you specify when you store the certificate.  To view or manage your certificates directly, please  log onto the administrative website for the product you purchased.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import certificates_api
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
    api_instance = certificates_api.CertificatesApi(api_client)
    company_id = 1 # int | The unique ID number of the company that recorded this certificate
    id = 1 # int | The unique ID number of this certificate
    file = open('/path/to/file', 'rb') # file_type | The exemption certificate file you wanted to upload. Accepted formats are: PDF, JPEG, TIFF, PNG.
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Upload an image or PDF attachment for this certificate
        api_response = api_instance.upload_certificate_image(company_id, id, file)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertificatesApi->upload_certificate_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload an image or PDF attachment for this certificate
        api_response = api_instance.upload_certificate_image(company_id, id, file, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertificatesApi->upload_certificate_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that recorded this certificate |
 **id** | **int**| The unique ID number of this certificate |
 **file** | **file_type**| The exemption certificate file you wanted to upload. Accepted formats are: PDF, JPEG, TIFF, PNG. |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

