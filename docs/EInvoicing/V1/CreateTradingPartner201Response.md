# CreateTradingPartner201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Avalara unique ID of the participant in the directory. | [optional] 
**status** | **str** | The status of the create operation. | [optional] 
**message** | **str** | A human-readable message providing additional context or feedback about the outcome of the operation. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.create_trading_partner201_response import CreateTradingPartner201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradingPartner201Response from a JSON string
create_trading_partner201_response_instance = CreateTradingPartner201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTradingPartner201Response.to_json())

# convert the object into a dict
create_trading_partner201_response_dict = create_trading_partner201_response_instance.to_dict()
# create an instance of CreateTradingPartner201Response from a dict
create_trading_partner201_response_from_dict = CreateTradingPartner201Response.from_dict(create_trading_partner201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


