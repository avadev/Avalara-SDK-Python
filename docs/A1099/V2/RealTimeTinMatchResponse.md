# RealTimeTinMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the TIN match (matched or rejected). | [optional] 
**irs_response** | [**RealTimeTinMatchIrsResponse**](RealTimeTinMatchIrsResponse.md) | The IRS response details. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.real_time_tin_match_response import RealTimeTinMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealTimeTinMatchResponse from a JSON string
real_time_tin_match_response_instance = RealTimeTinMatchResponse.from_json(json)
# print the JSON string representation of the object
print(RealTimeTinMatchResponse.to_json())

# convert the object into a dict
real_time_tin_match_response_dict = real_time_tin_match_response_instance.to_dict()
# create an instance of RealTimeTinMatchResponse from a dict
real_time_tin_match_response_from_dict = RealTimeTinMatchResponse.from_dict(real_time_tin_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


