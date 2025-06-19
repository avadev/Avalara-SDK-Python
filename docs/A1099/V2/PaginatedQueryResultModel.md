# PaginatedQueryResultModel

Generic paginated model to wrap query response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **int** |  | [optional] 
**value** | **List[object]** |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.paginated_query_result_model import PaginatedQueryResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQueryResultModel from a JSON string
paginated_query_result_model_instance = PaginatedQueryResultModel.from_json(json)
# print the JSON string representation of the object
print(PaginatedQueryResultModel.to_json())

# convert the object into a dict
paginated_query_result_model_dict = paginated_query_result_model_instance.to_dict()
# create an instance of PaginatedQueryResultModel from a dict
paginated_query_result_model_from_dict = PaginatedQueryResultModel.from_dict(paginated_query_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


