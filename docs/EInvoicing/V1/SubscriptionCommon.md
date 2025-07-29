# SubscriptionCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the subscription | [optional] 
**notification_url** | **str** | The URL of the webhook endpoint to which event messages will be delivered | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.subscription_common import SubscriptionCommon

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCommon from a JSON string
subscription_common_instance = SubscriptionCommon.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCommon.to_json())

# convert the object into a dict
subscription_common_dict = subscription_common_instance.to_dict()
# create an instance of SubscriptionCommon from a dict
subscription_common_from_dict = SubscriptionCommon.from_dict(subscription_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


