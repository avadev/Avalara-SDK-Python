# ResubmitRejectedFormsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resubmitted_forms_count** | **int** | Number of forms scheduled for replacement submission. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.resubmit_rejected_forms_response import ResubmitRejectedFormsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResubmitRejectedFormsResponse from a JSON string
resubmit_rejected_forms_response_instance = ResubmitRejectedFormsResponse.from_json(json)
# print the JSON string representation of the object
print(ResubmitRejectedFormsResponse.to_json())

# convert the object into a dict
resubmit_rejected_forms_response_dict = resubmit_rejected_forms_response_instance.to_dict()
# create an instance of ResubmitRejectedFormsResponse from a dict
resubmit_rejected_forms_response_from_dict = ResubmitRejectedFormsResponse.from_dict(resubmit_rejected_forms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


