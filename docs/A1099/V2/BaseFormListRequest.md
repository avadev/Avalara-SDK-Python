# BaseFormListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.base_form_list_request import BaseFormListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BaseFormListRequest from a JSON string
base_form_list_request_instance = BaseFormListRequest.from_json(json)
# print the JSON string representation of the object
print(BaseFormListRequest.to_json())

# convert the object into a dict
base_form_list_request_dict = base_form_list_request_instance.to_dict()
# create an instance of BaseFormListRequest from a dict
base_form_list_request_from_dict = BaseFormListRequest.from_dict(base_form_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


