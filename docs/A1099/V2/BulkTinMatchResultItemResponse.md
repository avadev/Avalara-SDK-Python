# BulkTinMatchResultItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**irs_response** | [**BulkTinMatchIrsResponse**](BulkTinMatchIrsResponse.md) |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_tin_match_result_item_response import BulkTinMatchResultItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTinMatchResultItemResponse from a JSON string
bulk_tin_match_result_item_response_instance = BulkTinMatchResultItemResponse.from_json(json)
# print the JSON string representation of the object
print(BulkTinMatchResultItemResponse.to_json())

# convert the object into a dict
bulk_tin_match_result_item_response_dict = bulk_tin_match_result_item_response_instance.to_dict()
# create an instance of BulkTinMatchResultItemResponse from a dict
bulk_tin_match_result_item_response_from_dict = BulkTinMatchResultItemResponse.from_dict(bulk_tin_match_result_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


