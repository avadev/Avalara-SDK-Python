# IUpdateForm1099Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ordinary_dividends** | **str** | Total ordinary dividends | [optional] 
**qualified_dividends** | **str** | Qualified dividends | [optional] 
**total_capital_gain_distr** | **str** | Total capital gain distributions | [optional] 
**unrecap_sec1250_gain** | **str** | Unrecaptured Section 1250 gain | [optional] 
**section1202_gain** | **str** | Section 1202 gain | [optional] 
**collectibles_gain** | **str** | Collectibles (28%) gain | [optional] 
**section897_ordinary_dividends** | **str** | Section 897 ordinary dividends | [optional] 
**section897_capital_gain** | **str** | Section 897 capital gain | [optional] 
**nondividend_distributions** | **str** | Nondividend distributions | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**section199_a_dividends** | **str** | Section 199A dividends | [optional] 
**investment_expenses** | **str** | Investment expenses | [optional] 
**foreign_tax_paid** | **str** | Foreign tax paid | [optional] 
**foreign_country_or_us_possession** | **str** | Foreign country or U.S. possession | [optional] 
**cash_liquidation_distributions** | **str** | Cash liquidation distributions | [optional] 
**noncash_liquidation_distributions** | **str** | Noncash liquidation distributions | [optional] 
**exempt_interest_dividends** | **str** | Exempt-interest dividends | [optional] 
**specified_private_activity_bond_interest_dividends** | **str** | Specified private activity bond interest dividends | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**type** | **str** |  | [optional] 
**issuer_id** | **str** | Issuer ID | [optional] 
**reference_id** | **str** | Reference ID | [optional] 
**recipient_tin** | **str** | Recipient Tax ID Number | [optional] 
**recipient_name** | **str** | Recipient name | 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | 
**state** | **str** | US state. Required if CountryCode is \&quot;US\&quot;. | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**recipient_email** | **str** | Recipient email address | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**recipient_non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | 
**federal_e_file** | **bool** | Boolean indicating that federal e-filing should be scheduled for this form | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_e_file** | **bool** | Boolean indicating that state e-filing should be scheduled for this form | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) | State and local withholding information | [optional] 
**second_tin_notice** | **bool** | Second TIN notice | [optional] 
**rents** | **float** | Rents | [optional] 
**royalties** | **float** | Royalties | [optional] 
**other_income** | **float** | Other income | [optional] 
**fed_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**fishing_boat_proceeds** | **float** | Fishing boat proceeds | [optional] 
**medical_health_care_payments** | **float** | Medical and health care payments | [optional] 
**direct_sales_indicator** | **bool** | Payer made direct sales totaling $5,000 or more of consumer products to recipient for resale | [optional] 
**substitute_payments** | **float** | Substitute payments in lieu of dividends or interest | [optional] 
**crop_insurance_proceeds** | **float** | Crop insurance proceeds | [optional] 
**gross_proceeds_paid_to_attorney** | **float** | Gross proceeds paid to an attorney | [optional] 
**fish_purchased_for_resale** | **float** | Fish purchased for resale | [optional] 
**section409_a_deferrals** | **float** | Section 409A deferrals | [optional] 
**excess_golden_parachute_payments** | **float** | (Legacy field) Excess golden parachute payments | [optional] 
**nonqualified_deferred_compensation** | **float** | Nonqualified deferred compensation | [optional] 
**nonemployee_compensation** | **float** | Nonemployee compensation | 

## Example

```python
from Avalara.SDK.models.A1099.V2.i_update_form1099_request import IUpdateForm1099Request

# TODO update the JSON string below
json = "{}"
# create an instance of IUpdateForm1099Request from a JSON string
i_update_form1099_request_instance = IUpdateForm1099Request.from_json(json)
# print the JSON string representation of the object
print(IUpdateForm1099Request.to_json())

# convert the object into a dict
i_update_form1099_request_dict = i_update_form1099_request_instance.to_dict()
# create an instance of IUpdateForm1099Request from a dict
i_update_form1099_request_from_dict = IUpdateForm1099Request.from_dict(i_update_form1099_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


