# FederalEfileStatusDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**errors** | [**List[FederalEfileError]**](FederalEfileError.md) | Errors the IRS returned for the form&#39;s most recent IRIS filing.  Present only when the filing was rejected or accepted with errors; omitted for forms not filed through IRIS. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.federal_efile_status_detail import FederalEfileStatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FederalEfileStatusDetail from a JSON string
federal_efile_status_detail_instance = FederalEfileStatusDetail.from_json(json)
# print the JSON string representation of the object
print(FederalEfileStatusDetail.to_json())

# convert the object into a dict
federal_efile_status_detail_dict = federal_efile_status_detail_instance.to_dict()
# create an instance of FederalEfileStatusDetail from a dict
federal_efile_status_detail_from_dict = FederalEfileStatusDetail.from_dict(federal_efile_status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


