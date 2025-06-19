# AuthorizedApiRequestV2DataModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.authorized_api_request_v2_data_model import AuthorizedApiRequestV2DataModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizedApiRequestV2DataModel from a JSON string
authorized_api_request_v2_data_model_instance = AuthorizedApiRequestV2DataModel.from_json(json)
# print the JSON string representation of the object
print(AuthorizedApiRequestV2DataModel.to_json())

# convert the object into a dict
authorized_api_request_v2_data_model_dict = authorized_api_request_v2_data_model_instance.to_dict()
# create an instance of AuthorizedApiRequestV2DataModel from a dict
authorized_api_request_v2_data_model_from_dict = AuthorizedApiRequestV2DataModel.from_dict(authorized_api_request_v2_data_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


