# FederalEfileErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The exact IRS/IRIS error code, when IRIS provides one. | [optional] 
**message** | **str** | The human-readable error message associated with the code, if provided by IRIS. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.federal_efile_error_response import FederalEfileErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FederalEfileErrorResponse from a JSON string
federal_efile_error_response_instance = FederalEfileErrorResponse.from_json(json)
# print the JSON string representation of the object
print(FederalEfileErrorResponse.to_json())

# convert the object into a dict
federal_efile_error_response_dict = federal_efile_error_response_instance.to_dict()
# create an instance of FederalEfileErrorResponse from a dict
federal_efile_error_response_from_dict = FederalEfileErrorResponse.from_dict(federal_efile_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


