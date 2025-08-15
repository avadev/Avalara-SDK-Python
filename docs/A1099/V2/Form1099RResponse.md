# Form1099RResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_distribution** | **float** | Gross distribution | [optional] 
**taxable_amount** | **float** | Taxable amount | [optional] 
**taxable_amount_not_determined** | **bool** | Taxable amount not determined | [optional] 
**total_distribution_determined** | **bool** | Total distribution | [optional] 
**capital_gain** | **float** | Capital gain (included in Box 2a) | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**employee_contributions_or_designated_roth_or_insurance_premiums** | **float** | Employee contributions/Designated Roth contributions or insurance premiums | [optional] 
**net_unrealized_appreciation_in_employer_securities** | **float** | Net unrealized appreciation in employer&#39;s securities | [optional] 
**distribution_code** | **str** | Distribution code | [optional] 
**second_distribution_code** | **str** | Second distribution code | [optional] 
**ira_sep_simple** | **bool** | IRA/SEP/SIMPLE | [optional] 
**traditional_ira_sep_simple_or_roth_conversion_amount** | **float** | Traditional IRA/SEP/SIMPLE or Roth conversion amount | [optional] 
**other_amount** | **float** | Other amount | [optional] 
**other_percentage** | **str** | Other percentage | [optional] 
**total_distribution_percentage** | **str** | Total distribution percentage | [optional] 
**total_employee_contributions** | **float** | Total employee contributions | [optional] 
**amount_allocable_to_irr_within5_years** | **float** | Amount allocable to IRR within 5 years | [optional] 
**first_year_of_designated_roth_contribution** | **str** | First year of designated Roth contribution | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**date_of_payment** | **datetime** | Date of payment | [optional] 
**type** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingResponse**](StateAndLocalWithholdingResponse.md) |  | [optional] 
**tin_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**issuer_id** | **str** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_tin** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**federal_e_file** | **bool** |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**state_e_file** | **bool** |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**no_tin** | **bool** |  | [optional] 
**second_tin_notice** | **bool** |  | [optional] 
**address_verification** | **bool** |  | [optional] 
**federal_efile_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**e_delivery_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**state_efile_status** | [**List[StateEfileStatusDetailResponse]**](StateEfileStatusDetailResponse.md) |  | [optional] 
**postal_mail_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**tin_match_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**address_verification_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**validation_errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_r_response import Form1099RResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099RResponse from a JSON string
form1099_r_response_instance = Form1099RResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099RResponse.to_json())

# convert the object into a dict
form1099_r_response_dict = form1099_r_response_instance.to_dict()
# create an instance of Form1099RResponse from a dict
form1099_r_response_from_dict = Form1099RResponse.from_dict(form1099_r_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


