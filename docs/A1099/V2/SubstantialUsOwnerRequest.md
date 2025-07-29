# SubstantialUsOwnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the substantial U.S. owner of the NFFE. | [optional] 
**address** | **str** | The address of the substantial U.S. owner of the NFFE. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN) of the substantial U.S. owner of the NFFE. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.substantial_us_owner_request import SubstantialUsOwnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubstantialUsOwnerRequest from a JSON string
substantial_us_owner_request_instance = SubstantialUsOwnerRequest.from_json(json)
# print the JSON string representation of the object
print(SubstantialUsOwnerRequest.to_json())

# convert the object into a dict
substantial_us_owner_request_dict = substantial_us_owner_request_instance.to_dict()
# create an instance of SubstantialUsOwnerRequest from a dict
substantial_us_owner_request_from_dict = SubstantialUsOwnerRequest.from_dict(substantial_us_owner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


