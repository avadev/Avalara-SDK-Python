# UpdateTradingPartner200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Avalara unique ID of the participant in the directory. | [optional] 
**status** | **str** | The status of the create operation. | [optional] 
**message** | **str** | A human-readable message providing additional context or feedback about the outcome of the operation. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.update_trading_partner200_response import UpdateTradingPartner200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTradingPartner200Response from a JSON string
update_trading_partner200_response_instance = UpdateTradingPartner200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTradingPartner200Response.to_json())

# convert the object into a dict
update_trading_partner200_response_dict = update_trading_partner200_response_instance.to_dict()
# create an instance of UpdateTradingPartner200Response from a dict
update_trading_partner200_response_from_dict = UpdateTradingPartner200Response.from_dict(update_trading_partner200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


