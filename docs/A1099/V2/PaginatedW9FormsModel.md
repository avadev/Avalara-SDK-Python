# PaginatedW9FormsModel

Paginated model for W9/W4/W8 forms query response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **int** |  | [optional] 
**value** | [**List[IW9FormDataModelsOneOf]**](IW9FormDataModelsOneOf.md) |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.paginated_w9_forms_model import PaginatedW9FormsModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedW9FormsModel from a JSON string
paginated_w9_forms_model_instance = PaginatedW9FormsModel.from_json(json)
# print the JSON string representation of the object
print(PaginatedW9FormsModel.to_json())

# convert the object into a dict
paginated_w9_forms_model_dict = paginated_w9_forms_model_instance.to_dict()
# create an instance of PaginatedW9FormsModel from a dict
paginated_w9_forms_model_from_dict = PaginatedW9FormsModel.from_dict(paginated_w9_forms_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


