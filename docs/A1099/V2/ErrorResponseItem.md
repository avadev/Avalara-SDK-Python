# ErrorResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | An identifier for this occurrence of the problem.  It is the name of a request&#39;s field when specific to that field.  Otherwise, for other types of errors, its value is empty. | [optional] 
**detail** | **str** | An explanation specific to this occurrence of the problem. | [optional] 

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


