# DataInputFieldsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **float** | Total count of results | [optional] 
**next_link** | **str** |  | [optional] 
**value** | [**List[DataInputField]**](DataInputField.md) | Array of Data Input Fields | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.data_input_fields_response import DataInputFieldsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataInputFieldsResponse from a JSON string
data_input_fields_response_instance = DataInputFieldsResponse.from_json(json)
# print the JSON string representation of the object
print(DataInputFieldsResponse.to_json())

# convert the object into a dict
data_input_fields_response_dict = data_input_fields_response_instance.to_dict()
# create an instance of DataInputFieldsResponse from a dict
data_input_fields_response_from_dict = DataInputFieldsResponse.from_dict(data_input_fields_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


