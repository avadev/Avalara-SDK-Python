# TaxIdentifierRequest

Represents a request to validate company’s tax identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter ISO-3166 country code of the tax identifier. | 
**identifier_type** | **str** | Type of the identifier. | 
**identifier** | **str** | The tax identifier of the company. | 
**extensions** | **object** | Optional field for adding additional details required by specific tax authorities. Refer to the GET /tax-identifiers/schema API endpoint for the full request structure for a given country. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_request import TaxIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIdentifierRequest from a JSON string
tax_identifier_request_instance = TaxIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(TaxIdentifierRequest.to_json())

# convert the object into a dict
tax_identifier_request_dict = tax_identifier_request_instance.to_dict()
# create an instance of TaxIdentifierRequest from a dict
tax_identifier_request_from_dict = TaxIdentifierRequest.from_dict(tax_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


