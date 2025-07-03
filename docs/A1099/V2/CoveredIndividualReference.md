# CoveredIndividualReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**tin** | **str** |  | [optional] 
**birth_date** | **datetime** |  | [optional] 
**covered_month0** | **bool** |  | [optional] 
**covered_month1** | **bool** |  | [optional] 
**covered_month2** | **bool** |  | [optional] 
**covered_month3** | **bool** |  | [optional] 
**covered_month4** | **bool** |  | [optional] 
**covered_month5** | **bool** |  | [optional] 
**covered_month6** | **bool** |  | [optional] 
**covered_month7** | **bool** |  | [optional] 
**covered_month8** | **bool** |  | [optional] 
**covered_month9** | **bool** |  | [optional] 
**covered_month10** | **bool** |  | [optional] 
**covered_month11** | **bool** |  | [optional] 
**covered_month12** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.covered_individual_reference import CoveredIndividualReference

# TODO update the JSON string below
json = "{}"
# create an instance of CoveredIndividualReference from a JSON string
covered_individual_reference_instance = CoveredIndividualReference.from_json(json)
# print the JSON string representation of the object
print(CoveredIndividualReference.to_json())

# convert the object into a dict
covered_individual_reference_dict = covered_individual_reference_instance.to_dict()
# create an instance of CoveredIndividualReference from a dict
covered_individual_reference_from_dict = CoveredIndividualReference.from_dict(covered_individual_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


