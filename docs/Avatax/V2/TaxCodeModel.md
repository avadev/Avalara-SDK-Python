# TaxCodeModel

Represents a tax code that can be applied to items on a transaction.  A tax code can have specific rules for specific jurisdictions that change the tax calculation behavior.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | **str** | A code string that identifies this tax code. | 
**tax_code_type_id** | **str** | The type of this tax code. | 
**id** | **int** | The unique ID number of this tax code. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the company that owns this tax code. | [optional] [readonly] 
**description** | **str** | A friendly description of this tax code. | [optional] 
**parent_tax_code** | **str** | If this tax code is a subset of a different tax code, this identifies the parent code. | [optional] 
**is_physical** | **bool** | True if this tax code type refers to a physical object.  Read only field. | [optional] [readonly] 
**goods_service_code** | **int** | The Avalara Goods and Service Code represented by this tax code. | [optional] 
**entity_use_code** | **str** | The Avalara Entity Use Code represented by this tax code. | [optional] 
**is_active** | **bool** | True if this tax code is active and can be used in transactions. | [optional] 
**is_sst_certified** | **bool** | True if this tax code has been certified by the Streamlined Sales Tax governing board.  By default, you should leave this value empty. | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


