# W9FormMinimalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w9\&quot; for this model). | [optional] [readonly] 
**email** | **str** | The email address of the individual associated with the form. | 
**name** | **str** | The name of the individual or entity associated with the form. | 
**account_number** | **str** | The account number associated with the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
**reference_id** | **str** | A reference identifier for the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_minimal_request import W9FormMinimalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormMinimalRequest from a JSON string
w9_form_minimal_request_instance = W9FormMinimalRequest.from_json(json)
# print the JSON string representation of the object
print(W9FormMinimalRequest.to_json())

# convert the object into a dict
w9_form_minimal_request_dict = w9_form_minimal_request_instance.to_dict()
# create an instance of W9FormMinimalRequest from a dict
w9_form_minimal_request_from_dict = W9FormMinimalRequest.from_dict(w9_form_minimal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


