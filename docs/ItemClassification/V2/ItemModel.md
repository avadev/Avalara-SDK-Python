# ItemModel

Represents an item in your company's product catalog.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID number of this item. | 
**item_code** | **str** | A unique code representing this item. | 
**description** | **str** | A friendly description of this item in your product catalog. | 
**company_id** | **int** | The unique ID number of the company that owns this item. | [optional] [readonly] 
**tax_code_id** | **int** | DEPRECATED - Date: 11/13/2018, Version: 18.12, Message: For identifying an &#x60;Item&#x60; with &#x60;Avalara TaxCode&#x60;, please call the [CreateItemClassification API] with your ItemCode and the Avalara TaxCode.  The unique ID number of the tax code that is applied when selling this item.  When creating or updating an item, you can either specify the Tax Code ID number or the Tax Code string; you do not need to specify both values. | [optional] 
**tax_code** | **str** | DEPRECATED - Date: 11/13/2018, Version: 18.12, Message: For identifying an &#x60;Item&#x60; with &#x60;Avalara TaxCode&#x60;, please call the [CreateItemClassification API] with your ItemCode and the Avalara TaxCode.  The unique code string of the Tax Code that is applied when selling this item.  When creating or updating an item, you can either specify the Tax Code ID number or the Tax Code string; you do not need to specify both values. | [optional] 
**item_group** | **str** | A way to group similar items. | [optional] 
**category** | **str** | A category of product | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**source** | **str** | Source of creation of this item | [optional] 
**upc** | **str** | Universal unique code for item | [optional] 
**classifications** | [**[ClassificationModel]**](ClassificationModel.md) | List of classifications that belong to this item.  A single classification consits of a productCode and a systemCode for a particular item. | [optional] 
**parameters** | [**[ItemParameterModel]**](ItemParameterModel.md) | List of item parameters. | [optional] 
**tags** | [**[ItemTagDetailModel]**](ItemTagDetailModel.md) | List of item tags. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


