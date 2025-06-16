# Avalara.SDK.FormsW9Api

All URIs are relative to *https://api-ava1099.eta.sbx.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_w9_form**](FormsW9Api.md#create_w9_form) | **POST** /w9/forms | Create a W9/W4/W8 form
[**delete_w9_form**](FormsW9Api.md#delete_w9_form) | **DELETE** /w9/forms/{id} | Delete a form
[**get_w9_form**](FormsW9Api.md#get_w9_form) | **GET** /w9/forms/{id} | Retrieve a W9/W4/W8 form
[**get_w9_form_request**](FormsW9Api.md#get_w9_form_request) | **GET** /w9/forms/requests/{formRequestId} | Retrieve a form request
[**list_w9_forms**](FormsW9Api.md#list_w9_forms) | **GET** /w9/forms | List W9/W4/W8 forms.
[**send_w9_form_email**](FormsW9Api.md#send_w9_form_email) | **POST** /w9/forms/{id}/$send-email | Sends a W9 email request to a vendor/payee
[**update_w9_form**](FormsW9Api.md#update_w9_form) | **PUT** /w9/forms/{id} | Update a W9/W4/W8 form
[**upload_w9_files**](FormsW9Api.md#upload_w9_files) | **PUT** /w9/forms/{id}/attachment | Upload files for a W9/W4/W8 form


# **create_w9_form**
> IW9FormDataModelsOneOf create_w9_form(avalara_version, x_correlation_id)

Create a W9/W4/W8 form

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
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'b5a0f20a-5d1f-417e-95e6-33559d36bac0' # str | Unique correlation Id in a GUID format
    iw9_form_data_models_one_of = Avalara.SDK.IW9FormDataModelsOneOf() # IW9FormDataModelsOneOf | Form to be created (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create a W9/W4/W8 form
        api_response = api_instance.create_w9_form(avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->create_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a W9/W4/W8 form
        api_response = api_instance.create_w9_form(avalara_version, x_correlation_id, iw9_form_data_models_one_of=iw9_form_data_models_one_of)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->create_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **iw9_form_data_models_one_of** | [**IW9FormDataModelsOneOf**](IW9FormDataModelsOneOf.md)| Form to be created | [optional]

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
**200** | The created W9/W4/W8 form |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_w9_form**
> delete_w9_form(id, avalara_version, x_correlation_id)

Delete a form

Delete a form

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
    id = 'id_example' # str | Id of the form to delete
    avalara_version = '2.0' # str | API version
    x_correlation_id = '6f87d641-f8d8-48a5-ac3f-82743b9e6630' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Delete a form
        api_instance.delete_w9_form(id, avalara_version, x_correlation_id)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->delete_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form to delete |
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
**204** | Empty response |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_w9_form**
> IW9FormDataModelsOneOf get_w9_form(id, avalara_version, x_correlation_id)

Retrieve a W9/W4/W8 form

Retrieve a W9/W4/W8 form

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
IW9FormDataModelsOneOf
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
    avalara_version = '2.0' # str | API version
    x_correlation_id = '181b84d8-aaf7-4cca-a34a-25de5e03efaa' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a W9/W4/W8 form
        api_response = api_instance.get_w9_form(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->get_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |

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
**200** | W9/W4/W8 form with id |  -  |
**401** | Authentication failed |  -  |
**404** | W9/W4/W8 form not found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_w9_form_request**
> FormRequestModel get_w9_form_request(form_request_id, avalara_version, x_correlation_id)

Retrieve a form request

Retrieve a form request after creation: not likely to be useful except in testing. Previously-valid form requests will be Not Found after `expires_at`.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import forms_w9_api
FormRequestModel
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
    form_request_id = 'form_request_id_example' # str | 
    avalara_version = '2.0' # str | API version
    x_correlation_id = '57a2d900-6533-48eb-8c08-719f9819479f' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a form request
        api_response = api_instance.get_w9_form_request(form_request_id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->get_w9_form_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_request_id** | **str**|  |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |

### Return type

[**FormRequestModel**](FormRequestModel.md)

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_w9_forms**
> PaginatedW9FormsModel list_w9_forms(avalara_version, x_correlation_id)

List W9/W4/W8 forms.

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
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'a055ea07-d8e8-461d-8539-2b22312e4aa8' # str | Unique correlation Id in a GUID format
    filter = 'filter_example' # str | A filter statement to identify specific records to retrieve. For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 10 # int | If nonzero, return no more than this number of results. Used with skip to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional) if omitted the server will use the default value of 10
    skip = 0 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional) if omitted the server will use the default value of 0
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | When true, returns a @recordSetCount in the result set (optional)
    # example passing only required values which don't have defaults set
    try:
        # List W9/W4/W8 forms.
        api_response = api_instance.list_w9_forms(avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->list_w9_forms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List W9/W4/W8 forms.
        api_response = api_instance.list_w9_forms(avalara_version, x_correlation_id, filter=filter, top=top, skip=skip, order_by=order_by, count=count)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->list_w9_forms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **filter** | **str**| A filter statement to identify specific records to retrieve. For more information on filtering, see &lt;a href&#x3D;\&quot;https://developer.avalara.com/avatax/filtering-in-rest/\&quot;&gt;Filtering in REST&lt;/a&gt;. | [optional]
 **top** | **int**| If nonzero, return no more than this number of results. Used with skip to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional] if omitted the server will use the default value of 10
 **skip** | **int**| If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. | [optional] if omitted the server will use the default value of 0
 **order_by** | **str**| A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. | [optional]
 **count** | **bool**| When true, returns a @recordSetCount in the result set | [optional]

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
> IW9FormDataModelsOneOf send_w9_form_email(id, avalara_version, x_correlation_id)

Sends a W9 email request to a vendor/payee

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
    avalara_version = '2.0' # str | API version
    x_correlation_id = '8ddc6fda-24d1-470f-855c-82e0e02ef1c0' # str | Unique correlation Id in a GUID format
    # example passing only required values which don't have defaults set
    try:
        # Sends a W9 email request to a vendor/payee
        api_response = api_instance.send_w9_form_email(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->send_w9_form_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the W9/W4/W8 form. |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |

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
> IW9FormDataModelsOneOf update_w9_form(id, avalara_version, x_correlation_id)

Update a W9/W4/W8 form

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
    id = 'id_example' # str | Id of the form to update
    avalara_version = '2.0' # str | API version
    x_correlation_id = '4ccd8ec1-5cee-444f-bf11-890e2551b0a1' # str | Unique correlation Id in a GUID format
    iw9_form_data_models_one_of = Avalara.SDK.IW9FormDataModelsOneOf() # IW9FormDataModelsOneOf | Form to be updated (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a W9/W4/W8 form
        api_response = api_instance.update_w9_form(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->update_w9_form: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a W9/W4/W8 form
        api_response = api_instance.update_w9_form(id, avalara_version, x_correlation_id, iw9_form_data_models_one_of=iw9_form_data_models_one_of)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->update_w9_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form to update |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
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
> str upload_w9_files(id, avalara_version, x_correlation_id)

Upload files for a W9/W4/W8 form

Upload files for a W9/W4/W8 form

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
    id = 'id_example' # str | Id of the form
    avalara_version = '2.0' # str | API version
    x_correlation_id = '389f401a-494d-4cd8-9559-665ef1b6d46b' # str | Unique correlation Id in a GUID format
    file = None # bytearray |  (optional)
    # example passing only required values which don't have defaults set
    try:
        # Upload files for a W9/W4/W8 form
        api_response = api_instance.upload_w9_files(id, avalara_version, x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->upload_w9_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload files for a W9/W4/W8 form
        api_response = api_instance.upload_w9_files(id, avalara_version, x_correlation_id, file=file)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling FormsW9Api->upload_w9_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format |
 **file** | [**bytearray**](bytearray.md)|  | [optional]

### Return type

**str**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | W9/W4/W8 form with id |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

