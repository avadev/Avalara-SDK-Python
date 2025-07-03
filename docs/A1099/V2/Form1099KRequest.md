# Form1099KRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filer_type** | **int** |  | [optional] 
**payment_type** | **int** |  | [optional] 
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
**issuer_id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_tin** | **str** |  | [optional] 
**tin_type** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**recipient_email** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**office_code** | **str** |  | [optional] 
**recipient_non_us_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**federal_e_file** | **bool** |  | [optional] 
**postal_mail** | **bool** |  | [optional] 
**state_e_file** | **bool** |  | [optional] 
**tin_match** | **bool** |  | [optional] 
**address_verification** | **bool** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) |  | [optional] 

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


