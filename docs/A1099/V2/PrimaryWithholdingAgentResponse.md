# PrimaryWithholdingAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_withholding_agent_name** | **str** |  | [optional] 
**primary_withholding_agent_ein** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.primary_withholding_agent_response import PrimaryWithholdingAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryWithholdingAgentResponse from a JSON string
primary_withholding_agent_response_instance = PrimaryWithholdingAgentResponse.from_json(json)
# print the JSON string representation of the object
print(PrimaryWithholdingAgentResponse.to_json())

# convert the object into a dict
primary_withholding_agent_response_dict = primary_withholding_agent_response_instance.to_dict()
# create an instance of PrimaryWithholdingAgentResponse from a dict
primary_withholding_agent_response_from_dict = PrimaryWithholdingAgentResponse.from_dict(primary_withholding_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


