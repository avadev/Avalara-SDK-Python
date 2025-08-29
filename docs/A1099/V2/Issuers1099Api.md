# Avalara.SDK.Issuers1099Api

All URIs are relative to *https://api.sbx.avalara.com/avalara1099*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issuer**](Issuers1099Api.md#create_issuer) | **POST** /1099/issuers | Create an issuer
[**delete_issuer**](Issuers1099Api.md#delete_issuer) | **DELETE** /1099/issuers/{id} | Delete an issuer
[**get_issuer**](Issuers1099Api.md#get_issuer) | **GET** /1099/issuers/{id} | Retrieve an issuer
[**get_issuers**](Issuers1099Api.md#get_issuers) | **GET** /1099/issuers | List issuers
[**update_issuer**](Issuers1099Api.md#update_issuer) | **PUT** /1099/issuers/{id} | Update an issuer


# **create_issuer**
> IssuerResponse create_issuer(avalara_version)

Create an issuer

Create an issuer (also known as a Payer).

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import issuers1099_api
CreateIssuerRequest
IssuerResponse
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
    api_instance = issuers1099_api.Issuers1099Api(api_client)
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '44b5fa45-dc8f-4939-9259-55c44e371c83' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    create_issuer_request = {"name":"Acme Corporation","dbaName":"Acme Widgets","tin":"94-2765431","referenceId":"issuer-001","telephone":"+1-555-123-4567","taxYear":2024,"countryCode":"US","email":"support@acmecorp.com","address":"123 Main Street","city":"San Francisco","state":"CA","zip":"94105","foreignProvince":"","transferAgentName":"","lastFiling":false} # CreateIssuerRequest | The issuer to create (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create an issuer
        api_response = api_instance.create_issuer(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->create_issuer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an issuer
        api_response = api_instance.create_issuer(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, create_issuer_request=create_issuer_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->create_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **create_issuer_request** | [**CreateIssuerRequest**](CreateIssuerRequest.md)| The issuer to create | [optional]

### Return type

[**IssuerResponse**](IssuerResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created issuer |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_issuer**
> delete_issuer(id, avalara_version)

Delete an issuer

Delete an issuer (also known as a Payer).

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import issuers1099_api
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
    api_instance = issuers1099_api.Issuers1099Api(api_client)
    id = 'id_example' # str | Id of the issuer to delete
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '18937e11-5cfa-4f80-b4ff-a8fdee349cf1' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Delete an issuer
        api_instance.delete_issuer(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->delete_issuer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an issuer
        api_instance.delete_issuer(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->delete_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the issuer to delete |
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

# **get_issuer**
> IssuerResponse get_issuer(id, avalara_version)

Retrieve an issuer

Retrieve an issuer (also known as a Payer).

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import issuers1099_api
IssuerResponse
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
    api_instance = issuers1099_api.Issuers1099Api(api_client)
    id = 'id_example' # str | Id of the issuer to retrieve
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '8e5147e0-a97c-47f5-9791-3ea7d3bf7f16' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # Retrieve an issuer
        api_response = api_instance.get_issuer(id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->get_issuer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve an issuer
        api_response = api_instance.get_issuer(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->get_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the issuer to retrieve |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]

### Return type

[**IssuerResponse**](IssuerResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single issuer |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_issuers**
> PaginatedQueryResultModelIssuerResponse get_issuers(avalara_version)

List issuers

List issuers (also known as Payers). Filterable fields are name, referenceId and taxYear.

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import issuers1099_api
PaginatedQueryResultModelIssuerResponse
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
    api_instance = issuers1099_api.Issuers1099Api(api_client)
    avalara_version = '2.0.0' # str | API version
    filter = 'taxYear eq 2024' # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see <a href=\"https://developer.avalara.com/avatax/filtering-in-rest/\">Filtering in REST</a>. (optional)
    top = 56 # int | If zero or greater than 1000, return at most 1000 results.  Otherwise, return this number of results.  Used with skip to provide pagination for large datasets. (optional)
    skip = 56 # int | If nonzero, skip this number of results before returning data. Used with top to provide pagination for large datasets. (optional)
    order_by = 'order_by_example' # str | A comma separated list of sort statements in the format (fieldname) [ASC|DESC], for example id ASC. (optional)
    count = True # bool | If true, return the global count of elements in the collection. (optional)
    count_only = True # bool | If true, return ONLY the global count of elements in the collection.  It only applies when count=true. (optional)
    x_correlation_id = 'da351fbb-2f00-42a7-8c6f-e3864f4bbf0c' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    # example passing only required values which don't have defaults set
    try:
        # List issuers
        api_response = api_instance.get_issuers(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->get_issuers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List issuers
        api_response = api_instance.get_issuers(avalara_version, filter=filter, top=top, skip=skip, order_by=order_by, count=count, count_only=count_only, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->get_issuers: %s\n" % e)
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

[**PaginatedQueryResultModelIssuerResponse**](PaginatedQueryResultModelIssuerResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of issuers |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**404** | Not Found |  -  |
**500** | Server Error |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_issuer**
> update_issuer(id, avalara_version)

Update an issuer

Update an issuer (also known as a Payer).

### Example

* Bearer Authentication (bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.A1099.V2 import issuers1099_api
CreateIssuerRequest
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
    api_instance = issuers1099_api.Issuers1099Api(api_client)
    id = 'id_example' # str | Id of the issuer to update
    avalara_version = '2.0.0' # str | API version
    x_correlation_id = '07298ef1-41b1-4610-9275-331b7ae88439' # str | Unique correlation Id in a GUID format (optional)
    x_avalara_client = 'Swagger UI; 22.1.0' # str | Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional)
    create_issuer_request = {"name":"Acme Corporation","dbaName":"Acme Widgets","tin":"94-2765431","referenceId":"issuer-001","telephone":"+1-555-123-4567","taxYear":2024,"countryCode":"US","email":"support@acmecorp.com","address":"123 Main Street","city":"San Francisco","state":"CA","zip":"94105","foreignProvince":"","transferAgentName":"","lastFiling":false} # CreateIssuerRequest | The issuer to update (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update an issuer
        api_instance.update_issuer(id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->update_issuer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an issuer
        api_instance.update_issuer(id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, create_issuer_request=create_issuer_request)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling Issuers1099Api->update_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the issuer to update |
 **avalara_version** | **str**| API version |
 **x_correlation_id** | **str**| Unique correlation Id in a GUID format | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API. For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional]
 **create_issuer_request** | [**CreateIssuerRequest**](CreateIssuerRequest.md)| The issuer to update | [optional]

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Issuer updated |  -  |
**400** | Bad request (e.g., invalid sort key) |  -  |
**401** | Unauthorized |  -  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

