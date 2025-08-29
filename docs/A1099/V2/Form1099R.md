# Form1099R

Form 1099-R: Distributions From Pensions, Annuities, Retirement or Profit-Sharing Plans, IRAs, Insurance Contracts, etc.

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
**date_of_payment** | **date** | Date of payment | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**type** | **str** | Form type | 
**id** | **str** | Form ID. Unique identifier set when the record is created. | [optional] [readonly] 
**issuer_id** | **str** | Issuer ID - only required when creating forms | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID - only required when creating forms | [optional] 
**issuer_tin** | **str** | Issuer TIN - readonly | [optional] 
**tax_year** | **int** | Tax Year - only required when creating forms | [optional] 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. | [optional] 
**tin** | **str** | Recipient&#39;s Federal Tax Identification Number (TIN). | [optional] 
**recipient_name** | **str** | Recipient name | 
**tin_type** | **str** | Type of TIN (Tax ID Number) | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address. | 
**address2** | **str** | Address line 2. | [optional] 
**city** | **str** | City. | 
**state** | **str** | Two-letter US state or Canadian province code (required for US/CA addresses). | [optional] 
**zip** | **str** | ZIP/postal code. | [optional] 
**email** | **str** | Recipient&#39;s Contact email address. | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**non_us_province** | **str** | Province or region for non-US/CA addresses. | [optional] 
**country_code** | **str** | Two-letter IRS country code (e.g., &#39;US&#39;, &#39;CA&#39;), as defined at https://www.irs.gov/e-file-providers/country-codes. | 
**federal_efile_date** | **date** | Date when federal e-filing should be scheduled for this form | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_efile_date** | **date** | Date when state e-filing should be scheduled for this form | [optional] 
**recipient_edelivery_date** | **date** | Date when recipient e-delivery should be scheduled for this form | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**no_tin** | **bool** | No TIN indicator | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) | State and local withholding information | [optional] 
**second_tin_notice** | **bool** | Second TIN notice | [optional] 
**federal_efile_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Federal e-file status | [optional] [readonly] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) | State e-file status | [optional] [readonly] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Postal mail to recipient status | [optional] [readonly] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | TIN Match status | [optional] [readonly] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Address verification status | [optional] [readonly] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | EDelivery status | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Date time when the record was created. | [optional] [readonly] 
**updated_at** | **datetime** | Date time when the record was last updated. | [optional] [readonly] 

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


