# EntryStatusResponse

Represents the entry status information for a W9 form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The form status. | [optional] 
**time** | **datetime** | The timestamp for the latest status update. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.entry_status_response import EntryStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntryStatusResponse from a JSON string
entry_status_response_instance = EntryStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EntryStatusResponse.to_json())

# convert the object into a dict
entry_status_response_dict = entry_status_response_instance.to_dict()
# create an instance of EntryStatusResponse from a dict
entry_status_response_from_dict = EntryStatusResponse.from_dict(entry_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


