# Form1099StatusDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_status_detail import Form1099StatusDetail

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099StatusDetail from a JSON string
form1099_status_detail_instance = Form1099StatusDetail.from_json(json)
# print the JSON string representation of the object
print(Form1099StatusDetail.to_json())

# convert the object into a dict
form1099_status_detail_dict = form1099_status_detail_instance.to_dict()
# create an instance of Form1099StatusDetail from a dict
form1099_status_detail_from_dict = Form1099StatusDetail.from_dict(form1099_status_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


