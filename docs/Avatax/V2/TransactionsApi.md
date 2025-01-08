# Avalara.SDK.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_adjust_transaction**](TransactionsApi.md#create_or_adjust_transaction) | **POST** /avatax/transactions/createoradjust | Create or adjust a transaction
[**get_transaction_by_code**](TransactionsApi.md#get_transaction_by_code) | **GET** /avatax/companies/{companyCode}/transactions/{transactionCode} | Retrieve a single transaction by code
[**list_transactions_by_company**](TransactionsApi.md#list_transactions_by_company) | **GET** /avatax/companies/{companyCode}/transactions | Retrieve all transactions


# **create_or_adjust_transaction**
> TransactionModel create_or_adjust_transaction()

Create or adjust a transaction

Records a new transaction or adjust an existing transaction in AvaTax.                The `CreateOrAdjustTransaction` endpoint is used to create a new transaction or update an existing one.  This API  can help you create an idempotent service that creates transactions  If there exists a transaction identified by code, the original transaction will be adjusted by using the meta data  in the input transaction.                The `CreateOrAdjustTransaction` API cannot modify any transaction that has been reported to a tax authority using  the Avalara Managed Returns Service or any other tax filing service.  If you call this API to attempt to modify  a transaction that has been reported on a tax filing, you will receive the error `CannotModifyLockedTransaction`.                To generate a refund for a transaction, use the `RefundTransaction` API.                If you don't specify the field `type` in your request, you will get an estimate of type `SalesOrder`, which will not be recorded in the database.                A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like  sales, purchases, inventory transfer, and returns (also called refunds).  You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:                * Lines  * Details (implies lines)  * Summary (implies details)  * Addresses  * SummaryOnly (omit lines and details - reduces API response size)  * LinesOnly (omit details - reduces API response size)  * ForceTimeout - Simulates a timeout.  This adds a 30 second delay and error to your API call.  This can be used to test your code to ensure it can respond correctly in the case of a dropped connection.                If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.                NOTE: Avoid using the following strings in your transaction codes as they are encoding strings and will be interpreted differently:  * \\_-ava2f-\\_  * \\_-ava2b-\\_  * \\_-ava3f-\\_  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro, BasicReturns. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import transactions_api
from Avalara.SDK.model.transaction_model import TransactionModel
from Avalara.SDK.model.create_or_adjust_transaction_model import CreateOrAdjustTransactionModel
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
    api_instance = transactions_api.TransactionsApi(api_client)
    include = "$include_example" # str | Specifies objects to include in the response after transaction is created (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = CreateOrAdjustTransactionModel(
        adjustment_reason="NotAdjusted",
        adjustment_description="Test Description",
        create_transaction_model=CreateTransactionModel(
            code="code_example",
            lines=[
                LineItemModel(
                    number="1",
                    quantity=1,
                    amount=100,
                    addresses=AddressesModel(
                        single_location=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        ship_from=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        ship_to=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        point_of_order_origin=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        point_of_order_acceptance=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        goods_place_or_service_rendered=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        _import=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                        bill_to=AddressLocationInfo(
                            location_code="location_code_example",
                            line1="2000 Main Street",
                            line2="line2_example",
                            line3="line3_example",
                            city="Irvine",
                            region="CA",
                            country="US",
                            postal_code="92614",
                            latitude=3.14,
                            longitude=3.14,
                        ),
                    ),
                    tax_code="PS081282",
                    customer_usage_type="customer_usage_type_example",
                    entity_use_code="entity_use_code_example",
                    item_code="Y0001",
                    exemption_code="exemption_code_example",
                    discounted=True,
                    tax_included=True,
                    revenue_account="revenue_account_example",
                    ref1="ref1_example",
                    ref2="ref2_example",
                    description="Yarn",
                    business_identification_no="business_identification_no_example",
                    tax_override=TaxOverrideModel(
                        type="None",
                        tax_amount=6.25,
                        tax_date=dateutil_parser('1970-01-01').date(),
                        reason="Precalculated Tax",
                        tax_amount_by_tax_types=[
                            TransactionLineTaxAmountByTaxTypeModel(
                                tax_type_id="tax_type_id_example",
                                tax_amount=3.14,
                            ),
                        ],
                    ),
                    parameters=[
                        TransactionLineParameterModel(
                            name="ScreenSize",
                            value="22.0",
                            unit="Inch",
                        ),
                    ],
                    user_defined_fields=[
                        TransactionLineUserDefinedFieldModel(
                            name="UDF1",
                            value="100",
                        ),
                    ],
                    hs_code="hs_code_example",
                    merchant_seller_id=1,
                    merchant_seller_identifier="merchant_seller_identifier_example",
                    marketplace_liability_type="Marketplace",
                    origination_document_id="origination_document_id_example",
                    origination_site="origination_site_example",
                    category="category_example",
                    summary="summary_example",
                ),
            ],
            type="SalesOrder",
            company_code="DEFAULT",
            date=dateutil_parser('1970-01-01').date(),
            salesperson_code="salesperson_code_example",
            customer_code="ABC",
            customer_usage_type="customer_usage_type_example",
            entity_use_code="entity_use_code_example",
            discount=3.14,
            purchase_order_no="2022-07-28-001",
            exemption_no="exemption_no_example",
            addresses=AddressesModel(
                single_location=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                ship_from=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                ship_to=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                point_of_order_origin=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                point_of_order_acceptance=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                goods_place_or_service_rendered=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                _import=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
                bill_to=AddressLocationInfo(
                    location_code="location_code_example",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    country="US",
                    postal_code="92614",
                    latitude=3.14,
                    longitude=3.14,
                ),
            ),
            parameters=[
                TransactionParameterModel(
                    name="ScreenSize",
                    value="22.0",
                    unit="Inch",
                ),
            ],
            user_defined_fields=[
                TransactionUserDefinedFieldModel(
                    name="UDF1",
                    value="100",
                ),
            ],
            reference_code="reference_code_example",
            reporting_location_code="reporting_location_code_example",
            commit=True,
            batch_code="batch_code_example",
            tax_override=TaxOverrideModel(
                type="None",
                tax_amount=6.25,
                tax_date=dateutil_parser('1970-01-01').date(),
                reason="Precalculated Tax",
                tax_amount_by_tax_types=[
                    TransactionLineTaxAmountByTaxTypeModel(
                        tax_type_id="tax_type_id_example",
                        tax_amount=3.14,
                    ),
                ],
            ),
            currency_code="USD",
            service_mode="Automatic",
            exchange_rate=3.14,
            exchange_rate_effective_date=dateutil_parser('1970-01-01').date(),
            exchange_rate_currency_code="exchange_rate_currency_code_example",
            pos_lane_code="pos_lane_code_example",
            business_identification_no="business_identification_no_example",
            is_seller_importer_of_record=True,
            description="Yarn",
            email="email_example",
            debug_level="Normal",
            customer_supplier_name="customer_supplier_name_example",
            data_source_id=1,
            delivery_terms="DAP",
        ),
    ) # CreateOrAdjustTransactionModel | The transaction you wish to create or adjust (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or adjust a transaction
        api_response = api_instance.create_or_adjust_transaction(include=include, x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TransactionsApi->create_or_adjust_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Specifies objects to include in the response after transaction is created | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**CreateOrAdjustTransactionModel**](CreateOrAdjustTransactionModel.md)| The transaction you wish to create or adjust | [optional]

### Return type

[**TransactionModel**](TransactionModel.md)

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

[[Back to top]](#) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transaction_by_code**
> TransactionModel get_transaction_by_code(company_code, transaction_code)

Retrieve a single transaction by code

Get the current transaction identified by this company code, transaction code, and document type.                A transaction is uniquely identified by `companyCode`, `code` (often called Transaction Code), and `documentType`.                For compatibility purposes, when this API finds multiple transactions with the same transaction code, and if you have not specified  the `type` parameter to this API, it will default to selecting the `SalesInvoices` transaction. To change this behavior, use the  optional `documentType` parameter to specify the specific document type you wish to find.                If this transaction was adjusted, the return value of this API will be the current transaction with this code.                You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:                * Lines  * Details (implies lines)  * Summary (implies details)  * Addresses  * SummaryOnly (omit lines and details - reduces API response size)  * LinesOnly (omit details - reduces API response size)                NOTE: If your companyCode or transactionCode contains any of these characters /, +, ? or a space please use the following encoding before making a request:  * Replace '/' with '\\_-ava2f-\\_'  For example: document/Code becomes document_-ava2f-_Code  * Replace '+' with '\\_-ava2b-\\_'  For example: document+Code becomes document_-ava2b-_Code  * Replace '?' with '\\_-ava3f-\\_'  For example: document?Code becomes document_-ava3f-_Code  * Replace '%' with '\\_-ava25-\\_'  For example: document%Code becomes document_-ava25-_Code  * Replace '#' with '\\_-ava23-\\_'  For example: document#Code becomes document_-ava23-_Code  * Replace ' ' with '%20'  For example: document Code becomes document%20Code  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro, BasicReturns. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import transactions_api
from Avalara.SDK.model.transaction_model import TransactionModel
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
    api_instance = transactions_api.TransactionsApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded this transaction
    transaction_code = "transactionCode_example" # str | The transaction code to retrieve
    document_type = "SalesOrder" # str | (Optional): The document type of the transaction to retrieve (optional)
    include = "$include_example" # str | Specifies objects to include in this fetch call (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single transaction by code
        api_response = api_instance.get_transaction_by_code(company_code, transaction_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a single transaction by code
        api_response = api_instance.get_transaction_by_code(company_code, transaction_code, document_type=document_type, include=include, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded this transaction |
 **transaction_code** | **str**| The transaction code to retrieve |
 **document_type** | **str**| (Optional): The document type of the transaction to retrieve | [optional]
 **include** | **str**| Specifies objects to include in this fetch call | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**TransactionModel**](TransactionModel.md)

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

# **list_transactions_by_company**
> TransactionModelFetchResult list_transactions_by_company(company_code)

Retrieve all transactions

List all transactions attached to this company.                This endpoint is limited to returning 1,000 transactions at a time maximum.                When listing transactions, you must specify a `date` range filter.  If you do not specify a `$filter` that includes a `date` field  criteria, the query will default to looking at only those transactions with `date` in the past 30 days.                A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like  sales, purchases, inventory transfer, and returns (also called refunds).                Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .  Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.                You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:                * Lines  * Details (implies lines)  * Summary (implies details)  * Addresses  * SummaryOnly (omit lines and details - reduces API response size)  * LinesOnly (omit details - reduces API response size)                NOTE: If your companyCode or transactionCode contains any of these characters /, +, ? or a space please use the following encoding before making a request:  * Replace '/' with '\\_-ava2f-\\_'  For example: document/Code becomes document_-ava2f-_Code  * Replace '+' with '\\_-ava2b-\\_'  For example: document+Code becomes document_-ava2b-_Code  * Replace '?' with '\\_-ava3f-\\_'  For example: document?Code becomes document_-ava3f-_Code  * Replace '%' with '\\_-ava25-\\_'  For example: document%Code becomes document_-ava25-_Code  * Replace '#' with '\\_-ava23-\\_'  For example: document#Code becomes document_-ava23-_Code  * Replace ' ' with '%20'  For example: document Code becomes document%20Code  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, AccountUser, BatchServiceAdmin, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser. * This API depends on the following active services:*Required* (all):  AvaTaxPro, BasicReturns. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import transactions_api
from Avalara.SDK.model.transaction_model_fetch_result import TransactionModelFetchResult
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
    api_instance = transactions_api.TransactionsApi(api_client)
    company_code = "companyCode_example" # str | The company code of the company that recorded this transaction
    data_source_id = 1 # int | Optionally filter transactions to those from a specific data source. (optional)
    include = "$include_example" # str | Specifies objects to include in this fetch call (optional)
    filter = "$filter_example" # str | A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* exchangeRateCurrencyCode, totalDiscount, lines, addresses, locationTypes, summary, taxDetailsByTaxType, parameters, userDefinedFields, messages, invoiceMessages, isFakeTransaction, deliveryTerms (optional)
    top = 1 # int | If nonzero, return no more than this number of results.  Used with `$skip` to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. (optional)
    skip = 1 # int | If nonzero, skip this number of results before returning data.  Used with `$top` to provide pagination for large datasets. (optional)
    order_by = "$orderBy_example" # str | A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`. (optional)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    # example passing only required values which don't have defaults set
    try:
        # Retrieve all transactions
        api_response = api_instance.list_transactions_by_company(company_code)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions_by_company: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all transactions
        api_response = api_instance.list_transactions_by_company(company_code, data_source_id=data_source_id, include=include, filter=filter, top=top, skip=skip, order_by=order_by, x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling TransactionsApi->list_transactions_by_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_code** | **str**| The company code of the company that recorded this transaction |
 **data_source_id** | **int**| Optionally filter transactions to those from a specific data source. | [optional]
 **include** | **str**| Specifies objects to include in this fetch call | [optional]
 **filter** | **str**| A filter statement to identify specific records to retrieve.  For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).&lt;br /&gt;*Not filterable:* exchangeRateCurrencyCode, totalDiscount, lines, addresses, locationTypes, summary, taxDetailsByTaxType, parameters, userDefinedFields, messages, invoiceMessages, isFakeTransaction, deliveryTerms | [optional]
 **top** | **int**| If nonzero, return no more than this number of results.  Used with &#x60;$skip&#x60; to provide pagination for large datasets.  Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records. | [optional]
 **skip** | **int**| If nonzero, skip this number of results before returning data.  Used with &#x60;$top&#x60; to provide pagination for large datasets. | [optional]
 **order_by** | **str**| A comma separated list of sort statements in the format &#x60;(fieldname) [ASC|DESC]&#x60;, for example &#x60;id ASC&#x60;. | [optional]
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

### Return type

[**TransactionModelFetchResult**](TransactionModelFetchResult.md)

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

