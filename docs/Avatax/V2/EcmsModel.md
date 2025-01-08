# EcmsModel

Exempt certificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_cert_id** | **int** | The calc_id associated with a certificate in CertCapture. | 
**company_id** | **int** | Company ID | 
**customer_code** | **str** | Customer code | 
**region** | **str** | Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API &#x60;ListRegions&#x60;. | 
**country** | **str** | Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | 
**exempt_cert_type_id** | **str** | The type of exemption certificate. Permitted values are: Blanket and Single. | 
**business_type_id** | **int** | Business type the customer belongs to. | 
**regions_applicable** | **str** | A list of applicable regions for this exempt certificate.                To list more than one applicable region, separate the list of region codes with commas. | 
**exempt_cert_status_id** | **str** | Status for this exempt certificate | 
**country_issued** | **str** | Name or ISO 3166 code identifying the country that issued this ECMS certificate.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | 
**customer_name** | **str** | Customer name | [optional] 
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**address3** | **str** | Address line 3 | [optional] 
**city** | **str** | City | [optional] 
**postal_code** | **str** | Postal code / zip code | [optional] 
**document_ref_no** | **str** | Document Reference Number, in the case of single-use exemption certificates, the DocumentCode or PurchaseOrderNo to which the certificate should apply. | [optional] 
**business_type_other_description** | **str** | Other description for this business type | [optional] 
**exempt_reason_id** | **str** | Exempt reason associated with the certificate, coded by CustomerUsageType.  Example: A - Federal Government. | [optional] 
**exempt_reason_other_description** | **str** | Other description for exempt reason i.e. Populated on if exemptReasonId is &#39;L&#39; - Other. | [optional] 
**effective_date** | **datetime** | Effective date for this exempt certificate | [optional] 
**created_date** | **datetime** | Date when this exempt certificate was created | [optional] 
**last_transaction_date** | **datetime** | Date when last transaction with this exempt certificate happened | [optional] [readonly] 
**expiry_date** | **datetime** | When this exempt certificate will expire | [optional] 
**created_user_id** | **int** | User that creates the certificate | [optional] 
**modified_date** | **datetime** | Date when this exempt certificate was modified | [optional] 
**modified_user_id** | **int** | Who modified this exempt certificate | [optional] 
**ava_cert_id** | **str** | If the certificate record was synced from an AvaTax Certs account(as opposed to being entered in ECMS directly),  the unique AvaTax Certs identifier for the certificate record. Usually same as the Id of a Certificate. | [optional] 
**exempt_cert_review_status_id** | **str** | Review status for this exempt certificate | [optional] 
**details** | [**[EcmsDetailModel]**](EcmsDetailModel.md) | Exempt Cert details | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


