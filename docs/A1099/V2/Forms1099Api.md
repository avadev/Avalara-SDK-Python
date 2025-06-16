# Avalara.SDK.Forms1099Api

All URIs are relative to *https://api-ava1099.eta.sbx.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_upsert1099_forms**](Forms1099Api.md#bulk_upsert1099_forms) | **POST** /1099/forms/$bulk-upsert | Creates or updates multiple 1099 forms.
[**create1099_form**](Forms1099Api.md#create1099_form) | **POST** /1099/forms | Creates a 1099 form.
[**delete1099_form**](Forms1099Api.md#delete1099_form) | **DELETE** /1099/forms/{id} | Deletes a 1099 form.
[**get1099_form**](Forms1099Api.md#get1099_form) | **GET** /1099/forms/{id} | Retrieves a 1099 form.
[**get1099_form_pdf**](Forms1099Api.md#get1099_form_pdf) | **GET** /1099/forms/{id}/pdf | Retrieves the PDF file for a single 1099 by form id.
[**list1099_forms**](Forms1099Api.md#list1099_forms) | **GET** /1099/forms | Retrieves a list of 1099 forms based on query parameters.
[**update1099_form**](Forms1099Api.md#update1099_form) | **PUT** /1099/forms/{id} | Updates a 1099 form.


# **bulk_upsert1099_forms**
> Form1099ProccessResult bulk_upsert1099_forms(avalara_version, x_correlation_id)

Creates or updates multiple 1099 forms.

This endpoint allows you to create or update multiple 1099 forms.  You can use one of the following payload structures:                **Form 1099-MISC:**  ```json  {     \"formType\": \"1099-MISC\",     \"forms\": [         {             \"IssuerId\": \"123456\",             \"IssuerReferenceId\": \"REF123\",             \"IssuerTin\": \"12-3456789\",             \"TaxYear\": 2023,             \"ReferenceId\": \"FORM123456\",             \"RecipientName\": \"John Doe\",             \"RecipientTin\": \"987-65-4321\",             \"TinType\": 1,             \"RecipientSecondName\": \"Jane Doe\",             \"StreetAddress\": \"123 Main Street\",             \"StreetAddressLine2\": \"Apt 4B\",             \"City\": \"New York\",             \"State\": \"NY\",             \"Zip\": \"10001\",             \"RecipientEmail\": \"john.doe@email.com\",             \"AccountNumber\": \"ACC123456\",             \"OfficeCode\": \"NYC01\",             \"SecondTinNotice\": false,             \"RecipientNonUsProvince\": \"\",             \"CountryCode\": \"US\",             \"Rents\": 12000.00,             \"Royalties\": 5000.00,             \"OtherIncome\": 3000.00,             \"FishingBoatProceeds\": 0.00,             \"MedicalHealthCarePayments\": 15000.00,             \"SubstitutePayments\": 1000.00,             \"CropInsuranceProceeds\": 0.00,             \"GrossProceedsPaidToAttorney\": 7500.00,             \"FishPurchasedForResale\": 0.00,             \"FedIncomeTaxWithheld\": 5000.00,             \"Section409ADeferrals\": 0.00,             \"ExcessGoldenParachutePayments\": 0.00,             \"NonqualifiedDeferredCompensation\": 0.00,             \"PayerMadeDirectSales\": false,             \"FatcaFilingRequirement\": false,             \"StateAndLocalWithholding\": {               \"StateTaxWithheld\": 2500.00,               \"LocalTaxWithheld\": 1000.00,               \"State\": \"NY\",               \"StateIdNumber\": \"NY123456\",               \"Locality\": \"New York City\",               \"StateIncome\": 35000.00,               \"LocalIncome\": 35000.00             }         }     ]  }  ```                **Form 1099-NEC:**  ```json  {    \"formType\": \"1099-NEC\",    \"forms\": [      {        \"issuerID\": \"180337282\",        \"issuerReferenceId\": \"ISS123\",        \"issuerTin\": \"12-3000000\",        \"taxYear\": 2024,        \"referenceID\": \"REF-002\",        \"recipientName\": \"Jane Smith\",        \"recipientSecondName\": \"\",        \"recipientTin\": \"987-65-4321\",        \"tinType\": 1,        \"streetAddress\": \"123 Center St\",        \"streetAddressLine2\": \"\",        \"city\": \"Santa Monica\",        \"state\": \"CA\",        \"zip\": \"90401\",        \"countryCode\": \"US\",        \"recipientNonUsProvince\": \"\",        \"recipientEmail\": \"\",        \"accountNumber\": \"\",        \"officeCode\": \"\",        \"secondTinNotice\": false,        \"nonemployeeCompensation\": 123.45,        \"payerMadeDirectSales\": false,        \"federalIncomeTaxWithheld\": 12.34,        \"stateAndLocalWithholding\": {          \"state\": \"CA\",          \"stateIdNumber\": \"123123123\"          \"stateIncome\": 123.45,          \"stateTaxWithheld\": 12.34,          \"locality\": \"Santa Monica\",          \"localityIdNumber\": \"456456\",          \"localTaxWithheld\": 12.34          \"localIncome\": 50000.00         },        \"federalEFile\": true,        \"postalMail\": true,        \"stateEFile\": true,        \"tinMatch\": true,        \"addressVerification\": true       }     ]   }  ```  For the full version of the payload and its schema details, refer to the Swagger schemas section.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Form1099ProccessResult
BulkUpsert1099FormsRequest
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'b4591fca-ad23-44f7-acfe-1b29e86ef386' # str | Unique correlation Id in a GUID format
    dry_run = False # bool |  (optional) if omitted the server will use the default value of False
    bulk_upsert1099_forms_request = Avalara.SDK.BulkUpsert1099FormsRequest() # BulkUpsert1099FormsRequest |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates or updates multiple 1099 forms.
        api_response = api_instance.bulk_upsert1099_forms(avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->bulk_upsert1099_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates or updates multiple 1099 forms.
        api_response = api_instance.bulk_upsert1099_forms(avalara_version, x_correlation_id, dry_run=dry_run, bulk_upsert1099_forms_request=bulk_upsert1099_forms_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->bulk_upsert1099_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **dry_run** | **bool**|  | [optional] if omitted the server will use the default value of False
 **bulk_upsert1099_forms_request** | [**BulkUpsert1099FormsRequest**](BulkUpsert1099FormsRequest.md)|  | [optional]

### Return type

[**Form1099ProccessResult**](Form1099ProccessResult.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create1099_form**
> FormResponseBase create1099_form(avalara_version, x_correlation_id)

Creates a 1099 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
FormResponseBase
ErrorResponse
ICreateForm1099Request
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'e7998dc4-619c-441e-8e45-694347c43c62' # str | Unique correlation Id in a GUID format
    i_create_form1099_request = Avalara.SDK.ICreateForm1099Request() # ICreateForm1099Request |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates a 1099 form.
        api_response = api_instance.create1099_form(avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->create1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a 1099 form.
        api_response = api_instance.create1099_form(avalara_version, x_correlation_id, i_create_form1099_request=i_create_form1099_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->create1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **i_create_form1099_request** | [**ICreateForm1099Request**](ICreateForm1099Request.md)|  | [optional]

### Return type

[**FormResponseBase**](FormResponseBase.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete1099_form**
> delete1099_form(id, avalara_version, x_correlation_id)

Deletes a 1099 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    id = 'id_example' # str | The unique identifier of the desired form to delete.
    avalara_version = '2.0' # str | API version
    x_correlation_id = '5a798b0d-9637-46c1-9b5c-7acdb70f315a' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Deletes a 1099 form.
        api_instance.delete1099_form(id, avalara_version, x_correlation_id)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->delete1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the desired form to delete. |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Client Error |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get1099_form**
> FormResponseBase get1099_form(id, avalara_version, x_correlation_id)

Retrieves a 1099 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
FormResponseBase
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    id = 'id_example' # str | 
    avalara_version = '2.0' # str | API version
    x_correlation_id = '4ee0ec52-a2a8-413b-b6d8-ab796bc6be1a' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Retrieves a 1099 form.
        api_response = api_instance.get1099_form(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |

### Return type

[**FormResponseBase**](FormResponseBase.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get1099_form_pdf**
> FormResponseBase get1099_form_pdf(id, avalara_version, x_correlation_id)

Retrieves the PDF file for a single 1099 by form id.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
FormResponseBase
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    id = 'id_example' # str | 
    avalara_version = '2.0' # str | API version
    x_correlation_id = '67e8f361-ee44-4f51-8cee-691cfefd8069' # str | Unique correlation Id in a GUID format
    mark_edelivered = True # bool | The parameter for marked e-delivered (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieves the PDF file for a single 1099 by form id.
        api_response = api_instance.get1099_form_pdf(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form_pdf: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves the PDF file for a single 1099 by form id.
        api_response = api_instance.get1099_form_pdf(id, avalara_version, x_correlation_id, mark_edelivered=mark_edelivered)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **mark_edelivered** | **bool**| The parameter for marked e-delivered | [optional]

### Return type

[**FormResponseBase**](FormResponseBase.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list1099_forms**
> Form1099List list1099_forms(avalara_version, x_correlation_id)

Retrieves a list of 1099 forms based on query parameters.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Form1099List
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    avalara_version = '2.0' # str | API version
    x_correlation_id = '4b177bbc-0a5b-4761-8b09-a6319700daf1' # str | Unique correlation Id in a GUID format
    filter = 'filter_example' # str | A filter statement to identify specific records to retrieve. For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>.    Collections support filtering only on certain fields. An attempt to filter on an unsupported field will receive a 400 Bad Request response.    Supported filtering fields are as follows:        issuerId      issuerReferenceId      taxYear      addressVerificationStatus - possible values are: unknown, pending, failed, incomplete, unchanged, verified      createdAt      edeliveryStatus - possible values are: sent, unscheduled, bad_verify, bad_verify_limit, scheduled, bounced, accepted      email      federalEfileStatus - possible values are: unscheduled, scheduled, sent, corrected_scheduled, accepted, corrected, corrected_accepted, held      firstPayeeName      mailStatus - possible values are: sent, unscheduled, pending, delivered      referenceId      tinMatchStatus - possible values are: none, pending, matched, failed      type - possible values are: 940, 941, 943, 944, 945, 1042, 1042-S, 1095-B, 1095-C, 1097-BTC, 1098, 1098-C, 1098-E, 1098-Q, 1098-T, 3921, 3922, 5498, 5498-ESA, 5498-SA, 1099-MISC, 1099-A, 1099-B, 1099-C, 1099-CAP, 1099-DIV, 1099-G, 1099-INT, 1099-K, 1099-LS, 1099-LTC, 1099-NEC, 1099-OID, 1099-PATR, 1099-Q, 1099-R, 1099-S, 1099-SA, T4A, W-2, W-2G, 1099-HC      updatedAt      validity - possible values are: true, false (optional)
    top = 10 # int | If nonzero, return no more than this number of results.     Used with skip to provide pagination for large datasets.     Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional) if omitted the server will use the default value of 10
    skip = 0 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional) if omitted the server will use the default value of 0
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example issuerReferenceId ASC.    Supported sorting fields are:         issuerReferenceId       taxYear       createdAt       firstPayeeName      updatedAt (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieves a list of 1099 forms based on query parameters.
        api_response = api_instance.list1099_forms(avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->list1099_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves a list of 1099 forms based on query parameters.
        api_response = api_instance.list1099_forms(avalara_version, x_correlation_id, filter=filter, top=top, skip=skip, order_by=order_by)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->list1099_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **filter** | **str**| A filter statement to identify specific records to retrieve. For more information on filtering, see &lt;a href&#x3D;\&quot;https://developer.avalara.com/avatax/filtering-in-rest/\&quot;&gt;Filtering in REST&lt;/a&gt;.    Collections support filtering only on certain fields. An attempt to filter on an unsupported field will receive a 400 Bad Request response.    Supported filtering fields are as follows:        issuerId      issuerReferenceId      taxYear      addressVerificationStatus - possible values are: unknown, pending, failed, incomplete, unchanged, verified      createdAt      edeliveryStatus - possible values are: sent, unscheduled, bad_verify, bad_verify_limit, scheduled, bounced, accepted      email      federalEfileStatus - possible values are: unscheduled, scheduled, sent, corrected_scheduled, accepted, corrected, corrected_accepted, held      firstPayeeName      mailStatus - possible values are: sent, unscheduled, pending, delivered      referenceId      tinMatchStatus - possible values are: none, pending, matched, failed      type - possible values are: 940, 941, 943, 944, 945, 1042, 1042-S, 1095-B, 1095-C, 1097-BTC, 1098, 1098-C, 1098-E, 1098-Q, 1098-T, 3921, 3922, 5498, 5498-ESA, 5498-SA, 1099-MISC, 1099-A, 1099-B, 1099-C, 1099-CAP, 1099-DIV, 1099-G, 1099-INT, 1099-K, 1099-LS, 1099-LTC, 1099-NEC, 1099-OID, 1099-PATR, 1099-Q, 1099-R, 1099-S, 1099-SA, T4A, W-2, W-2G, 1099-HC      updatedAt      validity - possible values are: true, false | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.     Used with skip to provide pagination for large datasets.     Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional] if omitted the server will use the default value of 10
 **skip** | **int**| If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. | [optional] if omitted the server will use the default value of 0
 **order_by** | **str**| A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example issuerReferenceId ASC.    Supported sorting fields are:         issuerReferenceId       taxYear       createdAt       firstPayeeName      updatedAt | [optional]

### Return type

[**Form1099List**](Form1099List.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update1099_form**
> FormResponseBase update1099_form(id, avalara_version, x_correlation_id)

Updates a 1099 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
IUpdateForm1099Request
FormResponseBase
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
    api_instance = forms1099_api.Forms1099Api(api_client)
    id = 'id_example' # str | 
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'c15eef59-ae3f-4cc9-975f-6dc1e90c0a88' # str | Unique correlation Id in a GUID format
    i_update_form1099_request = Avalara.SDK.IUpdateForm1099Request() # IUpdateForm1099Request |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Updates a 1099 form.
        api_response = api_instance.update1099_form(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->update1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a 1099 form.
        api_response = api_instance.update1099_form(id, avalara_version, x_correlation_id, i_update_form1099_request=i_update_form1099_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->update1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **i_update_form1099_request** | [**IUpdateForm1099Request**](IUpdateForm1099Request.md)|  | [optional]

### Return type

[**FormResponseBase**](FormResponseBase.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

