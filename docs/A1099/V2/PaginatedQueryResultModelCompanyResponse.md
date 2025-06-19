# PaginatedQueryResultModelCompanyResponse

Generic paginated model to wrap query response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **int** |  | [optional] 
**value** | [**List[CompanyResponse]**](CompanyResponse.md) |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.paginated_query_result_model_company_response import PaginatedQueryResultModelCompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedQueryResultModelCompanyResponse from a JSON string
paginated_query_result_model_company_response_instance = PaginatedQueryResultModelCompanyResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedQueryResultModelCompanyResponse.to_json())

# convert the object into a dict
paginated_query_result_model_company_response_dict = paginated_query_result_model_company_response_instance.to_dict()
# create an instance of PaginatedQueryResultModelCompanyResponse from a dict
paginated_query_result_model_company_response_from_dict = PaginatedQueryResultModelCompanyResponse.from_dict(paginated_query_result_model_company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


