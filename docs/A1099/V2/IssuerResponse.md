# IssuerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier set when the record is created | [optional] [readonly] 
**name** | **str** | Legal name, not DBA | [optional] 
**name_dba** | **str** | Optional DBA name or continuation of a long legal name | [optional] 
**tin** | **str** | Tax identification number | [optional] 
**reference_id** | **str** | Optional identifier for your reference, never shown to any agency or recipient.  We will also prefix download filenames with this value, if present.  Can only include letters, numbers, dashes, underscores and spaces. | [optional] 
**telephone** | **str** | Telephone number | [optional] 
**tax_year** | **int** | Tax year | [optional] 
**country_code** | **str** | If there is a transfer agent, use the address of the transfer agent. | [optional] 
**email** | **str** | Email address | [optional] 
**address** | **str** | Address | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**zip** | **str** | Zip code | [optional] 
**foreign_province** | **str** | Foreign province | [optional] 
**transfer_agent_name** | **str** | Transfer Agent&#39;s Name | [optional] 
**last_filing** | **bool** | Last year of filing for this payer | [optional] 
**created_at** | **datetime** | Date time when the issuer was created | [optional] [readonly] 
**updated_at** | **datetime** | Date time when the issuer was updated | [optional] [readonly] 

## Example

```python
from Avalara.SDK.models.A1099.V2.issuer_response import IssuerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerResponse from a JSON string
issuer_response_instance = IssuerResponse.from_json(json)
# print the JSON string representation of the object
print(IssuerResponse.to_json())

# convert the object into a dict
issuer_response_dict = issuer_response_instance.to_dict()
# create an instance of IssuerResponse from a dict
issuer_response_from_dict = IssuerResponse.from_dict(issuer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


