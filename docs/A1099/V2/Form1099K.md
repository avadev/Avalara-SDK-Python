# Form1099K


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
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**issuer_id** | **int** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**federal_efile** | **bool** |  | [optional] 
**federal_efile_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**state_efile** | **bool** |  | [optional] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**address_verification** | **bool** |  | [optional] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) |  | [optional] 
**reference_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**tin_type** | **str** |  | [optional] 
**fatca_filing_requirement** | **bool** |  | [optional] 
**tin** | **str** |  | [optional] 
**no_tin** | **bool** |  | [optional] 
**second_tin_notice** | **bool** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_k import Form1099K

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099K from a JSON string
form1099_k_instance = Form1099K.from_json(json)
# print the JSON string representation of the object
print(Form1099K.to_json())

# convert the object into a dict
form1099_k_dict = form1099_k_instance.to_dict()
# create an instance of Form1099K from a dict
form1099_k_from_dict = Form1099K.from_dict(form1099_k_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


