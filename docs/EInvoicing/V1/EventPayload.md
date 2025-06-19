# EventPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**SignatureValueSignature**](SignatureValueSignature.md) |  | 
**message** | **object** | Event-specific information | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.event_payload import EventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EventPayload from a JSON string
event_payload_instance = EventPayload.from_json(json)
# print the JSON string representation of the object
print(EventPayload.to_json())

# convert the object into a dict
event_payload_dict = event_payload_instance.to_dict()
# create an instance of EventPayload from a dict
event_payload_from_dict = EventPayload.from_dict(event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


