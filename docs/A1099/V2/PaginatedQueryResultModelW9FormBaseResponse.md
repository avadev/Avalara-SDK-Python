# PaginatedQueryResultModelW9FormBaseResponse

Generic paginated model to wrap query response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **int** |  | [optional] 
**value** | [**List[CreateW9Form201Response]**](CreateW9Form201Response.md) |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.paginated_query_result_model_w9_form_base_response import PaginatedQueryResultModelW9FormBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQueryResultModelW9FormBaseResponse from a JSON string
paginated_query_result_model_w9_form_base_response_instance = PaginatedQueryResultModelW9FormBaseResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedQueryResultModelW9FormBaseResponse.to_json())

# convert the object into a dict
paginated_query_result_model_w9_form_base_response_dict = paginated_query_result_model_w9_form_base_response_instance.to_dict()
# create an instance of PaginatedQueryResultModelW9FormBaseResponse from a dict
paginated_query_result_model_w9_form_base_response_from_dict = PaginatedQueryResultModelW9FormBaseResponse.from_dict(paginated_query_result_model_w9_form_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


