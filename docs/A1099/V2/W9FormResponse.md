# W9FormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;W9\&quot; for this model). | [optional] [readonly] 
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
**tin_type** | **str** | Tax Identification Number (TIN) type. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**backup_withholding** | **bool** | Indicates whether backup withholding applies. | [optional] 
**is1099able** | **bool** | Indicates whether the individual or entity should be issued a 1099 form. | [optional] 
**tin_match_status** | [**TinMatchStatusResponse**](TinMatchStatusResponse.md) | The TIN Match status from IRS. | [optional] 
**id** | **str** | The unique identifier for the form. | [optional] 
**entry_status** | [**EntryStatusResponse**](EntryStatusResponse.md) | The entry status information for the form. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | [optional] 
**display_name** | **str** | The display name associated with the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 
**archived** | **bool** | Indicates whether the form is archived. | [optional] 
**ancestor_id** | **str** | Form ID of previous version. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**signed_date** | **datetime** | The date the form was signed. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**created_at** | **datetime** | The creation date of the form. | [optional] 
**updated_at** | **datetime** | The last updated date of the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w9_form_response import W9FormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of W9FormResponse from a JSON string
w9_form_response_instance = W9FormResponse.from_json(json)
# print the JSON string representation of the object
print(W9FormResponse.to_json())

# convert the object into a dict
w9_form_response_dict = w9_form_response_instance.to_dict()
# create an instance of W9FormResponse from a dict
w9_form_response_from_dict = W9FormResponse.from_dict(w9_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


