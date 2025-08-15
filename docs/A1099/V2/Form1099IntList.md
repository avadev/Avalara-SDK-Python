# Form1099IntList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099IntListItem]**](Form1099IntListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_int_list import Form1099IntList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099IntList from a JSON string
form1099_int_list_instance = Form1099IntList.from_json(json)
# print the JSON string representation of the object
print(Form1099IntList.to_json())

# convert the object into a dict
form1099_int_list_dict = form1099_int_list_instance.to_dict()
# create an instance of Form1099IntList from a dict
form1099_int_list_from_dict = Form1099IntList.from_dict(form1099_int_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


