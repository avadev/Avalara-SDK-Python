# Form1099DivResponse


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
from Avalara.SDK.models.A1099.V2.form1099_div_response import Form1099DivResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099DivResponse from a JSON string
form1099_div_response_instance = Form1099DivResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099DivResponse.to_json())

# convert the object into a dict
form1099_div_response_dict = form1099_div_response_instance.to_dict()
# create an instance of Form1099DivResponse from a dict
form1099_div_response_from_dict = Form1099DivResponse.from_dict(form1099_div_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


