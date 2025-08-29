# Form1095C

Form 1095-C: Employer-Provided Health Insurance Offer and Coverage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_first_name** | **str** | Employee&#39;s first name | 
**employee_middle_name** | **str** | Employee&#39;s middle name | [optional] 
**employee_last_name** | **str** | Employee&#39;s last name | 
**employee_name_suffix** | **str** | Employee&#39;s name suffix | [optional] 
**recipient_date_of_birth** | **date** | Recipient&#39;s date of birth | [optional] 
**plan_start_month** | **str** | Plan start month.  The calendar month during which the plan year begins of the health plan in which the employee is offered coverage (or would be offered coverage if the employee were eligible to participate in the plan).  Available values:  - 00: None  - 01: January  - 02: February  - 03: March  - 04: April  - 05: May  - 06: June  - 07: July  - 08: August  - 09: September  - 10: October  - 11: November  - 12: December | 
**employer_provided_si_coverage** | **bool** | Employer provided self-insured coverage | [optional] 
**offer_and_coverages** | [**List[OfferAndCoverage]**](OfferAndCoverage.md) | Offer and coverage information | 
**covered_individuals** | [**List[CoveredIndividual]**](CoveredIndividual.md) | Covered individuals information | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1095_c import Form1095C

# TODO update the JSON string below
json = "{}"
# create an instance of Form1095C from a JSON string
form1095_c_instance = Form1095C.from_json(json)
# print the JSON string representation of the object
print(Form1095C.to_json())

# convert the object into a dict
form1095_c_dict = form1095_c_instance.to_dict()
# create an instance of Form1095C from a dict
form1095_c_from_dict = Form1095C.from_dict(form1095_c_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


