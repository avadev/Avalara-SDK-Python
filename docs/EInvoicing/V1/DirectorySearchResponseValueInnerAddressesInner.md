# DirectorySearchResponseValueInnerAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Address line 1 | [optional] 
**line2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Country | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.directory_search_response_value_inner_addresses_inner import DirectorySearchResponseValueInnerAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorySearchResponseValueInnerAddressesInner from a JSON string
directory_search_response_value_inner_addresses_inner_instance = DirectorySearchResponseValueInnerAddressesInner.from_json(json)
# print the JSON string representation of the object
print(DirectorySearchResponseValueInnerAddressesInner.to_json())

# convert the object into a dict
directory_search_response_value_inner_addresses_inner_dict = directory_search_response_value_inner_addresses_inner_instance.to_dict()
# create an instance of DirectorySearchResponseValueInnerAddressesInner from a dict
directory_search_response_value_inner_addresses_inner_from_dict = DirectorySearchResponseValueInnerAddressesInner.from_dict(directory_search_response_value_inner_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


