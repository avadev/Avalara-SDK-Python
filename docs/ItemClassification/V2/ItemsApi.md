# Avalara.SDK.ItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_catalogue_item**](ItemsApi.md#delete_catalogue_item) | **DELETE** /ims/companies/{companyId}/itemcatalogue/{itemCode} | Delete a single item
[**delete_item**](ItemsApi.md#delete_item) | **DELETE** /ims/companies/{companyId}/items/{id} | Delete a single item
[**get_item**](ItemsApi.md#get_item) | **GET** /ims/companies/{companyId}/items/{id} | Retrieve a single item
[**sync_item_catalogue**](ItemsApi.md#sync_item_catalogue) | **POST** /ims/companies/{companyId}/itemcatalogue | Create or update items from a product catalog.
[**update_item**](ItemsApi.md#update_item) | **PUT** /ims/companies/{companyId}/items/{id} | Update a single item


# **delete_catalogue_item**
> [ErrorDetail] delete_catalogue_item(company_id, item_code)

Delete a single item

Deletes the item object at this URL.                Items are a way of separating your tax calculation process from your tax configuration details.   Use this endpoint to delete an existing item with item code.                Deleting an item will also delete the parameters, classifications, and product categories associated with that item.    NOTE: If your item code contains any of these characters /, +, ? or a space, please use the following encoding before making a request:  * Replace '/' with '\\_-ava2f-\\_'  For example: 'Item/Code' becomes 'Item_-ava2f-_Code'  * Replace '+' with '\\_-ava2b-\\_'  For example: 'Item+Code' becomes 'Item_-ava2b-_Code'  * Replace '?' with '\\_-ava3f-\\_'  For example: 'Item?Code' becomes 'Item_-ava3f-_Code'  * Replace '%' with '\\_-ava25-\\_'  For example: 'Item%Code' becomes 'Item_-ava25-_Code'  * Replace '#' with '\\_-ava23-\\_'  For example: 'Item#Code' becomes 'Item_-ava23-_Code'  * Replace '_'_' with '\\_-ava27-\\_'  For example: 'Item'Code' becomes 'Item_-ava27-_Code'  * Replace '\"' with '\\_-ava22-\\_'  For example: 'Item\"Code' becomes 'Item_-ava22-_Code'  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, BatchServiceAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import items_api
from Avalara.SDK.model.error_detail import ErrorDetail
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = 1 # int | The ID of the company that owns this item.
    item_code = "itemCode_example" # str | The code of the item you want to delete.
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Delete a single item
        api_response = api_instance.delete_catalogue_item(company_id, item_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->delete_catalogue_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a single item
        api_response = api_instance.delete_catalogue_item(company_id, item_code, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->delete_catalogue_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company that owns this item. |
 **item_code** | **str**| The code of the item you want to delete. |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**[ErrorDetail]**](ErrorDetail.md)

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

# **delete_item**
> [ErrorDetail] delete_item(company_id, id)

Delete a single item

Deletes the item object at this URL.                Items are a way of separating your tax calculation process from your tax configuration details.  If you choose, you  can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,  and other data fields.  AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters  from the item table instead.  This allows your CreateTransaction call to be as simple as possible, and your tax compliance  team can manage your item catalog and adjust the tax behavior of items without having to modify your software.                Deleting an item will also delete the parameters and classifications associated with that item.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, BatchServiceAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import items_api
from Avalara.SDK.model.error_detail import ErrorDetail
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = 1 # int | The ID of the company that owns this item.
    id = 1 # int | The ID of the item you wish to delete.
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Delete a single item
        api_response = api_instance.delete_item(company_id, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->delete_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a single item
        api_response = api_instance.delete_item(company_id, id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company that owns this item. |
 **id** | **int**| The ID of the item you wish to delete. |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**[ErrorDetail]**](ErrorDetail.md)

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

# **get_item**
> ItemModel get_item(company_id, id)

Retrieve a single item

Get the `Item` object identified by this URL.                Items are a way of separating your tax calculation process from your tax configuration details.  If you choose, you  can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,  and other data fields.  AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters  from the item table instead.  This allows your CreateTransaction call to be as simple as possible, and your tax compliance  team can manage your item catalog and adjust the tax behavior of items without having to modify your software.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import items_api
from Avalara.SDK.model.item_model import ItemModel
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = 1 # int | The ID of the company that owns this item object
    id = 1 # int | The primary key of this item
    include = "$include_example" # str | A comma separated list of additional data to retrieve. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single item
        api_response = api_instance.get_item(company_id, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->get_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a single item
        api_response = api_instance.get_item(company_id, id, include=include, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company that owns this item object |
 **id** | **int**| The primary key of this item |
 **include** | **str**| A comma separated list of additional data to retrieve. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**ItemModel**](ItemModel.md)

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

# **sync_item_catalogue**
> ItemCatalogueOutputModel sync_item_catalogue(company_id)

Create or update items from a product catalog.

Creates/updates one or more item objects with additional properties and the AvaTax category attached to this company.                Items are a way of separating your tax calculation process from your tax configuration details. Use this endpoint to create  a new or update an existing item. This can be used to sync the items with Avalara. For example, an accounting software  system can use this to sync all their items from an ERP with Avalara.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, BatchServiceAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import items_api
from Avalara.SDK.model.item_catalogue_input_model import ItemCatalogueInputModel
from Avalara.SDK.model.item_catalogue_output_model import ItemCatalogueOutputModel
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = 1 # int | The ID of the company that owns this item.
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = [
        ItemCatalogueInputModel(
            item_code="ITEM-101",
            description="Concord Grape",
            summary="Apple Cider Vinegar Drink",
            tax_code="",
            upc="7846226233",
            item_group="Drinks",
            category="beverages - vinegar - drink",
            source="QBO",
            properties={
                "key": "key_example",
            },
        ),
    ] # [ItemCatalogueInputModel] | The items you want to create or update. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create or update items from a product catalog.
        api_response = api_instance.sync_item_catalogue(company_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->sync_item_catalogue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update items from a product catalog.
        api_response = api_instance.sync_item_catalogue(company_id, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->sync_item_catalogue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company that owns this item. |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**[ItemCatalogueInputModel]**](ItemCatalogueInputModel.md)| The items you want to create or update. | [optional]

### Return type

[**ItemCatalogueOutputModel**](ItemCatalogueOutputModel.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_item**
> ItemModel update_item(company_id, id)

Update a single item

Replace the existing `Item` object at this URL with an updated object.                Items are a way of separating your tax calculation process from your tax configuration details.  If you choose, you  can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,  and other data fields.  AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters  from the item table instead.  This allows your CreateTransaction call to be as simple as possible, and your tax compliance  team can manage your item catalog and adjust the tax behavior of items without having to modify your software.                All data from the existing object will be replaced with data in the object you PUT.  To set a field's value to null,  you may either set its value to null or omit that field from the object you post.                The tax code takes precedence over the tax code id if both are provided.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, BatchServiceAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import items_api
from Avalara.SDK.model.item_model import ItemModel
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = 1 # int | The ID of the company that this item belongs to.
    id = 1 # int | The ID of the item you wish to update
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = ItemModel(
        id=56789,
        item_code="CERMUG",
        tax_code_id=1,
        tax_code="P0000000",
        description="Ceramic Mug",
        item_group="Mugs",
        category="Home > Kitchen > Mugs",
        source="source_example",
        upc="upc_example",
        classifications=[
            ClassificationModel(
                product_code="9011900000",
                system_code="TARIC",
            ),
        ],
        parameters=[
            ItemParameterModel(
                name="ScreenSize",
                value="24",
                unit="inch",
                item_id=1,
            ),
        ],
        tags=[
            ItemTagDetailModel(
                tag_name="CLASSIFICATION_INITIATIONERROR",
                item_id=151284220,
                company_id=8010687,
            ),
        ],
    ) # ItemModel | The item object you wish to update. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a single item
        api_response = api_instance.update_item(company_id, id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->update_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a single item
        api_response = api_instance.update_item(company_id, id, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling ItemsApi->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of the company that this item belongs to. |
 **id** | **int**| The ID of the item you wish to update |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**ItemModel**](ItemModel.md)| The item object you wish to update. | [optional]

### Return type

[**ItemModel**](ItemModel.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

