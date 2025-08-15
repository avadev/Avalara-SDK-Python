# Form1042S


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_form_id** | **str** |  | [optional] 
**recipient_date_of_birth** | **datetime** |  | [optional] 
**recipient_giin** | **str** |  | [optional] 
**recipient_foreign_tin** | **str** |  | [optional] 
**lob_code** | **str** |  | [optional] 
**income_code** | **str** |  | [optional] 
**gross_income** | **float** |  | [optional] 
**withholding_indicator** | **str** |  | [optional] 
**tax_country_code** | **str** |  | [optional] 
**exemption_code_chap3** | **str** |  | [optional] 
**exemption_code_chap4** | **str** |  | [optional] 
**tax_rate_chap3** | **str** |  | [optional] 
**withholding_allowance** | **float** |  | [optional] 
**federal_tax_withheld** | **float** |  | [optional] 
**tax_not_deposited_indicator** | **bool** |  | [optional] 
**academic_indicator** | **bool** |  | [optional] 
**tax_withheld_other_agents** | **float** |  | [optional] 
**amount_repaid** | **float** |  | [optional] 
**tax_paid_agent** | **float** |  | [optional] 
**chap3_status_code** | **str** |  | [optional] 
**chap4_status_code** | **str** |  | [optional] 
**primary_withholding_agent** | [**PrimaryWithholdingAgent**](PrimaryWithholdingAgent.md) |  | [optional] 
**intermediary_or_flow_through** | [**IntermediaryOrFlowThrough**](IntermediaryOrFlowThrough.md) |  | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1042_s import Form1042S

# TODO update the JSON string below
json = "{}"
# create an instance of Form1042S from a JSON string
form1042_s_instance = Form1042S.from_json(json)
# print the JSON string representation of the object
print(Form1042S.to_json())

# convert the object into a dict
form1042_s_dict = form1042_s_instance.to_dict()
# create an instance of Form1042S from a dict
form1042_s_from_dict = Form1042S.from_dict(form1042_s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


