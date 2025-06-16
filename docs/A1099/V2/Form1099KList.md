# Form1099KList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099KListItem]**](Form1099KListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_k_list import Form1099KList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099KList from a JSON string
form1099_k_list_instance = Form1099KList.from_json(json)
# print the JSON string representation of the object
print(Form1099KList.to_json())

# convert the object into a dict
form1099_k_list_dict = form1099_k_list_instance.to_dict()
# create an instance of Form1099KList from a dict
form1099_k_list_from_dict = Form1099KList.from_dict(form1099_k_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


