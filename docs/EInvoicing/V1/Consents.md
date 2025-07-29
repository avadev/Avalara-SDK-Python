# Consents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_in_avalara_directory** | **bool** | Indicates whether the trading partner consents to being listed in the directory. If not provided in the payload, its value will default to true. | [optional] [default to True]

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.consents import Consents

# TODO update the JSON string below
json = "{}"
# create an instance of Consents from a JSON string
consents_instance = Consents.from_json(json)
# print the JSON string representation of the object
print(Consents.to_json())

# convert the object into a dict
consents_dict = consents_instance.to_dict()
# create an instance of Consents from a dict
consents_from_dict = Consents.from_dict(consents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


