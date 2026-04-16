# CodeListSummary

Displays a summary of information about a code list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Two-letter ISO 3166-1 alpha-2 country code indicating the jurisdiction this code list applies to. | [optional] 
**code_list_id** | **str** | System-generated unique identifier of the code list definition. Typically a UUID used to reference this code list internally or via APIs. | [optional] 
**code_list_name** | **str** | Human-readable name of the code list, usually describing what the codes represent (for example, document types, tax categories, currencies). | [optional] 
**description** | **str** | Textual description of the code list, including what it is used for and whether it represents a global standard (e.g., UN/CEFACT, ISO, EN16931) or a jurisdiction-specific/local extension of that standard. | [optional] 
**standard** | **str** | Identifier of the underlying standard or authoritative source for this code list. This may be a formal code list name (e.g., UNCL1001), a standard reference (e.g., EN16931), or an internal standard identifier. | [optional] 
**versions** | [**List[CodeListVersion]**](CodeListVersion.md) | Array of versioned definitions of this code list for the given jurisdiction. Each entry represents a version that is valid for a specific effective/sunset date range, optionally per locale. | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.code_list_summary import CodeListSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CodeListSummary from a JSON string
code_list_summary_instance = CodeListSummary.from_json(json)
# print the JSON string representation of the object
print(CodeListSummary.to_json())

# convert the object into a dict
code_list_summary_dict = code_list_summary_instance.to_dict()
# create an instance of CodeListSummary from a dict
code_list_summary_from_dict = CodeListSummary.from_dict(code_list_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


