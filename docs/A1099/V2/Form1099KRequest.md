# Form1099KRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filer_type** | **str** | Filer type (PSE or EPF) | [optional] 
**payment_type** | **str** | Payment type (payment card or third party network) | [optional] 
**payment_settlement_entity_name_phone_number** | **str** | Payment settlement entity name and phone number | [optional] 
**gross_amount_payment_card** | **float** | Gross amount of payment card/third party network transactions | [optional] 
**card_not_present_transactions** | **float** | Card not present transactions | [optional] 
**merchant_category_code** | **str** | Merchant category code | [optional] 
**payment_transaction_number** | **float** | Number of payment transactions | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_k_request import Form1099KRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099KRequest from a JSON string
form1099_k_request_instance = Form1099KRequest.from_json(json)
# print the JSON string representation of the object
print(Form1099KRequest.to_json())

# convert the object into a dict
form1099_k_request_dict = form1099_k_request_instance.to_dict()
# create an instance of Form1099KRequest from a dict
form1099_k_request_from_dict = Form1099KRequest.from_dict(form1099_k_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


