# DataInputFieldRequiredFor

Array of CountryMandate names for which this field is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_mandate** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.data_input_field_required_for import DataInputFieldRequiredFor

# TODO update the JSON string below
json = "{}"
# create an instance of DataInputFieldRequiredFor from a JSON string
data_input_field_required_for_instance = DataInputFieldRequiredFor.from_json(json)
# print the JSON string representation of the object
print(DataInputFieldRequiredFor.to_json())

# convert the object into a dict
data_input_field_required_for_dict = data_input_field_required_for_instance.to_dict()
# create an instance of DataInputFieldRequiredFor from a dict
data_input_field_required_for_from_dict = DataInputFieldRequiredFor.from_dict(data_input_field_required_for_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


