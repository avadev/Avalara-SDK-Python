# ItemParameterModel

Represents a parameter associated with an item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The parameter&#39;s name. | 
**value** | **str** | The value for the parameter. | 
**id** | **int** | The id of the parameter. | [optional] [readonly] 
**unit** | **str** | The unit of measurement code for the parameter. | [optional] 
**item_id** | **int** | The item id | [optional] 
**is_needed_for_calculation** | **bool** | This field identifies if parameter is needed for calculation | [optional] [readonly] 
**is_needed_for_returns** | **bool** | This field identifies if parameter is needed for returns | [optional] [readonly] 
**is_needed_for_classification** | **bool** | This field identifies if parameter is needed for classification | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


