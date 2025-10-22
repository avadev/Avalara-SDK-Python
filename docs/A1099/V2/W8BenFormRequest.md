# W8BenFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type (always \&quot;w8ben\&quot; for this model). | [optional] [readonly] 
**name** | **str** | The name of the individual or entity associated with the form. | 
**citizenship_country** | **str** | The country of citizenship.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more) | 
**residence_address** | **str** | The residential address of the individual or entity. | [optional] 
**residence_city** | **str** | The city of residence. | [optional] 
**residence_state** | **str** | The state of residence. Required for US and Canada.. Allowed values: AA, AE, AK, AL, AP, AR, AS, AZ, CA, CO (and 65 more) | [optional] 
**residence_zip** | **str** | The ZIP code of the residence. | [optional] 
**residence_country** | **str** | The country of residence.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more) | 
**residence_is_mailing** | **bool** | Indicates whether the residence address is the mailing address. | [optional] 
**mailing_address** | **str** | The mailing address. | [optional] 
**mailing_city** | **str** | The city of the mailing address. | [optional] 
**mailing_state** | **str** | The state of the mailing address. Required for US and Canada.. Allowed values: AA, AE, AK, AL, AP, AR, AS, AZ, CA, CO (and 65 more) | [optional] 
**mailing_zip** | **str** | The ZIP code of the mailing address. | [optional] 
**mailing_country** | **str** | The country of the mailing address.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more) | 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**foreign_tin_not_required** | **bool** | Indicates whether a foreign TIN is not legally required. | [optional] 
**foreign_tin** | **str** | The foreign taxpayer identification number (TIN). | [optional] 
**reference_number** | **str** | A reference number for the form. | [optional] 
**birthday** | **date** | The birthday of the individual associated with the form. | [optional] 
**treaty_country** | **str** | The country for which the treaty applies.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more) | [optional] 
**treaty_article** | **str** | The specific article of the treaty being claimed. | [optional] 
**treaty_reasons** | **str** | The reasons for claiming treaty benefits. | [optional] 
**withholding_rate** | **str** | The withholding rate applied as per the treaty. Must be a percentage with up to two decimals (e.g., 12.50, 0).. Allowed values: 0, 0.0, 0.00, 5, 5.5, 10, 12.50, 15, 20, 25 (and 1 more) | [optional] 
**income_type** | **str** | The type of income covered by the treaty. | [optional] 
**signer_name** | **str** | The name of the signer of the form. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**company_id** | **str** | The ID of the associated company. Required when creating a form. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w8_ben_form_request import W8BenFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of W8BenFormRequest from a JSON string
w8_ben_form_request_instance = W8BenFormRequest.from_json(json)
# print the JSON string representation of the object
print(W8BenFormRequest.to_json())

# convert the object into a dict
w8_ben_form_request_dict = w8_ben_form_request_instance.to_dict()
# create an instance of W8BenFormRequest from a dict
w8_ben_form_request_from_dict = W8BenFormRequest.from_dict(w8_ben_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


