# Form1099RListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 
**gross_distribution** | **float** |  | [optional] 
**taxable_amount** | **float** |  | [optional] 
**taxable_amount_not_determined** | **bool** |  | [optional] 
**total_distribution_determined** | **bool** |  | [optional] 
**capital_gain** | **float** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
**employee_contributions_or_designated_roth_or_insurance_premiums** | **float** |  | [optional] 
**net_unrealized_appreciation_in_employer_securities** | **float** |  | [optional] 
**distribution_code** | **str** |  | [optional] 
**second_distribution_code** | **str** |  | [optional] 
**ira_sep_simple** | **bool** |  | [optional] 
**traditional_ira_sep_simple_or_roth_conversion_amount** | **float** |  | [optional] 
**other_amount** | **float** |  | [optional] 
**other_percentage** | **str** |  | [optional] 
**total_distribution_percentage** | **str** |  | [optional] 
**total_employee_contributions** | **float** |  | [optional] 
**amount_allocable_to_irr_within5_years** | **float** |  | [optional] 
**first_year_of_designated_roth_contribution** | **int** |  | [optional] 
**fatca_filing_requirement** | **bool** |  | [optional] 
**date_of_payment** | **datetime** |  | [optional] 
**issuer_id** | **str** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_tin** | **str** |  | [optional] 
**tin_type** | **int** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**street_address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**recipient_email** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**recipient_non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**federal_e_file** | **bool** |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**state_e_file** | **bool** |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**address_verification** | **bool** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_r_list_item import Form1099RListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099RListItem from a JSON string
form1099_r_list_item_instance = Form1099RListItem.from_json(json)
# print the JSON string representation of the object
print(Form1099RListItem.to_json())

# convert the object into a dict
form1099_r_list_item_dict = form1099_r_list_item_instance.to_dict()
# create an instance of Form1099RListItem from a dict
form1099_r_list_item_from_dict = Form1099RListItem.from_dict(form1099_r_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


