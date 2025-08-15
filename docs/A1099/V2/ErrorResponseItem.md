# ErrorResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.error_response_item import ErrorResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseItem from a JSON string
error_response_item_instance = ErrorResponseItem.from_json(json)
# print the JSON string representation of the object
print(ErrorResponseItem.to_json())

# convert the object into a dict
error_response_item_dict = error_response_item_instance.to_dict()
# create an instance of ErrorResponseItem from a dict
error_response_item_from_dict = ErrorResponseItem.from_dict(error_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


