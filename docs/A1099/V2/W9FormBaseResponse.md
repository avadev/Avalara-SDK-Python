# W9FormBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the form. | [optional] 
**entry_status** | **str** | The form status. | [optional] 
**entry_status_date** | **datetime** | The timestamp for the latest status update. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | [optional] 
**display_name** | **str** | The display name associated with the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 
**archived** | **bool** | Indicates whether the form is archived. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**signed_date** | **datetime** | The date the form was signed. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**created_at** | **datetime** | The creation date of the form. | [optional] 
**updated_at** | **datetime** | The last updated date of the form. | [optional] 
**type** | **str** | The type of the response object. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_base_response import W9FormBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormBaseResponse from a JSON string
w9_form_base_response_instance = W9FormBaseResponse.from_json(json)
# print the JSON string representation of the object
print(W9FormBaseResponse.to_json())

# convert the object into a dict
w9_form_base_response_dict = w9_form_base_response_instance.to_dict()
# create an instance of W9FormBaseResponse from a dict
w9_form_base_response_from_dict = W9FormBaseResponse.from_dict(w9_form_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


