# Form1099Int


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_income** | **float** |  | [optional] 
**early_withdrawal_penalty** | **float** |  | [optional] 
**us_savings_bonds_interest** | **float** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
**investment_expenses** | **float** |  | [optional] 
**foreign_tax_paid** | **float** |  | [optional] 
**foreign_country** | **str** |  | [optional] 
**tax_exempt_interest** | **float** |  | [optional] 
**specified_private_activity_bond_interest** | **float** |  | [optional] 
**market_discount** | **float** |  | [optional] 
**bond_premium** | **float** |  | [optional] 
**bond_premium_on_treasury_obligations** | **float** |  | [optional] 
**bond_premium_on_tax_exempt_bond** | **float** |  | [optional] 
**tax_exempt_bond_cusip_number** | **str** |  | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_int import Form1099Int

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Int from a JSON string
form1099_int_instance = Form1099Int.from_json(json)
# print the JSON string representation of the object
print(Form1099Int.to_json())

# convert the object into a dict
form1099_int_dict = form1099_int_instance.to_dict()
# create an instance of Form1099Int from a dict
form1099_int_from_dict = Form1099Int.from_dict(form1099_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


