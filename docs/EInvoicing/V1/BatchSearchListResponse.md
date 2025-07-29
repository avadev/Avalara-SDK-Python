# BatchSearchListResponse

Response schema for listing batch search details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_set_count** | **int** | The count of records in the result set. | [optional] 
**next_link** | **str** | Next Link | [optional] 
**value** | [**List[BatchSearch]**](BatchSearch.md) | List of batch search records. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.batch_search_list_response import BatchSearchListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchSearchListResponse from a JSON string
batch_search_list_response_instance = BatchSearchListResponse.from_json(json)
# print the JSON string representation of the object
print(BatchSearchListResponse.to_json())

# convert the object into a dict
batch_search_list_response_dict = batch_search_list_response_instance.to_dict()
# create an instance of BatchSearchListResponse from a dict
batch_search_list_response_from_dict = BatchSearchListResponse.from_dict(batch_search_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


