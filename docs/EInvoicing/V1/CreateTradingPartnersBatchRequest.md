# CreateTradingPartnersBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TradingPartner]**](TradingPartner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.create_trading_partners_batch_request import CreateTradingPartnersBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingPartnersBatchRequest from a JSON string
create_trading_partners_batch_request_instance = CreateTradingPartnersBatchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTradingPartnersBatchRequest.to_json())

# convert the object into a dict
create_trading_partners_batch_request_dict = create_trading_partners_batch_request_instance.to_dict()
# create an instance of CreateTradingPartnersBatchRequest from a dict
create_trading_partners_batch_request_from_dict = CreateTradingPartnersBatchRequest.from_dict(create_trading_partners_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


