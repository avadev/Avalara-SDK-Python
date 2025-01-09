# ConditionalForField

Mandates for which this field is conditional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_mandate** | **str** |  | [optional] 
**required_when** | [**List[RequiredWhenField]**](RequiredWhenField.md) | Array of scenarios which describe when a particular field is conditional for a country mandate | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.conditional_for_field import ConditionalForField

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionalForField from a JSON string
conditional_for_field_instance = ConditionalForField.from_json(json)
# print the JSON string representation of the object
print(ConditionalForField.to_json())

# convert the object into a dict
conditional_for_field_dict = conditional_for_field_instance.to_dict()
# create an instance of ConditionalForField from a dict
conditional_for_field_from_dict = ConditionalForField.from_dict(conditional_for_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


