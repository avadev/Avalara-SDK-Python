# DirectorySearchResponseValueInnerIdentifiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Peppol Participant ID if the participant is in Peppol network | [optional] 
**value** | **str** | Value of the identifier | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.directory_search_response_value_inner_identifiers_inner import DirectorySearchResponseValueInnerIdentifiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorySearchResponseValueInnerIdentifiersInner from a JSON string
directory_search_response_value_inner_identifiers_inner_instance = DirectorySearchResponseValueInnerIdentifiersInner.from_json(json)
# print the JSON string representation of the object
print(DirectorySearchResponseValueInnerIdentifiersInner.to_json())

# convert the object into a dict
directory_search_response_value_inner_identifiers_inner_dict = directory_search_response_value_inner_identifiers_inner_instance.to_dict()
# create an instance of DirectorySearchResponseValueInnerIdentifiersInner from a dict
directory_search_response_value_inner_identifiers_inner_from_dict = DirectorySearchResponseValueInnerIdentifiersInner.from_dict(directory_search_response_value_inner_identifiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


