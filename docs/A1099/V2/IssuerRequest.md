# IssuerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** | Business name. Required when the recipient of the form is a business; should only be used for businesses. | 
**business_name2** | **str** | Business name line 2. Should only be used for businesses. Use either this or &#39;transferAgentName&#39;. | [optional] 
**name** | **str** | Legal name. Not the DBA name. Deprecated alias for &#39;businessName&#39;. | [optional] 
**dba_name** | **str** | Doing Business As (DBA) name or continuation of a long legal name. Deprecated alias for &#39;businessName2&#39;. Use either this or &#39;transferAgentName&#39;. | [optional] 
**tin_type** | **str** | Recipient classification.  The platform is transitioning from tax identifier classifications to recipient entity classifications. New values represent recipient entity types and should be preferred. Deprecated values represent identifier formats and remain supported for backward compatibility only.  Available values: - INDIVIDUAL: Recipient is an individual - BUSINESS: Recipient is a business - UNKNOWN: Recipient classification is unknown - EIN: (Deprecated - use BUSINESS) Employer Identification Number - SSN: (Deprecated - use INDIVIDUAL) Social Security Number - ITIN: (Deprecated - use INDIVIDUAL) Individual Taxpayer Identification Number - ATIN: (Deprecated - use INDIVIDUAL) Adoption Taxpayer Identification Number | [optional] 
**first_name** | **str** | First name. Required when the recipient of the form is an individual; should only be used for individuals. | [optional] 
**middle_name** | **str** | Middle name. Should only be used for individuals. | [optional] 
**last_name** | **str** | Last name. Required when the recipient of the form is an individual; should only be used for individuals. | [optional] 
**suffix** | **str** | Suffix name. Should only be used for individuals. | [optional] 
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


