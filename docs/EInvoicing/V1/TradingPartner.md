# TradingPartner

Represents a participant in the Avalara directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Avalara unique ID of the participant in the directory. | [optional] [readonly] 
**name** | **str** | Name of the participant (typically, the name of the business entity). | 
**network** | **str** | The network where the participant is present. When creating or updating a trading partner, the value provided for the attribute &#39;network&#39; will be ignored. | [optional] [readonly] 
**registration_date** | **str** | Registration date of the participant if available. | [optional] 
**identifiers** | [**List[Identifier]**](Identifier.md) | A list of identifiers associated with the trading partner. Each identifier should consistently include the fields name, and value to maintain clarity and ensure consistent structure across entries. When creating or updating a trading partner, the attribute &#39;name&#39; must be agreed upon with Avalara to ensure consistency. Failing to adhere to the agreed values will result in a validation error. Further, when creating or updating a trading partner, the value provided for the attribute &#39;displayName&#39; will be ignored and instead retrieved from the standard set of display names maintained. | 
**addresses** | [**List[Address]**](Address.md) |  | 
**supported_document_types** | [**List[SupportedDocumentTypes]**](SupportedDocumentTypes.md) | A list of document types supported by the trading partner for exchange. Each document type identifier value must match the standard list maintained by Avalara, which includes Peppol and other public network document type identifier schemes and values, as well as any approved partner-specific identifiers. The &#39;value&#39; field must exactly match an entry from the provided document identifier list. Any attempt to submit unsupported document types will result in a validation error. Further, when creating or updating a trading partner, the value provided for the attributes &#39;name&#39; and &#39;supportedByAvalara&#39; will be ignored. | 
**consents** | [**Consents**](Consents.md) |  | [optional] 
**extensions** | [**List[Extension]**](Extension.md) | Optional array used to carry additional metadata or configuration values that may be required by specific networks. When creating or updating a trading partner, the keys provided in the &#39;extensions&#39; attribute must be selected from a predefined list of supported extensions. Using any unsupported keys will result in a validation error. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.trading_partner import TradingPartner

# TODO update the JSON string below
json = "{}"
# create an instance of TradingPartner from a JSON string
trading_partner_instance = TradingPartner.from_json(json)
# print the JSON string representation of the object
print(TradingPartner.to_json())

# convert the object into a dict
trading_partner_dict = trading_partner_instance.to_dict()
# create an instance of TradingPartner from a dict
trading_partner_from_dict = TradingPartner.from_dict(trading_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


