# PrimaryWithholdingAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_withholding_agent_name** | **str** |  | [optional] 
**primary_withholding_agent_ein** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.primary_withholding_agent import PrimaryWithholdingAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryWithholdingAgent from a JSON string
primary_withholding_agent_instance = PrimaryWithholdingAgent.from_json(json)
# print the JSON string representation of the object
print(PrimaryWithholdingAgent.to_json())

# convert the object into a dict
primary_withholding_agent_dict = primary_withholding_agent_instance.to_dict()
# create an instance of PrimaryWithholdingAgent from a dict
primary_withholding_agent_from_dict = PrimaryWithholdingAgent.from_dict(primary_withholding_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


