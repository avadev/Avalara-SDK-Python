# Avalara.SDK.CompaniesW9Api

All URIs are relative to *https://api-ava1099.eta.sbx.us-east-1.aws.avalara.io/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company**](CompaniesW9Api.md#create_company) | **POST** /w9/companies | Creates a new company
[**delete_company**](CompaniesW9Api.md#delete_company) | **DELETE** /w9/companies/{id} | Deletes a company
[**get_companies**](CompaniesW9Api.md#get_companies) | **GET** /w9/companies | List companies
[**get_company**](CompaniesW9Api.md#get_company) | **GET** /w9/companies/{id} | Retrieve a company
[**update_company**](CompaniesW9Api.md#update_company) | **PUT** /w9/companies/{id} | Update a company


# **create_company**
> CompanyResponseModel create_company(avalara_version)

Creates a new company

Creates a new company

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import companies_w9_api
CompanyResponseModel
CompanyCreateUpdateRequestModel
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
    api_instance = companies_w9_api.CompaniesW9Api(api_client)
    avalara_version = '2.0' # str | API version
    x_correlation_id = '25acab19-7c21-4b00-84c0-376ded0f3e95' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    company_create_update_request_model = Avalara.SDK.CompanyCreateUpdateRequestModel() # CompanyCreateUpdateRequestModel | The company to create (optional)
    # example passing only required values which don't have defaults set
    try:
        # Creates a new company
        api_response = api_instance.create_company(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->create_company: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new company
        api_response = api_instance.create_company(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, company_create_update_request_model=company_create_update_request_model)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->create_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **company_create_update_request_model** | [**CompanyCreateUpdateRequestModel**](CompanyCreateUpdateRequestModel.md)| The company to create | [optional]

### Return type

[**CompanyResponseModel**](CompanyResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created company |  -  |
**400** | Bad request (e.g., model validation failed) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_company**
> delete_company(id, avalara_version)

Deletes a company

Deletes a company

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import companies_w9_api
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
    api_instance = companies_w9_api.CompaniesW9Api(api_client)
    id = 'id_example' # str | The company to delete
    avalara_version = '2.0' # str | API version
    x_correlation_id = '55124ac1-2398-4a89-a8c3-80318b0598b0' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Deletes a company
        api_instance.delete_company(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->delete_company: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a company
        api_instance.delete_company(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->delete_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The company to delete |
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
**204** | Company deleted |  -  |
**401** | Authentication failed. |  -  |
**404** | Company was not found or your user does not have to permission to delete it. |  -  |
**409** | Company can&#39;t be deleted since it still have forms associated with it. |  -  |
**500** | An error happened while attempting to delete the company. |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_companies**
> PaginatedQueryResultModelCompanyResponse get_companies(avalara_version)

List companies

List existing companies. Filterable/Sortable fields are: \"name\", \"referenceId\", \"group.name\", \"createdAt\" and \"updatedAt\".

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import companies_w9_api
PaginatedQueryResultModelCompanyResponse
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
    api_instance = companies_w9_api.CompaniesW9Api(api_client)
    avalara_version = '2.0' # str | API version
    filter = 'filter_example' # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 56 # int | If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. (optional)
    skip = 56 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional)
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | If true, return the global count of elements in the collection. (optional)
    count_only = True # bool | If true, return ONLY the global count of elements in the collection.  It only applies when count=true. (optional)
    x_correlation_id = 'bd6be5ac-f793-4dd7-9aae-b8d2482663f9' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # List companies
        api_response = api_instance.get_companies(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->get_companies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List companies
        api_response = api_instance.get_companies(avalara_version, filter=filter, top=top, skip=skip, order_by=order_by, count=count, count_only=count_only, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->get_companies: %s\n" % e)
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

[**PaginatedQueryResultModelCompanyResponse**](PaginatedQueryResultModelCompanyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of companies |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_company**
> CompanyResponse get_company(id, avalara_version)

Retrieve a company

Retrieve an existing company

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import companies_w9_api
CompanyResponse
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
    api_instance = companies_w9_api.CompaniesW9Api(api_client)
    id = 'id_example' # str | Id of the company
    avalara_version = '2.0' # str | API version
    x_correlation_id = '64e6674f-d459-4bc1-b82a-f7baecd188a5' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a company
        api_response = api_instance.get_company(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->get_company: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a company
        api_response = api_instance.get_company(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the company |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**CompanyResponse**](CompanyResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single company |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**404** | Company not found |  -  |
**500** | Server Error |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_company**
> CompanyResponseModel update_company(id, avalara_version)

Update a company

Update a company

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import companies_w9_api
CompanyResponseModel
CompanyCreateUpdateRequestModel
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
    api_instance = companies_w9_api.CompaniesW9Api(api_client)
    id = 'id_example' # str | The ID of the company to update
    avalara_version = '2.0' # str | API version
    x_correlation_id = 'd81f2a70-6221-4b5d-88d2-d11388dd1568' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    company_create_update_request_model = Avalara.SDK.CompanyCreateUpdateRequestModel() # CompanyCreateUpdateRequestModel | The updated company data (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a company
        api_response = api_instance.update_company(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->update_company: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a company
        api_response = api_instance.update_company(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, company_create_update_request_model=company_create_update_request_model)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesW9Api->update_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the company to update |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **company_create_update_request_model** | [**CompanyCreateUpdateRequestModel**](CompanyCreateUpdateRequestModel.md)| The updated company data | [optional]

### Return type

[**CompanyResponseModel**](CompanyResponseModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated company |  -  |
**400** | Bad request (e.g., model validation failed) |  -  |
**401** | Authentication failed |  -  |
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

