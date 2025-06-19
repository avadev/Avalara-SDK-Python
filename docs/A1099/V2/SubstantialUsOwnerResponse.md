# SubstantialUsOwnerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the substantial U.S. owner of the NFFE. | [optional] 
**address** | **str** | The address of the substantial U.S. owner of the NFFE. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN) of the substantial U.S. owner of the NFFE. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.substantial_us_owner_response import SubstantialUsOwnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubstantialUsOwnerResponse from a JSON string
substantial_us_owner_response_instance = SubstantialUsOwnerResponse.from_json(json)
# print the JSON string representation of the object
print(SubstantialUsOwnerResponse.to_json())

# convert the object into a dict
substantial_us_owner_response_dict = substantial_us_owner_response_instance.to_dict()
# create an instance of SubstantialUsOwnerResponse from a dict
substantial_us_owner_response_from_dict = SubstantialUsOwnerResponse.from_dict(substantial_us_owner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


