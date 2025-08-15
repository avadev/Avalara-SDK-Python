# Form1099ProccessResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_data** | [**Data**](Data.md) |  | [optional] 
**processed_forms** | [**List[Form1099ProccessResultProcessedFormsInner]**](Form1099ProccessResultProcessedFormsInner.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_proccess_result import Form1099ProccessResult

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099ProccessResult from a JSON string
form1099_proccess_result_instance = Form1099ProccessResult.from_json(json)
# print the JSON string representation of the object
print(Form1099ProccessResult.to_json())

# convert the object into a dict
form1099_proccess_result_dict = form1099_proccess_result_instance.to_dict()
# create an instance of Form1099ProccessResult from a dict
form1099_proccess_result_from_dict = Form1099ProccessResult.from_dict(form1099_proccess_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


