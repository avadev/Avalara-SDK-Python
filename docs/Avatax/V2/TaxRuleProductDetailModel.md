# TaxRuleProductDetailModel

Represents a tax rule product detail that changes the behavior of Avalara's tax engine for certain tax rules.                Avalara supports a two types of tax product detail.  For information about tax rule Product Types  HSCode and TaxCode                Because different types of tax rules have different behavior, some fields may change their behavior based on  the type of tax rule selected.  Please read the documentation for each field carefully and ensure that  the value you send is appropriate for the type of tax rule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_rule_product_detail_id** | **int** | The unique ID number of this Tax rule product detail. | [optional] 
**tax_rule_id** | **int** | TaxRule Id of TaxRule Product Detail entry | [optional] 
**product_code** | **str** | Product Code value | [optional] 
**effective_date** | **datetime** | The first date at which this product detail applies.  If &#x60;null&#x60;, this product detail will apply to all dates prior to the end date. | [optional] 
**end_date** | **datetime** | The last date for which this product detail applies.  If &#x60;null&#x60;, this product detail will apply to all dates after the effective date. | [optional] 
**system_id** | **int** | Represents the system Id the detail is applicable for. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


