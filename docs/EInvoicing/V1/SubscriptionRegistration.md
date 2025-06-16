# SubscriptionRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the subscription | [optional] 
**notification_url** | **str** | The URL of the webhook endpoint to which event messages will be delivered | 
**signature** | [**SignatureSignature**](SignatureSignature.md) |  | 
**events** | [**List[EventSubscription]**](EventSubscription.md) |  | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.subscription_registration import SubscriptionRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRegistration from a JSON string
subscription_registration_instance = SubscriptionRegistration.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRegistration.to_json())

# convert the object into a dict
subscription_registration_dict = subscription_registration_instance.to_dict()
# create an instance of SubscriptionRegistration from a dict
subscription_registration_from_dict = SubscriptionRegistration.from_dict(subscription_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


