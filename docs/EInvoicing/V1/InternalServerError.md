# InternalServerError

Returns an optional message with a 'InternalServerError' response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | A bad request error code | [optional] 
**message** | **str** | A message explaining the bad request error | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.internal_server_error import InternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerError from a JSON string
internal_server_error_instance = InternalServerError.from_json(json)
# print the JSON string representation of the object
print(InternalServerError.to_json())

# convert the object into a dict
internal_server_error_dict = internal_server_error_instance.to_dict()
# create an instance of InternalServerError from a dict
internal_server_error_from_dict = InternalServerError.from_dict(internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


