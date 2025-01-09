# MandatesResponse

Mandate list response schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordset_count** | **float** | Total count of results | [optional] 
**next_link** | **str** |  | [optional] 
**value** | [**List[Mandate]**](Mandate.md) | Mandates schema | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.mandates_response import MandatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MandatesResponse from a JSON string
mandates_response_instance = MandatesResponse.from_json(json)
# print the JSON string representation of the object
print(MandatesResponse.to_json())

# convert the object into a dict
mandates_response_dict = mandates_response_instance.to_dict()
# create an instance of MandatesResponse from a dict
mandates_response_from_dict = MandatesResponse.from_dict(mandates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


