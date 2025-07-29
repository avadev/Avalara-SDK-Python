# StateAndLocalWithholdingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_tax_withheld** | **float** | Amount of state tax that was withheld | [optional] 
**state** | **str** | US state | [optional] 
**state_id_number** | **str** | State ID number of the entity issuing the form | [optional] 
**state_income** | **float** | Amount of state income | [optional] 
**local_tax_withheld** | **float** | Amount of local tax that was withheld | [optional] 
**locality** | **str** | Locality name | [optional] 
**locality_id_number** | **str** | Locality ID number of the entity issuing the form | [optional] 
**local_income** | **float** | Amount of local income | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.state_and_local_withholding_response import StateAndLocalWithholdingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StateAndLocalWithholdingResponse from a JSON string
state_and_local_withholding_response_instance = StateAndLocalWithholdingResponse.from_json(json)
# print the JSON string representation of the object
print(StateAndLocalWithholdingResponse.to_json())

# convert the object into a dict
state_and_local_withholding_response_dict = state_and_local_withholding_response_instance.to_dict()
# create an instance of StateAndLocalWithholdingResponse from a dict
state_and_local_withholding_response_from_dict = StateAndLocalWithholdingResponse.from_dict(state_and_local_withholding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


