# InputDataFormats

Format and version used when inputting the data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Document format | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.input_data_formats import InputDataFormats

# TODO update the JSON string below
json = "{}"
# create an instance of InputDataFormats from a JSON string
input_data_formats_instance = InputDataFormats.from_json(json)
# print the JSON string representation of the object
print(InputDataFormats.to_json())

# convert the object into a dict
input_data_formats_dict = input_data_formats_instance.to_dict()
# create an instance of InputDataFormats from a dict
input_data_formats_from_dict = InputDataFormats.from_dict(input_data_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


