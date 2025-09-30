# W9FormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w9\&quot; for this model). | [optional] [readonly] 
**name** | **str** | The name of the individual or entity associated with the form. | 
**business_name** | **str** | The name of the business associated with the form. | [optional] 
**business_classification** | **str** | The classification of the business.  Available values:  - Individual: Individual/sole proprietor  - C Corporation: C Corporation  - S Corporation: S Corporation  - Partnership: Partnership  - Trust/estate: Trust/estate  - LLC-C: Limited liability company (C Corporation)  - LLC-S: Limited liability company (S Corporation)  - LLC-P: Limited liability company (Partnership)  - Other: Other (requires BusinessOther field to be populated) | 
**business_other** | **str** | The classification description when \&quot;businessClassification\&quot; is \&quot;Other\&quot;. | [optional] 
**foreign_partner_owner_or_beneficiary** | **bool** | Indicates whether the individual is a foreign partner, owner, or beneficiary. | [optional] 
**exempt_payee_code** | **str** | The exempt payee code. Allowed values (1–13):  - 1 — Organization exempt under §501(a) or IRA; custodial account under §403(b)(7)  - 2 — U.S. government or its agencies/instrumentalities  - 3 — U.S. state, DC, U.S. territory/possession, or their political subdivisions/agencies/instrumentalities  - 4 — Foreign government or its political subdivisions/agencies/instrumentalities  - 5 — Corporation  - 6 — Dealer in securities or commodities required to register in the U.S., DC, or U.S. territory/possession  - 7 — Futures commission merchant registered with the CFTC  - 8 — Real estate investment trust (REIT)  - 9 — Entity registered at all times during the tax year under the Investment Company Act of 1940  - 10 — Common trust fund operated by a bank under §584(a)  - 11 — Financial institution (see §581)  - 12 — Broker (nominee/custodian)  - 13 — Trust exempt under §664 or described in §4947 | [optional] 
**exempt_fatca_code** | **str** | The exemption from FATCA reporting code. Allowed values (A–M):  - A — Tax‑exempt organization under §501(a) or IRA (§7701(a)(37))  - B — U.S. government or any of its agencies/instrumentalities  - C — U.S. state, DC, territory/possession, or their political subdivisions/instrumentalities  - D — Corporation whose stock is regularly traded on an established securities market  - E — Corporation that is a member of the same expanded affiliated group as a D corporation  - F — Registered dealer in securities/commodities/derivatives  - G — REIT (Real Estate Investment Trust)  - H — Regulated investment company (§851) or entity registered all year under the Investment Company Act of 1940  - I — Common trust fund (§584(a))  - J — Bank (§581)  - K — Broker  - L — Charitable remainder trust (§664) or trust described in §4947(a)(1)  - M — Trust under §403(b) plan or §457(g) plan | [optional] 
**foreign_country_indicator** | **bool** | Indicates whether the individual or entity is in a foreign country. | [optional] 
**address** | **str** | The address of the individual or entity. | 
**foreign_address** | **str** | The foreign address of the individual or entity. | [optional] 
**city** | **str** | The city of the address. | 
**state** | **str** | The state of the address. | 
**zip** | **str** | The ZIP code of the address. | 
**account_number** | **str** | The account number associated with the form. | [optional] 
**tin_type** | **str** | Tax Identification Number (TIN) type. SSN/ITIN (for individuals) and EIN (for businesses). | 
**tin** | **str** | The taxpayer identification number (TIN). | 
**backup_withholding** | **bool** | Indicates whether backup withholding applies. | [optional] 
**is1099able** | **bool** | Indicates whether the individual or entity should be issued a 1099 form. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**company_id** | **str** | The ID of the associated company. Required when creating a form. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_request import W9FormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormRequest from a JSON string
w9_form_request_instance = W9FormRequest.from_json(json)
# print the JSON string representation of the object
print(W9FormRequest.to_json())

# convert the object into a dict
w9_form_request_dict = w9_form_request_instance.to_dict()
# create an instance of W9FormRequest from a dict
w9_form_request_from_dict = W9FormRequest.from_dict(w9_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


