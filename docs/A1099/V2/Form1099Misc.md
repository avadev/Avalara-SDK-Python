# Form1099Misc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**type_of_tin** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**first_payee_name** | **str** |  | [optional] 
**second_payee_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address_recipient_second** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**foreign_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_misc import Form1099Misc

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099Misc from a JSON string
form1099_misc_instance = Form1099Misc.from_json(json)
# print the JSON string representation of the object
print(Form1099Misc.to_json())

# convert the object into a dict
form1099_misc_dict = form1099_misc_instance.to_dict()
# create an instance of Form1099Misc from a dict
form1099_misc_from_dict = Form1099Misc.from_dict(form1099_misc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


