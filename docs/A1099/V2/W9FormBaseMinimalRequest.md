# W9FormBaseMinimalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type. | [optional] [readonly] 
**company_id** | **str** | The ID of the associated company. Required when creating a form. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_base_minimal_request import W9FormBaseMinimalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormBaseMinimalRequest from a JSON string
w9_form_base_minimal_request_instance = W9FormBaseMinimalRequest.from_json(json)
# print the JSON string representation of the object
print(W9FormBaseMinimalRequest.to_json())

# convert the object into a dict
w9_form_base_minimal_request_dict = w9_form_base_minimal_request_instance.to_dict()
# create an instance of W9FormBaseMinimalRequest from a dict
w9_form_base_minimal_request_from_dict = W9FormBaseMinimalRequest.from_dict(w9_form_base_minimal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


