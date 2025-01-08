# ItemCatalogueInputModel

Represents an item in your company's product catalog.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_code** | **str** | A unique code representing this item. | 
**description** | **str** | A friendly description of this item in your product catalog. | 
**source** | **str** | The source of creation of this item. | 
**summary** | **str** | A summary for selection of the tax code. | [optional] 
**tax_code** | **str** | The tax code of the item. | [optional] 
**upc** | **str** | The universal product code of the item. | [optional] 
**item_group** | **str** | A way to group similar items. | [optional] 
**category** | **str** | A path to the category where item is included. | [optional] 
**properties** | **{str: (str,)}** | Additional key-description of the product. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


