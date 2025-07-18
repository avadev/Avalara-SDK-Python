# ErrorModel

Error model returned in response for all API errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | HTTP error code in 4xx or 5xx. | [optional] 
**status** | **str** | HTTP error code in 4xx or 5xx. | [optional] 
**title** | **str** | Description of the HTTP error code. | [optional] 
**detail** | **str** | Detailed error message. | [optional] 
**instance** | **str** | Error code. | [optional] 
**source** | **object** | Cause of error. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.error_model import ErrorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorModel from a JSON string
error_model_instance = ErrorModel.from_json(json)
# print the JSON string representation of the object
print(ErrorModel.to_json())

# convert the object into a dict
error_model_dict = error_model_instance.to_dict()
# create an instance of ErrorModel from a dict
error_model_from_dict = ErrorModel.from_dict(error_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


