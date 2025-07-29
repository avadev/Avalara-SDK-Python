# PrimaryWithholdingAgentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_withholding_agent_name** | **str** |  | [optional] 
**primary_withholding_agent_ein** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.primary_withholding_agent_request import PrimaryWithholdingAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryWithholdingAgentRequest from a JSON string
primary_withholding_agent_request_instance = PrimaryWithholdingAgentRequest.from_json(json)
# print the JSON string representation of the object
print(PrimaryWithholdingAgentRequest.to_json())

# convert the object into a dict
primary_withholding_agent_request_dict = primary_withholding_agent_request_instance.to_dict()
# create an instance of PrimaryWithholdingAgentRequest from a dict
primary_withholding_agent_request_from_dict = PrimaryWithholdingAgentRequest.from_dict(primary_withholding_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


