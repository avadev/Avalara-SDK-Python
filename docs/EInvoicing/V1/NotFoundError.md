# NotFoundError

Returns an HTTP error code and message for a 'not found' error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The three-digit HTTP error code for a not found error | [optional] 
**message** | **str** | A message about the not found error | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.not_found_error import NotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundError from a JSON string
not_found_error_instance = NotFoundError.from_json(json)
# print the JSON string representation of the object
print(NotFoundError.to_json())

# convert the object into a dict
not_found_error_dict = not_found_error_instance.to_dict()
# create an instance of NotFoundError from a dict
not_found_error_from_dict = NotFoundError.from_dict(not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


