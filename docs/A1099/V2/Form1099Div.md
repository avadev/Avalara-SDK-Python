# Form1099Div


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ordinary_dividends** | **float** |  | [optional] 
**qualified_dividends** | **float** |  | [optional] 
**total_capital_gain_distributions** | **float** |  | [optional] 
**unrecaptured_section1250_gain** | **float** |  | [optional] 
**section1202_gain** | **float** |  | [optional] 
**collectibles_gain** | **float** |  | [optional] 
**section897_ordinary_dividends** | **float** |  | [optional] 
**section897_capital_gain** | **float** |  | [optional] 
**nondividend_distributions** | **float** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
**section199_a_dividends** | **float** |  | [optional] 
**investment_expenses** | **float** |  | [optional] 
**foreign_tax_paid** | **float** |  | [optional] 
**foreign_country_or_us_possession** | **str** |  | [optional] 
**cash_liquidation_distributions** | **float** |  | [optional] 
**noncash_liquidation_distributions** | **float** |  | [optional] 
**exempt_interest_dividends** | **float** |  | [optional] 
**specified_private_activity_bond_interest_dividends** | **float** |  | [optional] 
**fatca_filing_requirement** | **bool** |  | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_div import Form1099Div

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Div from a JSON string
form1099_div_instance = Form1099Div.from_json(json)
# print the JSON string representation of the object
print(Form1099Div.to_json())

# convert the object into a dict
form1099_div_dict = form1099_div_instance.to_dict()
# create an instance of Form1099Div from a dict
form1099_div_from_dict = Form1099Div.from_dict(form1099_div_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


