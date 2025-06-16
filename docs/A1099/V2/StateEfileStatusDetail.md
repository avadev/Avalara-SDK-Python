# StateEfileStatusDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**jurisdiction** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.state_efile_status_detail import StateEfileStatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StateEfileStatusDetail from a JSON string
state_efile_status_detail_instance = StateEfileStatusDetail.from_json(json)
# print the JSON string representation of the object
print(StateEfileStatusDetail.to_json())

# convert the object into a dict
state_efile_status_detail_dict = state_efile_status_detail_instance.to_dict()
# create an instance of StateEfileStatusDetail from a dict
state_efile_status_detail_from_dict = StateEfileStatusDetail.from_dict(state_efile_status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


