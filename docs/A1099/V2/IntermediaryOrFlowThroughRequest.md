# IntermediaryOrFlowThroughRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ein** | **str** |  | [optional] 
**chap3_status_code** | **str** |  | [optional] 
**chap4_status_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**giin** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**foreign_tin** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.intermediary_or_flow_through_request import IntermediaryOrFlowThroughRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediaryOrFlowThroughRequest from a JSON string
intermediary_or_flow_through_request_instance = IntermediaryOrFlowThroughRequest.from_json(json)
# print the JSON string representation of the object
print(IntermediaryOrFlowThroughRequest.to_json())

# convert the object into a dict
intermediary_or_flow_through_request_dict = intermediary_or_flow_through_request_instance.to_dict()
# create an instance of IntermediaryOrFlowThroughRequest from a dict
intermediary_or_flow_through_request_from_dict = IntermediaryOrFlowThroughRequest.from_dict(intermediary_or_flow_through_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


