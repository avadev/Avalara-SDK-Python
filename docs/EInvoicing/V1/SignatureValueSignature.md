# SignatureValueSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**algorithm** | **str** | The algorithm used to create the signature. | 
**value** | **str** | Signature of the message. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.signature_value_signature import SignatureValueSignature

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureValueSignature from a JSON string
signature_value_signature_instance = SignatureValueSignature.from_json(json)
# print the JSON string representation of the object
print(SignatureValueSignature.to_json())

# convert the object into a dict
signature_value_signature_dict = signature_value_signature_instance.to_dict()
# create an instance of SignatureValueSignature from a dict
signature_value_signature_from_dict = SignatureValueSignature.from_dict(signature_value_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


