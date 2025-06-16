# DocumentSummary

Displays a summary of information about the document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for this document | [optional] 
**company_id** | **str** | Unique identifier that represents the company within the system. | [optional] 
**process_date_time** | **str** | The date and time when the document was processed, displayed in the format YYYY-MM-DDThh:mm:ss | [optional] 
**status** | **str** | The Document status | [optional] 
**supplier_name** | **str** | The name of the supplier in the transaction | [optional] 
**customer_name** | **str** | The name of the customer in the transaction | [optional] 
**document_type** | **str** | The document type | [optional] 
**document_version** | **str** | The document version | [optional] 
**document_number** | **str** | The document number | [optional] 
**document_date** | **str** | The document issue date | [optional] 
**flow** | **str** | The document direction, where issued &#x3D; &#x60;out&#x60; and received &#x3D; &#x60;in&#x60; | [optional] 
**country_code** | **str** | The two-letter ISO-3166 country code for the country where the document is being submitted | [optional] 
**country_mandate** | **str** | The e-invoicing mandate for the specified country | [optional] 
**interface** | **str** | The interface where the document is sent | [optional] 
**receiver** | **str** | The document recipient based on the interface | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.document_summary import DocumentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSummary from a JSON string
document_summary_instance = DocumentSummary.from_json(json)
# print the JSON string representation of the object
print(DocumentSummary.to_json())

# convert the object into a dict
document_summary_dict = document_summary_instance.to_dict()
# create an instance of DocumentSummary from a dict
document_summary_from_dict = DocumentSummary.from_dict(document_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


