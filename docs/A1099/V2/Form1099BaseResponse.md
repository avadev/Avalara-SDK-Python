# Form1099BaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the form | [readonly] 
**type** | **str** | Type of the form. Will be one of:  * 940  * 941  * 943  * 944  * 945  * 1042  * 1042-S  * 1095-B  * 1095-C  * 1097-BTC  * 1098  * 1098-C  * 1098-E  * 1098-Q  * 1098-T  * 3921  * 3922  * 5498  * 5498-ESA  * 5498-SA  * 1099-MISC  * 1099-A  * 1099-B  * 1099-C  * 1099-CAP  * 1099-DIV  * 1099-G  * 1099-INT  * 1099-K  * 1099-LS  * 1099-LTC  * 1099-NEC  * 1099-OID  * 1099-PATR  * 1099-Q  * 1099-R  * 1099-S  * 1099-SA  * T4A  * W-2  * W-2G  * 1099-HC | 
**issuer_id** | **int** | Issuer ID | 
**issuer_reference_id** | **str** | Issuer Reference ID | [optional] 
**issuer_tin** | **str** | Issuer TIN | [optional] 
**tax_year** | **int** | Tax year | [optional] 
**federal_efile** | **bool** | Boolean indicating that federal e-filing has been scheduled for this form | 
**federal_efile_status** | [**Form1099StatusDetailResponse**](Form1099StatusDetailResponse.md) | Federal e-file status | [optional] [readonly] 
**state_efile** | **bool** | Boolean indicating that state e-filing has been scheduled for this form | 
**state_efile_status** | [**List[StateEfileStatusDetailResponse]**](StateEfileStatusDetailResponse.md) | State e-file status | [optional] [readonly] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient has been scheduled for this form | 
**postal_mail_status** | [**Form1099StatusDetailResponse**](Form1099StatusDetailResponse.md) | Postal mail to recipient status | [optional] [readonly] 
**tin_match** | **bool** | Boolean indicating that TIN Matching has been scheduled for this form | 
**tin_match_status** | [**Form1099StatusDetailResponse**](Form1099StatusDetailResponse.md) | TIN Match status | [optional] [readonly] 
**address_verification** | **bool** | Boolean indicating that address verification has been scheduled for this form | 
**address_verification_status** | [**Form1099StatusDetailResponse**](Form1099StatusDetailResponse.md) | Address verification status | [optional] [readonly] 
**reference_id** | **str** | Reference ID | [optional] 
**email** | **str** | Recipient email address | [optional] 
**tin_type** | **str** | Type of TIN (Tax ID Number). Will be one of:  * SSN  * EIN  * ITIN  * ATIN | [optional] 
**tin** | **str** | Recipient Tax ID Number | [optional] 
**recipient_name** | **str** | Recipient name | [optional] 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | US state | [optional] 
**zip** | **str** | Zip/postal code | [optional] 
**foreign_province** | **str** | Foreign province | [optional] 
**country_code** | **str** | Country code, as defined at https://www.irs.gov/e-file-providers/country-codes | [optional] 
**validation_errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Creation time | [optional] [readonly] 
**updated_at** | **datetime** | Update time | [optional] [readonly] 
**state_and_local_withholding** | [**StateAndLocalWithholdingResponse**](StateAndLocalWithholdingResponse.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_base_response import Form1099BaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099BaseResponse from a JSON string
form1099_base_response_instance = Form1099BaseResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099BaseResponse.to_json())

# convert the object into a dict
form1099_base_response_dict = form1099_base_response_instance.to_dict()
# create an instance of Form1099BaseResponse from a dict
form1099_base_response_from_dict = Form1099BaseResponse.from_dict(form1099_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


