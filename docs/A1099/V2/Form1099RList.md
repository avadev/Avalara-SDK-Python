# Form1099RList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099RListItem]**](Form1099RListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_r_list import Form1099RList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099RList from a JSON string
form1099_r_list_instance = Form1099RList.from_json(json)
# print the JSON string representation of the object
print(Form1099RList.to_json())

# convert the object into a dict
form1099_r_list_dict = form1099_r_list_instance.to_dict()
# create an instance of Form1099RList from a dict
form1099_r_list_from_dict = Form1099RList.from_dict(form1099_r_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


