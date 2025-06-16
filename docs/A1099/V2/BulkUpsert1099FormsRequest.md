# BulkUpsert1099FormsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099RListItem]**](Form1099RListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.bulk_upsert1099_forms_request import BulkUpsert1099FormsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpsert1099FormsRequest from a JSON string
bulk_upsert1099_forms_request_instance = BulkUpsert1099FormsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpsert1099FormsRequest.to_json())

# convert the object into a dict
bulk_upsert1099_forms_request_dict = bulk_upsert1099_forms_request_instance.to_dict()
# create an instance of BulkUpsert1099FormsRequest from a dict
bulk_upsert1099_forms_request_from_dict = BulkUpsert1099FormsRequest.from_dict(bulk_upsert1099_forms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


