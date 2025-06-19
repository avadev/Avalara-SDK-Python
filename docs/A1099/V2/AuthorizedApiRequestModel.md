# AuthorizedApiRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path and query of the API request you want to pre-authorize, omitting the leading /api/ | [optional] 
**ttl** | **int** | Seconds until this AuthorizedApiRequest should expire, 3600 if omitted; values greater than 86400 will not be honored | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.authorized_api_request_model import AuthorizedApiRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizedApiRequestModel from a JSON string
authorized_api_request_model_instance = AuthorizedApiRequestModel.from_json(json)
# print the JSON string representation of the object
print(AuthorizedApiRequestModel.to_json())

# convert the object into a dict
authorized_api_request_model_dict = authorized_api_request_model_instance.to_dict()
# create an instance of AuthorizedApiRequestModel from a dict
authorized_api_request_model_from_dict = AuthorizedApiRequestModel.from_dict(authorized_api_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


