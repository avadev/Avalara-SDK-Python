# CoveredIndividualRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Covered individual&#39;s first name | [optional] 
**middle_name** | **str** | Covered individual&#39;s middle name | [optional] 
**last_name** | **str** | Covered individual&#39;s last name | [optional] 
**name_suffix** | **str** | Covered individual&#39;s name suffix | [optional] 
**tin** | **str** | Covered individual&#39;s TIN (SSN or ITIN) | [optional] 
**birth_date** | **datetime** | Covered individual&#39;s date of birth | [optional] 
**covered_all_months** | **bool** | Coverage indicator for all 12 months | [optional] 
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


