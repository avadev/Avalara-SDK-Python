# Avalara.SDK.CertExpressInvitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cert_express_invitation**](CertExpressInvitesApi.md#create_cert_express_invitation) | **POST** /avatax/companies/{companyId}/customers/{customerCode}/certexpressinvites | Create a CertExpress invitation
[**get_cert_express_invitation**](CertExpressInvitesApi.md#get_cert_express_invitation) | **GET** /avatax/companies/{companyId}/customers/{customerCode}/certexpressinvites/{id} | Retrieve a single CertExpress invitation
[**list_cert_express_invitations**](CertExpressInvitesApi.md#list_cert_express_invitations) | **GET** /avatax/companies/{companyId}/certexpressinvites | List CertExpress invitations


# **create_cert_express_invitation**
> [CertExpressInvitationStatusModel] create_cert_express_invitation(company_id, customer_code)

Create a CertExpress invitation

Creates an invitation for a customer to self-report certificates using the CertExpress website.                This invitation is delivered by your choice of method, or you can present a hyperlink to the user  directly in your connector.  Your customer will be redirected to https://app.certexpress.com/ where  they can follow a step-by-step guide to enter information about their exemption certificates.  The  certificates entered will be recorded and automatically linked to their customer record.                The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.  Using CertExpress with this API will ensure that your certificates are automatically linked correctly into  your company so that they can be used for tax exemptions.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import cert_express_invites_api
from Avalara.SDK.model.cert_express_invitation_status_model import CertExpressInvitationStatusModel
from Avalara.SDK.model.create_cert_express_invitation_model import CreateCertExpressInvitationModel
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
    api_instance = cert_express_invites_api.CertExpressInvitesApi(api_client)
    company_id = 1 # int | The unique ID number of the company that will record certificates
    customer_code = "customerCode_example" # str | The number of the customer where the request is sent to
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = [
        CreateCertExpressInvitationModel(
            recipient="bob@example.org",
            cover_letter_title="STANDARD_REQUEST",
            exposure_zones=[89],
            exempt_reasons=[70],
            delivery_method="Email",
        ),
    ] # [CreateCertExpressInvitationModel] | the requests to send out to customers (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create a CertExpress invitation
        api_response = api_instance.create_cert_express_invitation(company_id, customer_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->create_cert_express_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a CertExpress invitation
        api_response = api_instance.create_cert_express_invitation(company_id, customer_code, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->create_cert_express_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that will record certificates |
 **customer_code** | **str**| The number of the customer where the request is sent to |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**[CreateCertExpressInvitationModel]**](CreateCertExpressInvitationModel.md)| the requests to send out to customers | [optional]

### Return type

[**[CertExpressInvitationStatusModel]**](CertExpressInvitationStatusModel.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cert_express_invitation**
> CertExpressInvitationModel get_cert_express_invitation(company_id, customer_code, id)

Retrieve a single CertExpress invitation

Retrieve an existing CertExpress invitation sent to a customer.                A CertExpression invitation allows a customer to follow a helpful step-by-step guide to provide information  about their certificates.  This step by step guide allows the customer to complete and upload the full  certificate in a convenient, friendly web browser experience.  When the customer completes their certificates,  they will automatically be recorded to your company and linked to the customer record.                The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.  Using CertExpress with this API will ensure that your certificates are automatically linked correctly into  your company so that they can be used for tax exemptions.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import cert_express_invites_api
from Avalara.SDK.model.cert_express_invitation_model import CertExpressInvitationModel
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
    api_instance = cert_express_invites_api.CertExpressInvitesApi(api_client)
    company_id = 1 # int | The unique ID number of the company that issued this invitation
    customer_code = "customerCode_example" # str | The number of the customer where the request is sent to
    id = 1 # int | The unique ID number of this CertExpress invitation
    include = "$include_example" # str | OPTIONAL: A comma separated list of special fetch options.  No options are defined at this time. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single CertExpress invitation
        api_response = api_instance.get_cert_express_invitation(company_id, customer_code, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->get_cert_express_invitation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a single CertExpress invitation
        api_response = api_instance.get_cert_express_invitation(company_id, customer_code, id, include=include, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->get_cert_express_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that issued this invitation |
 **customer_code** | **str**| The number of the customer where the request is sent to |
 **id** | **int**| The unique ID number of this CertExpress invitation |
 **include** | **str**| OPTIONAL: A comma separated list of special fetch options.  No options are defined at this time. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**CertExpressInvitationModel**](CertExpressInvitationModel.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_cert_express_invitations**
> CertExpressInvitationModelFetchResult list_cert_express_invitations(company_id)

List CertExpress invitations

Retrieve CertExpress invitations sent by this company.                A CertExpression invitation allows a customer to follow a helpful step-by-step guide to provide information  about their certificates.  This step by step guide allows the customer to complete and upload the full  certificate in a convenient, friendly web browser experience.  When the customer completes their certificates,  they will automatically be recorded to your company and linked to the customer record.                The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.  Using CertExpress with this API will ensure that your certificates are automatically linked correctly into  your company so that they can be used for tax exemptions.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import cert_express_invites_api
from Avalara.SDK.model.cert_express_invitation_model_fetch_result import CertExpressInvitationModelFetchResult
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
    api_instance = cert_express_invites_api.CertExpressInvitesApi(api_client)
    company_id = 1 # int | The unique ID number of the company that issued this invitation
    include = "$include_example" # str | OPTIONAL: A comma separated list of special fetch options.                             No options are defined at this time. (optional)
    filter = "$filter_example" # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* companyId, customer, coverLetter, exposureZones, exemptReasons, requestLink (optional)
    top = 1 # int | If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 1 # int | If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets. (optional)
    order_by = "$orderBy_example" # str | A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # List CertExpress invitations
        api_response = api_instance.list_cert_express_invitations(company_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->list_cert_express_invitations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List CertExpress invitations
        api_response = api_instance.list_cert_express_invitations(company_id, include=include, filter=filter, top=top, skip=skip, order_by=order_by, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CertExpressInvitesApi->list_cert_express_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that issued this invitation |
 **include** | **str**| OPTIONAL: A comma separated list of special fetch options.                             No options are defined at this time. | [optional]
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).&lt;br /&gt;*Not filterable:* companyId, customer, coverLetter, exposureZones, exemptReasons, requestLink | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.  Used with &#x60;$skip&#x60; to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data.  Used with &#x60;$top&#x60; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format &#x60;(fieldname) [ASC|DESC]&#x60;, for example &#x60;id ASC&#x60;. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**CertExpressInvitationModelFetchResult**](CertExpressInvitationModelFetchResult.md)

### Authorization

[Bearer](../README.md#Bearer), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

