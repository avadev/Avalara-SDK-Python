# StatusDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.status_detail import StatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDetail from a JSON string
status_detail_instance = StatusDetail.from_json(json)
# print the JSON string representation of the object
print(StatusDetail.to_json())

# convert the object into a dict
status_detail_dict = status_detail_instance.to_dict()
# create an instance of StatusDetail from a dict
status_detail_from_dict = StatusDetail.from_dict(status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


