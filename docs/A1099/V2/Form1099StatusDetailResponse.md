# Form1099StatusDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** | The date the form is scheduled for or the time the status last changed | [optional] 
**status** | **str** | The status of the form. Will be one of:  * unsent  * scheduled  * sent  * corrected_scheduled  * accepted  * corrected  * corrected_accepted  * held  * pending  * delivered  * bad_verify  * bad_verify_limit  * bounced  * verified  * incomplete  * failed  * unchanged  * unknown | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form1099_status_detail_response import Form1099StatusDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Form1099StatusDetailResponse from a JSON string
form1099_status_detail_response_instance = Form1099StatusDetailResponse.from_json(json)
# print the JSON string representation of the object
print(Form1099StatusDetailResponse.to_json())

# convert the object into a dict
form1099_status_detail_response_dict = form1099_status_detail_response_instance.to_dict()
# create an instance of Form1099StatusDetailResponse from a dict
form1099_status_detail_response_from_dict = Form1099StatusDetailResponse.from_dict(form1099_status_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


