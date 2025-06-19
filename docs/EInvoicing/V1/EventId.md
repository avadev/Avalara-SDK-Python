# EventId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | Unique, to the delivery system, identifier of the event. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.event_id import EventId

# TODO update the JSON string below
json = "{}"
# create an instance of EventId from a JSON string
event_id_instance = EventId.from_json(json)
# print the JSON string representation of the object
print(EventId.to_json())

# convert the object into a dict
event_id_dict = event_id_instance.to_dict()
# create an instance of EventId from a dict
event_id_from_dict = EventId.from_dict(event_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


