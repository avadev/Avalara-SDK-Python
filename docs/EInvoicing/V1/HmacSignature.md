# HmacSignature

Basic signature utilizing a shared key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | HMAC key for authentication | 
**algorithm** | **str** | HMAC algorithm for authentication | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.hmac_signature import HmacSignature

# TODO update the JSON string below
json = "{}"
# create an instance of HmacSignature from a JSON string
hmac_signature_instance = HmacSignature.from_json(json)
# print the JSON string representation of the object
print(HmacSignature.to_json())

# convert the object into a dict
hmac_signature_dict = hmac_signature_instance.to_dict()
# create an instance of HmacSignature from a dict
hmac_signature_from_dict = HmacSignature.from_dict(hmac_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


