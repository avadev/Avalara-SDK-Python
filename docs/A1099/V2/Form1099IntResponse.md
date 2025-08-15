# Form1099IntResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_income** | **float** | Interest Income | [optional] 
**early_withdrawal_penalty** | **float** | Early Withdrawal Penalty | [optional] 
**us_savings_bonds_interest** | **float** | Interest on U.S. Savings Bonds and Treasury obligations | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**investment_expenses** | **float** | Investment Expenses | [optional] 
**foreign_tax_paid** | **float** | Foreign tax paid | [optional] 
**foreign_country** | **str** | Foreign country or U.S. possession | [optional] 
**tax_exempt_interest** | **float** | Tax-Exempt Interest | [optional] 
**specified_private_activity_bond_interest** | **float** | Specified Private activity | [optional] 
**market_discount** | **float** | Market Discount | [optional] 
**bond_premium** | **float** | Bond Premium | [optional] 
**bond_premium_on_treasury_obligations** | **float** | Bond Premium on Treasury obligations | [optional] 
**bond_premium_on_tax_exempt_bond** | **float** | Bond Premium on tax exempt bond | [optional] 
**tax_exempt_bond_cusip_number** | **str** | Tax exempt bond CUSIP no. | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1099_int_response import Form1099IntResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099IntResponse from a JSON string
form1099_int_response_instance = Form1099IntResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099IntResponse.to_json())

# convert the object into a dict
form1099_int_response_dict = form1099_int_response_instance.to_dict()
# create an instance of Form1099IntResponse from a dict
form1099_int_response_from_dict = Form1099IntResponse.from_dict(form1099_int_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


