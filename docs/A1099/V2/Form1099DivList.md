# Form1099DivList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099DivListItem]**](Form1099DivListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_div_list import Form1099DivList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099DivList from a JSON string
form1099_div_list_instance = Form1099DivList.from_json(json)
# print the JSON string representation of the object
print(Form1099DivList.to_json())

# convert the object into a dict
form1099_div_list_dict = form1099_div_list_instance.to_dict()
# create an instance of Form1099DivList from a dict
form1099_div_list_from_dict = Form1099DivList.from_dict(form1099_div_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


