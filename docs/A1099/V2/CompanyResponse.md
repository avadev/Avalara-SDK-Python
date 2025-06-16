# CompanyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**dba_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**foreign_province** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**do_tin_match** | **bool** |  | [optional] 
**resend_requests** | **bool** |  | [optional] 
**resend_interval_days** | **int** |  | [optional] 
**max_reminder_attempts** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.company_response import CompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyResponse from a JSON string
company_response_instance = CompanyResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyResponse.to_json())

# convert the object into a dict
company_response_dict = company_response_instance.to_dict()
# create an instance of CompanyResponse from a dict
company_response_from_dict = CompanyResponse.from_dict(company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


