# FetchDocumentsRequestDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Descriptor of the identifier | 
**value** | **str** | Value of the identifier | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.fetch_documents_request_data_inner import FetchDocumentsRequestDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDocumentsRequestDataInner from a JSON string
fetch_documents_request_data_inner_instance = FetchDocumentsRequestDataInner.from_json(json)
# print the JSON string representation of the object
print(FetchDocumentsRequestDataInner.to_json())

# convert the object into a dict
fetch_documents_request_data_inner_dict = fetch_documents_request_data_inner_instance.to_dict()
# create an instance of FetchDocumentsRequestDataInner from a dict
fetch_documents_request_data_inner_from_dict = FetchDocumentsRequestDataInner.from_dict(fetch_documents_request_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


