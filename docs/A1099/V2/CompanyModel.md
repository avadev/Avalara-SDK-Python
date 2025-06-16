# CompanyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Company ID | [optional] 
**user_id** | **int** | User ID associated with the company | [optional] 
**account_id** | **int** | Account ID associated with the company | [optional] 
**created_at** | **datetime** | Record creation timestamp | [optional] 
**updated_at** | **datetime** | Record last update timestamp | [optional] 
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
from Avalara.SDK.models.A1099.V2.company_model import CompanyModel

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyModel from a JSON string
company_model_instance = CompanyModel.from_json(json)
# print the JSON string representation of the object
print(CompanyModel.to_json())

# convert the object into a dict
company_model_dict = company_model_instance.to_dict()
# create an instance of CompanyModel from a dict
company_model_from_dict = CompanyModel.from_dict(company_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


