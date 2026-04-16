# CodeListValue

Represents a single code entry in a code list version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The actual code value used in documents or systems. This is typically what appears in the e-invoice payload, such as a numeric or alphanumeric code from the official code list. | [optional] 
**value** | **str** | Human-readable label or name for the code, localized according to the locale field of the version. | [optional] 
**description** | **str** | Detailed explanation of what the code represents, localized according to the locale field of the version. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.code_list_value import CodeListValue

# TODO update the JSON string below
json = "{}"
# create an instance of CodeListValue from a JSON string
code_list_value_instance = CodeListValue.from_json(json)
# print the JSON string representation of the object
print(CodeListValue.to_json())

# convert the object into a dict
code_list_value_dict = code_list_value_instance.to_dict()
# create an instance of CodeListValue from a dict
code_list_value_from_dict = CodeListValue.from_dict(code_list_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


