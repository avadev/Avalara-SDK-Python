# Form1099RListItem


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
**first_year_of_designated_roth_contribution** | **int** | First year of designated Roth contribution | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**date_of_payment** | **datetime** | Date of payment | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**issuer_tin** | **str** | Issuer TIN. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**tax_year** | **int** | Tax year | 
**issuer_id** | **str** | Issuer ID | [optional] 
**reference_id** | **str** | Reference ID | [optional] 
**recipient_tin** | **str** | Recipient Tax ID Number | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | 
**state** | **str** | US state. Required if CountryCode is \&quot;US\&quot;. | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**email** | **str** | Recipient email address | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | 
**federal_e_file** | **bool** | Boolean indicating that federal e-filing should be scheduled for this form | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_e_file** | **bool** | Boolean indicating that state e-filing should be scheduled for this form | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**no_tin** | **bool** | Indicates whether the recipient has no TIN | [optional] 
**second_tin_notice** | **bool** | Second TIN notice in three years | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) | State and local withholding information | [optional] 

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


