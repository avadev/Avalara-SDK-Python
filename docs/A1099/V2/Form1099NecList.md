# Form1099NecList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forms** | [**List[Form1099NecListItem]**](Form1099NecListItem.md) |  | [optional] 
**form_type** | **str** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_nec_list import Form1099NecList

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099NecList from a JSON string
form1099_nec_list_instance = Form1099NecList.from_json(json)
# print the JSON string representation of the object
print(Form1099NecList.to_json())

# convert the object into a dict
form1099_nec_list_dict = form1099_nec_list_instance.to_dict()
# create an instance of Form1099NecList from a dict
form1099_nec_list_from_dict = Form1099NecList.from_dict(form1099_nec_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


