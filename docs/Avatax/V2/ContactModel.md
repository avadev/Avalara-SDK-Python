# ContactModel

A contact person for a company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_code** | **str** | A unique code for this contact. | 
**id** | **int** | The unique ID number of this contact. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the company to which this contact belongs. | [optional] [readonly] 
**first_name** | **str** | The first or given name of this contact. | [optional] 
**middle_name** | **str** | The middle name of this contact. | [optional] 
**last_name** | **str** | The last or family name of this contact. | [optional] 
**title** | **str** | Professional title of this contact. | [optional] 
**line1** | **str** | The first line of the postal mailing address of this contact. | [optional] 
**line2** | **str** | The second line of the postal mailing address of this contact. | [optional] 
**line3** | **str** | The third line of the postal mailing address of this contact. | [optional] 
**city** | **str** | The city of the postal mailing address of this contact. | [optional] 
**region** | **str** | Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API &#x60;ListRegions&#x60;. | [optional] 
**postal_code** | **str** | The postal code or zip code of the postal mailing address of this contact. | [optional] 
**country** | **str** | Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | [optional] 
**email** | **str** | The email address of this contact. | [optional] 
**phone** | **str** | The main phone number for this contact. | [optional] 
**mobile** | **str** | The mobile phone number for this contact. | [optional] 
**fax** | **str** | The facsimile phone number for this contact. | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


