# WorkflowIds

Workflow ID list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this workflow | [optional] 
**description** | **str** | Workflow description | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.workflow_ids import WorkflowIds

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowIds from a JSON string
workflow_ids_instance = WorkflowIds.from_json(json)
# print the JSON string representation of the object
print(WorkflowIds.to_json())

# convert the object into a dict
workflow_ids_dict = workflow_ids_instance.to_dict()
# create an instance of WorkflowIds from a dict
workflow_ids_from_dict = WorkflowIds.from_dict(workflow_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


