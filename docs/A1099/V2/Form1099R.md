# Form1099R

Form 1099-R: Distributions From Pensions, Annuities, Retirement or Profit-Sharing Plans, IRAs, Insurance Contracts, etc.                *At least one of the following amounts must be provided:*   Gross distribution, Taxable amount, Capital gain, Employee contributions/Designated Roth contributions or insurance premiums,  Net unrealized appreciation in employer's securities, Other amount, Total employee contributions,  Traditional IRA/SEP/SIMPLE or Roth conversion amount, or Amount allocable to IRR within 5 years

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
**distribution_code** | **str** | Distribution code.    Available values:  - 1: Early distribution, no known exception (in most cases, under age 59½)  - 2: Early distribution, exception applies (under age 59½)  - 3: Disability  - 4: Death  - 5: Prohibited transaction  - 6: Section 1035 exchange (a tax-free exchange of life insurance, annuity, qualified long-term care insurance, or endowment contracts)  - 7: Normal distribution  - 8: Excess contributions plus earnings/excess deferrals (and/or earnings) taxable in payment year  - 9: Cost of current life insurance protection (premiums paid by a trustee or custodian for current insurance protection)  - A: May be eligible for 10-year tax option  - B: Designated Roth account distribution  - C: Reportable Death Benefits Under Section 6050Y(c)  - D: Annuity payments from nonqualified annuity payments and distributions from life insurance contracts that may be subject to tax under section 1411  - E: Distribution under Employee Plans Compliance Resolution System (EPCRS)  - F: Charitable gift annuity  - G: Direct rollover and rollover contribution  - H: Direct rollover of distribution from a designated Roth account to a Roth IRA  - J: Early distribution from a Roth IRA (This code may be used with a Code 8 or P)  - K: Distribution of IRA Assets Not Having A Readily Available FMV  - L: Loans treated as deemed distributions under section 72(p)  - M: Qualified Plan Loan Offsets  - N: Recharacterized IRA contribution made for year following payment year  - P: Excess contributions plus earnings/excess deferrals taxable for year prior to payment year  - Q: Qualified distribution from a Roth IRA (Distribution from a Roth IRA when the 5-year holding period has been met, and the recipient has reached 59½, has died, or is disabled)  - R: Recharacterized IRA contribution made for year prior to payment year  - S: Early distribution from a SIMPLE IRA in first 2 years no known exceptions  - T: Roth IRA distribution exception applies because participant has reached 59½, died or is disabled, but it is unknown if the 5-year period has been met  - U: Distribution from ESOP under Section 404(k)  - W: Charges or payments for purchasing qualified long-term care insurance contracts under combined arrangements | 
**second_distribution_code** | **str** | Second distribution code. Must be a valid combination with the first distribution code.  See DistributionCode property documentation for code descriptions.    Valid combinations based on first distribution code:  - 1: _, 8, B, D, K, L, M, P  - 2: _, 8, B, D, K, L, M, P  - 3: _, D  - 4: _, 8, A, B, D, G, H, K, L, M, P  - 5: _  - 6: _, W  - 7: _, A, B, D, K, L, M  - 8: _, 1, 2, 4, B, J, K  - 9: _  - A: 4, 7  - B: _, 1, 2, 4, 7, 8, G, L, M, P, U  - C: _, D  - D: 1, 2, 3, 4, 7, C  - E: _  - F: _  - G: _, 4, B, K  - H: _, 4  - J: _, 8, P  - K: 1, 2, 4, 7, 8, G  - L: _, 1, 2, 4, 7, B  - M: _, 1, 2, 4, 7, B  - N: _  - P: _, 1, 2, 4, B, J  - Q: _  - R: _  - S: _  - T: _  - U: _, B  - W: _, 6                (_ indicates no second distribution code)    (format: firstDistributionCode: availableSecondDistributionCodes) | [optional] 
**ira_sep_simple** | **bool** | IRA/SEP/SIMPLE | [optional] 
**traditional_ira_sep_simple_or_roth_conversion_amount** | **float** | Traditional IRA/SEP/SIMPLE or Roth conversion amount | [optional] 
**other_amount** | **float** | Other amount | [optional] 
**other_percentage** | **str** | Other percentage | [optional] 
**total_distribution_percentage** | **str** | Total distribution percentage | [optional] 
**total_employee_contributions** | **float** | Total employee contributions | [optional] 
**amount_allocable_to_irr_within5_years** | **float** | Amount allocable to IRR within 5 years | [optional] 
**first_year_of_designated_roth_contribution** | **str** | First year of designated Roth contribution | [optional] 
**date_of_payment** | **date** | Date of payment | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement. | [optional] 
**type** | **str** | Form type. | 
**id** | **str** | Form ID. Unique identifier set when the record is created. | [optional] [readonly] 
**issuer_id** | **str** | Issuer ID - only required when creating forms | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID - only required when creating forms via $bulk-upsert | [optional] 
**issuer_tin** | **str** | Issuer TIN - readonly | [optional] 
**tax_year** | **int** | Tax Year - only required when creating forms via $bulk-upsert | [optional] 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. | [optional] 
**tin** | **str** | Recipient&#39;s Federal Tax Identification Number (TIN). | [optional] 
**recipient_name** | **str** | Recipient name | 
**tin_type** | **str** | Tax Identification Number (TIN) type.  Available values: - EIN: Employer Identification Number - SSN: Social Security Number - ITIN: Individual Taxpayer Identification Number - ATIN: Adoption Taxpayer Identification Number | [optional] 
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
**federal_efile_date** | **date** | Date when federal e-filing should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_efile_date** | **date** | Date when state e-filing should be scheduled. Must be on or after federalEfileDate. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**recipient_edelivery_date** | **date** | Date when recipient e-delivery should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**no_tin** | **bool** | No TIN indicator | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) | State and local withholding information | [optional] 
**second_tin_notice** | **bool** | Second TIN notice | [optional] 
**federal_efile_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Federal e-file status.  Available values:  - unscheduled: Form has not been scheduled for federal e-filing  - scheduled: Form is scheduled for federal e-filing  - airlock: Form is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - sent: Form has been sent to the IRS  - accepted: Form was accepted by the IRS  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlock: Correction is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - corrected: A correction has been sent to the IRS  - corrected_accepted: Correction was accepted by the IRS  - rejected: Form was rejected by the IRS  - corrected_rejected: Correction was rejected by the IRS  - held: Form is held and will not be submitted to IRS (used for certain forms submitted only to states) | [optional] [readonly] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) | State e-file status.  Available values:  - unscheduled: Form has not been scheduled for state e-filing  - scheduled: Form is scheduled for state e-filing  - airlocked: Form is in process of being uploaded to the state  - sent: Form has been sent to the state  - rejected: Form was rejected by the state  - accepted: Form was accepted by the state  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlocked: Correction is in process of being uploaded to the state  - corrected_sent: Correction has been sent to the state  - corrected_rejected: Correction was rejected by the state  - corrected_accepted: Correction was accepted by the state | [optional] [readonly] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Postal mail to recipient status.  Available values:  - unscheduled: Postal mail has not been scheduled  - pending: Postal mail is pending to be sent  - sent: Postal mail has been sent  - delivered: Postal mail has been delivered | [optional] [readonly] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | TIN Match status.  Available values:  - none: TIN matching has not been performed  - pending: TIN matching request is pending  - matched: Name/TIN combination matches IRS records  - unknown: TIN is missing, invalid, or request contains errors  - rejected: Name/TIN combination does not match IRS records or TIN not currently issued | [optional] [readonly] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Address verification status.  Available values:  - unknown: Address verification has not been checked  - pending: Address verification is in progress  - failed: Address verification failed  - incomplete: Address verification is incomplete  - unchanged: User declined address changes  - verified: Address has been verified and accepted | [optional] [readonly] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | EDelivery status.  Available values:  - unscheduled: E-delivery has not been scheduled  - scheduled: E-delivery is scheduled to be sent  - sent: E-delivery has been sent to recipient  - bounced: E-delivery bounced back (invalid email)  - refused: E-delivery was refused by recipient  - bad_verify: E-delivery failed verification  - accepted: E-delivery was accepted by recipient  - bad_verify_limit: E-delivery failed verification limit reached  - second_delivery: Second e-delivery attempt  - undelivered: E-delivery is undelivered (temporary state allowing resend) | [optional] [readonly] 
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


