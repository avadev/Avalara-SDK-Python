# Form1099RListItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_distributions** | **float** | Gross distribution | [optional] 
**taxable_amount** | **float** | Taxable amount | [optional] 
**taxable_amount_not_determined** | **bool** | Taxable amount not determined | [optional] 
**total_distribution_indicator** | **bool** | Total distribution | [optional] 
**capital_gain** | **float** | Capital gain (included in Box 2a) | [optional] 
**fed_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**employee_contributions** | **float** | Employee contributions/Designated Roth contributions or insurance premiums | [optional] 
**net_unrealized_appreciation** | **float** | Net unrealized appreciation in employer&#39;s securities | [optional] 
**distribution_code_required** | **str** | Distribution code | [optional] 
**distribution_code_optional** | **str** | Second distribution code | [optional] 
**ira_sep_simple_indicator** | **bool** | IRA/SEP/SIMPLE | [optional] 
**total_ira_sep_simple_distribution** | **float** | Traditional IRA/SEP/SIMPLE or Roth conversion amount | [optional] 
**other** | **float** | Other amount | [optional] 
**other_percent** | **str** | Other percentage | [optional] 
**percentage_total_distribution** | **str** | Total distribution percentage | [optional] 
**total_employee_contributions** | **float** | Total employee contributions | [optional] 
**amount_allocable_to_irr** | **float** | Amount allocable to IRR within 5 years | [optional] 
**first_year_designated_roth_contrib** | **str** | First year of designated Roth contribution | [optional] 
**fatca_requirement_indicator** | **bool** | FATCA filing requirement | [optional] 
**date_of_payment** | **str** | Date of payment | [optional] 
**id** | **str** | ID of the form | [readonly] 
**type** | **str** | Type of the form. Will be one of:  * 940  * 941  * 943  * 944  * 945  * 1042  * 1042-S  * 1095-B  * 1095-C  * 1097-BTC  * 1098  * 1098-C  * 1098-E  * 1098-Q  * 1098-T  * 3921  * 3922  * 5498  * 5498-ESA  * 5498-SA  * 1099-MISC  * 1099-A  * 1099-B  * 1099-C  * 1099-CAP  * 1099-DIV  * 1099-G  * 1099-INT  * 1099-K  * 1099-LS  * 1099-LTC  * 1099-NEC  * 1099-OID  * 1099-PATR  * 1099-Q  * 1099-R  * 1099-S  * 1099-SA  * T4A  * W-2  * W-2G  * 1099-HC | 
**issuer_id** | **int** | Issuer ID | 
**issuer_reference_id** | **str** | Issuer Reference ID | [optional] 
**issuer_tin** | **str** | Issuer TIN | [optional] 
**tax_year** | **int** | Tax year | [optional] 
**federal_efile** | **bool** | Boolean indicating that federal e-filing has been scheduled for this form | 
**federal_efile_status** | [**StatusDetail**](StatusDetail.md) | Federal e-file status | [optional] [readonly] 
**state_efile** | **bool** | Boolean indicating that state e-filing has been scheduled for this form | 
**state_efile_status** | [**List[StateEfileStatusDetailResponse]**](StateEfileStatusDetailResponse.md) | State e-file status | [optional] [readonly] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient has been scheduled for this form | 
**postal_mail_status** | [**StatusDetail**](StatusDetail.md) | Postal mail to recipient status | [optional] [readonly] 
**tin_match** | **bool** | Boolean indicating that TIN Matching has been scheduled for this form | 
**tin_match_status** | [**StatusDetail**](StatusDetail.md) | TIN Match status | [optional] [readonly] 
**address_verification** | **bool** | Boolean indicating that address verification has been scheduled for this form | 
**address_verification_status** | [**StatusDetail**](StatusDetail.md) | Address verification status | [optional] [readonly] 
**e_delivery_status** | [**StatusDetail**](StatusDetail.md) | EDelivery status | [optional] [readonly] 
**reference_id** | **str** | Reference ID | [optional] 
**email** | **str** | Recipient email address | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**tin** | **str** | Recipient Tax ID Number | [optional] 
**no_tin** | **bool** | Indicates whether the recipient has no TIN | [optional] 
**second_tin_notice** | **bool** | Second Tin Notice | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | US state | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**non_us_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | [optional] 
**account_number** | **str** | Account Number | [optional] 
**office_code** | **str** | Office Code | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement | [optional] 
**validation_errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Creation time | [optional] [readonly] 
**updated_at** | **datetime** | Update time | [optional] [readonly] 
**state_and_local_withholding** | [**StateAndLocalWithholdingResponse**](StateAndLocalWithholdingResponse.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_r_list_item_response import Form1099RListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099RListItemResponse from a JSON string
form1099_r_list_item_response_instance = Form1099RListItemResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099RListItemResponse.to_json())

# convert the object into a dict
form1099_r_list_item_response_dict = form1099_r_list_item_response_instance.to_dict()
# create an instance of Form1099RListItemResponse from a dict
form1099_r_list_item_response_from_dict = Form1099RListItemResponse.from_dict(form1099_r_list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


