# DocumentFetchRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | Specifies a unique ID for this workflow. | 
**data_format** | **str** | Specifies the data format for this workflow | 
**data_format_version** | **float** | Specifies the data format version number | 
**country_code** | **str** | The two-letter ISO-3166 country code for the country for which document is being retrieved | 
**country_mandate** | **str** | The e-invoicing mandate for the specified country | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_fetch_request_metadata import DocumentFetchRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFetchRequestMetadata from a JSON string
document_fetch_request_metadata_instance = DocumentFetchRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(DocumentFetchRequestMetadata.to_json())

# convert the object into a dict
document_fetch_request_metadata_dict = document_fetch_request_metadata_instance.to_dict()
# create an instance of DocumentFetchRequestMetadata from a dict
document_fetch_request_metadata_from_dict = DocumentFetchRequestMetadata.from_dict(document_fetch_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


