# TransactionSummary

Summary information about an overall transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Two character ISO-3166 country code. | [optional] 
**region** | **str** | Two or three character ISO region, state or province code, if applicable. | [optional] 
**juris_type** | **str** | The type of jurisdiction that collects this tax. | [optional] 
**juris_code** | **str** | Jurisdiction Code for the taxing jurisdiction | [optional] 
**juris_name** | **str** | The name of the jurisdiction that collects this tax. | [optional] 
**tax_authority_type** | **int** | The unique ID of the Tax Authority Type that collects this tax. | [optional] 
**state_assigned_no** | **str** | The state assigned number of the jurisdiction that collects this tax. | [optional] 
**tax_type** | **str** | The tax type of this tax. | [optional] 
**tax_sub_type** | **str** | The tax subtype of this tax. | [optional] 
**tax_name** | **str** | The name of the tax. | [optional] 
**tax_group** | **str** | Group code when special grouping is enabled. | [optional] 
**rate_type** | **str** | DEPRECATED - Date: 3/1/2018, Version: 18.3, Message: Please use rateTypeCode instead.  Indicates the tax rate type. | [optional] 
**rate_type_code** | **str** | Indicates the code of the rate type.  Use [ListRateTypesByCountry](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Definitions/ListRateTypesByCountry/) API for a full list of rate type codes. | [optional] 
**taxable** | **float** | Tax Base - The adjusted taxable amount. | [optional] 
**rate** | **float** | Tax Rate - The rate of taxation, as a fraction of the amount. | [optional] 
**tax** | **float** | Tax amount - The calculated tax (Base * Rate). | [optional] 
**tax_calculated** | **float** | The amount of tax that AvaTax calculated for the transaction.                If you used a &#x60;taxOverride&#x60; of type &#x60;taxAmount&#x60;, there may be a difference between  the &#x60;tax&#x60; field which applies your override, and the &#x60;TaxCalculated&#x60; field which  represents the amount of tax that AvaTax calculated for this transaction without override.                You can use this for comparison. | [optional] 
**non_taxable** | **float** | The amount of the transaction that was non-taxable. | [optional] 
**exemption** | **float** | The amount of the transaction that was exempt. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


