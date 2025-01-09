# DocumentFetchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentFetchRequestDataInner]**](DocumentFetchRequestDataInner.md) | Array of key-value pairs used to retrieve inbound documents from the Tax Authority | [optional] 
**metadata** | [**DocumentFetchRequestMetadata**](DocumentFetchRequestMetadata.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_fetch_request import DocumentFetchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFetchRequest from a JSON string
document_fetch_request_instance = DocumentFetchRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentFetchRequest.to_json())

# convert the object into a dict
document_fetch_request_dict = document_fetch_request_instance.to_dict()
# create an instance of DocumentFetchRequest from a dict
document_fetch_request_from_dict = DocumentFetchRequest.from_dict(document_fetch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


