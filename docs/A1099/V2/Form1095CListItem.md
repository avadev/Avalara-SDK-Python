# Form1095CListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_first_name** | **str** | Employee&#39;s first name | [optional] 
**employee_middle_name** | **str** | Employee&#39;s middle name | [optional] 
**employee_last_name** | **str** | Employee&#39;s last name | [optional] 
**employee_name_suffix** | **str** | Employee&#39;s name suffix | [optional] 
**recipient_date_of_birth** | **datetime** | Recipient&#39;s date of birth | [optional] 
**plan_start_month** | **str** | Plan start month | [optional] 
**offer_and_coverages** | [**List[OfferAndCoverageRequest]**](OfferAndCoverageRequest.md) | Offer and coverage information | [optional] 
**employer_provided_si_coverage** | **bool** | Employer provided self-insured coverage | [optional] 
**covered_individuals** | [**List[CoveredIndividualRequest]**](CoveredIndividualRequest.md) | Covered individuals information | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**issuer_tin** | **str** | Issuer TIN. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**tax_year** | **int** | Tax year | 
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
**fatca_filing_requirement** | **bool** | Fatca filing requirement | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) | State and local withholding information | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1095_c_list_item import Form1095CListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1095CListItem from a JSON string
form1095_c_list_item_instance = Form1095CListItem.from_json(json)
# print the JSON string representation of the object
print(Form1095CListItem.to_json())

# convert the object into a dict
form1095_c_list_item_dict = form1095_c_list_item_instance.to_dict()
# create an instance of Form1095CListItem from a dict
form1095_c_list_item_from_dict = Form1095CListItem.from_dict(form1095_c_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


