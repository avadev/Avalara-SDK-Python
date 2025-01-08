# Avalara.SDK.CustomersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customers**](CustomersApi.md#create_customers) | **POST** /avatax/companies/{companyId}/customers | Create customers for this company
[**list_certificates_for_customer**](CustomersApi.md#list_certificates_for_customer) | **GET** /avatax/companies/{companyId}/customers/{customerCode}/certificates | List certificates linked to a customer
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /avatax/companies/{companyId}/customers/{customerCode} | Update a single customer


# **create_customers**
> [CustomerModel] create_customers(company_id)

Create customers for this company

Create one or more customers for this company.                A customer object defines information about a person or business that purchases products from your  company.  When you create a tax transaction in AvaTax, you can use the `customerCode` from this  record in your `CreateTransaction` API call.  AvaTax will search for this `customerCode` value and  identify any certificates linked to this `customer` object.  If any certificate applies to the transaction,  AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.                A nested object such as CustomFields could be specified and created along with the customer object. To fetch the  nested object, please call 'GetCustomer' API with appropriate $include parameters.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import customers_api
from Avalara.SDK.model.customer_model import CustomerModel
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = 1 # int | The unique ID number of the company that recorded this customer
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = [
        CustomerModel(
            company_id=0,
            customer_code="509bd9b4-65bb-4c7f-b157-6535b93a89f9",
            alternate_id="987654321",
            name="Dr. Bob Example",
            attn_name="Attn: Receiving",
            line1="645 Main Street",
            line2="line2_example",
            city="Irvine",
            postal_code="92614",
            phone_number="(949) 555-1212",
            fax_number="949.555.1213",
            email_address="dr.bob.example@example.org",
            contact_name="Alice Smith",
            country="US",
            region="CA",
            is_bill=True,
            is_ship=True,
            taxpayer_id_number="taxpayer_id_number_example",
            certificates=[
                CertificateModel(
                    id=0,
                    company_id=1,
                    signed_date=dateutil_parser('1970-01-01').date(),
                    expiration_date=dateutil_parser('1970-01-01').date(),
                    filename="18f1a69f-3b62-4a38-9c53-dcdb999bf636",
                    valid=True,
                    exempt_percentage=0,
                    exemption_number="Exempt-1234",
                    validated_exemption_reason=ExemptionReasonModel(
                        id=1,
                        name="EXPOSURE",
                    ),
                    exemption_reason=ExemptionReasonModel(
                        id=1,
                        name="EXPOSURE",
                    ),
                    created_date=dateutil_parser('2022-07-28T20:12:08.808Z'),
                    modified_date=dateutil_parser('1970-01-01').date(),
                    tax_number_type="FEIN",
                    business_number_type="Business Services",
                    customers=[
                        CustomerModel(),
                    ],
                    po_numbers=[
                        PoNumberModel(
                            po_number="test",
                        ),
                    ],
                    exposure_zone=ExposureZoneModel(
                        company_id=1,
                        name="Washington",
                        tag="tag_example",
                        description="description_example",
                        created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    attributes=[
                        CertificateAttributeModel(
                            id=0,
                            name="DIRECT PAY",
                            description="description_example",
                            is_system_code=False,
                        ),
                    ],
                    ecms_id=1,
                    ecms_status="ecms_status_example",
                    pdf="pdf_example",
                    pages=[
                        "pages_example",
                    ],
                ),
            ],
            custom_fields=[
                CustomFieldModel(
                    name="Customer Type",
                    value="my customer type",
                ),
            ],
            exposure_zones=[
                ExposureZoneModel(
                    company_id=1,
                    name="Washington",
                    tag="tag_example",
                    description="description_example",
                    created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            ship_tos=[
                CustomerModel(),
            ],
            attributes=[
                CustomerAttributeModel(
                    id=1,
                    name="ADDRESS CHANGE NEEDED",
                    description="Customer address change is needed.",
                    is_system_code=False,
                    is_non_deliver=True,
                    is_changeable=True,
                ),
            ],
        ),
    ] # [CustomerModel] | The list of customer objects to be created (optional)
    # example passing only required values which don't have defaults set
    try:
        # Create customers for this company
        api_response = api_instance.create_customers(company_id)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->create_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create customers for this company
        api_response = api_instance.create_customers(company_id, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->create_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that recorded this customer |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**[CustomerModel]**](CustomerModel.md)| The list of customer objects to be created | [optional]

### Return type

[**[CustomerModel]**](CustomerModel.md)

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

# **list_certificates_for_customer**
> CertificateModelFetchResult list_certificates_for_customer(company_id, customer_code)

List certificates linked to a customer

List all certificates linked to a customer.                A customer object defines information about a person or business that purchases products from your  company.  When you create a tax transaction in AvaTax, you can use the `customerCode` from this  record in your `CreateTransaction` API call.  AvaTax will search for this `customerCode` value and  identify any certificates linked to this `customer` object.  If any certificate applies to the transaction,  AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import customers_api
from Avalara.SDK.model.certificate_model_fetch_result import CertificateModelFetchResult
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = 1 # int | The unique ID number of the company that recorded this customer
    customer_code = "customerCode_example" # str | The unique code representing this customer
    include = "$include_example" # str | OPTIONAL: A comma separated list of special fetch options.  You can specify one or more of the following:                             * customers - Retrieves the list of customers linked to the certificate.               * po_numbers - Retrieves all PO numbers tied to the certificate.               * attributes - Retrieves all attributes applied to the certificate. (optional)
    filter = "$filter_example" # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* exemptionNumber, status, ecmsId, ecmsStatus, pdf, pages (optional)
    top = 1 # int | If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 1 # int | If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets. (optional)
    order_by = "$orderBy_example" # str | A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # List certificates linked to a customer
        api_response = api_instance.list_certificates_for_customer(company_id, customer_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->list_certificates_for_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List certificates linked to a customer
        api_response = api_instance.list_certificates_for_customer(company_id, customer_code, include=include, filter=filter, top=top, skip=skip, order_by=order_by, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->list_certificates_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that recorded this customer |
 **customer_code** | **str**| The unique code representing this customer |
 **include** | **str**| OPTIONAL: A comma separated list of special fetch options.  You can specify one or more of the following:                             * customers - Retrieves the list of customers linked to the certificate.               * po_numbers - Retrieves all PO numbers tied to the certificate.               * attributes - Retrieves all attributes applied to the certificate. | [optional]
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).&lt;br /&gt;*Not filterable:* exemptionNumber, status, ecmsId, ecmsStatus, pdf, pages | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.  Used with &#x60;$skip&#x60; to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data.  Used with &#x60;$top&#x60; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format &#x60;(fieldname) [ASC|DESC]&#x60;, for example &#x60;id ASC&#x60;. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**CertificateModelFetchResult**](CertificateModelFetchResult.md)

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

# **update_customer**
> CustomerModel update_customer(company_id, customer_code)

Update a single customer

Replace the customer object at this URL with a new record.                A customer object defines information about a person or business that purchases products from your  company.  When you create a tax transaction in AvaTax, you can use the `customerCode` from this  record in your `CreateTransaction` API call.  AvaTax will search for this `customerCode` value and  identify any certificates linked to this `customer` object.  If any certificate applies to the transaction,  AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.                Before you can use any exemption certificates endpoints, you must set up your company for exemption certificate data storage.  Companies that do not have this storage system set up will see `CertCaptureNotConfiguredError` when they call exemption   certificate related APIs. To check if this is set up for a company, call `GetCertificateSetup`.  To request setup of exemption   certificate storage for this company, call `RequestCertificateSetup`.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin. * This API depends on the following active services:*Required* (all):  AvaTaxPro. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import customers_api
from Avalara.SDK.model.customer_model import CustomerModel
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = 1 # int | The unique ID number of the company that recorded this customer
    customer_code = "customerCode_example" # str | The unique code representing this customer
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = CustomerModel(
        company_id=0,
        customer_code="509bd9b4-65bb-4c7f-b157-6535b93a89f9",
        alternate_id="987654321",
        name="Dr. Bob Example",
        attn_name="Attn: Receiving",
        line1="645 Main Street",
        line2="line2_example",
        city="Irvine",
        postal_code="92614",
        phone_number="(949) 555-1212",
        fax_number="949.555.1213",
        email_address="dr.bob.example@example.org",
        contact_name="Alice Smith",
        country="US",
        region="CA",
        is_bill=True,
        is_ship=True,
        taxpayer_id_number="taxpayer_id_number_example",
        certificates=[
            CertificateModel(
                id=0,
                company_id=1,
                signed_date=dateutil_parser('1970-01-01').date(),
                expiration_date=dateutil_parser('1970-01-01').date(),
                filename="18f1a69f-3b62-4a38-9c53-dcdb999bf636",
                valid=True,
                exempt_percentage=0,
                exemption_number="Exempt-1234",
                validated_exemption_reason=ExemptionReasonModel(
                    id=1,
                    name="EXPOSURE",
                ),
                exemption_reason=ExemptionReasonModel(
                    id=1,
                    name="EXPOSURE",
                ),
                created_date=dateutil_parser('2022-07-28T20:12:08.808Z'),
                modified_date=dateutil_parser('1970-01-01').date(),
                tax_number_type="FEIN",
                business_number_type="Business Services",
                customers=[
                    CustomerModel(),
                ],
                po_numbers=[
                    PoNumberModel(
                        po_number="test",
                    ),
                ],
                exposure_zone=ExposureZoneModel(
                    company_id=1,
                    name="Washington",
                    tag="tag_example",
                    description="description_example",
                    created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
                attributes=[
                    CertificateAttributeModel(
                        id=0,
                        name="DIRECT PAY",
                        description="description_example",
                        is_system_code=False,
                    ),
                ],
                ecms_id=1,
                ecms_status="ecms_status_example",
                pdf="pdf_example",
                pages=[
                    "pages_example",
                ],
            ),
        ],
        custom_fields=[
            CustomFieldModel(
                name="Customer Type",
                value="my customer type",
            ),
        ],
        exposure_zones=[
            ExposureZoneModel(
                company_id=1,
                name="Washington",
                tag="tag_example",
                description="description_example",
                created=dateutil_parser('1970-01-01T00:00:00.00Z'),
                modified=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        ship_tos=[
            CustomerModel(),
        ],
        attributes=[
            CustomerAttributeModel(
                id=1,
                name="ADDRESS CHANGE NEEDED",
                description="Customer address change is needed.",
                is_system_code=False,
                is_non_deliver=True,
                is_changeable=True,
            ),
        ],
    ) # CustomerModel | The new customer model that will replace the existing record at this URL (optional)
    # example passing only required values which don't have defaults set
    try:
        # Update a single customer
        api_response = api_instance.update_customer(company_id, customer_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a single customer
        api_response = api_instance.update_customer(company_id, customer_code, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The unique ID number of the company that recorded this customer |
 **customer_code** | **str**| The unique code representing this customer |
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**CustomerModel**](CustomerModel.md)| The new customer model that will replace the existing record at this URL | [optional]

### Return type

[**CustomerModel**](CustomerModel.md)

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

