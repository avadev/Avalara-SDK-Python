# DocumentSubmissionError

Returns an HTTP status code and message for an 'exception'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **str** | The three-digit HTTP status code for the exception | [optional] 
**message** | **str** | A message explaining the exception | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_submission_error import DocumentSubmissionError

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSubmissionError from a JSON string
document_submission_error_instance = DocumentSubmissionError.from_json(json)
# print the JSON string representation of the object
print(DocumentSubmissionError.to_json())

# convert the object into a dict
document_submission_error_dict = document_submission_error_instance.to_dict()
# create an instance of DocumentSubmissionError from a dict
document_submission_error_from_dict = DocumentSubmissionError.from_dict(document_submission_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


