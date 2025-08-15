# Form1099R


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_distributions** | **float** |  | [optional] 
**taxable_amount** | **float** |  | [optional] 
**taxable_amount_not_determined** | **bool** |  | [optional] 
**total_distribution_indicator** | **bool** |  | [optional] 
**capital_gain** | **float** |  | [optional] 
**fed_income_tax_withheld** | **float** |  | [optional] 
**employee_contributions** | **float** |  | [optional] 
**net_unrealized_appreciation** | **float** |  | [optional] 
**distribution_code_required** | **str** |  | [optional] 
**distribution_code_optional** | **str** |  | [optional] 
**ira_sep_simple_indicator** | **bool** |  | [optional] 
**total_ira_sep_simple_distribution** | **float** |  | [optional] 
**other** | **float** |  | [optional] 
**other_percent** | **str** |  | [optional] 
**percentage_total_distribution** | **str** |  | [optional] 
**total_employee_contributions** | **float** |  | [optional] 
**amount_allocable_to_irr** | **float** |  | [optional] 
**first_year_designated_roth_contrib** | **str** |  | [optional] 
**date_of_payment** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issuer_id** | **int** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**federal_efile** | **bool** |  | [optional] 
**federal_efile_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**state_efile** | **bool** |  | [optional] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**address_verification** | **bool** |  | [optional] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**reference_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**tin_type** | **str** |  | [optional] 
**fatca_filing_requirement** | **bool** |  | [optional] 
**tin** | **str** |  | [optional] 
**no_tin** | **bool** |  | [optional] 
**second_tin_notice** | **bool** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_r import Form1099R

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099R from a JSON string
form1099_r_instance = Form1099R.from_json(json)
# print the JSON string representation of the object
print(Form1099R.to_json())

# convert the object into a dict
form1099_r_dict = form1099_r_instance.to_dict()
# create an instance of Form1099R from a dict
form1099_r_from_dict = Form1099R.from_dict(form1099_r_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


