# CreateAndSendW9FormEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type. | [optional] [readonly] 
**email** | **str** | The email address of the individual associated with the form. | 
**employee_first_name** | **str** | The first name of the employee. | 
**employee_last_name** | **str** | The last name of the employee. | 
**office_code** | **str** | The office code associated with the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**name** | **str** | The name of the individual or entity associated with the form. | 
**reference_number** | **str** | A reference number for the form. | [optional] 
**account_number** | **str** | The account number associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.create_and_send_w9_form_email_request import CreateAndSendW9FormEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAndSendW9FormEmailRequest from a JSON string
create_and_send_w9_form_email_request_instance = CreateAndSendW9FormEmailRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAndSendW9FormEmailRequest.to_json())

# convert the object into a dict
create_and_send_w9_form_email_request_dict = create_and_send_w9_form_email_request_instance.to_dict()
# create an instance of CreateAndSendW9FormEmailRequest from a dict
create_and_send_w9_form_email_request_from_dict = CreateAndSendW9FormEmailRequest.from_dict(create_and_send_w9_form_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


