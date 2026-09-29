# BulkTinMatchAcceptedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bulk identifier required to get the results. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_tin_match_accepted_response import BulkTinMatchAcceptedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTinMatchAcceptedResponse from a JSON string
bulk_tin_match_accepted_response_instance = BulkTinMatchAcceptedResponse.from_json(json)
# print the JSON string representation of the object
print(BulkTinMatchAcceptedResponse.to_json())

# convert the object into a dict
bulk_tin_match_accepted_response_dict = bulk_tin_match_accepted_response_instance.to_dict()
# create an instance of BulkTinMatchAcceptedResponse from a dict
bulk_tin_match_accepted_response_from_dict = BulkTinMatchAcceptedResponse.from_dict(bulk_tin_match_accepted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


