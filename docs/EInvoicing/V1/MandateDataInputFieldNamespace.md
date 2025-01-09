# MandateDataInputFieldNamespace

The namespace of the UBL element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The namespace prefix for the UBL Element | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.mandate_data_input_field_namespace import MandateDataInputFieldNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of MandateDataInputFieldNamespace from a JSON string
mandate_data_input_field_namespace_instance = MandateDataInputFieldNamespace.from_json(json)
# print the JSON string representation of the object
print(MandateDataInputFieldNamespace.to_json())

# convert the object into a dict
mandate_data_input_field_namespace_dict = mandate_data_input_field_namespace_instance.to_dict()
# create an instance of MandateDataInputFieldNamespace from a dict
mandate_data_input_field_namespace_from_dict = MandateDataInputFieldNamespace.from_dict(mandate_data_input_field_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


