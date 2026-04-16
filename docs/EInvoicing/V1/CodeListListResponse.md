# CodeListListResponse

Returns the requested list of code lists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **str** | Count of code lists for the given query parameters | [optional] 
**next_link** | **str** |  | [optional] 
**value** | [**List[CodeListSummary]**](CodeListSummary.md) | Array of code lists matching query parameters | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.code_list_list_response import CodeListListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeListListResponse from a JSON string
code_list_list_response_instance = CodeListListResponse.from_json(json)
# print the JSON string representation of the object
print(CodeListListResponse.to_json())

# convert the object into a dict
code_list_list_response_dict = code_list_list_response_instance.to_dict()
# create an instance of CodeListListResponse from a dict
code_list_list_response_from_dict = CodeListListResponse.from_dict(code_list_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


