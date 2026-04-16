# Avalara.SDK.SubscriptionsApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](SubscriptionsApi.md#create_webhook_subscription) | **POST** /webhooks/subscriptions | Create a subscription to events
[**delete_webhook_subscription**](SubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /webhooks/subscriptions/{subscriptionId} | Unsubscribe from events
[**get_webhook_subscription**](SubscriptionsApi.md#get_webhook_subscription) | **GET** /webhooks/subscriptions/{subscriptionId} | Get details of a subscription
[**list_webhook_subscriptions**](SubscriptionsApi.md#list_webhook_subscriptions) | **GET** /webhooks/subscriptions | List all subscriptions


# **create_webhook_subscription**
> SuccessResponse create_webhook_subscription(avalara_version, subscription_registration)

Create a subscription to events

Create a new webhook subscription and return the created subscription details.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import subscriptions_api
SuccessResponse
WebhooksErrorResponse
SubscriptionRegistration
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    avalara_version = 'avalara_version_example' # str | The version of the API to use, e.g., \"1.6\".
    subscription_registration = Avalara.SDK.SubscriptionRegistration() # SubscriptionRegistration | 
    x_correlation_id = 'x_correlation_id_example' # str | A unique identifier for tracking the request and its response (optional)
    x_avalara_client = 'x_avalara_client_example' # str | Client application identification (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create a subscription to events
        api_response = api_instance.create_webhook_subscription(avalara_version, subscription_registration)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->create_webhook_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a subscription to events
        api_response = api_instance.create_webhook_subscription(avalara_version, subscription_registration, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->create_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The version of the API to use, e.g., \&quot;1.6\&quot;. |
 **subscription_registration** | [**SubscriptionRegistration**](SubscriptionRegistration.md)|  |
 **x_correlation_id** | **str**| A unique identifier for tracking the request and its response | [optional]
 **x_avalara_client** | **str**| Client application identification | [optional]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created successfully. Returns the created SubscriptionDetail object. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**400** | Bad request. The request payload is invalid or contains missing required fields. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**401** | Unauthorized. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**403** | Forbidden. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(subscription_id, avalara_version)

Unsubscribe from events

Delete the specified webhook subscription.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import subscriptions_api
WebhooksErrorResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Unique identifier of the subscription.
    avalara_version = 'avalara_version_example' # str | The version of the API to use, e.g., \"1.6\".
    x_correlation_id = 'x_correlation_id_example' # str | A unique identifier for tracking the request and its response (optional)
    x_avalara_client = 'x_avalara_client_example' # str | Client application identification (optional)
    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe from events
        api_instance.delete_webhook_subscription(subscription_id, avalara_version)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->delete_webhook_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unsubscribe from events
        api_instance.delete_webhook_subscription(subscription_id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->delete_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier of the subscription. |
 **avalara_version** | **str**| The version of the API to use, e.g., \&quot;1.6\&quot;. |
 **x_correlation_id** | **str**| A unique identifier for tracking the request and its response | [optional]
 **x_avalara_client** | **str**| Client application identification | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subscription deleted successfully. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**401** | Unauthorized. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**403** | Forbidden. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**404** | Subscription not found for the specified subscriptionId. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_webhook_subscription**
> SubscriptionDetail get_webhook_subscription(subscription_id, avalara_version)

Get details of a subscription

Retrieve details of a specific subscription.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import subscriptions_api
SubscriptionDetail
WebhooksErrorResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | Unique identifier of the subscription.
    avalara_version = 'avalara_version_example' # str | The version of the API to use, e.g., \"1.6\".
    x_correlation_id = 'x_correlation_id_example' # str | A unique identifier for tracking the request and its response (optional)
    x_avalara_client = 'x_avalara_client_example' # str | Client application identification (optional)
    # example passing only required values which don't have defaults set
    try:
        # Get details of a subscription
        api_response = api_instance.get_webhook_subscription(subscription_id, avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->get_webhook_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of a subscription
        api_response = api_instance.get_webhook_subscription(subscription_id, avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->get_webhook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Unique identifier of the subscription. |
 **avalara_version** | **str**| The version of the API to use, e.g., \&quot;1.6\&quot;. |
 **x_correlation_id** | **str**| A unique identifier for tracking the request and its response | [optional]
 **x_avalara_client** | **str**| Client application identification | [optional]

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the SubscriptionDetail object for the specified subscriptionId. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**401** | Unauthorized. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**403** | Forbidden. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**404** | Subscription not found for the specified subscriptionId. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_webhook_subscriptions**
> SubscriptionListResponse list_webhook_subscriptions(avalara_version)

List all subscriptions

Retrieve a list of webhook subscriptions.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import subscriptions_api
SubscriptionListResponse
WebhooksErrorResponse
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
    api_instance = subscriptions_api.SubscriptionsApi(api_client)
    avalara_version = 'avalara_version_example' # str | The version of the API to use, e.g., \"1.6\".
    x_correlation_id = 'x_correlation_id_example' # str | A unique identifier for tracking the request and its response (optional)
    x_avalara_client = 'x_avalara_client_example' # str | Client application identification (optional)
    top = 56 # int | The number of items to include in the result. (optional)
    skip = 56 # int | The number of items to skip in the result. (optional)
    count = True # bool | Whether to include the total count of records in the result. (optional)
    count_only = True # bool | Whether to return only the count of records, without the list of records. (optional)
    # example passing only required values which don't have defaults set
    try:
        # List all subscriptions
        api_response = api_instance.list_webhook_subscriptions(avalara_version)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->list_webhook_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all subscriptions
        api_response = api_instance.list_webhook_subscriptions(avalara_version, x_correlation_id=x_correlation_id, x_avalara_client=x_avalara_client, top=top, skip=skip, count=count, count_only=count_only)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling SubscriptionsApi->list_webhook_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The version of the API to use, e.g., \&quot;1.6\&quot;. |
 **x_correlation_id** | **str**| A unique identifier for tracking the request and its response | [optional]
 **x_avalara_client** | **str**| Client application identification | [optional]
 **top** | **int**| The number of items to include in the result. | [optional]
 **skip** | **int**| The number of items to skip in the result. | [optional]
 **count** | **bool**| Whether to include the total count of records in the result. | [optional]
 **count_only** | **bool**| Whether to return only the count of records, without the list of records. | [optional]

### Return type

[**SubscriptionListResponse**](SubscriptionListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of webhook subscriptions in a SubscriptionListResponse object. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**401** | Unauthorized. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**403** | Forbidden. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |
**500** | Internal server error. |  * X-Correlation-ID - Correlation ID from the request, or a new one if not provided in request <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

