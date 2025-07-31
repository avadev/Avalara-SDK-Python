# Form1042SRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_form_id** | **str** | Unique form identifier | [optional] 
**recipient_date_of_birth** | **datetime** | Recipient&#39;s date of birth | [optional] 
**recipient_giin** | **str** | Recipient&#39;s GIIN (Global Intermediary Identification Number) | [optional] 
**recipient_foreign_tin** | **str** | Recipient&#39;s foreign TIN | [optional] 
**lob_code** | **str** | Limitation on benefits code | [optional] 
**income_code** | **str** | Income code | [optional] 
**gross_income** | **float** | Gross income | [optional] 
**withholding_indicator** | **str** | Withholding indicator | [optional] 
**tax_country_code** | **str** | Country code | [optional] 
**exemption_code_chap3** | **str** | Exemption code (Chapter 3) | [optional] 
**exemption_code_chap4** | **str** | Exemption code (Chapter 4) | [optional] 
**tax_rate_chap3** | **str** | Tax rate (Chapter 3) | [optional] 
**withholding_allowance** | **float** | Withholding allowance | [optional] 
**federal_tax_withheld** | **float** | Federal tax withheld | [optional] 
**tax_not_deposited_indicator** | **bool** | Tax not deposited indicator | [optional] 
**academic_indicator** | **bool** | Academic indicator | [optional] 
**tax_withheld_other_agents** | **float** | Tax withheld by other agents | [optional] 
**amount_repaid** | **float** | Amount repaid to recipient | [optional] 
**tax_paid_agent** | **float** | Tax paid by withholding agent | [optional] 
**chap3_status_code** | **str** | Chapter 3 status code | [optional] 
**chap4_status_code** | **str** | Chapter 4 status code | [optional] 
**primary_withholding_agent** | [**PrimaryWithholdingAgentRequest**](PrimaryWithholdingAgentRequest.md) | Primary withholding agent information | [optional] 
**intermediary_or_flow_through** | [**IntermediaryOrFlowThroughRequest**](IntermediaryOrFlowThroughRequest.md) | Intermediary or flow-through entity information | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) | State and local withholding information | [optional] 
**type** | **str** |  | [optional] 
**issuer_id** | **str** | Issuer ID | [optional] 
**reference_id** | **str** | Reference ID | [optional] 
**recipient_tin** | **str** | Recipient Tax ID Number | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | 
**state** | **str** | US state. Required if CountryCode is \&quot;US\&quot;. | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**email** | **str** | Recipient email address | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | 
**federal_e_file** | **bool** | Boolean indicating that federal e-filing should be scheduled for this form | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_e_file** | **bool** | Boolean indicating that state e-filing should be scheduled for this form | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**no_tin** | **bool** | Indicates whether the recipient has no TIN | [optional] 
**second_tin_notice** | **bool** | Second TIN notice in three years | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1042_s_request import Form1042SRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Form1042SRequest from a JSON string
form1042_s_request_instance = Form1042SRequest.from_json(json)
# print the JSON string representation of the object
print(Form1042SRequest.to_json())

# convert the object into a dict
form1042_s_request_dict = form1042_s_request_instance.to_dict()
# create an instance of Form1042SRequest from a dict
form1042_s_request_from_dict = Form1042SRequest.from_dict(form1042_s_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


