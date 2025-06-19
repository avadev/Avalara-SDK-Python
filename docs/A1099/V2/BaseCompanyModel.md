# BaseCompanyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**dba_name** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**do_tin_match** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**foreign_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**resend_requests** | **bool** |  | [optional] 
**resend_interval_days** | **int** |  | [optional] 
**max_reminder_attempts** | **int** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.base_company_model import BaseCompanyModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCompanyModel from a JSON string
base_company_model_instance = BaseCompanyModel.from_json(json)
# print the JSON string representation of the object
print(BaseCompanyModel.to_json())

# convert the object into a dict
base_company_model_dict = base_company_model_instance.to_dict()
# create an instance of BaseCompanyModel from a dict
base_company_model_from_dict = BaseCompanyModel.from_dict(base_company_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


