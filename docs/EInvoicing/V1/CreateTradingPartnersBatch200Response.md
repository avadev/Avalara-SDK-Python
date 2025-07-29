# CreateTradingPartnersBatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** | A message indicating the result of the batch operation. | [optional] 
**value** | [**List[CreateTradingPartnersBatch200ResponseValueInner]**](CreateTradingPartnersBatch200ResponseValueInner.md) | A list of trading partners successfully created. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.create_trading_partners_batch200_response import CreateTradingPartnersBatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingPartnersBatch200Response from a JSON string
create_trading_partners_batch200_response_instance = CreateTradingPartnersBatch200Response.from_json(json)
# print the JSON string representation of the object
print(CreateTradingPartnersBatch200Response.to_json())

# convert the object into a dict
create_trading_partners_batch200_response_dict = create_trading_partners_batch200_response_instance.to_dict()
# create an instance of CreateTradingPartnersBatch200Response from a dict
create_trading_partners_batch200_response_from_dict = CreateTradingPartnersBatch200Response.from_dict(create_trading_partners_batch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


