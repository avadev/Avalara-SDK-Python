# Form1099Misc

Form 1099-MISC: Miscellaneous Income

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rents** | **float** | Rents | [optional] 
**royalties** | **float** | Royalties | [optional] 
**other_income** | **float** | Other income | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_misc import Form1099Misc

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Misc from a JSON string
form1099_misc_instance = Form1099Misc.from_json(json)
# print the JSON string representation of the object
print(Form1099Misc.to_json())

# convert the object into a dict
form1099_misc_dict = form1099_misc_instance.to_dict()
# create an instance of Form1099Misc from a dict
form1099_misc_from_dict = Form1099Misc.from_dict(form1099_misc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


