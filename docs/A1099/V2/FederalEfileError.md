# FederalEfileError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | IRIS error code | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.federal_efile_error import FederalEfileError

# TODO update the JSON string below
json = "{}"
# create an instance of FederalEfileError from a JSON string
federal_efile_error_instance = FederalEfileError.from_json(json)
# print the JSON string representation of the object
print(FederalEfileError.to_json())

# convert the object into a dict
federal_efile_error_dict = federal_efile_error_instance.to_dict()
# create an instance of FederalEfileError from a dict
federal_efile_error_from_dict = FederalEfileError.from_dict(federal_efile_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


