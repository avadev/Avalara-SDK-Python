# ValidationErrorApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.validation_error_app import ValidationErrorApp

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorApp from a JSON string
validation_error_app_instance = ValidationErrorApp.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorApp.to_json())

# convert the object into a dict
validation_error_app_dict = validation_error_app_instance.to_dict()
# create an instance of ValidationErrorApp from a dict
validation_error_app_from_dict = ValidationErrorApp.from_dict(validation_error_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


