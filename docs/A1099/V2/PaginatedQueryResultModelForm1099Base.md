# PaginatedQueryResultModelForm1099Base

Generic paginated model to wrap query response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **int** |  | [optional] 
**value** | [**List[Get1099Form200Response]**](Get1099Form200Response.md) |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.paginated_query_result_model_form1099_base import PaginatedQueryResultModelForm1099Base

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQueryResultModelForm1099Base from a JSON string
paginated_query_result_model_form1099_base_instance = PaginatedQueryResultModelForm1099Base.from_json(json)
# print the JSON string representation of the object
print(PaginatedQueryResultModelForm1099Base.to_json())

# convert the object into a dict
paginated_query_result_model_form1099_base_dict = paginated_query_result_model_form1099_base_instance.to_dict()
# create an instance of PaginatedQueryResultModelForm1099Base from a dict
paginated_query_result_model_form1099_base_from_dict = PaginatedQueryResultModelForm1099Base.from_dict(paginated_query_result_model_form1099_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


