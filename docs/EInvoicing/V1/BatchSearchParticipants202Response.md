# BatchSearchParticipants202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the batch search. | [optional] 
**status** | **str** | Status of the batch search. | [optional] 
**message** | **str** | A message indicating that the batch search request has been accepted. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.batch_search_participants202_response import BatchSearchParticipants202Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchSearchParticipants202Response from a JSON string
batch_search_participants202_response_instance = BatchSearchParticipants202Response.from_json(json)
# print the JSON string representation of the object
print(BatchSearchParticipants202Response.to_json())

# convert the object into a dict
batch_search_participants202_response_dict = batch_search_participants202_response_instance.to_dict()
# create an instance of BatchSearchParticipants202Response from a dict
batch_search_participants202_response_from_dict = BatchSearchParticipants202Response.from_dict(batch_search_participants202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


