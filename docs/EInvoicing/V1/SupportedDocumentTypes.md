# SupportedDocumentTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document type name. | [optional] 
**value** | **str** | Document type value. | 
**supported_by_trading_partner** | **bool** | Does trading partner support receiving this document type. | 
**supported_by_avalara** | **bool** | Does avalara support exchanging this document type. | [optional] 
**extensions** | [**List[Extension]**](Extension.md) | Optional array used to carry additional metadata or configuration values that may be required by specific document types. When creating or updating a trading partner, the keys provided in the &#39;extensions&#39; attribute must be selected from a predefined list of supported extensions. Using any unsupported keys will result in a validation error. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.supported_document_types import SupportedDocumentTypes

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedDocumentTypes from a JSON string
supported_document_types_instance = SupportedDocumentTypes.from_json(json)
# print the JSON string representation of the object
print(SupportedDocumentTypes.to_json())

# convert the object into a dict
supported_document_types_dict = supported_document_types_instance.to_dict()
# create an instance of SupportedDocumentTypes from a dict
supported_document_types_from_dict = SupportedDocumentTypes.from_dict(supported_document_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


