# DocumentFetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for this document that can be used for status checking and file downloads. This is a UID created by the Avalara E-Invoicing platform. | [optional] 
**status** | **str** | Status of the document | [optional] 
**event_date_time** | **str** | The date and time when the inbound document was accepted by the Avalara E-Invoicing Platform | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_fetch import DocumentFetch

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFetch from a JSON string
document_fetch_instance = DocumentFetch.from_json(json)
# print the JSON string representation of the object
print(DocumentFetch.to_json())

# convert the object into a dict
document_fetch_dict = document_fetch_instance.to_dict()
# create an instance of DocumentFetch from a dict
document_fetch_from_dict = DocumentFetch.from_dict(document_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


