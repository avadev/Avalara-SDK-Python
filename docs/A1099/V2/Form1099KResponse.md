# Form1099KResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filer_type** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**payment_settlement_entity_name_phone_number** | **str** |  | [optional] 
**gross_amount_payment_card** | **float** |  | [optional] 
**card_not_present_transactions** | **float** |  | [optional] 
**merchant_category_code** | **str** |  | [optional] 
**payment_transaction_number** | **float** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
**january** | **float** |  | [optional] 
**february** | **float** |  | [optional] 
**march** | **float** |  | [optional] 
**april** | **float** |  | [optional] 
**may** | **float** |  | [optional] 
**june** | **float** |  | [optional] 
**july** | **float** |  | [optional] 
**august** | **float** |  | [optional] 
**sept** | **float** |  | [optional] 
**october** | **float** |  | [optional] 
**november** | **float** |  | [optional] 
**december** | **float** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingResponse**](StateAndLocalWithholdingResponse.md) |  | [optional] 
**tin_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**issuer_id** | **str** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_tin** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**federal_e_file** | **bool** |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**state_e_file** | **bool** |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**no_tin** | **bool** |  | [optional] 
**second_tin_notice** | **bool** |  | [optional] 
**address_verification** | **bool** |  | [optional] 
**federal_efile_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**e_delivery_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**state_efile_status** | [**List[StateEfileStatusDetailResponse]**](StateEfileStatusDetailResponse.md) |  | [optional] 
**postal_mail_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**tin_match_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**address_verification_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**validation_errors** | [**List[ValidationErrorResponse]**](ValidationErrorResponse.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_k_response import Form1099KResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099KResponse from a JSON string
form1099_k_response_instance = Form1099KResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099KResponse.to_json())

# convert the object into a dict
form1099_k_response_dict = form1099_k_response_instance.to_dict()
# create an instance of Form1099KResponse from a dict
form1099_k_response_from_dict = Form1099KResponse.from_dict(form1099_k_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


