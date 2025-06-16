# FetchDocumentsRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Specifies a unique ID for this workflow. | 
**data_format** | **str** | Specifies the data format for this workflow | 
**data_format_version** | **float** | Specifies the data format version number | 
**output_data_format** | **str** | Specifies the format of the output document to be generated for the recipient. This format should be chosen based on the recipient&#39;s preferences or requirements as defined by applicable e-invoicing regulations. When not specified for mandates that don&#39;t require a specific output format, the system will use the default format defined for that mandate. | 
**output_data_format_version** | **float** | Specifies the version of the selected output document format | 
**country_code** | **str** | The two-letter ISO-3166 country code for the country for which document is being retrieved | 
**country_mandate** | **str** | The e-invoicing mandate for the specified country | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.fetch_documents_request_metadata import FetchDocumentsRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDocumentsRequestMetadata from a JSON string
fetch_documents_request_metadata_instance = FetchDocumentsRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(FetchDocumentsRequestMetadata.to_json())

# convert the object into a dict
fetch_documents_request_metadata_dict = fetch_documents_request_metadata_instance.to_dict()
# create an instance of FetchDocumentsRequestMetadata from a dict
fetch_documents_request_metadata_from_dict = FetchDocumentsRequestMetadata.from_dict(fetch_documents_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


