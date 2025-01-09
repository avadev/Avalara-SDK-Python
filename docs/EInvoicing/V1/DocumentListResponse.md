# DocumentListResponse

Returns the requested list of documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **str** | Count of collections for the given date range | [optional] 
**next_link** | **str** |  | [optional] 
**value** | [**List[DocumentSummary]**](DocumentSummary.md) | Array of documents matching query parameters | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_list_response import DocumentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentListResponse from a JSON string
document_list_response_instance = DocumentListResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentListResponse.to_json())

# convert the object into a dict
document_list_response_dict = document_list_response_instance.to_dict()
# create an instance of DocumentListResponse from a dict
document_list_response_from_dict = DocumentListResponse.from_dict(document_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


