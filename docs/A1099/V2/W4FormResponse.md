# W4FormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_first_name** | **str** | The first name of the employee. | [optional] 
**employee_middle_name** | **str** | The middle name of the employee. | [optional] 
**employee_last_name** | **str** | The last name of the employee. | [optional] 
**employee_name_suffix** | **str** | The name suffix of the employee. | [optional] 
**tin_type** | **str** | The type of TIN provided. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**address** | **str** | The address of the employee. | [optional] 
**city** | **str** | The city of residence of the employee. | [optional] 
**state** | **str** | The state of residence of the employee. | [optional] 
**zip** | **str** | The ZIP code of residence of the employee. | [optional] 
**marital_status** | **str** | The marital status of the employee. | [optional] 
**last_name_differs** | **bool** | Indicates whether the last name differs from prior records. | [optional] 
**num_allowances** | **int** | The number of allowances claimed by the employee. | [optional] 
**other_dependents** | **int** | The number of dependents other than allowances. | [optional] 
**non_job_income** | **float** | The amount of non-job income. | [optional] 
**deductions** | **float** | The amount of deductions claimed. | [optional] 
**additional_withheld** | **float** | The additional amount withheld. | [optional] 
**exempt_from_withholding** | **bool** | Indicates whether the employee is exempt from withholding. | [optional] 
**office_code** | **str** | The office code associated with the form. | [optional] 
**id** | **str** | The unique identifier for the form. | [optional] 
**type** | **str** | The form type. | [optional] 
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

## Example

```python
from Avalara.SDK.models.A1099.V2.w4_form_response import W4FormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of W4FormResponse from a JSON string
w4_form_response_instance = W4FormResponse.from_json(json)
# print the JSON string representation of the object
print(W4FormResponse.to_json())

# convert the object into a dict
w4_form_response_dict = w4_form_response_instance.to_dict()
# create an instance of W4FormResponse from a dict
w4_form_response_from_dict = W4FormResponse.from_dict(w4_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


