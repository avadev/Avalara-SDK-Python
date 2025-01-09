# DirectorySearchResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Avalara unique ID of the participant in the directory. | [optional] 
**name** | **str** | Name of the participant (typically, the name of the business entity). | [optional] 
**network** | **str** | The network where the participant is present. | [optional] 
**registration_date** | **date** | Registration date of the participant if available | [optional] 
**identifiers** | [**List[DirectorySearchResponseValueInnerIdentifiersInner]**](DirectorySearchResponseValueInnerIdentifiersInner.md) |  | [optional] 
**addresses** | [**List[DirectorySearchResponseValueInnerAddressesInner]**](DirectorySearchResponseValueInnerAddressesInner.md) |  | [optional] 
**supported_document_types** | [**List[DirectorySearchResponseValueInnerSupportedDocumentTypesInner]**](DirectorySearchResponseValueInnerSupportedDocumentTypesInner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.directory_search_response_value_inner import DirectorySearchResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorySearchResponseValueInner from a JSON string
directory_search_response_value_inner_instance = DirectorySearchResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(DirectorySearchResponseValueInner.to_json())

# convert the object into a dict
directory_search_response_value_inner_dict = directory_search_response_value_inner_instance.to_dict()
# create an instance of DirectorySearchResponseValueInner from a dict
directory_search_response_value_inner_from_dict = DirectorySearchResponseValueInner.from_dict(directory_search_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


