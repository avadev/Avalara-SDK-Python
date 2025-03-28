# CompanyModel

A company or business entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID number of this company. | 
**account_id** | **int** | The unique ID number of the account this company belongs to. | 
**name** | **str** | The name of this company, as shown to customers. | 
**default_country** | **str** | The two character ISO-3166 country code of the default country for this company. | 
**parent_company_id** | **int** | If this company is fully owned by another company, this is the unique identity of the parent company. | [optional] 
**sst_pid** | **str** | If this company files Streamlined Sales Tax, this is the PID of this company as defined by the Streamlined Sales Tax governing board. | [optional] 
**company_code** | **str** | A unique code that references this company within your account. | [optional] 
**is_default** | **bool** | This flag is true if this company is the default company for this account.  Only one company may be set as the default. | [optional] 
**default_location_id** | **int** | If set, this is the unique ID number of the default location for this company. | [optional] 
**is_active** | **bool** | This flag indicates whether tax activity can occur for this company.  Set this flag to true to permit the company to process transactions. | [optional] 
**taxpayer_id_number** | **str** | For United States companies, this field contains your Taxpayer Identification Number.  This is a nine digit number that is usually called an EIN for an Employer Identification Number if this company is a corporation,  or SSN for a Social Security Number if this company is a person.  This value is required if the address provided is inside the US and if you subscribed to the Avalara Managed Returns or SST Certified Service Provider service. Otherwise it is optional. | [optional] 
**is_fein** | **bool** | Set this field to true if the taxPayerIdNumber is a FEIN. | [optional] 
**has_profile** | **bool** | Set this flag to true to give this company its own unique tax profile.  If this flag is true, this company will have its own Nexus, TaxRule, TaxCode, and Item definitions.  If this flag is false, this company will inherit all profile values from its parent. | [optional] 
**is_reporting_entity** | **bool** | Set this flag to true if this company must file its own tax returns.  For users who have Returns enabled, this flag turns on monthly Worksheet generation for the company. | [optional] 
**sst_effective_date** | **date** | If this company participates in Streamlined Sales Tax, this is the date when the company joined the SST program. | [optional] 
**base_currency_code** | **str** | This is the three character ISO-4217 currency code of the default currency used by this company. | [optional] 
**rounding_level_id** | **str** | Indicates whether this company prefers to round amounts at the document level or line level. | [optional] 
**warnings_enabled** | **bool** | Set this value to true to receive warnings in API calls via SOAP. | [optional] 
**is_test** | **bool** | Set this flag to true to indicate that this company is a test company.  If you have Returns enabled, Test companies will not file tax returns and can be used for validation purposes. | [optional] 
**tax_dependency_level_id** | **str** | Used to apply tax detail dependency at a jurisdiction level. | [optional] 
**in_progress** | **bool** | Set this value to true to indicate that you are still working to finish configuring this company.  While this value is true, no tax reporting will occur and the company will not be usable for transactions. | [optional] 
**business_identification_no** | **str** | Business Identification No | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**contacts** | [**[ContactModel]**](ContactModel.md) | Optional: A list of contacts defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;Contacts&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**items** | [**[ItemModel]**](ItemModel.md) | Optional: A list of items defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;Items&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**locations** | [**[LocationModel]**](LocationModel.md) | Optional: A list of locations defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;Locations&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**nexus** | [**[NexusModel]**](NexusModel.md) | Optional: A list of nexus defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;Nexus&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**settings** | [**[SettingModel]**](SettingModel.md) | Optional: A list of settings defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;Settings&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**tax_codes** | [**[TaxCodeModel]**](TaxCodeModel.md) | Optional: A list of tax codes defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;TaxCodes&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**tax_rules** | [**[TaxRuleModel]**](TaxRuleModel.md) | Optional: A list of tax rules defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;TaxRules&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**upcs** | [**[UPCModel]**](UPCModel.md) | Optional: A list of UPCs defined for this company.  To fetch this list, add the query string &#x60;?$include&#x3D;UPCs&#x60; to your URL.                When calling &#x60;CreateCompany&#x60;, you may provide a list of objects in this element and they will be created alongside the company.  The &#x60;UpdateCompany&#x60; API does not permit updating nested objects. | [optional] 
**non_reporting_child_companies** | [**[CompanyModel]**](CompanyModel.md) | Optional: A list of non reporting child companies associated with this company.  To fetch this list, add the query string &#x60;?$include&#x3D;NonReportingChildren&#x60; to your URL. | [optional] [readonly] 
**exempt_certs** | [**[EcmsModel]**](EcmsModel.md) | DEPRECATED - Date: 9/15/2017, Version: 17.10, Message: Please use the &#x60;ListCertificates&#x60; API.   | [optional] [readonly] 
**moss_id** | **str** | The unique identifier of the mini-one-stop-shop used for Value Added Tax (VAT) processing. | [optional] 
**moss_country** | **str** | The country code of the mini-one-stop-shop used for Value Added Tax (VAT) processing. | [optional] 
**parameters** | [**[CompanyParameterDetailModel]**](CompanyParameterDetailModel.md) | The parameters of a company | [optional] [readonly] 
**supplierandcustomers** | [**[CustomerSupplierModel]**](CustomerSupplierModel.md) | The customers and suppliers of a company | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


