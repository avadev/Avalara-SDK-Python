# DocumentSubmitResponse

Returns the unique ID of a successful document submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for this document that can be used for status checking and file downloads. This is a UID created by the Avalara E-Invoicing platform. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_submit_response import DocumentSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSubmitResponse from a JSON string
document_submit_response_instance = DocumentSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSubmitResponse.to_json())

# convert the object into a dict
document_submit_response_dict = document_submit_response_instance.to_dict()
# create an instance of DocumentSubmitResponse from a dict
document_submit_response_from_dict = DocumentSubmitResponse.from_dict(document_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


