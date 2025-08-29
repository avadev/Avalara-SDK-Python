# IntermediaryOrFlowThrough

Intermediary or flow-through entity information for tax forms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ein** | **str** | EIN (Employer Identification Number) of the intermediary or flow-through entity | [optional] 
**chap3_status_code** | **str** | Chapter 3 status code for the intermediary or flow-through entity | [optional] 
**chap4_status_code** | **str** | Chapter 4 status code for the intermediary or flow-through entity | [optional] 
**name** | **str** | Name of the intermediary or flow-through entity | [optional] 
**giin** | **str** | GIIN (Global Intermediary Identification Number) of the intermediary or flow-through entity | [optional] 
**country_code** | **str** | Country code for the intermediary or flow-through entity | [optional] 
**foreign_tin** | **str** | Foreign TIN of the intermediary or flow-through entity | [optional] 
**address** | **str** | Address of the intermediary or flow-through entity | [optional] 
**city** | **str** | City of the intermediary or flow-through entity | [optional] 
**state** | **str** | State of the intermediary or flow-through entity | [optional] 
**zip** | **str** | Zip code of the intermediary or flow-through entity | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.intermediary_or_flow_through import IntermediaryOrFlowThrough

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryOrFlowThrough from a JSON string
intermediary_or_flow_through_instance = IntermediaryOrFlowThrough.from_json(json)
# print the JSON string representation of the object
print(IntermediaryOrFlowThrough.to_json())

# convert the object into a dict
intermediary_or_flow_through_dict = intermediary_or_flow_through_instance.to_dict()
# create an instance of IntermediaryOrFlowThrough from a dict
intermediary_or_flow_through_from_dict = IntermediaryOrFlowThrough.from_dict(intermediary_or_flow_through_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


