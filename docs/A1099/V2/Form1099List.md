# Form1099List


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Form1099ListDataInner]**](Form1099ListDataInner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_list import Form1099List

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099List from a JSON string
form1099_list_instance = Form1099List.from_json(json)
# print the JSON string representation of the object
print(Form1099List.to_json())

# convert the object into a dict
form1099_list_dict = form1099_list_instance.to_dict()
# create an instance of Form1099List from a dict
form1099_list_from_dict = Form1099List.from_dict(form1099_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


