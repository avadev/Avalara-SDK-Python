# StateEfileStatusDetailApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**time** | **str** |  | [optional] 
**jurisdiction** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.state_efile_status_detail_app import StateEfileStatusDetailApp

# TODO update the JSON string below
json = "{}"
# create an instance of StateEfileStatusDetailApp from a JSON string
state_efile_status_detail_app_instance = StateEfileStatusDetailApp.from_json(json)
# print the JSON string representation of the object
print(StateEfileStatusDetailApp.to_json())

# convert the object into a dict
state_efile_status_detail_app_dict = state_efile_status_detail_app_instance.to_dict()
# create an instance of StateEfileStatusDetailApp from a dict
state_efile_status_detail_app_from_dict = StateEfileStatusDetailApp.from_dict(state_efile_status_detail_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


