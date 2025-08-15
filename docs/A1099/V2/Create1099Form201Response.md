# Create1099Form201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the form | [readonly] 
**type** | **str** | Type of the form. Will be one of:  * 940  * 941  * 943  * 944  * 945  * 1042  * 1042-S  * 1095-B  * 1095-C  * 1097-BTC  * 1098  * 1098-C  * 1098-E  * 1098-Q  * 1098-T  * 3921  * 3922  * 5498  * 5498-ESA  * 5498-SA  * 1099-MISC  * 1099-A  * 1099-B  * 1099-C  * 1099-CAP  * 1099-DIV  * 1099-G  * 1099-INT  * 1099-K  * 1099-LS  * 1099-LTC  * 1099-NEC  * 1099-OID  * 1099-PATR  * 1099-Q  * 1099-R  * 1099-S  * 1099-SA  * T4A  * W-2  * W-2G  * 1099-HC | 
**issuer_id** | **int** | Issuer ID | 
**issuer_reference_id** | **str** | Issuer Reference ID | [optional] 
**issuer_tin** | **str** | Issuer TIN | [optional] 
**tax_year** | **int** | Tax year | [optional] 
**federal_efile** | **bool** | Boolean indicating that federal e-filing has been scheduled for this form | 
**federal_efile_status** | [**StatusDetail**](StatusDetail.md) | Federal e-file status | [optional] [readonly] 
**state_efile** | **bool** | Boolean indicating that state e-filing has been scheduled for this form | 
**state_efile_status** | [**List[StateEfileStatusDetailResponse]**](StateEfileStatusDetailResponse.md) | State e-file status | [optional] [readonly] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient has been scheduled for this form | 
**postal_mail_status** | [**StatusDetail**](StatusDetail.md) | Postal mail to recipient status | [optional] [readonly] 
**tin_match** | **bool** | Boolean indicating that TIN Matching has been scheduled for this form | 
**tin_match_status** | [**StatusDetail**](StatusDetail.md) | TIN Match status | [optional] [readonly] 
**address_verification** | **bool** | Boolean indicating that address verification has been scheduled for this form | 
**address_verification_status** | [**StatusDetail**](StatusDetail.md) | Address verification status | [optional] [readonly] 
**e_delivery_status** | [**StatusDetail**](StatusDetail.md) | EDelivery status | [optional] [readonly] 
**reference_id** | **str** | Reference ID | [optional] 
**email** | **str** | Recipient email address | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**tin** | **str** | Recipient Tax ID Number | [optional] 
**no_tin** | **bool** | Indicates whether the recipient has no TIN | [optional] 
**second_tin_notice** | **bool** | Second Tin Notice | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | US state | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | [optional] 
**account_number** | **str** | Account Number | [optional] 
**office_code** | **str** | Office Code | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**validation_errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Creation time | [optional] [readonly] 
**updated_at** | **datetime** | Update time | [optional] [readonly] 
**state_and_local_withholding** | [**StateAndLocalWithholdingResponse**](StateAndLocalWithholdingResponse.md) |  | [optional] 
**unique_form_id** | **str** | Unique form identifier | [optional] 
**recipient_date_of_birth** | **datetime** | Recipient&#39;s date of birth | [optional] 
**recipient_giin** | **str** | Recipient&#39;s GIIN (Global Intermediary Identification Number) | [optional] 
**recipient_foreign_tin** | **str** | Recipient&#39;s foreign TIN | [optional] 
**lob_code** | **str** | Limitation on benefits code | [optional] 
**income_code** | **str** | Income code | [optional] 
**gross_income** | **float** | Gross income | [optional] 
**withholding_indicator** | **str** | Withholding indicator | [optional] 
**tax_country_code** | **str** | Country code | [optional] 
**exemption_code_chap3** | **str** | Exemption code (Chapter 3) | [optional] 
**exemption_code_chap4** | **str** | Exemption code (Chapter 4) | [optional] 
**tax_rate_chap3** | **str** | Tax rate (Chapter 3) | [optional] 
**withholding_allowance** | **float** | Withholding allowance | [optional] 
**federal_tax_withheld** | **float** | Federal tax withheld | [optional] 
**tax_not_deposited_indicator** | **bool** | Tax not deposited indicator | [optional] 
**academic_indicator** | **bool** | Academic indicator | [optional] 
**tax_withheld_other_agents** | **float** | Tax withheld by other agents | [optional] 
**amount_repaid** | **float** | Amount repaid to recipient | [optional] 
**tax_paid_agent** | **float** | Tax paid by withholding agent | [optional] 
**chap3_status_code** | **str** | Chapter 3 status code | [optional] 
**chap4_status_code** | **str** | Chapter 4 status code | [optional] 
**primary_withholding_agent** | [**PrimaryWithholdingAgentResponse**](PrimaryWithholdingAgentResponse.md) | Primary withholding agent information | [optional] 
**intermediary_or_flow_through** | [**IntermediaryOrFlowThroughResponse**](IntermediaryOrFlowThroughResponse.md) | Intermediary or flow-through entity information | [optional] 
**origin_of_health_coverage_code** | **str** | Origin of health coverage code | [optional] 
**covered_individuals** | [**List[CoveredIndividualReferenceResponse]**](CoveredIndividualReferenceResponse.md) | Covered individuals information | [optional] 
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
**interest_income** | **float** | Interest Income | [optional] 
**early_withdrawal_penalty** | **float** | Early withdrawal penalty | [optional] 
**us_savings_bonds_interest** | **float** | Interest on U.S. Savings Bonds and Treasury obligations | [optional] 
**foreign_country** | **str** | Foreign country or U.S. possession | [optional] 
**tax_exempt_interest** | **float** | Tax-exempt interest | [optional] 
**specified_private_activity_bond_interest** | **float** | Specified private activity bond interest | [optional] 
**market_discount** | **float** | Market discount | [optional] 
**bond_premium** | **float** | Bond premium | [optional] 
**bond_premium_on_treasury_obligations** | **float** | Bond premium on Treasury obligations | [optional] 
**bond_premium_on_tax_exempt_bond** | **float** | Bond premium on tax exempt bond | [optional] 
**tax_exempt_bond_cusip_number** | **str** | Tax exempt bond CUSIP number | [optional] 
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
**rents** | **float** | Rents | [optional] 
**royalties** | **float** | Royalties | [optional] 
**other_income** | **float** | Other income | [optional] 
**fed_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**fishing_boat_proceeds** | **float** | Fishing boat proceeds | [optional] 
**medical_and_health_care_payments** | **float** | Medical and health care payments | [optional] 
**substitute_payments** | **float** | Substitute payments in lieu of dividends or interest | [optional] 
**direct_sales_indicator** | **bool** | Payer made direct sales totaling $5,000 or more of consumer products to recipient for resale | [optional] 
**crop_insurance_proceeds** | **float** | Crop insurance proceeds | [optional] 
**excess_golden_parachute_payments** | **float** | (Legacy field) Excess golden parachute payments | [optional] 
**gross_proceeds_paid_to_attorney** | **float** | Gross proceeds paid to an attorney | [optional] 
**fish_purchased_for_resale** | **float** | Fish purchased for resale | [optional] 
**section409_a_deferrals** | **float** | Section 409A deferrals | [optional] 
**nonqualified_deferred_compensation** | **float** | Nonqualified deferred compensation | [optional] 
**nonemployee_compensation** | **float** | Nonemployee compensation | [optional] 
**gross_distributions** | **float** | Gross distribution | [optional] 
**taxable_amount** | **float** | Taxable amount | [optional] 
**taxable_amount_not_determined** | **bool** | Taxable amount not determined | [optional] 
**total_distribution_indicator** | **bool** | Total distribution | [optional] 
**capital_gain** | **float** | Capital gain (included in Box 2a) | [optional] 
**employee_contributions** | **float** | Employee contributions/Designated Roth contributions or insurance premiums | [optional] 
**net_unrealized_appreciation** | **float** | Net unrealized appreciation in employer&#39;s securities | [optional] 
**distribution_code_required** | **str** | Distribution code | [optional] 
**distribution_code_optional** | **str** | Second distribution code | [optional] 
**ira_sep_simple_indicator** | **bool** | IRA/SEP/SIMPLE | [optional] 
**total_ira_sep_simple_distribution** | **float** | Traditional IRA/SEP/SIMPLE or Roth conversion amount | [optional] 
**other** | **float** | Other amount | [optional] 
**other_percent** | **str** | Other percentage | [optional] 
**percentage_total_distribution** | **str** | Total distribution percentage | [optional] 
**total_employee_contributions** | **float** | Total employee contributions | [optional] 
**amount_allocable_to_irr** | **float** | Amount allocable to IRR within 5 years | [optional] 
**first_year_designated_roth_contrib** | **str** | First year of designated Roth contribution | [optional] 
**date_of_payment** | **str** | Date of payment | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.create1099_form201_response import Create1099Form201Response

# TODO update the JSON string below
json = "{}"
# create an instance of Create1099Form201Response from a JSON string
create1099_form201_response_instance = Create1099Form201Response.from_json(json)
# print the JSON string representation of the object
print(Create1099Form201Response.to_json())

# convert the object into a dict
create1099_form201_response_dict = create1099_form201_response_instance.to_dict()
# create an instance of Create1099Form201Response from a dict
create1099_form201_response_from_dict = Create1099Form201Response.from_dict(create1099_form201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


