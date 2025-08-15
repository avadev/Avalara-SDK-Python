# Form1095BRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_first_name** | **str** | Employee&#39;s first name | [optional] 
**employee_middle_name** | **str** | Employee&#39;s middle name | [optional] 
**employee_last_name** | **str** | Employee&#39;s last name | [optional] 
**employee_name_suffix** | **str** | Employee&#39;s name suffix | [optional] 
**employee_date_of_birth** | **datetime** | Employee&#39;s date of birth | [optional] 
**origin_of_health_coverage_code** | **str** | Origin of health coverage code | [optional] 
**covered_individuals** | [**List[CoveredIndividualRequest]**](CoveredIndividualRequest.md) | Covered individuals information | [optional] 
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
**fatca_filing_requirement** | **bool** | Fatca filing requirement | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) | State and local withholding information | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1095_b_request import Form1095BRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Form1095BRequest from a JSON string
form1095_b_request_instance = Form1095BRequest.from_json(json)
# print the JSON string representation of the object
print(Form1095BRequest.to_json())

# convert the object into a dict
form1095_b_request_dict = form1095_b_request_instance.to_dict()
# create an instance of Form1095BRequest from a dict
form1095_b_request_from_dict = Form1095BRequest.from_dict(form1095_b_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


