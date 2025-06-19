# StateAndLocalWithholdingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_tax_withheld** | **float** |  | [optional] 
**state** | **str** |  | [optional] 
**state_id_number** | **str** |  | [optional] 
**state_income** | **float** |  | [optional] 
**local_tax_withheld** | **float** |  | [optional] 
**locality** | **str** |  | [optional] 
**locality_id_number** | **str** |  | [optional] 
**local_income** | **float** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.state_and_local_withholding_request import StateAndLocalWithholdingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StateAndLocalWithholdingRequest from a JSON string
state_and_local_withholding_request_instance = StateAndLocalWithholdingRequest.from_json(json)
# print the JSON string representation of the object
print(StateAndLocalWithholdingRequest.to_json())

# convert the object into a dict
state_and_local_withholding_request_dict = state_and_local_withholding_request_instance.to_dict()
# create an instance of StateAndLocalWithholdingRequest from a dict
state_and_local_withholding_request_from_dict = StateAndLocalWithholdingRequest.from_dict(state_and_local_withholding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


