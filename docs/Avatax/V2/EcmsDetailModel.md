# EcmsDetailModel

Represents an ECMS record, used internally by AvaTax to track information about exemptions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_cert_detail_id** | **int** | Unique, system-assigned identifier of a ExemptCertDetail record. | 
**exempt_cert_id** | **int** | The calc_id associated with a certificate in CertCapture. | 
**state_fips** | **str** | State FIPS | 
**region** | **str** | Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API &#x60;ListRegions&#x60;. | 
**country** | **str** | Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | 
**id_no** | **str** | The customer Tax Id Number (tax_number) associated with a certificate. This is same as exemptionNo in Transactions. | [optional] 
**end_date** | **datetime** | End date of this exempt certificate | [optional] 
**id_type** | **str** | The type of idNo (tax_number) associated with a certificate.  Example: Driver&#39;s Licence Number, Permit Number. | [optional] 
**is_tax_code_list_exclusion_list** | **int** | Is the tax code list an exculsion list? | [optional] 
**tax_codes** | [**[EcmsDetailTaxCodeModel]**](EcmsDetailTaxCodeModel.md) | optional: list of tax code associated with this exempt certificate detail | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


