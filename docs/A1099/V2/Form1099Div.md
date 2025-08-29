# Form1099Div

Form 1099-DIV: Dividends and Distributions

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
from Avalara.SDK.models.A1099.V2.form1099_div import Form1099Div

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Div from a JSON string
form1099_div_instance = Form1099Div.from_json(json)
# print the JSON string representation of the object
print(Form1099Div.to_json())

# convert the object into a dict
form1099_div_dict = form1099_div_instance.to_dict()
# create an instance of Form1099Div from a dict
form1099_div_from_dict = Form1099Div.from_dict(form1099_div_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


