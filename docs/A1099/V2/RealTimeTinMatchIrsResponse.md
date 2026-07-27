# RealTimeTinMatchIrsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The IRS response code. | [optional] 
**description** | **str** | The description for the IRS response. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.real_time_tin_match_irs_response import RealTimeTinMatchIrsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealTimeTinMatchIrsResponse from a JSON string
real_time_tin_match_irs_response_instance = RealTimeTinMatchIrsResponse.from_json(json)
# print the JSON string representation of the object
print(RealTimeTinMatchIrsResponse.to_json())

# convert the object into a dict
real_time_tin_match_irs_response_dict = real_time_tin_match_irs_response_instance.to_dict()
# create an instance of RealTimeTinMatchIrsResponse from a dict
real_time_tin_match_irs_response_from_dict = RealTimeTinMatchIrsResponse.from_dict(real_time_tin_match_irs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


