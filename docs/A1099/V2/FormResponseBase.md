# FormResponseBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_id** | **str** |  | [optional] 
**issuer_reference_id** | **str** |  | [optional] 
**issuer_tin** | **str** |  | [optional] 
**tax_year** | **int** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**recipient_name** | **str** |  | [optional] 
**recipient_federal_id** | **str** |  | [optional] 
**federal_id_type** | **int** |  | [optional] 
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

## Example

```python
from Avalara.SDK.models.A1099.V2.form_response_base import FormResponseBase

# TODO update the JSON string below
json = "{}"
# create an instance of FormResponseBase from a JSON string
form_response_base_instance = FormResponseBase.from_json(json)
# print the JSON string representation of the object
print(FormResponseBase.to_json())

# convert the object into a dict
form_response_base_dict = form_response_base_instance.to_dict()
# create an instance of FormResponseBase from a dict
form_response_base_from_dict = FormResponseBase.from_dict(form_response_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


