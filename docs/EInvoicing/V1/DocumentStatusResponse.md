# DocumentStatusResponse

Returns the current document ID and status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for this document | [optional] 
**status** | **str** | Document status. See the &#x60;supportedDocumentStatuses&#x60; field in the GET /mandates response for full status definitions. | [optional] 
**business_status** | **str** | Represents the document&#39;s business lifecycle state based on responses from external actors (Tax Authority, PDP, or ERP), such as acceptance, rejection, or validation. | [optional] 
**events** | [**List[StatusEvent]**](StatusEvent.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_status_response import DocumentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatusResponse from a JSON string
document_status_response_instance = DocumentStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentStatusResponse.to_json())

# convert the object into a dict
document_status_response_dict = document_status_response_instance.to_dict()
# create an instance of DocumentStatusResponse from a dict
document_status_response_from_dict = DocumentStatusResponse.from_dict(document_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


