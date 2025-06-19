# SignatureValue

Includes the actual signature applied to a webhook message along with the algorithm used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**SignatureValueSignature**](SignatureValueSignature.md) |  | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.signature_value import SignatureValue

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureValue from a JSON string
signature_value_instance = SignatureValue.from_json(json)
# print the JSON string representation of the object
print(SignatureValue.to_json())

# convert the object into a dict
signature_value_dict = signature_value_instance.to_dict()
# create an instance of SignatureValue from a dict
signature_value_from_dict = SignatureValue.from_dict(signature_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


