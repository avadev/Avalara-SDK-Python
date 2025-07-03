# Form1095BList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1095BListItem]**](Form1095BListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1095_b_list import Form1095BList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1095BList from a JSON string
form1095_b_list_instance = Form1095BList.from_json(json)
# print the JSON string representation of the object
print(Form1095BList.to_json())

# convert the object into a dict
form1095_b_list_dict = form1095_b_list_instance.to_dict()
# create an instance of Form1095BList from a dict
form1095_b_list_from_dict = Form1095BList.from_dict(form1095_b_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


