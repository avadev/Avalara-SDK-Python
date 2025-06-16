# SignatureSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**key** | **str** | HMAC key for authentication | 
**algorithm** | **str** | HMAC algorithm for authentication | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.signature_signature import SignatureSignature

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureSignature from a JSON string
signature_signature_instance = SignatureSignature.from_json(json)
# print the JSON string representation of the object
print(SignatureSignature.to_json())

# convert the object into a dict
signature_signature_dict = signature_signature_instance.to_dict()
# create an instance of SignatureSignature from a dict
signature_signature_from_dict = SignatureSignature.from_dict(signature_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


