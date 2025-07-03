# CoveredIndividualRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**birth_date** | **datetime** |  | [optional] 
**covered_month_indicator0** | **bool** |  | [optional] 
**covered_month_indicator1** | **bool** |  | [optional] 
**covered_month_indicator2** | **bool** |  | [optional] 
**covered_month_indicator3** | **bool** |  | [optional] 
**covered_month_indicator4** | **bool** |  | [optional] 
**covered_month_indicator5** | **bool** |  | [optional] 
**covered_month_indicator6** | **bool** |  | [optional] 
**covered_month_indicator7** | **bool** |  | [optional] 
**covered_month_indicator8** | **bool** |  | [optional] 
**covered_month_indicator9** | **bool** |  | [optional] 
**covered_month_indicator10** | **bool** |  | [optional] 
**covered_month_indicator11** | **bool** |  | [optional] 
**covered_month_indicator12** | **bool** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.covered_individual_request import CoveredIndividualRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoveredIndividualRequest from a JSON string
covered_individual_request_instance = CoveredIndividualRequest.from_json(json)
# print the JSON string representation of the object
print(CoveredIndividualRequest.to_json())

# convert the object into a dict
covered_individual_request_dict = covered_individual_request_instance.to_dict()
# create an instance of CoveredIndividualRequest from a dict
covered_individual_request_from_dict = CoveredIndividualRequest.from_dict(covered_individual_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


