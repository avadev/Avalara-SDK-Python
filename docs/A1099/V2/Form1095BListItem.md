# Form1095BListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_first_name** | **str** |  | [optional] 
**employee_middle_name** | **str** |  | [optional] 
**employee_last_name** | **str** |  | [optional] 
**employee_name_suffix** | **str** |  | [optional] 
**employee_date_of_birth** | **datetime** |  | [optional] 
**origin_of_health_coverage_code** | **str** |  | [optional] 
**covered_individuals** | [**List[CoveredIndividualRequest]**](CoveredIndividualRequest.md) |  | [optional] 
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
from Avalara.SDK.models.A1099.V2.form1095_b_list_item import Form1095BListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1095BListItem from a JSON string
form1095_b_list_item_instance = Form1095BListItem.from_json(json)
# print the JSON string representation of the object
print(Form1095BListItem.to_json())

# convert the object into a dict
form1095_b_list_item_dict = form1095_b_list_item_instance.to_dict()
# create an instance of Form1095BListItem from a dict
form1095_b_list_item_from_dict = Form1095BListItem.from_dict(form1095_b_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


