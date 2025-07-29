# Avalara.SDK.FormsW9Api

All URIs are relative to *https://api-ava1099.eta.sbx.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_w9_form**](FormsW9Api.md#create_w9_form) | **POST** /w9/forms | Create a W9/W4/W8 form
[**delete_w9_form**](FormsW9Api.md#delete_w9_form) | **DELETE** /w9/forms/{id} | Delete a W9/W4/W8 form
[**get_w9_form**](FormsW9Api.md#get_w9_form) | **GET** /w9/forms/{id} | Retrieve a W9/W4/W8 form
[**list_w9_forms**](FormsW9Api.md#list_w9_forms) | **GET** /w9/forms | List W9/W4/W8 forms
[**send_w9_form_email**](FormsW9Api.md#send_w9_form_email) | **POST** /w9/forms/{id}/$send-email | Send an email to the vendor/payee requesting they fill out a W9/W4/W8 form
[**update_w9_form**](FormsW9Api.md#update_w9_form) | **PUT** /w9/forms/{id} | Update a W9/W4/W8 form
[**upload_w9_files**](FormsW9Api.md#upload_w9_files) | **POST** /w9/forms/{id}/attachment | Replace the PDF file for a W9/W4/W8 form


# **create_w9_form**
> CreateW9Form201Response create_w9_form(avalara_version)

Create a W9/W4/W8 form

Create a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
CreateW9FormRequest
CreateW9Form201Response
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '968b9850-b859-4a5a-8165-bd1e444fbf47' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    create_w9_form_request = {"type":"W9","name":"John Doe","businessName":"Acme Inc.","businessClassification":"Individual","businessOther":null,"foreignPartnerOwnerOrBeneficiary":false,"exemptPayeeCode":null,"exemptFatcaCode":null,"foreignCountryIndicator":false,"address":"123 Main St.","foreignAddress":null,"city":"Anytown","state":"CA","zip":"12345","accountNumber":null,"tinType":"SSN","tin":"543456789","backupWithholding":false,"is1099able":true,"companyId":"32553266","referenceId":null,"email":null,"eDeliveryConsentedAt":null,"signature":null} # CreateW9FormRequest | Form to be created (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create a W9/W4/W8 form
        api_response = api_instance.create_w9_form(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->create_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a W9/W4/W8 form
        api_response = api_instance.create_w9_form(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, create_w9_form_request=create_w9_form_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->create_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **create_w9_form_request** | [**CreateW9FormRequest**](CreateW9FormRequest.md)| Form to be created | [optional]

### Return type

[**CreateW9Form201Response**](CreateW9Form201Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created W9/W4/W8 form |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_w9_form**
> delete_w9_form(id, avalara_version)

Delete a W9/W4/W8 form

Delete a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
ErrorModel
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    id = 'id_example' # str | ID of the form to delete
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '69926298-ed5b-4d78-8099-b5488589912d' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Delete a W9/W4/W8 form
        api_instance.delete_w9_form(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->delete_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a W9/W4/W8 form
        api_instance.delete_w9_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->delete_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the form to delete |
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
**204** | Empty response |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_w9_form**
> CreateW9Form201Response get_w9_form(id, avalara_version)

Retrieve a W9/W4/W8 form

Retrieve a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
CreateW9Form201Response
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    id = 'id_example' # str | ID of the form
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'e138390c-5561-49df-a969-49427e2c5ffa' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a W9/W4/W8 form
        api_response = api_instance.get_w9_form(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->get_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a W9/W4/W8 form
        api_response = api_instance.get_w9_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->get_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the form |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**CreateW9Form201Response**](CreateW9Form201Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | W9/W4/W8 form with id |  -  |
**401** | Authentication failed |  -  |
**404** | W9/W4/W8 form not found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_w9_forms**
> PaginatedW9FormsModel list_w9_forms(avalara_version)

List W9/W4/W8 forms

List W9/W4/W8 forms.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
ErrorModel
PaginatedW9FormsModel
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    avalara_version = '2.0.0' # str | API version
    filter = 'filter_example' # str | A filter statement to identify specific records to retrieve. For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 10 # int | If nonzero, return no more than this number of results. Used with skip to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional) if omitted the server will use the default value of 10
    skip = 0 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional) if omitted the server will use the default value of 0
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | When true, returns a @recordSetCount in the result set (optional)
    x_correlation_id = 'f80bd20b-84ec-47de-913f-304dd9951b58' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # List W9/W4/W8 forms
        api_response = api_instance.list_w9_forms(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->list_w9_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List W9/W4/W8 forms
        api_response = api_instance.list_w9_forms(avalara_version, filter=filter, top=top, skip=skip, order_by=order_by, count=count, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->list_w9_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **filter** | **str**| A filter statement to identify specific records to retrieve. For more information on filtering, see &lt;a href&#x3D;\&quot;https://developer.avalara.com/avatax/filtering-in-rest/\&quot;&gt;Filtering in REST&lt;/a&gt;. | [optional]
 **top** | **int**| If nonzero, return no more than this number of results. Used with skip to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional] if omitted the server will use the default value of 10
 **skip** | **int**| If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. | [optional] if omitted the server will use the default value of 0
 **order_by** | **str**| A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. | [optional]
 **count** | **bool**| When true, returns a @recordSetCount in the result set | [optional]
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**PaginatedW9FormsModel**](PaginatedW9FormsModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of forms |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_w9_form_email**
> IW9FormDataModelsOneOf send_w9_form_email(id, avalara_version)

Send an email to the vendor/payee requesting they fill out a W9/W4/W8 form

Send an email to the vendor/payee requesting they fill out a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
IW9FormDataModelsOneOf
ErrorModel
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    id = 'id_example' # str | The ID of the W9/W4/W8 form.
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '75735dc9-2909-4f11-bc6c-6e1ec0d77264' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Send an email to the vendor/payee requesting they fill out a W9/W4/W8 form
        api_response = api_instance.send_w9_form_email(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->send_w9_form_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send an email to the vendor/payee requesting they fill out a W9/W4/W8 form
        api_response = api_instance.send_w9_form_email(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->send_w9_form_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the W9/W4/W8 form. |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**IW9FormDataModelsOneOf**](IW9FormDataModelsOneOf.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated W9/W4/W8 form |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_w9_form**
> IW9FormDataModelsOneOf update_w9_form(id, avalara_version)

Update a W9/W4/W8 form

Update a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
IW9FormDataModelsOneOf
ErrorModel
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    id = 'id_example' # str | ID of the form to update
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'd24784a4-9522-46c7-b6e0-8f44cb176f17' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    iw9_form_data_models_one_of = Avalara.SDK.IW9FormDataModelsOneOf() # IW9FormDataModelsOneOf | Form to be updated (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a W9/W4/W8 form
        api_response = api_instance.update_w9_form(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->update_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a W9/W4/W8 form
        api_response = api_instance.update_w9_form(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, iw9_form_data_models_one_of=iw9_form_data_models_one_of)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->update_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the form to update |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **iw9_form_data_models_one_of** | [**IW9FormDataModelsOneOf**](IW9FormDataModelsOneOf.md)| Form to be updated | [optional]

### Return type

[**IW9FormDataModelsOneOf**](IW9FormDataModelsOneOf.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated W9/W4/W8 form |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_w9_files**
> upload_w9_files(id, avalara_version)

Replace the PDF file for a W9/W4/W8 form

Replaces the PDF file for a W9/W4/W8 form.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
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
    api_instance = forms_w9_api.FormsW9Api(api_client)
    id = 'id_example' # str | Id of the form
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = 'ee2e9278-6cdb-47ad-82a0-9d5a726f7412' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    file = None # bytearray |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Replace the PDF file for a W9/W4/W8 form
        api_instance.upload_w9_files(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->upload_w9_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace the PDF file for a W9/W4/W8 form
        api_instance.upload_w9_files(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, file=file)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->upload_w9_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **file** | [**bytearray**](bytearray.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request (e.g., Only .pdf files are allowed.) |  -  |
**401** | Authentication failed |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

