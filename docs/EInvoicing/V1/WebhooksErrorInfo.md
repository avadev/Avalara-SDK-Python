# WebhooksErrorInfo

Information about the error encountered

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | An identifying name for the error. | [optional] 
**status** | **str** | A conanoical error status. | [optional] 
**detail** | **str** | A detailed description of the error type. | [optional] 
**instance** | **str** | A detailed description of the specific error ocurrance. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.webhooks_error_info import WebhooksErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksErrorInfo from a JSON string
webhooks_error_info_instance = WebhooksErrorInfo.from_json(json)
# print the JSON string representation of the object
print(WebhooksErrorInfo.to_json())

# convert the object into a dict
webhooks_error_info_dict = webhooks_error_info_instance.to_dict()
# create an instance of WebhooksErrorInfo from a dict
webhooks_error_info_from_dict = WebhooksErrorInfo.from_dict(webhooks_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


