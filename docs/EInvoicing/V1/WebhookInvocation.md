# WebhookInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of this specific resource. | 
**retry_count** | **int** | The number of invocation attempts. | [optional] 
**retry_max** | **int** | The maximum retries that may be attempted in total. | [optional] 
**invocation_timestamp** | **datetime** | Initial timestamp of the first invocation attempt. | 
**retry_timestamp** | **datetime** | Timestamp of this invocation attempt. | [optional] 
**items** | [**List[EventMessage]**](EventMessage.md) | Array of events being delivered in the webhook | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.webhook_invocation import WebhookInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInvocation from a JSON string
webhook_invocation_instance = WebhookInvocation.from_json(json)
# print the JSON string representation of the object
print(WebhookInvocation.to_json())

# convert the object into a dict
webhook_invocation_dict = webhook_invocation_instance.to_dict()
# create an instance of WebhookInvocation from a dict
webhook_invocation_from_dict = WebhookInvocation.from_dict(webhook_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


