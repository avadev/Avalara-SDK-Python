# BulkTinMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkTinMatchRequestItem]**](BulkTinMatchRequestItem.md) | Collection of TINs to be submitted to TIN match. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_tin_match_request import BulkTinMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTinMatchRequest from a JSON string
bulk_tin_match_request_instance = BulkTinMatchRequest.from_json(json)
# print the JSON string representation of the object
print(BulkTinMatchRequest.to_json())

# convert the object into a dict
bulk_tin_match_request_dict = bulk_tin_match_request_instance.to_dict()
# create an instance of BulkTinMatchRequest from a dict
bulk_tin_match_request_from_dict = BulkTinMatchRequest.from_dict(bulk_tin_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


