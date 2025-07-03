# Get1099Form200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_of_health_coverage_code** | **str** |  | [optional] 
**covered_individuals** | [**List[CoveredIndividualReference]**](CoveredIndividualReference.md) |  | [optional] 
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
**reference_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**tin_type** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_second_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**foreign_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 
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
**rents** | **float** |  | [optional] 
**royalties** | **float** |  | [optional] 
**other_income** | **float** |  | [optional] 
**fed_income_tax_withheld** | **float** |  | [optional] 
**fishing_boat_proceeds** | **float** |  | [optional] 
**medical_and_health_care** | **float** |  | [optional] 
**nonemployee_compensation** | **float** |  | [optional] 
**substitute_payments** | **float** |  | [optional] 
**direct_sales_indicator** | **bool** |  | [optional] 
**crop_insurance_proceeds** | **float** |  | [optional] 
**excess_golden_parachute** | **float** |  | [optional] 
**gross_amount_paid_attorney** | **float** |  | [optional] 
**section409_a_deferrals** | **float** |  | [optional] 
**section409_a_income** | **float** |  | [optional] 
**gross_distributions** | **float** |  | [optional] 
**taxable_amount** | **float** |  | [optional] 
**taxable_amount_not_determined** | **bool** |  | [optional] 
**total_distribution_indicator** | **bool** |  | [optional] 
**capital_gain** | **float** |  | [optional] 
**employee_contributions** | **float** |  | [optional] 
**net_unrealized_appreciation** | **float** |  | [optional] 
**distribution_code_required** | **str** |  | [optional] 
**distribution_code_optional** | **str** |  | [optional] 
**ira_sep_simple_indicator** | **bool** |  | [optional] 
**total_ira_sep_simple_distribution** | **float** |  | [optional] 
**other** | **float** |  | [optional] 
**other_percent** | **str** |  | [optional] 
**percentage_total_distribution** | **str** |  | [optional] 
**total_employee_contributions** | **float** |  | [optional] 
**amount_allocable_to_irr** | **float** |  | [optional] 
**first_year_designated_roth_contrib** | **str** |  | [optional] 
**fatca_requirement_indicator** | **bool** |  | [optional] 
**date_of_payment** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.get1099_form200_response import Get1099Form200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Get1099Form200Response from a JSON string
get1099_form200_response_instance = Get1099Form200Response.from_json(json)
# print the JSON string representation of the object
print(Get1099Form200Response.to_json())

# convert the object into a dict
get1099_form200_response_dict = get1099_form200_response_instance.to_dict()
# create an instance of Get1099Form200Response from a dict
get1099_form200_response_from_dict = Get1099Form200Response.from_dict(get1099_form200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


