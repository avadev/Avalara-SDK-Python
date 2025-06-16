# FormRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**form_type** | **str** | \&quot;W9\&quot; is currently the only supported value | [optional] 
**company_id** | **int** | Track1099&#39;s ID of your company, found in the W-9 UI | [optional] 
**company_name** | **str** | Name of your company, set in the W-9 UI | [optional] 
**company_email** | **str** | Contact email of your company, set in the W-9 UI | [optional] 
**reference_id** | **str** | Your internal identifier for the vendor from whom you are requesting a form | [optional] 
**signed_at** | **datetime** | The timestamp this vendor (identified by your ReferenceId) last signed a complete W-9, null if you did not include a ReferenceId or the vendor has not yet signed a W-9 in Track1099 | [optional] 
**tin_match_status** | **str** | Result of IRS TIN match query for name and TIN in the last signed form, null if signed_at is null | [optional] 
**expires_at** | **datetime** | Timestamp when this FormRequest will expire, ttl (or 3600) seconds from creation | [optional] 
**signed_pdf** | **str** | URL of PDF representation of just-signed form, otherwise null. Integrations may use this value to offer a \&quot;download for your records\&quot; function after a vendor completes and signs a form. Link expires at the same time as this FormRequest. Treat the format of this URL as opaque and expect it to change in the future. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.form_request_model import FormRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of FormRequestModel from a JSON string
form_request_model_instance = FormRequestModel.from_json(json)
# print the JSON string representation of the object
print(FormRequestModel.to_json())

# convert the object into a dict
form_request_model_dict = form_request_model_instance.to_dict()
# create an instance of FormRequestModel from a dict
form_request_model_from_dict = FormRequestModel.from_dict(form_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


