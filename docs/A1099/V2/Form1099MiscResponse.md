# Form1099MiscResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**fatca_filing_requirement** | **bool** |  | [optional] 
**excess_golden_parachute_payments** | **float** |  | [optional] 
**nonqualified_deferred_compensation** | **float** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
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
**federal_efile_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**state_efile_status** | [**List[StateEfileStatusDetailApp]**](StateEfileStatusDetailApp.md) |  | [optional] 
**postal_mail_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**tin_match_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**address_verification_status** | [**StatusDetail**](StatusDetail.md) |  | [optional] 
**validation_errors** | [**List[ValidationErrorApp]**](ValidationErrorApp.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_misc_response import Form1099MiscResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099MiscResponse from a JSON string
form1099_misc_response_instance = Form1099MiscResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099MiscResponse.to_json())

# convert the object into a dict
form1099_misc_response_dict = form1099_misc_response_instance.to_dict()
# create an instance of Form1099MiscResponse from a dict
form1099_misc_response_from_dict = Form1099MiscResponse.from_dict(form1099_misc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


