# Form1042SList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1042SListItem]**](Form1042SListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1042_s_list import Form1042SList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1042SList from a JSON string
form1042_s_list_instance = Form1042SList.from_json(json)
# print the JSON string representation of the object
print(Form1042SList.to_json())

# convert the object into a dict
form1042_s_list_dict = form1042_s_list_instance.to_dict()
# create an instance of Form1042SList from a dict
form1042_s_list_from_dict = Form1042SList.from_dict(form1042_s_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


