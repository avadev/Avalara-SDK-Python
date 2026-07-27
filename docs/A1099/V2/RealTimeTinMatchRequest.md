# RealTimeTinMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tin_type** | **str** | The TIN type. | [optional] 
**tin** | **str** | The TIN to be submitted to TIN match. | [optional] 
**name** | **str** | The entity name to be submitted to TIN match. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.real_time_tin_match_request import RealTimeTinMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RealTimeTinMatchRequest from a JSON string
real_time_tin_match_request_instance = RealTimeTinMatchRequest.from_json(json)
# print the JSON string representation of the object
print(RealTimeTinMatchRequest.to_json())

# convert the object into a dict
real_time_tin_match_request_dict = real_time_tin_match_request_instance.to_dict()
# create an instance of RealTimeTinMatchRequest from a dict
real_time_tin_match_request_from_dict = RealTimeTinMatchRequest.from_dict(real_time_tin_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


