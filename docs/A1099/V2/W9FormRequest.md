# W9FormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w9\&quot; for this model). | [optional] [readonly] 
**name** | **str** | The name of the individual or entity associated with the form. | [optional] 
**business_name** | **str** | The name of the business associated with the form. | [optional] 
**business_classification** | **str** | The classification of the business. | [optional] 
**business_other** | **str** | The classification description when \&quot;businessClassification\&quot; is \&quot;Other\&quot;. | [optional] 
**foreign_partner_owner_or_beneficiary** | **bool** | Indicates whether the individual is a foreign partner, owner, or beneficiary. | [optional] 
**exempt_payee_code** | **str** | The exempt payee code. | [optional] 
**exempt_fatca_code** | **str** | The exemption from FATCA reporting code. | [optional] 
**foreign_country_indicator** | **bool** | Indicates whether the individual or entity is in a foreign country. | [optional] 
**address** | **str** | The address of the individual or entity. | [optional] 
**foreign_address** | **str** | The foreign address of the individual or entity. | [optional] 
**city** | **str** | The city of the address. | [optional] 
**state** | **str** | The state of the address. | [optional] 
**zip** | **str** | The ZIP code of the address. | [optional] 
**account_number** | **str** | The account number associated with the form. | [optional] 
**tin_type** | **str** | The type of TIN provided. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**backup_withholding** | **bool** | Indicates whether backup withholding applies. | [optional] 
**is1099able** | **bool** | Indicates whether the individual or entity should be issued a 1099 form. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | 
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


