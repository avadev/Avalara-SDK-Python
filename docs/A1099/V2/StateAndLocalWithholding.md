# StateAndLocalWithholding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_tax_withheld** | **float** | Amount of state tax that was withheld | [optional] 
**state** | **str** | US state | [optional] 
**state_id** | **str** | State ID of the entity issuing the form | [optional] 
**state_income** | **float** | Amount of state income | [optional] 
**local_tax_withheld** | **float** | Amount of local tax that was withheld | [optional] 
**locality** | **str** | Locality name | [optional] 
**locality_id** | **str** | Locality ID of the entity issuing the form | [optional] 
**local_income** | **float** | Amount of local income | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.state_and_local_withholding import StateAndLocalWithholding

# TODO update the JSON string below
json = "{}"
# create an instance of StateAndLocalWithholding from a JSON string
state_and_local_withholding_instance = StateAndLocalWithholding.from_json(json)
# print the JSON string representation of the object
print(StateAndLocalWithholding.to_json())

# convert the object into a dict
state_and_local_withholding_dict = state_and_local_withholding_instance.to_dict()
# create an instance of StateAndLocalWithholding from a dict
state_and_local_withholding_from_dict = StateAndLocalWithholding.from_dict(state_and_local_withholding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


