# DirectorySearchResponseValueInnerSupportedDocumentTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document type name. | [optional] 
**value** | **str** | Document type identifier. | [optional] 
**supported_by_trading_partner** | **bool** | Does trading partner support receiving this document type | [optional] 
**supported_by_avalara** | **bool** | Does avalara support exchanging this document type | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.directory_search_response_value_inner_supported_document_types_inner import DirectorySearchResponseValueInnerSupportedDocumentTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorySearchResponseValueInnerSupportedDocumentTypesInner from a JSON string
directory_search_response_value_inner_supported_document_types_inner_instance = DirectorySearchResponseValueInnerSupportedDocumentTypesInner.from_json(json)
# print the JSON string representation of the object
print(DirectorySearchResponseValueInnerSupportedDocumentTypesInner.to_json())

# convert the object into a dict
directory_search_response_value_inner_supported_document_types_inner_dict = directory_search_response_value_inner_supported_document_types_inner_instance.to_dict()
# create an instance of DirectorySearchResponseValueInnerSupportedDocumentTypesInner from a dict
directory_search_response_value_inner_supported_document_types_inner_from_dict = DirectorySearchResponseValueInnerSupportedDocumentTypesInner.from_dict(directory_search_response_value_inner_supported_document_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


