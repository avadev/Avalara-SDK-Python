# SubscriptionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of this specific resource. | 
**description** | **str** | Description of the subscription | [optional] 
**notification_url** | **str** | The URL of the webhook endpoint to which event messages will be delivered | 
**signature** | [**SignatureSignature**](SignatureSignature.md) |  | 
**events** | [**List[EventSubscription]**](EventSubscription.md) |  | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.subscription_detail import SubscriptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetail from a JSON string
subscription_detail_instance = SubscriptionDetail.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetail.to_json())

# convert the object into a dict
subscription_detail_dict = subscription_detail_instance.to_dict()
# create an instance of SubscriptionDetail from a dict
subscription_detail_from_dict = SubscriptionDetail.from_dict(subscription_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


