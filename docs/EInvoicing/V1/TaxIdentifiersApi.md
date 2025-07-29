# Avalara.SDK.TaxIdentifiersApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_identifier_schema_by_country**](TaxIdentifiersApi.md#tax_identifier_schema_by_country) | **GET** /tax-identifiers/schema | Returns the tax identifier request &amp; response schema for a specific country.
[**validate_tax_identifier**](TaxIdentifiersApi.md#validate_tax_identifier) | **POST** /tax-identifiers/validate | Validates a tax identifier.


# **tax_identifier_schema_by_country**
> TaxIdentifierSchemaByCountry200Response tax_identifier_schema_by_country(avalara_version, country_code)

Returns the tax identifier request & response schema for a specific country.

This endpoint retrieves the request and response schema required to validate tax identifiers based on a specific country's requirements. This can include both standard fields and any additional parameters required by the respective country's tax authority.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import tax_identifiers_api
TaxIdentifierSchemaByCountry200Response
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
    api_instance = tax_identifiers_api.TaxIdentifiersApi(api_client)
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    country_code = 'DE' # str | The two-letter ISO-3166 country code for which the schema should be retrieved.
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    type = 'request' # str | Specifies whether to return the request or response schema. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns the tax identifier request & response schema for a specific country.
        api_response = api_instance.tax_identifier_schema_by_country(avalara_version, country_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->tax_identifier_schema_by_country: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the tax identifier request & response schema for a specific country.
        api_response = api_instance.tax_identifier_schema_by_country(avalara_version, country_code, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id, type=type)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->tax_identifier_schema_by_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **country_code** | **str**| The two-letter ISO-3166 country code for which the schema should be retrieved. |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]
 **type** | **str**| Specifies whether to return the request or response schema. | [optional]

### Return type

[**TaxIdentifierSchemaByCountry200Response**](TaxIdentifierSchemaByCountry200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Correlation-Id -  <br>  |
**400** | Invalid request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_tax_identifier**
> TaxIdentifierResponse validate_tax_identifier(avalara_version, tax_identifier_request)

Validates a tax identifier.

This endpoint verifies whether a given tax identifier is valid and properly formatted according to the rules of the applicable country or tax system.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import time
import Avalara.SDK
from Avalara.SDK.api.EInvoicing.V1 import tax_identifiers_api
TaxIdentifierRequest
TaxIdentifierResponse
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
    api_instance = tax_identifiers_api.TaxIdentifiersApi(api_client)
    avalara_version = '1.4' # str | The HTTP Header meant to specify the version of the API intended to be used.
    tax_identifier_request = {"countryCode":"DE","identifierType":"vat","identifier":"123456789"} # TaxIdentifierRequest | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \"Fingerprint\". (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | The caller can use this as an identifier to use as a correlation id to trace the call. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Validates a tax identifier.
        api_response = api_instance.validate_tax_identifier(avalara_version, tax_identifier_request)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->validate_tax_identifier: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validates a tax identifier.
        api_response = api_instance.validate_tax_identifier(avalara_version, tax_identifier_request, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->validate_tax_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| The HTTP Header meant to specify the version of the API intended to be used. |
 **tax_identifier_request** | [**TaxIdentifierRequest**](TaxIdentifierRequest.md)|  |
 **x_avalara_client** | **str**| You can freely use any text you wish for this value. This feature can help you diagnose and solve problems with your software. The header can be treated like a \&quot;Fingerprint\&quot;. | [optional]
 **x_correlation_id** | **str**| The caller can use this as an identifier to use as a correlation id to trace the call. | [optional]

### Return type

[**TaxIdentifierResponse**](TaxIdentifierResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response. |  * X-Correlation-Id -  <br>  |
**400** | Invalid request |  * X-Correlation-Id -  <br>  |
**401** | Unauthorized |  * X-Correlation-Id -  <br>  |
**403** | Forbidden |  * X-Correlation-Id -  <br>  |
**429** | Rate limit exceeded |  * X-Correlation-Id -  <br>  |
**500** | Internal server error |  * X-Correlation-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

