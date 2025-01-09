# StatusEvent

Displays when a status event occurred

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_date_time** | **str** | The date and time when the status event occured, displayed in the format YYYY-MM-DDThh:mm:ss | [optional] 
**message** | **str** | A message describing the status event | [optional] 
**response_key** | **str** |  The type of number or acknowledgement returned by the tax authority (if applicable). For example, it could be an identification key, acknowledgement code, or any other relevant identifier. | [optional] 
**response_value** | **str** | The corresponding value associated with the response key. This value is provided by the tax authority in response to the event. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.status_event import StatusEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StatusEvent from a JSON string
status_event_instance = StatusEvent.from_json(json)
# print the JSON string representation of the object
print(StatusEvent.to_json())

# convert the object into a dict
status_event_dict = status_event_instance.to_dict()
# create an instance of StatusEvent from a dict
status_event_from_dict = StatusEvent.from_dict(status_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


