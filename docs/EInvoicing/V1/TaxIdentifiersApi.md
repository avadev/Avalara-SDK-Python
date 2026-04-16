# Avalara.SDK.TaxIdentifiersApi

All URIs are relative to *https://api.sbx.avalara.com/einvoicing*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_identifier_schema_by_country**](TaxIdentifiersApi.md#tax_identifier_schema_by_country) | **GET** /tax-identifiers/schema | Returns the tax identifier request and response schema for a specific country.
[**validate_tax_identifier**](TaxIdentifiersApi.md#validate_tax_identifier) | **POST** /tax-identifiers/validate | Validates a tax identifier.


# **tax_identifier_schema_by_country**
> TaxIdentifierSchemaByCountry200Response tax_identifier_schema_by_country(avalara_version, country_code)

Returns the tax identifier request and response schema for a specific country.

Returns the tax identifier request and response schema for a specific country.

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
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    country_code = 'DE' # str | Two-letter ISO 3166 country code for which to retrieve the schema (for example \"DE\").
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
    type = 'request' # str | Specifies which schema to return: \"request\" to receive the request validation schema or \"response\" to receive the response validation schema. (optional)
    # example passing only required values which don't have defaults set
    try:
        # Returns the tax identifier request and response schema for a specific country.
        api_response = api_instance.tax_identifier_schema_by_country(avalara_version, country_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->tax_identifier_schema_by_country: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the tax identifier request and response schema for a specific country.
        api_response = api_instance.tax_identifier_schema_by_country(avalara_version, country_code, x_avalara_client=x_avalara_client, x_correlation_id=x_correlation_id, type=type)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TaxIdentifiersApi->tax_identifier_schema_by_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **country_code** | **str**| Two-letter ISO 3166 country code for which to retrieve the schema (for example \&quot;DE\&quot;). |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]
 **type** | **str**| Specifies which schema to return: \&quot;request\&quot; to receive the request validation schema or \&quot;response\&quot; to receive the response validation schema. | [optional]

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
**200** | Returns an object containing countryCode, schemaType, and schema. The schema property contains a JSON Schema (Draft-07) used to validate tax identifier requests or responses for the specified country. |  * X-Correlation-ID -  <br>  |
**400** | Invalid request |  * X-Correlation-ID -  <br>  |
**401** | Unauthorized. |  * X-Correlation-ID -  <br>  |
**403** | Forbidden. |  * X-Correlation-ID -  <br>  |
**500** | Internal server error. |  * X-Correlation-ID -  <br>  |

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
    avalara_version = '1.6' # str | Header that specifies the API version to use (for example \"1.6\").
    tax_identifier_request = {"countryCode":"DE","identifierType":"vat","identifier":"123456789"} # TaxIdentifierRequest | 
    x_avalara_client = 'John's E-Invoicing-API Client' # str | Optional header for a client identifier string used for diagnostics (for example \"Fingerprint\"). (optional)
    x_correlation_id = 'f3f0d19a-01a1-4748-8a58-f000d0424f43' # str | Optional correlation identifier provided by the caller to trace the call (for example \"f3f0d19a-01a1-4748-8a58-f000d0424f43\"). (optional)
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
 **avalara_version** | **str**| Header that specifies the API version to use (for example \&quot;1.6\&quot;). |
 **tax_identifier_request** | [**TaxIdentifierRequest**](TaxIdentifierRequest.md)|  |
 **x_avalara_client** | **str**| Optional header for a client identifier string used for diagnostics (for example \&quot;Fingerprint\&quot;). | [optional]
 **x_correlation_id** | **str**| Optional correlation identifier provided by the caller to trace the call (for example \&quot;f3f0d19a-01a1-4748-8a58-f000d0424f43\&quot;). | [optional]

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
**200** | Validation completed. Returns a TaxIdentifierResponse object that includes countryCode and a value object with identifierType, identifier, and optional extensions when available. |  * X-Correlation-ID -  <br>  |
**400** | Bad request. The request is invalid or contains missing or incorrect parameters. |  * X-Correlation-ID -  <br>  |
**401** | Unauthorized. |  * X-Correlation-ID -  <br>  |
**403** | Forbidden. |  * X-Correlation-ID -  <br>  |
**429** | Rate limit exceeded. |  * X-Correlation-ID -  <br>  |
**500** | Internal server error. |  * X-Correlation-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

