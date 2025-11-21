# IssuerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Legal name. Not the DBA name. | 
**dba_name** | **str** | Doing Business As (DBA) name or continuation of a long legal name. Use either this or &#39;transferAgentName&#39;. | [optional] 
**tin** | **str** | Federal Tax Identification Number (TIN). | [optional] 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. If present, it will prefix download filenames. Allowed characters: letters, numbers, dashes, underscores, and spaces. | [optional] 
**telephone** | **str** | Contact phone number (must contain at least 10 digits, max 15 characters). For recipient inquiries. | 
**tax_year** | **int** | Tax year for which the forms are being filed (e.g., 2024). Must be within current tax year and current tax year - 4. It&#39;s only required on creation, and cannot be modified on update. | 
**country_code** | **str** | Two-letter IRS country code (e.g., &#39;US&#39;, &#39;CA&#39;), as defined at https://www.irs.gov/e-file-providers/country-codes. If there is a transfer agent, use the transfer agent&#39;s shipping address. | 
**email** | **str** | Contact email address. For recipient inquiries. Phone will be used on communications if you don&#39;t specify an email | [optional] 
**address** | **str** | Address. | 
**city** | **str** | City. | 
**state** | **str** | Two-letter US state or Canadian province code (required for US/CA addresses). | 
**zip** | **str** | ZIP/postal code. | 
**foreign_province** | **str** | Province or region for non-US/CA addresses. | [optional] 
**transfer_agent_name** | **str** | Name of the transfer agent, if applicable — optional; use either this or &#39;dbaName&#39;. | [optional] 
**last_filing** | **bool** | Indicates if this is the issuer&#39;s final year filing. | 

## Example

```python
from Avalara.SDK.models.A1099.V2.issuer_request import IssuerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerRequest from a JSON string
issuer_request_instance = IssuerRequest.from_json(json)
# print the JSON string representation of the object
print(IssuerRequest.to_json())

# convert the object into a dict
issuer_request_dict = issuer_request_instance.to_dict()
# create an instance of IssuerRequest from a dict
issuer_request_from_dict = IssuerRequest.from_dict(issuer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


