# SubmitDocumentMetadata

Key value pairs of metadata for a document submission <br><pre>{  \"workflowId\": \"partner-einvoicing\", \"dataFormat\": \"ubl-invoice\", \"dataFormatVersion\": \"2.1\", \"countryCode\": \"SA\", \"countryMandate\": \"SA-Phase1-B2B\" }</pre> <br> 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Specifies a unique ID for this workflow. | 
**data_format** | **str** | Specifies the data format for this workflow. | 
**data_format_version** | **str** | Specifies the data format version number. | 
**output_data_format** | **str** | Specifies the format of the output document to be generated for the recipient. This format should be chosen based on the recipient&#39;s preferences or requirements as defined by applicable e-invoicing regulations. When not specified for mandates that don&#39;t require a specific output format, the system will use the default format defined for that mandate. | [optional] 
**output_data_format_version** | **str** | Specifies the version of the selected output document format | [optional] 
**country_code** | **str** | The two-letter ISO-3166 country code for the country where the document is being submitted | 
**country_mandate** | **str** | The e-invoicing mandate for the specified country. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.submit_document_metadata import SubmitDocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitDocumentMetadata from a JSON string
submit_document_metadata_instance = SubmitDocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(SubmitDocumentMetadata.to_json())

# convert the object into a dict
submit_document_metadata_dict = submit_document_metadata_instance.to_dict()
# create an instance of SubmitDocumentMetadata from a dict
submit_document_metadata_from_dict = SubmitDocumentMetadata.from_dict(submit_document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


