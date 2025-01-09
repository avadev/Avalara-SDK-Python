# DataInputField

The Data Input Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Field UUID | [optional] 
**field_id** | **str** | Field ID | [optional] 
**applicable_document_roots** | **List[object]** |  | [optional] 
**path** | **str** | Path to this field | [optional] 
**namespace** | **str** | Namespace of this field | [optional] 
**field_name** | **str** | Field name | [optional] 
**example_or_fixed_value** | **str** | An example of the content for this field | [optional] 
**accepted_values** | **object** | An object representing the acceptable values for this field | [optional] 
**documentation_link** | **str** | An example of the content for this field | [optional] 
**description** | **str** | A description of this field | [optional] 
**is_segment** | **bool** | Is this a segment of the schema | [optional] 
**required_for** | [**DataInputFieldRequiredFor**](DataInputFieldRequiredFor.md) |  | [optional] 
**conditional_for** | [**List[ConditionalForField]**](ConditionalForField.md) |  | [optional] 
**not_used_for** | [**DataInputFieldNotUsedFor**](DataInputFieldNotUsedFor.md) |  | [optional] 
**optional_for** | [**DataInputFieldOptionalFor**](DataInputFieldOptionalFor.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.data_input_field import DataInputField

# TODO update the JSON string below
json = "{}"
# create an instance of DataInputField from a JSON string
data_input_field_instance = DataInputField.from_json(json)
# print the JSON string representation of the object
print(DataInputField.to_json())

# convert the object into a dict
data_input_field_dict = data_input_field_instance.to_dict()
# create an instance of DataInputField from a dict
data_input_field_from_dict = DataInputField.from_dict(data_input_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


