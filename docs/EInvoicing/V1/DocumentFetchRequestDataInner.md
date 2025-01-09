# DocumentFetchRequestDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Descriptor of the identifier | 
**value** | **str** | Value of the identifier | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_fetch_request_data_inner import DocumentFetchRequestDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFetchRequestDataInner from a JSON string
document_fetch_request_data_inner_instance = DocumentFetchRequestDataInner.from_json(json)
# print the JSON string representation of the object
print(DocumentFetchRequestDataInner.to_json())

# convert the object into a dict
document_fetch_request_data_inner_dict = document_fetch_request_data_inner_instance.to_dict()
# create an instance of DocumentFetchRequestDataInner from a dict
document_fetch_request_data_inner_from_dict = DocumentFetchRequestDataInner.from_dict(document_fetch_request_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


