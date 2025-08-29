# Form1099ListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**forms** | [**List[Get1099Form200Response]**](Get1099Form200Response.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_list_request import Form1099ListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099ListRequest from a JSON string
form1099_list_request_instance = Form1099ListRequest.from_json(json)
# print the JSON string representation of the object
print(Form1099ListRequest.to_json())

# convert the object into a dict
form1099_list_request_dict = form1099_list_request_instance.to_dict()
# create an instance of Form1099ListRequest from a dict
form1099_list_request_from_dict = Form1099ListRequest.from_dict(form1099_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


