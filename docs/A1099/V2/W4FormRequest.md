# W4FormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w4\&quot; for this model). | [optional] [readonly] 
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
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w4_form_request import W4FormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W4FormRequest from a JSON string
w4_form_request_instance = W4FormRequest.from_json(json)
# print the JSON string representation of the object
print(W4FormRequest.to_json())

# convert the object into a dict
w4_form_request_dict = w4_form_request_instance.to_dict()
# create an instance of W4FormRequest from a dict
w4_form_request_from_dict = W4FormRequest.from_dict(w4_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


