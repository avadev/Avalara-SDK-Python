# W8BenFormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;W8Ben\&quot; for this model). | [optional] [readonly] 
**name** | **str** | The name of the individual or entity associated with the form. | [optional] 
**citizenship_country** | **str** | The country of citizenship. | [optional] 
**residence_address** | **str** | The residential address of the individual or entity. | [optional] 
**residence_city** | **str** | The city of residence. | [optional] 
**residence_state** | **str** | The state of residence. | [optional] 
**residence_zip** | **str** | The ZIP code of the residence. | [optional] 
**residence_country** | **str** | The country of residence. | [optional] 
**residence_is_mailing** | **bool** | Indicates whether the residence address is the mailing address. | [optional] 
**mailing_address** | **str** | The mailing address. | [optional] 
**mailing_city** | **str** | The city of the mailing address. | [optional] 
**mailing_state** | **str** | The state of the mailing address. | [optional] 
**mailing_zip** | **str** | The ZIP code of the mailing address. | [optional] 
**mailing_country** | **str** | The country of the mailing address. | [optional] 
**tin_type** | **str** | Tax Identification Number (TIN) type. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**foreign_tin_not_required** | **bool** | Indicates whether a foreign TIN is not required. | [optional] 
**foreign_tin** | **str** | The foreign taxpayer identification number (TIN). | [optional] 
**reference_number** | **str** | A reference number for the form. | [optional] 
**birthday** | **date** | The birthday of the individual associated with the form. | [optional] 
**treaty_country** | **str** | The country for which the treaty applies. | [optional] 
**treaty_article** | **str** | The specific article of the treaty being claimed. | [optional] 
**treaty_reasons** | **str** | The reasons for claiming treaty benefits. | [optional] 
**withholding_rate** | **str** | The withholding rate applied as per the treaty. | [optional] 
**income_type** | **str** | The type of income covered by the treaty. | [optional] 
**signer_name** | **str** | The name of the signer of the form. | [optional] 
**signer_capacity** | **str** | The capacity in which the signer is signing the form. | [optional] 
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
from Avalara.SDK.models.A1099.V2.w8_ben_form_response import W8BenFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of W8BenFormResponse from a JSON string
w8_ben_form_response_instance = W8BenFormResponse.from_json(json)
# print the JSON string representation of the object
print(W8BenFormResponse.to_json())

# convert the object into a dict
w8_ben_form_response_dict = w8_ben_form_response_instance.to_dict()
# create an instance of W8BenFormResponse from a dict
w8_ben_form_response_from_dict = W8BenFormResponse.from_dict(w8_ben_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


