# SupportedDocumentStatuses

Represents a document status defined by the mandate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The name of the status (e.g., Approved, Fully Paid). | [optional] 
**description** | **str** | Explanation of what the status means. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.supported_document_statuses import SupportedDocumentStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedDocumentStatuses from a JSON string
supported_document_statuses_instance = SupportedDocumentStatuses.from_json(json)
# print the JSON string representation of the object
print(SupportedDocumentStatuses.to_json())

# convert the object into a dict
supported_document_statuses_dict = supported_document_statuses_instance.to_dict()
# create an instance of SupportedDocumentStatuses from a dict
supported_document_statuses_from_dict = SupportedDocumentStatuses.from_dict(supported_document_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


