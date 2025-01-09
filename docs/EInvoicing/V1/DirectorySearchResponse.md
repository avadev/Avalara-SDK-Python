# DirectorySearchResponse

Response schema for directory search results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_set_count** | **int** | The count of records in the result set | [optional] 
**next_link** | **str** | The next page link to get the next set of results. | [optional] 
**value** | [**List[DirectorySearchResponseValueInner]**](DirectorySearchResponseValueInner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.directory_search_response import DirectorySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorySearchResponse from a JSON string
directory_search_response_instance = DirectorySearchResponse.from_json(json)
# print the JSON string representation of the object
print(DirectorySearchResponse.to_json())

# convert the object into a dict
directory_search_response_dict = directory_search_response_instance.to_dict()
# create an instance of DirectorySearchResponse from a dict
directory_search_response_from_dict = DirectorySearchResponse.from_dict(directory_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


