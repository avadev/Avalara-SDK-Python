# HmacSignatureValue

Contains the HMAC algorithm and the resulting signature value used for verifying message integrity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The algorithm used to create the signature. | 
**value** | **str** | Signature of the message. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.hmac_signature_value import HmacSignatureValue

# TODO update the JSON string below
json = "{}"
# create an instance of HmacSignatureValue from a JSON string
hmac_signature_value_instance = HmacSignatureValue.from_json(json)
# print the JSON string representation of the object
print(HmacSignatureValue.to_json())

# convert the object into a dict
hmac_signature_value_dict = hmac_signature_value_instance.to_dict()
# create an instance of HmacSignatureValue from a dict
hmac_signature_value_from_dict = HmacSignatureValue.from_dict(hmac_signature_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


