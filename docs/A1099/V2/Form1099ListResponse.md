# Form1099ListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Form1099ListResponseValueInner]**](Form1099ListResponseValueInner.md) | List of Form 1099 responses | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_list_response import Form1099ListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099ListResponse from a JSON string
form1099_list_response_instance = Form1099ListResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099ListResponse.to_json())

# convert the object into a dict
form1099_list_response_dict = form1099_list_response_instance.to_dict()
# create an instance of Form1099ListResponse from a dict
form1099_list_response_from_dict = Form1099ListResponse.from_dict(form1099_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


