# Form1099DivListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ordinary_dividends** | **float** | Total ordinary dividends | [optional] 
**qualified_dividends** | **float** | Qualified dividends | [optional] 
**total_capital_gain_distributions** | **float** | Total capital gain distributions | [optional] 
**unrecaptured_section1250_gain** | **float** | Unrecaptured Section 1250 gain | [optional] 
**section1202_gain** | **float** | Section 1202 gain | [optional] 
**collectibles_gain** | **float** | Collectibles (28%) gain | [optional] 
**section897_ordinary_dividends** | **float** | Section 897 ordinary dividends | [optional] 
**section897_capital_gain** | **float** | Section 897 capital gain | [optional] 
**nondividend_distributions** | **float** | Nondividend distributions | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**section199_a_dividends** | **float** | Section 199A dividends | [optional] 
**investment_expenses** | **float** | Investment expenses | [optional] 
**foreign_tax_paid** | **float** | Foreign tax paid | [optional] 
**foreign_country_or_us_possession** | **str** | Foreign country or U.S. possession | [optional] 
**cash_liquidation_distributions** | **float** | Cash liquidation distributions | [optional] 
**noncash_liquidation_distributions** | **float** | Noncash liquidation distributions | [optional] 
**exempt_interest_dividends** | **float** | Exempt-interest dividends | [optional] 
**specified_private_activity_bond_interest_dividends** | **float** | Specified private activity bond interest dividends | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**issuer_tin** | **str** | Issuer TIN. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**tax_year** | **int** | Tax year | 
**issuer_id** | **str** | Issuer ID | [optional] 
**reference_id** | **str** | Reference ID | [optional] 
**recipient_tin** | **str** | Recipient Tax ID Number | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | US state. Required if CountryCode is \&quot;US\&quot;. | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**email** | **str** | Recipient email address | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_div_list_item import Form1099DivListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099DivListItem from a JSON string
form1099_div_list_item_instance = Form1099DivListItem.from_json(json)
# print the JSON string representation of the object
print(Form1099DivListItem.to_json())

# convert the object into a dict
form1099_div_list_item_dict = form1099_div_list_item_instance.to_dict()
# create an instance of Form1099DivListItem from a dict
form1099_div_list_item_from_dict = Form1099DivListItem.from_dict(form1099_div_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


