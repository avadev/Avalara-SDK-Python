# TinMatchStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | The current timestamp for the TIN match request. | [optional] 
**status** | **str** | The current status for the TIN match request. | [optional] 
**irs_response** | [**IrsResponse**](IrsResponse.md) | The IRS response. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.tin_match_status_response import TinMatchStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TinMatchStatusResponse from a JSON string
tin_match_status_response_instance = TinMatchStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TinMatchStatusResponse.to_json())

# convert the object into a dict
tin_match_status_response_dict = tin_match_status_response_instance.to_dict()
# create an instance of TinMatchStatusResponse from a dict
tin_match_status_response_from_dict = TinMatchStatusResponse.from_dict(tin_match_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


