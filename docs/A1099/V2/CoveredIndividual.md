# CoveredIndividual

Covered individual information for health coverage forms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Covered individual&#39;s ID | [optional] [readonly] 
**first_name** | **str** | Covered individual&#39;s first name | 
**middle_name** | **str** | Covered individual&#39;s middle name | [optional] 
**last_name** | **str** | Covered individual&#39;s last name | 
**name_suffix** | **str** | Covered individual&#39;s name suffix | [optional] 
**tin** | **str** | Covered individual&#39;s Federal Tax Identification Number (TIN).. SSN or ITIN. Required unless unavailable. | [optional] 
**birth_date** | **date** | Covered individual&#39;s date of birth - Required when SSN is missing. | [optional] 
**covered_january** | **bool** | Coverage indicator for January | [optional] 
**covered_february** | **bool** | Coverage indicator for February | [optional] 
**covered_march** | **bool** | Coverage indicator for March | [optional] 
**covered_april** | **bool** | Coverage indicator for April | [optional] 
**covered_may** | **bool** | Coverage indicator for May | [optional] 
**covered_june** | **bool** | Coverage indicator for June | [optional] 
**covered_july** | **bool** | Coverage indicator for July | [optional] 
**covered_august** | **bool** | Coverage indicator for August | [optional] 
**covered_september** | **bool** | Coverage indicator for September | [optional] 
**covered_october** | **bool** | Coverage indicator for October | [optional] 
**covered_november** | **bool** | Coverage indicator for November | [optional] 
**covered_december** | **bool** | Coverage indicator for December | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.covered_individual import CoveredIndividual

# TODO update the JSON string below
json = "{}"
# create an instance of CoveredIndividual from a JSON string
covered_individual_instance = CoveredIndividual.from_json(json)
# print the JSON string representation of the object
print(CoveredIndividual.to_json())

# convert the object into a dict
covered_individual_dict = covered_individual_instance.to_dict()
# create an instance of CoveredIndividual from a dict
covered_individual_from_dict = CoveredIndividual.from_dict(covered_individual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


