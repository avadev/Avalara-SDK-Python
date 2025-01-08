# DocumentSummary

Displays a summary of information about the document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for this document | [optional] 
**process_date_time** | **str** | The date and time when the document was processed, displayed in the format YYYY-MM-DDThh:mm:ss | [optional] 
**status** | **str** | The transaction status: &lt;br&gt; &#39;Pending&#39; &lt;br&gt; &#39;Failed&#39; &lt;br&gt; &#39;Complete&#39; | [optional] 
**supplier_name** | **str** | The name of the supplier in the transaction | [optional] 
**customer_name** | **str** | The name of the customer in the transaction | [optional] 
**document_number** | **str** | The invoice document number | [optional] 
**document_date** | **str** | The invoice issue date | [optional] 
**flow** | **str** | The invoice direction, where issued &#x3D; &#x60;out&#x60; and received &#x3D; &#x60;in&#x60; | [optional] 
**country_code** | **str** | The two-letter ISO-3166 country code for the country where the e-invoice is being submitted | [optional] 
**country_mandate** | **str** | The e-invoicing mandate for the specified country | [optional] 
**interface** | **str** | The interface where the invoice data is sent | [optional] 
**receiver** | **str** | The invoice recipient based on the interface | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


