# BulkTinMatchRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tin_type** | **str** | The TIN type. | [optional] 
**tin** | **str** | The TIN to be submitted to TIN match. | [optional] 
**name** | **str** | The entity name to be submitted to TIN match. | [optional] 
**reference_id** | **str** | The reference identifier for the TIN to be submitted. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_tin_match_request_item import BulkTinMatchRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTinMatchRequestItem from a JSON string
bulk_tin_match_request_item_instance = BulkTinMatchRequestItem.from_json(json)
# print the JSON string representation of the object
print(BulkTinMatchRequestItem.to_json())

# convert the object into a dict
bulk_tin_match_request_item_dict = bulk_tin_match_request_item_instance.to_dict()
# create an instance of BulkTinMatchRequestItem from a dict
bulk_tin_match_request_item_from_dict = BulkTinMatchRequestItem.from_dict(bulk_tin_match_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


