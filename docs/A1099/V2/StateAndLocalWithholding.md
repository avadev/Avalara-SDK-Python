# StateAndLocalWithholding


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


