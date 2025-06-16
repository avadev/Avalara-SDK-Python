# EventMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** | Event-specific information | 
**signature** | [**SignatureValueSignature**](SignatureValueSignature.md) |  | 
**tenant_id** | **str** | Tenant ID of the event | 
**correlation_id** | **str** | The correlation ID used by Avalara to aid in tracing through to provenance of this event massage. | [optional] 
**system_code** | **str** | The Avalara registered code for the system. See &lt;a href&#x3D;\&quot;https://avalara.atlassian.net/wiki/spaces/AIM/pages/637250338966/Taxonomy+Avalara+Systems\&quot;&gt;Taxonomy&amp;#58; Avalara Systems&lt;/a&gt; | 
**event_name** | **str** | Type of the event | 
**event_version** | **str** | Version of the included payload. | [optional] 
**receipt_timestamp** | **datetime** | Timestamp when the event was received by the dispatch service. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.event_message import EventMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EventMessage from a JSON string
event_message_instance = EventMessage.from_json(json)
# print the JSON string representation of the object
print(EventMessage.to_json())

# convert the object into a dict
event_message_dict = event_message_instance.to_dict()
# create an instance of EventMessage from a dict
event_message_from_dict = EventMessage.from_dict(event_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


