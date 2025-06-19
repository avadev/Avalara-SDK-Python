# FetchDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FetchDocumentsRequestDataInner]**](FetchDocumentsRequestDataInner.md) | Array of key-value pairs used to retrieve inbound documents from the Tax Authority | [optional] 
**metadata** | [**FetchDocumentsRequestMetadata**](FetchDocumentsRequestMetadata.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.fetch_documents_request import FetchDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDocumentsRequest from a JSON string
fetch_documents_request_instance = FetchDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(FetchDocumentsRequest.to_json())

# convert the object into a dict
fetch_documents_request_dict = fetch_documents_request_instance.to_dict()
# create an instance of FetchDocumentsRequest from a dict
fetch_documents_request_from_dict = FetchDocumentsRequest.from_dict(fetch_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


