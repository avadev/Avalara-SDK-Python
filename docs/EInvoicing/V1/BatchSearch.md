# BatchSearch

Represents a single batch search operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the batch search | [optional] 
**name** | **str** | Name of the batch report | [optional] 
**created_by** | **str** | Email of the user who created the batch search | [optional] 
**created** | **datetime** | Timestamp when the batch search was created | [optional] 
**last_modified** | **datetime** | Timestamp when the batch search was created | [optional] 
**status** | **str** | Status of the batch search | [optional] 
**error** | [**ErrorResponse**](ErrorResponse.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.batch_search import BatchSearch

# TODO update the JSON string below
json = "{}"
# create an instance of BatchSearch from a JSON string
batch_search_instance = BatchSearch.from_json(json)
# print the JSON string representation of the object
print(BatchSearch.to_json())

# convert the object into a dict
batch_search_dict = batch_search_instance.to_dict()
# create an instance of BatchSearch from a dict
batch_search_from_dict = BatchSearch.from_dict(batch_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


