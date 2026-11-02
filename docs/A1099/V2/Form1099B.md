# Form1099B

Form 1099-B: Proceeds From Broker and Barter Exchange Transactions                The recipient is the customer and the issuer is the broker or barter exchange. Each form reports one sale.                *Required:* `applicableCheckboxOnForm8949`, `descriptionOfProperty`, `proceeds` (which can be zero or negative) and  `proceedsReportedToIrs`. `typeOfGainOrLoss` is required unless `noncoveredSecurity` is `true`.                `dateSoldOrDisposed` must fall in the tax year. `dateAcquired` can't be after the tax year or before January 1 of the  year 50 years before the current filing year, whatever the form's tax year. `costOrOtherBasis`,  `washSaleLossDisallowed` and `federalIncomeTaxWithheld` can't be negative; the other amounts can.  `federalIncomeTaxWithheld` must be less than `proceeds` (zero when `proceeds` is zero or negative), and can't be more  than 24% of the other amounts on the form combined, not counting state and local withholding.                `stateAndLocalWithholding` carries `state`, `stateId`, `stateTaxWithheld`, `locality`, `localityId` and  `localTaxWithheld`. `state` and `stateId` are required when `stateTaxWithheld` has an amount. Form 1099-B has no state  or local income fields, so `stateIncome` and `localIncome` are discarded and read back as `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_checkbox_on_form8949** | **str** | Applicable checkbox on Form 8949.                * &#x60;A&#x60; - Short-term transaction, basis reported to the IRS  * &#x60;B&#x60; - Short-term transaction, basis not reported to the IRS  * &#x60;D&#x60; - Long-term transaction, basis reported to the IRS  * &#x60;E&#x60; - Long-term transaction, basis not reported to the IRS  * &#x60;X&#x60; - Basis not reported to the IRS and the holding period is unknown | 
**cusip_number** | **str** | CUSIP number (up to 13 letters or digits) | [optional] 
**description_of_property** | **str** | Description of property, such as the number of shares and the name of the stock | 
**date_acquired** | **date** | Date acquired. Can&#39;t be after the tax year or before January 1 of the year 50 years before the current  filing year (for example, 1975-01-01 when filing for 2025), whatever the form&#39;s tax year. | [optional] 
**date_sold_or_disposed** | **date** | Date sold or disposed. Must fall in the tax year. | [optional] 
**proceeds** | **float** | Proceeds. Can be zero, or negative for a loss. | 
**cost_or_other_basis** | **float** | Cost or other basis | [optional] 
**accrued_market_discount** | **float** | Accrued market discount | [optional] 
**wash_sale_loss_disallowed** | **float** | Wash sale loss disallowed | [optional] 
**type_of_gain_or_loss** | **str** | Type of gain or loss. Required unless &#x60;noncoveredSecurity&#x60; is &#x60;true&#x60;.                * &#x60;SHORT_TERM&#x60; - Short-term gain or loss  * &#x60;LONG_TERM&#x60; - Long-term gain or loss  * &#x60;ORDINARY_SHORT_TERM&#x60; - Ordinary, short-term  * &#x60;ORDINARY_LONG_TERM&#x60; - Ordinary, long-term | [optional] 
**proceeds_from** | **str** | Source of the proceeds, if they are from collectibles or a Qualified Opportunity Fund.                * &#x60;COLLECTIBLES&#x60; - Collectibles  * &#x60;QOF&#x60; - Qualified Opportunity Fund (QOF) | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld. Must be less than &#x60;proceeds&#x60; (zero when &#x60;proceeds&#x60; is zero or negative), and can&#39;t be  more than 24% of the other amounts on the form combined, not counting state and local withholding. | [optional] 
**noncovered_security** | **bool** | If checked, the security is noncovered | [optional] 
**proceeds_reported_to_irs** | **str** | Whether gross or net proceeds are reported to the IRS.                * &#x60;GROSS&#x60; - Gross proceeds  * &#x60;NET&#x60; - Net proceeds | 
**loss_not_allowed** | **bool** | If checked, the loss is not allowed based on the amount in &#x60;proceeds&#x60; | [optional] 
**profit_or_loss_realized_on_closed_contracts** | **float** | Profit or (loss) realized in the tax year on closed contracts | [optional] 
**unrealized_profit_or_loss_on_open_contracts_prior_year** | **float** | Unrealized profit or (loss) on open contracts at the end of the prior tax year | [optional] 
**unrealized_profit_or_loss_on_open_contracts_current_year** | **float** | Unrealized profit or (loss) on open contracts at the end of the tax year | [optional] 
**aggregate_profit_or_loss_on_contracts** | **float** | Aggregate profit or (loss) on contracts | [optional] 
**basis_reported_to_irs** | **bool** | If checked, the basis is reported to the IRS. Only takes effect when &#x60;noncoveredSecurity&#x60; is also checked:  otherwise it isn&#39;t sent to the IRS, and changing it doesn&#39;t trigger a correction. | [optional] 
**bartering** | **float** | Bartering | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**type** | **str** | Form type. | 
**id** | **str** | Form ID. Unique identifier set when the record is created. | [optional] [readonly] 
**issuer_id** | **str** | Issuer ID - only required when creating forms | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID - only required when creating forms via $bulk-upsert | [optional] 
**issuer_tin** | **str** | Issuer TIN - readonly | [optional] 
**tax_year** | **int** | Tax Year - only required when creating forms via $bulk-upsert | [optional] 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. | [optional] 
**tin** | **str** | Recipient&#39;s Federal Tax Identification Number (TIN). | [optional] 
**recipient_name** | **str** | DEPRECATED: Use &#x60;businessName&#x60; for businesses; use &#x60;firstName&#x60;, &#x60;middleName&#x60;, &#x60;lastName&#x60;, and &#x60;suffixName&#x60; for individuals. | [optional] 
**address** | **str** | Address. | 
**address2** | **str** | Address line 2. | [optional] 
**city** | **str** | City. | 
**state** | **str** | Two-letter US state or Canadian province code (required for US/CA addresses). | [optional] 
**zip** | **str** | ZIP/postal code. | [optional] 
**email** | **str** | Recipient&#39;s Contact email address. | [optional] 
**non_us_province** | **str** | Province or region for non-US/CA addresses. | [optional] 
**country_code** | **str** | Two-letter IRS country code (e.g., &#39;US&#39;, &#39;CA&#39;), as defined at https://www.irs.gov/e-file-providers/country-codes. | 
**federal_efile_date** | **date** | Date when federal e-filing should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_efile_date** | **date** | Date when state e-filing should be scheduled. Must be on or after federalEfileDate. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**recipient_edelivery_date** | **date** | Date when recipient e-delivery should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) | State and local withholding information | [optional] 
**federal_efile_status** | [**FederalEfileStatusDetail**](FederalEfileStatusDetail.md) | Federal e-file status.  Available values:  - unscheduled: Form has not been scheduled for federal e-filing  - scheduled: Form is scheduled for federal e-filing  - airlock: Form is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - sent: Form has been sent to the IRS  - accepted: Form was accepted by the IRS  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlock: Correction is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - corrected: A correction has been sent to the IRS  - corrected_accepted: Correction was accepted by the IRS  - rejected: Form was rejected by the IRS  - corrected_rejected: Correction was rejected by the IRS  - held: Form is held and will not be submitted to IRS (used for certain forms submitted only to states)  When the form&#39;s most recent IRIS filing was rejected or accepted with errors, &#x60;errors&#x60; lists what the IRS reported. | [optional] [readonly] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) | State e-file status.  Available values:  - unscheduled: Form has not been scheduled for state e-filing  - scheduled: Form is scheduled for state e-filing  - airlocked: Form is in process of being uploaded to the state  - sent: Form has been sent to the state  - rejected: Form was rejected by the state  - accepted: Form was accepted by the state  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlocked: Correction is in process of being uploaded to the state  - corrected_sent: Correction has been sent to the state  - corrected_rejected: Correction was rejected by the state  - corrected_accepted: Correction was accepted by the state | [optional] [readonly] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Postal mail to recipient status.  Available values:  - unscheduled: Postal mail has not been scheduled  - pending: Postal mail is pending to be sent  - sent: Postal mail has been sent  - delivered: Postal mail has been delivered | [optional] [readonly] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | TIN Match status.  Available values:  - none: TIN matching has not been performed  - pending: TIN matching request is pending  - matched: Name/TIN combination matches IRS records  - unknown: TIN is missing, invalid, or request contains errors  - rejected: Name/TIN combination does not match IRS records or TIN not currently issued | [optional] [readonly] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Address verification status.  Available values:  - unknown: Address verification has not been checked  - pending: Address verification is in progress  - failed: Address verification failed  - incomplete: Address verification is incomplete  - unchanged: User declined address changes  - verified: Address has been verified and accepted | [optional] [readonly] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | EDelivery status.  Available values:  - unscheduled: E-delivery has not been scheduled  - scheduled: E-delivery is scheduled to be sent  - sent: E-delivery has been sent to recipient  - bounced: E-delivery bounced back (invalid email)  - refused: E-delivery was refused by recipient  - bad_verify: E-delivery failed verification  - accepted: E-delivery was accepted by recipient  - bad_verify_limit: E-delivery failed verification limit reached  - second_delivery: Second e-delivery attempt  - undelivered: E-delivery is undelivered (temporary state allowing resend) | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Date time when the record was created. | [optional] [readonly] 
**updated_at** | **datetime** | Date time when the record was last updated. | [optional] [readonly] 
**tin_type** | **str** | Recipient classification.  The platform is transitioning from tax identifier classifications to recipient entity classifications. New values represent recipient entity types and should be preferred. Deprecated values represent identifier formats and remain supported for backward compatibility only.  Available values: - INDIVIDUAL: Recipient is an individual - BUSINESS: Recipient is a business - UNKNOWN: Recipient classification is unknown - EIN: (Deprecated - use BUSINESS) Employer Identification Number - SSN: (Deprecated - use INDIVIDUAL) Social Security Number - ITIN: (Deprecated - use INDIVIDUAL) Individual Taxpayer Identification Number - ATIN: (Deprecated - use INDIVIDUAL) Adoption Taxpayer Identification Number | [optional] 
**business_name** | **str** | Business name. Required when the recipient of the form is a business; should only be used for businesses. | [optional] 
**business_name2** | **str** | Business name line 2. Should only be used for businesses. | [optional] 
**first_name** | **str** | First name. Required when the recipient of the form is an individual; should only be used for individuals. | [optional] 
**middle_name** | **str** | Middle name. Should only be used for individuals. | [optional] 
**last_name** | **str** | Last name. Required when the recipient of the form is an individual; should only be used for individuals. | [optional] 
**suffix_name** | **str** | Suffix name. Should only be used for individuals. | [optional] 
**recipient_second_name** | **str** | DEPRECATED: Use &#x60;businessName2&#x60; instead. | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**no_tin** | **bool** | No TIN indicator | [optional] 
**second_tin_notice** | **bool** | Second TIN notice | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_b import Form1099B

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099B from a JSON string
form1099_b_instance = Form1099B.from_json(json)
# print the JSON string representation of the object
print(Form1099B.to_json())

# convert the object into a dict
form1099_b_dict = form1099_b_instance.to_dict()
# create an instance of Form1099B from a dict
form1099_b_from_dict = Form1099B.from_dict(form1099_b_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


