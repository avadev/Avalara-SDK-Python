# DataInputField

The Data Input Field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field UUID | [optional] 
**field_id** | **str** | Field ID | [optional] 
**applicable_document_roots** | **[dict]** |  | [optional] 
**path** | **str** | Path to this field | [optional] 
**name_space** | **str** | Namespace of this field | [optional] 
**field_name** | **str** | Field name | [optional] 
**example_or_fixed_value** | **str** | An example of the content for this field | [optional] 
**accepted_values** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An object representing the acceptable values for this field | [optional] 
**documentation_link** | **str** | An example of the content for this field | [optional] 
**description** | **str** | A description of this field | [optional] 
**is_segment** | **bool** | Is this a segment of the schema | [optional] 
**required_for** | [**DataInputFieldRequiredFor**](DataInputFieldRequiredFor.md) |  | [optional] 
**conditional_for** | [**[ConditionalForField]**](ConditionalForField.md) |  | [optional] 
**not_used_for** | [**DataInputFieldNotUsedFor**](DataInputFieldNotUsedFor.md) |  | [optional] 
**optional_for** | [**DataInputFieldOptionalFor**](DataInputFieldOptionalFor.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


