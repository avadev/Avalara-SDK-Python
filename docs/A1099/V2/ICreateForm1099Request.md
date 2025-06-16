# ICreateForm1099Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ordinary_dividends** | **str** |  | [optional] 
**qualified_dividends** | **str** |  | [optional] 
**total_capital_gain_distr** | **str** |  | [optional] 
**unrecap_sec1250_gain** | **str** |  | [optional] 
**section1202_gain** | **str** |  | [optional] 
**collectibles_gain** | **str** |  | [optional] 
**section897_ordinary_dividends** | **str** |  | [optional] 
**section897_capital_gain** | **str** |  | [optional] 
**nondividend_distributions** | **str** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
**section199_a_dividends** | **str** |  | [optional] 
**investment_expenses** | **str** |  | [optional] 
**foreign_tax_paid** | **str** |  | [optional] 
**foreign_country_or_us_possession** | **str** |  | [optional] 
**cash_liquidation_distributions** | **str** |  | [optional] 
**noncash_liquidation_distributions** | **str** |  | [optional] 
**exempt_interest_dividends** | **str** |  | [optional] 
**specified_private_activity_bond_interest_dividends** | **str** |  | [optional] 
**fatca_filing_requirement** | **bool** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholdingRequest**](StateAndLocalWithholdingRequest.md) |  | [optional] 
**type** | **str** |  | [optional] 
**issuer_id** | **str** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_tin** | **str** |  | [optional] 
**tin_type** | **int** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**street_address_line2** | **str** |  | [optional] 
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
**second_tin_notice** | **bool** |  | [optional] 
**rents** | **float** |  | [optional] 
**royalties** | **float** |  | [optional] 
**other_income** | **float** |  | [optional] 
**fed_income_tax_withheld** | **float** |  | [optional] 
**fishing_boat_proceeds** | **float** |  | [optional] 
**medical_health_care_payments** | **float** |  | [optional] 
**payer_made_direct_sales** | **bool** |  | [optional] 
**substitute_payments** | **float** |  | [optional] 
**crop_insurance_proceeds** | **float** |  | [optional] 
**gross_proceeds_paid_to_attorney** | **float** |  | [optional] 
**fish_purchased_for_resale** | **float** |  | [optional] 
**section409_a_deferrals** | **float** |  | [optional] 
**excess_golden_parachute_payments** | **float** |  | [optional] 
**nonqualified_deferred_compensation** | **float** |  | [optional] 
**nonemployee_compensation** | **float** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.i_create_form1099_request import ICreateForm1099Request

# TODO update the JSON string below
json = "{}"
# create an instance of ICreateForm1099Request from a JSON string
i_create_form1099_request_instance = ICreateForm1099Request.from_json(json)
# print the JSON string representation of the object
print(ICreateForm1099Request.to_json())

# convert the object into a dict
i_create_form1099_request_dict = i_create_form1099_request_instance.to_dict()
# create an instance of ICreateForm1099Request from a dict
i_create_form1099_request_from_dict = ICreateForm1099Request.from_dict(i_create_form1099_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


