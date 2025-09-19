# Form1099Int

Form 1099-INT: Interest Imcome                *At least one of the following amounts must be provided:*   Interest Income, Interest on U.S. Savings Bonds and Treasury obligations, or Tax-Exempt Interest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_income** | **float** | Interest Income | [optional] 
**early_withdrawal_penalty** | **float** | Early Withdrawal Penalty | [optional] 
**us_savings_bonds_interest** | **float** | Interest on U.S. Savings Bonds and Treasury obligations | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**investment_expenses** | **float** | Investment Expenses | [optional] 
**foreign_tax_paid** | **float** | Foreign tax paid | [optional] 
**foreign_country** | **str** | Foreign country or U.S. possession | [optional] 
**tax_exempt_interest** | **float** | Tax-Exempt Interest | [optional] 
**specified_private_activity_bond_interest** | **float** | Specified Private activity | [optional] 
**market_discount** | **float** | Market Discount | [optional] 
**bond_premium** | **float** | Bond Premium | [optional] 
**bond_premium_on_treasury_obligations** | **float** | Bond Premium on Treasury obligations | [optional] 
**bond_premium_on_tax_exempt_bond** | **float** | Bond Premium on tax exempt bond | [optional] 
**tax_exempt_bond_cusip_number** | **str** | Tax exempt bond CUSIP no.   Enter VARIOUS if the tax-exempt interest is reported in the aggregate for multiple bonds or accounts. | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_int import Form1099Int

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Int from a JSON string
form1099_int_instance = Form1099Int.from_json(json)
# print the JSON string representation of the object
print(Form1099Int.to_json())

# convert the object into a dict
form1099_int_dict = form1099_int_instance.to_dict()
# create an instance of Form1099Int from a dict
form1099_int_from_dict = Form1099Int.from_dict(form1099_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


