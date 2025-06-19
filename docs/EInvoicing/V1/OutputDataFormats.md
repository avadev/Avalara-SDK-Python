# OutputDataFormats

Format and version used when outputting the data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Document format | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.output_data_formats import OutputDataFormats

# TODO update the JSON string below
json = "{}"
# create an instance of OutputDataFormats from a JSON string
output_data_formats_instance = OutputDataFormats.from_json(json)
# print the JSON string representation of the object
print(OutputDataFormats.to_json())

# convert the object into a dict
output_data_formats_dict = output_data_formats_instance.to_dict()
# create an instance of OutputDataFormats from a dict
output_data_formats_from_dict = OutputDataFormats.from_dict(output_data_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


