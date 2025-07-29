# Form1099MiscListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**excess_golden_parachute_payments** | **float** | (Legacy field) Excess golden parachute payments | [optional] 
**nonqualified_deferred_compensation** | **float** | Nonqualified deferred compensation | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**issuer_tin** | **str** | Issuer TIN. One of &#x60;issuerReferenceId&#x60; or &#x60;issuerTin&#x60; is required. | [optional] 
**tax_year** | **int** | Tax year | 
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

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_misc_list_item import Form1099MiscListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099MiscListItem from a JSON string
form1099_misc_list_item_instance = Form1099MiscListItem.from_json(json)
# print the JSON string representation of the object
print(Form1099MiscListItem.to_json())

# convert the object into a dict
form1099_misc_list_item_dict = form1099_misc_list_item_instance.to_dict()
# create an instance of Form1099MiscListItem from a dict
form1099_misc_list_item_from_dict = Form1099MiscListItem.from_dict(form1099_misc_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


