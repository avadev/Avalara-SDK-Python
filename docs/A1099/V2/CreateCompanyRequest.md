# CreateCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Legal name. Not the DBA name. | 
**dba_name** | **str** | Doing Business As (DBA) name or continuation of a long legal name. | [optional] 
**email** | **str** | Contact email address. For inquiries by vendors/employees. | 
**address** | **str** | Address. | 
**city** | **str** | City. | 
**state** | **str** | Two-letter US state or Canadian province code (required for US/CA addresses). | [optional] 
**zip** | **str** | ZIP/postal code. | 
**telephone** | **str** | Contact phone number (must contain at least 10 digits, max 15 characters). | 
**tin** | **str** | Federal Tax Identification Number (TIN). EIN/Tax ID (required for US companies). | 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. | [optional] 
**do_tin_match** | **bool** | Indicates whether the company authorizes IRS TIN matching. | [optional] 
**group_name** | **str** | Group name for organizing companies (creates or finds group by name). | [optional] 
**foreign_province** | **str** | Province or region for non-US/CA addresses. | [optional] 
**country_code** | **str** | Two-letter IRS country code (e.g., &#39;US&#39;, &#39;CA&#39;), as defined at https://www.irs.gov/e-file-providers/country-codes. | 
**resend_requests** | **bool** | Boolean to enable automatic reminder emails (default: false). | [optional] 
**resend_interval_days** | **int** | Days between reminder emails (7-365, required if resendRequests is true). | [optional] 
**max_reminder_attempts** | **int** | Maximum number of reminder attempts (1-52, required if resendRequests is true). | [optional] 
**id** | **str** | Unique identifier set when the record is created. | [optional] 
**created_at** | **datetime** | Date time when the record was created. | [optional] 
**updated_at** | **datetime** | Date time when the record was last updated. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.create_company_request import CreateCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequest from a JSON string
create_company_request_instance = CreateCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequest.to_json())

# convert the object into a dict
create_company_request_dict = create_company_request_instance.to_dict()
# create an instance of CreateCompanyRequest from a dict
create_company_request_from_dict = CreateCompanyRequest.from_dict(create_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


