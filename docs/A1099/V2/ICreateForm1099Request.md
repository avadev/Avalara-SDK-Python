# ICreateForm1099Request


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
**fatca_filing_requirement** | **bool** | Fatca filing requirement | [optional] 
**type** | **str** |  | [optional] 
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
**rents** | **float** | Rents | [optional] 
**royalties** | **float** | Royalties | [optional] 
**other_income** | **float** | Other income | [optional] 
**fed_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**fishing_boat_proceeds** | **float** | Fishing boat proceeds | [optional] 
**medical_and_health_care_payments** | **float** | Medical and health care payments | [optional] 
**direct_sales_indicator** | **bool** | Payer made direct sales totaling $5,000 or more of consumer products to recipient for resale | [optional] 
**substitute_payments** | **float** | Substitute payments in lieu of dividends or interest | [optional] 
**crop_insurance_proceeds** | **float** | Crop insurance proceeds | [optional] 
**gross_proceeds_paid_to_attorney** | **float** | Gross proceeds paid to an attorney | [optional] 
**fish_purchased_for_resale** | **float** | Fish purchased for resale | [optional] 
**section409_a_deferrals** | **float** | Section 409A deferrals | [optional] 
**excess_golden_parachute_payments** | **float** | (Legacy field) Excess golden parachute payments | [optional] 
**nonqualified_deferred_compensation** | **float** | Nonqualified deferred compensation | [optional] 
**filer_type** | **str** | Filer type (PSE or EPF) | [optional] 
**payment_type** | **str** | Payment type (payment card or third party network) | [optional] 
**payment_settlement_entity_name_phone_number** | **str** | Payment settlement entity name and phone number | [optional] 
**gross_amount_payment_card** | **float** | Gross amount of payment card/third party network transactions | [optional] 
**card_not_present_transactions** | **float** | Card not present transactions | [optional] 
**merchant_category_code** | **str** | Merchant category code | [optional] 
**payment_transaction_number** | **float** | Number of payment transactions | [optional] 
**january** | **float** | January gross payments | [optional] 
**february** | **float** | February gross payments | [optional] 
**march** | **float** | March gross payments | [optional] 
**april** | **float** | April gross payments | [optional] 
**may** | **float** | May gross payments | [optional] 
**june** | **float** | June gross payments | [optional] 
**july** | **float** | July gross payments | [optional] 
**august** | **float** | August gross payments | [optional] 
**sept** | **float** | September gross payments | [optional] 
**october** | **float** | October gross payments | [optional] 
**november** | **float** | November gross payments | [optional] 
**december** | **float** | December gross payments | [optional] 
**nonemployee_compensation** | **float** | Nonemployee compensation | 

## Example

```python
from Avalara.SDK.models.A1099.V2.i_create_form1099_request import ICreateForm1099Request

# TODO update the JSON string below
json = "{}"
# create an instance of ICreateForm1099Request from a JSON string
i_create_form1099_request_instance = ICreateForm1099Request.from_json(json)
# print the JSON string representation of the object
print(ICreateForm1099Request.to_json())

# convert the object into a dict
i_create_form1099_request_dict = i_create_form1099_request_instance.to_dict()
# create an instance of ICreateForm1099Request from a dict
i_create_form1099_request_from_dict = ICreateForm1099Request.from_dict(i_create_form1099_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


