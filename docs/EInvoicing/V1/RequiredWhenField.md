# RequiredWhenField

Mandates for which this field is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.required_when_field import RequiredWhenField

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredWhenField from a JSON string
required_when_field_instance = RequiredWhenField.from_json(json)
# print the JSON string representation of the object
print(RequiredWhenField.to_json())

# convert the object into a dict
required_when_field_dict = required_when_field_instance.to_dict()
# create an instance of RequiredWhenField from a dict
required_when_field_from_dict = RequiredWhenField.from_dict(required_when_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


