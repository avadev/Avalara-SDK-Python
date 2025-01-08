# UPCModel

One Universal Product Code object as defined for your company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upc** | **str** | The 12-14 character Universal Product Code, European Article Number, or Global Trade Identification Number. | 
**description** | **str** | Description of the product to which this UPC applies. | 
**id** | **int** | The unique ID number for this UPC. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the company to which this UPC belongs. | [optional] [readonly] 
**legacy_tax_code** | **str** | Legacy Tax Code applied to any product sold with this UPC. | [optional] 
**effective_date** | **date** | If this UPC became effective on a certain date, this contains the first date on which the UPC was effective. | [optional] 
**end_date** | **date** | If this UPC expired or will expire on a certain date, this contains the last date on which the UPC was effective. | [optional] 
**usage** | **int** | A usage identifier for this UPC code. | [optional] 
**is_system** | **int** | A flag indicating whether this UPC code is attached to the AvaTax system or to a company. | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


