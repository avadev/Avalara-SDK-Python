# SubmitInteropDocument202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interchange_id** | **str** | The unique interchange ID for this submission. | [optional] 
**message** | **str** | A message indicating that the document has been accepted. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.submit_interop_document202_response import SubmitInteropDocument202Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitInteropDocument202Response from a JSON string
submit_interop_document202_response_instance = SubmitInteropDocument202Response.from_json(json)
# print the JSON string representation of the object
print(SubmitInteropDocument202Response.to_json())

# convert the object into a dict
submit_interop_document202_response_dict = submit_interop_document202_response_instance.to_dict()
# create an instance of SubmitInteropDocument202Response from a dict
submit_interop_document202_response_from_dict = SubmitInteropDocument202Response.from_dict(submit_interop_document202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


