# W8BenFormMinimalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w8ben\&quot; for this model). | [optional] [readonly] 
**email** | **str** | The email address of the individual associated with the form. | 
**name** | **str** | The name of the individual or entity associated with the form. | 
**reference_number** | **str** | A reference number for the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
**reference_id** | **str** | A reference identifier for the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w8_ben_form_minimal_request import W8BenFormMinimalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W8BenFormMinimalRequest from a JSON string
w8_ben_form_minimal_request_instance = W8BenFormMinimalRequest.from_json(json)
# print the JSON string representation of the object
print(W8BenFormMinimalRequest.to_json())

# convert the object into a dict
w8_ben_form_minimal_request_dict = w8_ben_form_minimal_request_instance.to_dict()
# create an instance of W8BenFormMinimalRequest from a dict
w8_ben_form_minimal_request_from_dict = W8BenFormMinimalRequest.from_dict(w8_ben_form_minimal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


