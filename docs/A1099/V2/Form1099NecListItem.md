# Form1099NecListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) |  | [optional] 
**second_tin_notice** | **bool** |  | [optional] 
**nonemployee_compensation** | **float** |  | [optional] 
**payer_made_direct_sales** | **bool** |  | [optional] 
**federal_income_tax_withheld** | **float** |  | [optional] 
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

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_nec_list_item import Form1099NecListItem

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099NecListItem from a JSON string
form1099_nec_list_item_instance = Form1099NecListItem.from_json(json)
# print the JSON string representation of the object
print(Form1099NecListItem.to_json())

# convert the object into a dict
form1099_nec_list_item_dict = form1099_nec_list_item_instance.to_dict()
# create an instance of Form1099NecListItem from a dict
form1099_nec_list_item_from_dict = Form1099NecListItem.from_dict(form1099_nec_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


