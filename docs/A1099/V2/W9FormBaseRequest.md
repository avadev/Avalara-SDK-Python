# W9FormBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type. | [optional] [readonly] 
**company_id** | **str** | The ID of the associated company. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_base_request import W9FormBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormBaseRequest from a JSON string
w9_form_base_request_instance = W9FormBaseRequest.from_json(json)
# print the JSON string representation of the object
print(W9FormBaseRequest.to_json())

# convert the object into a dict
w9_form_base_request_dict = w9_form_base_request_instance.to_dict()
# create an instance of W9FormBaseRequest from a dict
w9_form_base_request_from_dict = W9FormBaseRequest.from_dict(w9_form_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


