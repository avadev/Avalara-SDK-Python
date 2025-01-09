# ForbiddenError

Returns an optional message with a 'forbidden' response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message that informs the user that they may not access a resource | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.forbidden_error import ForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenError from a JSON string
forbidden_error_instance = ForbiddenError.from_json(json)
# print the JSON string representation of the object
print(ForbiddenError.to_json())

# convert the object into a dict
forbidden_error_dict = forbidden_error_instance.to_dict()
# create an instance of ForbiddenError from a dict
forbidden_error_from_dict = ForbiddenError.from_dict(forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


