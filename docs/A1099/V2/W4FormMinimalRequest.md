# W4FormMinimalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w4\&quot; for this model). | [optional] [readonly] 
**email** | **str** | The email address of the individual associated with the form. | 
**employee_first_name** | **str** | The first name of the employee. | 
**employee_last_name** | **str** | The last name of the employee. | 
**office_code** | **str** | The office code associated with the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
**reference_id** | **str** | A reference identifier for the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w4_form_minimal_request import W4FormMinimalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W4FormMinimalRequest from a JSON string
w4_form_minimal_request_instance = W4FormMinimalRequest.from_json(json)
# print the JSON string representation of the object
print(W4FormMinimalRequest.to_json())

# convert the object into a dict
w4_form_minimal_request_dict = w4_form_minimal_request_instance.to_dict()
# create an instance of W4FormMinimalRequest from a dict
w4_form_minimal_request_from_dict = W4FormMinimalRequest.from_dict(w4_form_minimal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


