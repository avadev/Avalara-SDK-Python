# AddressValidationInfo

TextCase info for input address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | First line of the street address | [optional] 
**text_case** | **str** | Specify the text case for the validated address result.  If not specified, will return uppercase. | [optional] 
**line2** | **str** | Second line of the street address | [optional] 
**line3** | **str** | Third line of the street address | [optional] 
**city** | **str** | City component of the address | [optional] 
**region** | **str** | Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API &#x60;ListRegions&#x60;. | [optional] 
**country** | **str** | Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | [optional] 
**postal_code** | **str** | Postal Code / Zip Code component of the address. | [optional] 
**latitude** | **float** | Geospatial latitude measurement, in Decimal Degrees floating point format. | [optional] 
**longitude** | **float** | Geospatial longitude measurement, in Decimal Degrees floating point format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


