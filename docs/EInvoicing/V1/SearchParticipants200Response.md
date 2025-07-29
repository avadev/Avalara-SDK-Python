# SearchParticipants200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_set_count** | **int** | The count of records in the result set. | [optional] 
**next_link** | **str** | The next page link to get the next set of results. | [optional] 
**value** | [**List[TradingPartner]**](TradingPartner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.search_participants200_response import SearchParticipants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchParticipants200Response from a JSON string
search_participants200_response_instance = SearchParticipants200Response.from_json(json)
# print the JSON string representation of the object
print(SearchParticipants200Response.to_json())

# convert the object into a dict
search_participants200_response_dict = search_participants200_response_instance.to_dict()
# create an instance of SearchParticipants200Response from a dict
search_participants200_response_from_dict = SearchParticipants200Response.from_dict(search_participants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


