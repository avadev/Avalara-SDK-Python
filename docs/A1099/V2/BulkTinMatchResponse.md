# BulkTinMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**results_url** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_tin_match_response import BulkTinMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTinMatchResponse from a JSON string
bulk_tin_match_response_instance = BulkTinMatchResponse.from_json(json)
# print the JSON string representation of the object
print(BulkTinMatchResponse.to_json())

# convert the object into a dict
bulk_tin_match_response_dict = bulk_tin_match_response_instance.to_dict()
# create an instance of BulkTinMatchResponse from a dict
bulk_tin_match_response_from_dict = BulkTinMatchResponse.from_dict(bulk_tin_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


