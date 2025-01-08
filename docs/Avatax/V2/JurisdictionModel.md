# JurisdictionModel

Represents information about a single legal taxing jurisdiction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code that is used to identify this jurisdiction | 
**name** | **str** | The name of this jurisdiction | 
**type** | **str** | The type of the jurisdiction, indicating whether it is a country, state/region, city, for example. | 
**signature_code** | **str** | The Avalara-supplied signature code for this jurisdiction. | 
**rate** | **float** | The base rate of tax specific to this jurisdiction. | [optional] 
**sales_rate** | **float** | The \&quot;Sales\&quot; tax rate specific to this jurisdiction. | [optional] 
**region** | **str** | Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API &#x60;ListRegions&#x60;. | [optional] 
**use_rate** | **float** | The \&quot;Seller&#39;s Use\&quot; tax rate specific to this jurisdiction. | [optional] 
**city** | **str** | The city name of this jurisdiction | [optional] 
**county** | **str** | The county name of this jurisdiction | [optional] 
**country** | **str** | Name or ISO 3166 code identifying the country of this jurisdiction.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | [optional] 
**short_name** | **str** | A short name of the jurisidiction | [optional] 
**state_fips** | **str** | State FIPS code | [optional] 
**county_fips** | **str** | County FIPS code | [optional] 
**place_fips** | **str** | City FIPS code | [optional] 
**id** | **int** | Unique AvaTax Id of this Jurisdiction | [optional] 
**effective_date** | **datetime** | The date this jurisdiction starts to take effect on tax calculations | [optional] 
**end_date** | **datetime** | The date this jurisdiction stops to take effect on tax calculations | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


