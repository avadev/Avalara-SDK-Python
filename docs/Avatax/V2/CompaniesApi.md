# Avalara.SDK.CompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_companies**](CompaniesApi.md#create_companies) | **POST** /avatax/companies | Create new companies


# **create_companies**
> [CompanyModel] create_companies()

Create new companies

Create one or more new company objects.  A 'company' represents a single corporation or individual that is registered to handle transactional taxes.  You may attach nested data objects such as contacts, locations, and nexus with this CREATE call, and those objects will be created with the company.                NOTE: Please do not use these blacklisted characters in company name and code: ';', '\\', '|'.  ### Security Policies  * This API requires one of the following user roles: AccountAdmin, BatchServiceAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin. 

### Example

* Bearer (JWT) Authentication (Bearer):
* OAuth Authentication (OAuth):

```python
import time
import Avalara.SDK
from Avalara.SDK.api import companies_api
from Avalara.SDK.model.company_model import CompanyModel
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
    api_instance = companies_api.CompaniesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = [
        CompanyModel(
            id=12345,
            account_id=123456789,
            parent_company_id=1,
            sst_pid="sst_pid_example",
            company_code="DEFAULT",
            name="Default Company",
            is_default=False,
            default_location_id=1,
            is_active=True,
            taxpayer_id_number="123456789",
            is_fein=True,
            has_profile=True,
            is_reporting_entity=False,
            sst_effective_date=dateutil_parser('1970-01-01').date(),
            default_country="US",
            base_currency_code="USD",
            rounding_level_id="Line",
            warnings_enabled=True,
            is_test=True,
            tax_dependency_level_id="Document",
            in_progress=False,
            business_identification_no="business_identification_no_example",
            contacts=[
                ContactModel(
                    contact_code="TestContactac6d799c5e524e",
                    first_name="Bob",
                    middle_name="middle_name_example",
                    last_name="McExample",
                    title="Owner",
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    region="CA",
                    postal_code="92614",
                    country="US",
                    email="bob@example.org",
                    phone="714 555-1212",
                    mobile="mobile_example",
                    fax="fax_example",
                ),
            ],
            items=[
                ItemModel(
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
                ),
            ],
            locations=[
                LocationModel(
                    id=56789,
                    location_code="DEFAULT",
                    description="Bob's Artisan Pottery",
                    address_type_id="Location",
                    address_category_id="Storefront",
                    is_marketplace_outside_usa=False,
                    line1="2000 Main Street",
                    line2="line2_example",
                    line3="line3_example",
                    city="Irvine",
                    county="Orange",
                    region="CA",
                    postal_code="92614",
                    country="US",
                    is_default=True,
                    is_registered=True,
                    dba_name="Bob's Artisan Pottery",
                    outlet_name="Main Office",
                    effective_date=dateutil_parser('1970-01-01').date(),
                    end_date=dateutil_parser('1970-01-01').date(),
                    registered_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    settings=[
                        LocationSettingModel(
                            question_id=17,
                            question_name="question_name_example",
                            value="abcdefghij",
                        ),
                    ],
                ),
            ],
            nexus=[
                NexusModel(
                    company_id=0,
                    country="US",
                    region="CA",
                    juris_type_id="STA",
                    jurisdiction_type_id="Country",
                    juris_code="06",
                    juris_name="CALIFORNIA",
                    effective_date=dateutil_parser('1970-01-01').date(),
                    end_date=dateutil_parser('1970-01-01').date(),
                    nexus_type_id="None",
                    sourcing="Mixed",
                    has_local_nexus=True,
                    local_nexus_type_id="Selected",
                    has_permanent_establishment=True,
                    tax_id="tax_id_example",
                    tax_type_group="SalesAndUse",
                    nexus_tax_type_group="SalesAndUse",
                    tax_authority_id=1,
                    is_seller_importer_of_record=False,
                ),
            ],
            settings=[
                SettingModel(
                    id=56789,
                    set="ItemsToRemember",
                    name="Texas",
                    value="Alamo",
                    modified_user_id=1,
                ),
            ],
            tax_codes=[
                TaxCodeModel(
                    tax_code="PS081282",
                    tax_code_type_id="P",
                    description="Yarn",
                    parent_tax_code="PS080100",
                    goods_service_code=0,
                    entity_use_code="",
                    is_active=True,
                    is_sst_certified=False,
                ),
            ],
            tax_rules=[
                TaxRuleModel(
                    id=56789,
                    company_id=12345,
                    tax_code_id=1,
                    tax_code="FR020800",
                    state_fips="04",
                    juris_name="MARICOPA",
                    juris_code="013",
                    juris_type_id="STA",
                    jurisdiction_type_id="Country",
                    customer_usage_type="customer_usage_type_example",
                    entity_use_code="entity_use_code_example",
                    tax_type_id="E",
                    tax_type_code="ALL",
                    tax_rule_product_detail=[
                        TaxRuleProductDetailModel(
                            tax_rule_product_detail_id=1,
                            tax_rule_id=123,
                            product_code="220720",
                            effective_date=dateutil_parser('2022-07-28T00:00:00Z'),
                            end_date=dateutil_parser('2023-07-28T00:00:00Z'),
                            system_id=28,
                        ),
                    ],
                    rate_type_id="ReducedA",
                    rate_type_code="rate_type_code_example",
                    tax_rule_type_id="RateRule",
                    is_all_juris=False,
                    value=0,
                    cap=0,
                    threshold=0,
                    options="options_example",
                    effective_date=dateutil_parser('1970-01-01').date(),
                    end_date=dateutil_parser('1970-01-01').date(),
                    description="Freight",
                    county_fips="013",
                    is_st_pro=True,
                    country="US",
                    region="AZ",
                    sourcing="Mixed",
                    tax_type_group="SalesAndUse",
                    tax_sub_type="ALL",
                    non_passthrough_expression="non_passthrough_expression_example",
                    currency_code="currency_code_example",
                    preferred_program_id=1,
                    uom_id=1,
                    unit_of_basis="unit_of_basis_example",
                ),
            ],
            upcs=[
                UPCModel(
                    upc="023032550992",
                    legacy_tax_code="PS081282",
                    description="Yarn",
                    effective_date=dateutil_parser('1970-01-01').date(),
                    end_date=dateutil_parser('1970-01-01').date(),
                    usage=1,
                    is_system=1,
                ),
            ],
            moss_id="moss_id_example",
            moss_country="moss_country_example",
        ),
    ] # [CompanyModel] | Either a single company object or an array of companies to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create new companies
        api_response = api_instance.create_companies(x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling CompaniesApi->create_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_avalara_client** | **str**| Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . | [optional] if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
 **body** | [**[CompanyModel]**](CompanyModel.md)| Either a single company object or an array of companies to create | [optional]

### Return type

[**[CompanyModel]**](CompanyModel.md)

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

