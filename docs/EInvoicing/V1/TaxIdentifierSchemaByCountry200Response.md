# TaxIdentifierSchemaByCountry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The two-letter ISO-3166 country code of the tax identifier. | 
**var_schema** | **object** | The JSON Schema definition, following Draft-07 specification, used to validate tax identifier data. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.tax_identifier_schema_by_country200_response import TaxIdentifierSchemaByCountry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIdentifierSchemaByCountry200Response from a JSON string
tax_identifier_schema_by_country200_response_instance = TaxIdentifierSchemaByCountry200Response.from_json(json)
# print the JSON string representation of the object
print(TaxIdentifierSchemaByCountry200Response.to_json())

# convert the object into a dict
tax_identifier_schema_by_country200_response_dict = tax_identifier_schema_by_country200_response_instance.to_dict()
# create an instance of TaxIdentifierSchemaByCountry200Response from a dict
tax_identifier_schema_by_country200_response_from_dict = TaxIdentifierSchemaByCountry200Response.from_dict(tax_identifier_schema_by_country200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


