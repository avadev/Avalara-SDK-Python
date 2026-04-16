# ReportListResponse

Returns the requested list of reports matching the query parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **str** | Count of reports matching the filter for the given query. Present when the request includes $count&#x3D;true. | [optional] 
**next_link** | **str** | URL to retrieve the next page of results when more items match the query. Omitted or null when there is no next page. | [optional] 
**value** | [**List[ReportItem]**](ReportItem.md) | Array of reports matching the query parameters. | 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.report_list_response import ReportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportListResponse from a JSON string
report_list_response_instance = ReportListResponse.from_json(json)
# print the JSON string representation of the object
print(ReportListResponse.to_json())

# convert the object into a dict
report_list_response_dict = report_list_response_instance.to_dict()
# create an instance of ReportListResponse from a dict
report_list_response_from_dict = ReportListResponse.from_dict(report_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


