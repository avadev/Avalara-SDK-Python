# CreateTradingPartnersBatch200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the created trading partner. | [optional] 
**index** | **int** | Index number of the trading partner. | [optional] 
**message** | **str** | A success message for the specific created record. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.create_trading_partners_batch200_response_value_inner import CreateTradingPartnersBatch200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingPartnersBatch200ResponseValueInner from a JSON string
create_trading_partners_batch200_response_value_inner_instance = CreateTradingPartnersBatch200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(CreateTradingPartnersBatch200ResponseValueInner.to_json())

# convert the object into a dict
create_trading_partners_batch200_response_value_inner_dict = create_trading_partners_batch200_response_value_inner_instance.to_dict()
# create an instance of CreateTradingPartnersBatch200ResponseValueInner from a dict
create_trading_partners_batch200_response_value_inner_from_dict = CreateTradingPartnersBatch200ResponseValueInner.from_dict(create_trading_partners_batch200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


