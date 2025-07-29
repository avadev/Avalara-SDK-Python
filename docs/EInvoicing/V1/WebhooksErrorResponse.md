# WebhooksErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**WebhooksErrorInfo**](WebhooksErrorInfo.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.webhooks_error_response import WebhooksErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksErrorResponse from a JSON string
webhooks_error_response_instance = WebhooksErrorResponse.from_json(json)
# print the JSON string representation of the object
print(WebhooksErrorResponse.to_json())

# convert the object into a dict
webhooks_error_response_dict = webhooks_error_response_instance.to_dict()
# create an instance of WebhooksErrorResponse from a dict
webhooks_error_response_from_dict = WebhooksErrorResponse.from_dict(webhooks_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


