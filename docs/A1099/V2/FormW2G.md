# FormW2G

Form W-2G: Certain Gambling Winnings                The recipient is the winner and the issuer is the payer.                *Required:* `reportableWinnings`, `dateWon`, which must fall in the tax year, and `typeOfWager`.  `reportableWinnings` only has to be present; zero is accepted.                When the issuer's account checks for reasonable withholding, `federalIncomeTaxWithheld` can't be more than  31.58% of `reportableWinnings` and `winningsFromIdenticalWagers` combined (40% in January).                The text fields are not length-checked, but only the first 15 characters (`transaction`, `firstId` and `secondId`)  or 5 characters (`race`, `cashier` and `window`) are e-filed.                `state` and `stateId` are required when `stateTaxWithheld` has an amount. W-2G has no locality ID field, so  `localityId` is discarded and reads back as `null`.                Form W-2G has no second TIN notice, so `secondTinNotice` is discarded and reads back as `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reportable_winnings** | **float** | Reportable winnings | 
**date_won** | **date** | Date won. Must fall in the tax year. | 
**type_of_wager** | **str** | Type of wager.                * &#x60;1&#x60; - Horse race track (or off-track betting of a horse track nature)  * &#x60;2&#x60; - Dog race track (or off-track betting of a dog track nature)  * &#x60;3&#x60; - Jai-alai  * &#x60;4&#x60; - State-conducted lottery  * &#x60;5&#x60; - Keno  * &#x60;6&#x60; - Bingo  * &#x60;7&#x60; - Slot machines  * &#x60;8&#x60; - Poker winnings  * &#x60;9&#x60; - Any other type of gambling winnings                Any other code is treated as missing, so the form is saved with a \&quot;can&#39;t be blank\&quot; error on  &#x60;#/box_3_type_wager&#x60;. | 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**transaction** | **str** | Transaction, such as the ticket or card number | [optional] 
**race** | **str** | Race, such as the race or game number | [optional] 
**winnings_from_identical_wagers** | **float** | Winnings from identical wagers | [optional] 
**cashier** | **str** | Cashier | [optional] 
**window** | **str** | Window | [optional] 
**first_id** | **str** | First identification of the winner, such as a driver&#39;s license number | [optional] 
**second_id** | **str** | Second identification of the winner | [optional] 
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
from Avalara.SDK.models.A1099.V2.form_w2_g import FormW2G

# TODO update the JSON string below
json = "{}"
# create an instance of FormW2G from a JSON string
form_w2_g_instance = FormW2G.from_json(json)
# print the JSON string representation of the object
print(FormW2G.to_json())

# convert the object into a dict
form_w2_g_dict = form_w2_g_instance.to_dict()
# create an instance of FormW2G from a dict
form_w2_g_from_dict = FormW2G.from_dict(form_w2_g_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


