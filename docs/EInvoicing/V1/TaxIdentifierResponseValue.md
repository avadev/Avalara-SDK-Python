# TaxIdentifierResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_type** | **str** | Type of the identifier. | [optional] 
**identifier** | **str** | The tax identifier of the company. | [optional] 
**extensions** | **object** | Optional field containing additional company-related information such as companyName, companyAddress, blockListed, tradeName, and taxPayerType. It may also include other details specific to the given tax authority. Refer to the GET /tax-identifiers/schema API endpoint for the full response structure for a given country. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_response_value import TaxIdentifierResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIdentifierResponseValue from a JSON string
tax_identifier_response_value_instance = TaxIdentifierResponseValue.from_json(json)
# print the JSON string representation of the object
print(TaxIdentifierResponseValue.to_json())

# convert the object into a dict
tax_identifier_response_value_dict = tax_identifier_response_value_instance.to_dict()
# create an instance of TaxIdentifierResponseValue from a dict
tax_identifier_response_value_from_dict = TaxIdentifierResponseValue.from_dict(tax_identifier_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


