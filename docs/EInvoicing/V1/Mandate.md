# Mandate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mandate_id** | **str** | The &#x60;mandateId&#x60; is comprised of the country code, mandate type, and the network or regulation type (for example, AU-B2G-PEPPOL). Keep in mind the following when specifying a &#x60;mandateId&#x60;. - A country can have multiple mandate types (B2C, B2B, B2G). - A entity/company can opt in for multiple mandates. - A &#x60;mandateId&#x60; is the combination of country + mandate type + network/regulation. | [optional] 
**country_mandate** | **str** | **[LEGACY]** This field is retained for backward compatibility. It is recommended to use &#x60;mandateId&#x60; instead. The &#x60;countryMandate&#x60; similar to the &#x60;mandateId&#x60; is comprised of the country code, mandate type, and the network or regulation type (for example, AU-B2G-PEPPOL).  | [optional] 
**country_code** | **str** | Country code | [optional] 
**description** | **str** | Mandate description | [optional] 
**supported_by_partner_api** | **bool** | Indicates whether this mandate supported by the partner API | [optional] 
**mandate_format** | **str** | Mandate format | [optional] 
**input_data_formats** | [**List[InputDataFormats]**](InputDataFormats.md) | Format and version used when inputting the data | [optional] 
**workflow_ids** | [**List[WorkflowIds]**](WorkflowIds.md) | Workflow ID list | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.mandate import Mandate

# TODO update the JSON string below
json = "{}"
# create an instance of Mandate from a JSON string
mandate_instance = Mandate.from_json(json)
# print the JSON string representation of the object
print(Mandate.to_json())

# convert the object into a dict
mandate_dict = mandate_instance.to_dict()
# create an instance of Mandate from a dict
mandate_from_dict = Mandate.from_dict(mandate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


