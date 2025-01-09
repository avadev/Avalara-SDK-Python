# MandateDataInputField

The Data Input Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **str** | Field ID | [optional] 
**document_type** | **str** | The document type | [optional] 
**document_version** | **str** | The document version | [optional] 
**path** | **str** | Path to this field | [optional] 
**path_type** | **str** | The type of path | [optional] 
**field_name** | **str** | Field name | [optional] 
**namespace** | [**MandateDataInputFieldNamespace**](MandateDataInputFieldNamespace.md) |  | [optional] 
**example_or_fixed_value** | **str** | An example of the content for this field | [optional] 
**accepted_values** | **List[str]** | An Array representing the acceptable values for this field | [optional] 
**documentation_link** | **str** | An example of the content for this field | [optional] 
**data_type** | **str** | The data type of this field. | [optional] 
**description** | **str** | A description of this field | [optional] 
**optionality** | **str** | Determines if the field if Required/Conditional/Optional or not required. | [optional] 
**cardinality** | **str** | Represents the number of times an element can appear within the document | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.mandate_data_input_field import MandateDataInputField

# TODO update the JSON string below
json = "{}"
# create an instance of MandateDataInputField from a JSON string
mandate_data_input_field_instance = MandateDataInputField.from_json(json)
# print the JSON string representation of the object
print(MandateDataInputField.to_json())

# convert the object into a dict
mandate_data_input_field_dict = mandate_data_input_field_instance.to_dict()
# create an instance of MandateDataInputField from a dict
mandate_data_input_field_from_dict = MandateDataInputField.from_dict(mandate_data_input_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


