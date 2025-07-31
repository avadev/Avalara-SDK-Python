# IrsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The IRS response code. | [optional] 
**description** | **str** | The description for the IRS response. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.irs_response import IrsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IrsResponse from a JSON string
irs_response_instance = IrsResponse.from_json(json)
# print the JSON string representation of the object
print(IrsResponse.to_json())

# convert the object into a dict
irs_response_dict = irs_response_instance.to_dict()
# create an instance of IrsResponse from a dict
irs_response_from_dict = IrsResponse.from_dict(irs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


