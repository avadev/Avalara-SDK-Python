# TaxIdentifierResponse

Represents the response for a tax identifier validation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter ISO-3166 country code of the tax identifier. | 
**value** | [**TaxIdentifierResponseValue**](TaxIdentifierResponseValue.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_response import TaxIdentifierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIdentifierResponse from a JSON string
tax_identifier_response_instance = TaxIdentifierResponse.from_json(json)
# print the JSON string representation of the object
print(TaxIdentifierResponse.to_json())

# convert the object into a dict
tax_identifier_response_dict = tax_identifier_response_instance.to_dict()
# create an instance of TaxIdentifierResponse from a dict
tax_identifier_response_from_dict = TaxIdentifierResponse.from_dict(tax_identifier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


