# Avalara.SDK.Forms1099Api

All URIs are relative to *https://api.sbx.avalara.com/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_upsert1099_forms**](Forms1099Api.md#bulk_upsert1099_forms) | **POST** /1099/forms/$bulk-upsert | Create or update multiple 1099/1095/W2/1042S forms
[**create1099_form**](Forms1099Api.md#create1099_form) | **POST** /1099/forms | Create a 1099/1095/W2/1042S form
[**delete1099_form**](Forms1099Api.md#delete1099_form) | **DELETE** /1099/forms/{id} | Delete a 1099/1095/W2/1042S form
[**get1099_form**](Forms1099Api.md#get1099_form) | **GET** /1099/forms/{id} | Retrieve a 1099/1095/W2/1042S form
[**get1099_form_pdf**](Forms1099Api.md#get1099_form_pdf) | **GET** /1099/forms/{id}/pdf | Retrieve the PDF file for a 1099/1095/W2/1042S form
[**list1099_forms**](Forms1099Api.md#list1099_forms) | **GET** /1099/forms | List 1099/1095/W2/1042S forms
[**update1099_form**](Forms1099Api.md#update1099_form) | **PUT** /1099/forms/{id} | Update a 1099/1095/W2/1042S form


# **bulk_upsert1099_forms**
> JobResponse bulk_upsert1099_forms(avalara_version)

Create or update multiple 1099/1095/W2/1042S forms

This endpoint allows you to create or update multiple 1099/1095/W2/1042S forms.  Maximum of 5000 forms can be processed in a single bulk request.    **Date Scheduling Rules:**    If federalEfileDate, stateEfileDate, or recipientEdeliveryDate are between current date and beginning of blackout period, scheduled to that date.  If dates are in the past or blackout period, scheduled to next available date.  For blackout period information, see https://www.track1099.com/info/IRS_info.  StateEfileDate must be on or after federalEfileDate.  Set dates to null to leave unscheduled.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Form1099ListRequest
JobResponse
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
    avalara_version = '2.0.0' # str | API version
    dry_run = False # bool | defaults to false. If true, it will NOT change the DB. It will just return a report of what would've have been changed in the DB (optional) if omitted the server will use the default value of False
    x_correlation_id = 'eec0b095-bfa8-4786-bbad-3f20a4b61ac2' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    form1099_list_request = {"type":"1042-S","forms":[{"type":"1042-S","issuerId":"12345","issuerReferenceId":"issuer-001","issuerTin":"94-2765431","taxYear":2024,"referenceId":"1042S-REF-001","tin":"112233445","recipientName":"Michael Jackson","recipientSecondName":"SuperStart","address":"1234 Corporate Blvd","address2":"Suite 500","city":"Anytown","state":"MA","zip":"12345","email":"email@example.com","accountNumber":"ACC01","nonUsProvince":null,"countryCode":"US","federalEfileDate":"2024-03-15","postalMail":true,"stateEfileDate":null,"recipientEdeliveryDate":"2024-03-25","tinMatch":false,"noTin":false,"addressVerification":true,"stateAndLocalWithholding":{"stateTaxWithheld":50,"state":"CA","stateIdNumber":"CA98765432"},"secondTinNotice":true,"uniqueFormId":"1234567890","recipientDateOfBirth":"1990-01-01","recipientGiin":"748291.59302.US.001","recipientForeignTin":"920456.38475.GM.002","lobCode":"06","incomeCode":"16","grossIncome":10000.5,"withholdingIndicator":"3","taxCountryCode":"GM","exemptionCodeChap3":"00","exemptionCodeChap4":"13","taxRateChap3":"30.00","withholdingAllowance":15,"federalTaxWithheld":1500.25,"taxNotDepositedIndicator":true,"academicIndicator":true,"taxWithheldOtherAgents":100,"amountRepaid":200,"taxPaidAgent":50.5,"chap3StatusCode":"06","chap4StatusCode":"02","primaryWithholdingAgent":{"name":"Primary Agent Name","ein":"98-3456789"},"intermediaryOrFlowThrough":{"ein":"98-7654321","chap3StatusCode":"03","chap4StatusCode":"04","name":"Intermediary Name","giin":"748291.59302.US.002","countryCode":"US","foreignTin":"123-45-6789","address":"123 Main St.","city":"Cityville","state":"CA","zip":"98765"}}]} # Form1099ListRequest |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create or update multiple 1099/1095/W2/1042S forms
        api_response = api_instance.bulk_upsert1099_forms(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->bulk_upsert1099_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update multiple 1099/1095/W2/1042S forms
        api_response = api_instance.bulk_upsert1099_forms(avalara_version, dry_run=dry_run, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, form1099_list_request=form1099_list_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->bulk_upsert1099_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **dry_run** | **bool**| defaults to false. If true, it will NOT change the DB. It will just return a report of what would&#39;ve have been changed in the DB | [optional] if omitted the server will use the default value of False
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **form1099_list_request** | [**Form1099ListRequest**](Form1099ListRequest.md)|  | [optional]

### Return type

[**JobResponse**](JobResponse.md)

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
> Get1099Form200Response create1099_form(avalara_version)

Create a 1099/1095/W2/1042S form

Create a 1099/1095/W2/1042S form.    **Date Scheduling Rules:**    If federalEfileDate, stateEfileDate, or recipientEdeliveryDate are between current date and beginning of blackout period, scheduled to that date.  If dates are in the past or blackout period, scheduled to next available date.  For blackout period information, see https://www.track1099.com/info/IRS_info.  StateEfileDate must be on or after federalEfileDate.  Set dates to null to leave unscheduled.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Get1099Form200Response
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
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'ea80e3d4-6198-4297-9fff-4b12b5d270a0' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    get1099_form200_response = {"type":"1042-S","issuerId":"12345","referenceId":"1042S-REF-001","tin":"112233445","recipientName":"Michael Jackson","recipientSecondName":"SuperStart","address":"1234 Corporate Blvd","address2":"Suite 500","city":"Anytown","state":"MA","zip":"12345","email":"email@example.com","accountNumber":"ACC01","nonUsProvince":null,"countryCode":"US","federalEfileDate":"2024-03-15","postalMail":true,"stateEfileDate":null,"recipientEdeliveryDate":"2024-03-25","tinMatch":false,"noTin":false,"addressVerification":true,"stateAndLocalWithholding":{"stateTaxWithheld":50,"state":"CA","stateIdNumber":"CA98765432"},"secondTinNotice":true,"uniqueFormId":"1234567890","recipientDateOfBirth":"1990-01-01","recipientGiin":"748291.59302.US.001","recipientForeignTin":"920456.38475.GM.002","lobCode":"06","incomeCode":"16","grossIncome":10000.5,"withholdingIndicator":"3","taxCountryCode":"GM","exemptionCodeChap3":"00","exemptionCodeChap4":"13","taxRateChap3":"30.00","withholdingAllowance":15,"federalTaxWithheld":1500.25,"taxNotDepositedIndicator":true,"academicIndicator":true,"taxWithheldOtherAgents":100,"amountRepaid":200,"taxPaidAgent":50.5,"chap3StatusCode":"06","chap4StatusCode":"02","primaryWithholdingAgent":{"name":"Primary Agent Name","ein":"98-3456789"},"intermediaryOrFlowThrough":{"ein":"98-7654321","chap3StatusCode":"03","chap4StatusCode":"04","name":"Intermediary Name","giin":"748291.59302.US.002","countryCode":"US","foreignTin":"123-45-6789","address":"123 Main St.","city":"Cityville","state":"CA","zip":"98765"}} # Get1099Form200Response |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create a 1099/1095/W2/1042S form
        api_response = api_instance.create1099_form(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->create1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 1099/1095/W2/1042S form
        api_response = api_instance.create1099_form(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, get1099_form200_response=get1099_form200_response)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->create1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **get1099_form200_response** | [**Get1099Form200Response**](Get1099Form200Response.md)|  | [optional]

### Return type

[**Get1099Form200Response**](Get1099Form200Response.md)

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
> delete1099_form(id, avalara_version)

Delete a 1099/1095/W2/1042S form

Delete a 1099/1095/W2/1042S form.

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
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '6f61d545-12cb-445a-b60c-bd21c3f78ae3' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Delete a 1099/1095/W2/1042S form
        api_instance.delete1099_form(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->delete1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a 1099/1095/W2/1042S form
        api_instance.delete1099_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->delete1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the desired form to delete. |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

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
> Get1099Form200Response get1099_form(id, avalara_version)

Retrieve a 1099/1095/W2/1042S form

Retrieve a 1099/1095/W2/1042S form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Get1099Form200Response
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
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '3dda6df9-8f00-4ac0-8eab-0e56263c2895' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a 1099/1095/W2/1042S form
        api_response = api_instance.get1099_form(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a 1099/1095/W2/1042S form
        api_response = api_instance.get1099_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**Get1099Form200Response**](Get1099Form200Response.md)

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
> bytearray get1099_form_pdf(id, avalara_version)

Retrieve the PDF file for a 1099/1095/W2/1042S form

Retrieve the PDF file for a 1099/1095/W2/1042S form.

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
    id = 'id_example' # str | The ID of the form
    avalara_version = '2.0.0' # str | API version
    mark_edelivered = True # bool | Optional boolean that if set indicates that the form should be marked as having been successfully edelivered (optional)
    x_correlation_id = '83471033-6587-4425-a03e-1057de8d14cf' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieve the PDF file for a 1099/1095/W2/1042S form
        api_response = api_instance.get1099_form_pdf(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form_pdf: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the PDF file for a 1099/1095/W2/1042S form
        api_response = api_instance.get1099_form_pdf(id, avalara_version, mark_edelivered=mark_edelivered, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->get1099_form_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the form |
 **avalara_version** | **str**| API version |
 **mark_edelivered** | **bool**| Optional boolean that if set indicates that the form should be marked as having been successfully edelivered | [optional]
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

**bytearray**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json


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
> PaginatedQueryResultModelForm1099Base list1099_forms(avalara_version)

List 1099/1095/W2/1042S forms

List 1099/1095/W2/1042S forms.                Collections support filtering only on certain fields. An attempt to filter on an unsupported field will receive a 400 Bad Request response.                Supported filtering fields are as follows:                - issuerId  - issuerReferenceId  - taxYear  - addressVerificationStatus - possible values are: unknown, pending, failed, incomplete, unchanged, verified  - createdAt  - edeliveryStatus - possible values are: sent, unscheduled, bad_verify, bad_verify_limit, scheduled, bounced, accepted  - email  - federalEfileStatus - possible values are: unscheduled, scheduled, sent, corrected_scheduled, accepted, corrected, corrected_accepted, held  - recipientName  - mailStatus - possible values are: sent, unscheduled, pending, delivered  - referenceId  - tinMatchStatus - possible values are: none, pending, matched, failed  - type - possible values are: 940, 941, 943, 944, 945, 1042, 1042-S, 1095-B, 1095-C, 1097-BTC, 1098, 1098-C, 1098-E, 1098-Q, 1098-T, 3921, 3922, 5498, 5498-ESA, 5498-SA, 1099-MISC, 1099-A, 1099-B, 1099-C, 1099-CAP, 1099-DIV, 1099-G, 1099-INT, 1099-K, 1099-LS, 1099-LTC, 1099-NEC, 1099-OID, 1099-PATR, 1099-Q, 1099-R, 1099-S, 1099-SA, T4A, W-2, W-2G, 1099-HC  - updatedAt  - validity - possible values are: true, false                For more information on filtering, see <see href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</see>.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
PaginatedQueryResultModelForm1099Base
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
    avalara_version = '2.0.0' # str | API version
    filter = 'issuerId eq 884781823' # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 56 # int | If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. (optional)
    skip = 56 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional)
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | If true, return the global count of elements in the collection. (optional)
    count_only = True # bool | If true, return ONLY the global count of elements in the collection.  It only applies when count=true. (optional)
    x_correlation_id = '9cd2b713-72ed-419c-8c1f-4aeef9f6b0d4' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # List 1099/1095/W2/1042S forms
        api_response = api_instance.list1099_forms(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->list1099_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List 1099/1095/W2/1042S forms
        api_response = api_instance.list1099_forms(avalara_version, filter=filter, top=top, skip=skip, order_by=order_by, count=count, count_only=count_only, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->list1099_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see &lt;a href&#x3D;\&quot;https://developer.avalara.com/avatax/filtering-in-rest/\&quot;&gt;Filtering in REST&lt;/a&gt;. | [optional]
 **top** | **int**| If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. | [optional]
 **count** | **bool**| If true, return the global count of elements in the collection. | [optional]
 **count_only** | **bool**| If true, return ONLY the global count of elements in the collection.  It only applies when count&#x3D;true. | [optional]
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**PaginatedQueryResultModelForm1099Base**](PaginatedQueryResultModelForm1099Base.md)

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
> Get1099Form200Response update1099_form(id, avalara_version)

Update a 1099/1095/W2/1042S form

Update a 1099/1095/W2/1042S form.    **Date Update Rules:**    Possible to update scheduled dates (same validation rules apply).  Cannot change from scheduled to unscheduled status - must delete form and create new one.  If dates are between current date and blackout period, scheduled to that date.  If dates are in past or blackout period, scheduled to next available date.  For blackout period information, see https://www.track1099.com/info/IRS_info.  StateEfileDate must be on or after federalEfileDate.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms1099_api
Get1099Form200Response
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
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'b0bb9771-ffdf-4884-bac3-7cf00bf7c745' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    get1099_form200_response = {"type":"1042-S","issuerId":"12345","referenceId":"1042S-REF-001","tin":"112233445","recipientName":"Michael Jackson","recipientSecondName":"SuperStart","address":"1234 Corporate Blvd","address2":"Suite 500","city":"Anytown","state":"MA","zip":"12345","email":"email@example.com","accountNumber":"ACC01","nonUsProvince":null,"countryCode":"US","federalEfileDate":"2024-03-15","postalMail":true,"stateEfileDate":null,"recipientEdeliveryDate":"2024-03-25","tinMatch":false,"noTin":false,"addressVerification":true,"stateAndLocalWithholding":{"stateTaxWithheld":50,"state":"CA","stateIdNumber":"CA98765432"},"secondTinNotice":true,"uniqueFormId":"1234567890","recipientDateOfBirth":"1990-01-01","recipientGiin":"748291.59302.US.001","recipientForeignTin":"920456.38475.GM.002","lobCode":"06","incomeCode":"16","grossIncome":10000.5,"withholdingIndicator":"3","taxCountryCode":"GM","exemptionCodeChap3":"00","exemptionCodeChap4":"13","taxRateChap3":"30.00","withholdingAllowance":15,"federalTaxWithheld":1500.25,"taxNotDepositedIndicator":true,"academicIndicator":true,"taxWithheldOtherAgents":100,"amountRepaid":200,"taxPaidAgent":50.5,"chap3StatusCode":"06","chap4StatusCode":"02","primaryWithholdingAgent":{"name":"Primary Agent Name","ein":"98-3456789"},"intermediaryOrFlowThrough":{"ein":"98-7654321","chap3StatusCode":"03","chap4StatusCode":"04","name":"Intermediary Name","giin":"748291.59302.US.002","countryCode":"US","foreignTin":"123-45-6789","address":"123 Main St.","city":"Cityville","state":"CA","zip":"98765"}} # Get1099Form200Response |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a 1099/1095/W2/1042S form
        api_response = api_instance.update1099_form(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->update1099_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 1099/1095/W2/1042S form
        api_response = api_instance.update1099_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, get1099_form200_response=get1099_form200_response)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Forms1099Api->update1099_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **get1099_form200_response** | [**Get1099Form200Response**](Get1099Form200Response.md)|  | [optional]

### Return type

[**Get1099Form200Response**](Get1099Form200Response.md)

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

