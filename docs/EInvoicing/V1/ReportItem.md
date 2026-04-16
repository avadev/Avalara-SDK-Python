# ReportItem

Represents a single report with full details including metadata and associated transaction IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_id** | **str** | The unique ID for this report. | [optional] 
**job_id** | **str** | The unique ID of the job that generated this report. | [optional] 
**report_generate_date** | **datetime** | The date and time when the report was generated. | [optional] 
**report_from** | **date** | The start date of the reporting period. | [optional] 
**report_to** | **date** | The end date of the reporting period. | [optional] 
**country_code** | **str** | The two-letter ISO-3166 country code for which this report was generated. | [optional] 
**country_mandate** | **str** | The e-invoicing mandate for the specified country. | [optional] 
**document_type** | **str** | The type of document covered by this report. | [optional] 
**document_sub_type** | **str** | The sub-type of the document. | [optional] 
**report_reference** | **str** | An internal reference path for the report. | [optional] 
**report_name** | **str** | The name of the report file. | [optional] 
**status** | **str** | The current status of the report. Possible values include: PENDING, PROCESSING, COMPLETED, FAILED, SENT_TO_PPF, ERROR. | [optional] 
**report_format_mimetypes** | **str** | The MIME type of the report file. | [optional] 
**tenant_id** | **str** | The tenant identifier associated with this report. | [optional] 
**ta_name** | **str** | The name of the tax authority for this report. | [optional] 
**tax_invoice_amount** | **float** | The total invoice amount covered by this report. | [optional] 
**total_tax_amount** | **float** | The total tax amount covered by this report. | [optional] 
**metadata** | **object** | Additional report metadata (free-form JSON). Contents vary by country mandate. | [optional] 
**transaction_ids** | **List[str]** | List of transaction IDs associated with this report. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.report_item import ReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportItem from a JSON string
report_item_instance = ReportItem.from_json(json)
# print the JSON string representation of the object
print(ReportItem.to_json())

# convert the object into a dict
report_item_dict = report_item_instance.to_dict()
# create an instance of ReportItem from a dict
report_item_from_dict = ReportItem.from_dict(report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


