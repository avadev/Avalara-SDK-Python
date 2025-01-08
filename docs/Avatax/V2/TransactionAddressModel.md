# TransactionAddressModel

An address used within this transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID number of this address. | [optional] [readonly] 
**transaction_id** | **int** | The unique ID number of the document to which this address belongs. | [optional] [readonly] 
**boundary_level** | **str** | The boundary level at which this address was validated. | [optional] [readonly] 
**line1** | **str** | The first line of the address. | [optional] 
**line2** | **str** | The second line of the address. | [optional] 
**line3** | **str** | The third line of the address. | [optional] 
**city** | **str** | The city for the address. | [optional] 
**region** | **str** | The ISO 3166 region code. E.g., the second part of ISO 3166-2. | [optional] 
**postal_code** | **str** | The postal code or zip code for the address. | [optional] 
**country** | **str** | The ISO 3166 country code | [optional] 
**tax_region_id** | **int** | The unique ID number of the tax region for this address. | [optional] 
**latitude** | **str** | Latitude for this address | [optional] 
**longitude** | **str** | Longitude for this address | [optional] 
**jurisdictions** | [**[JurisdictionModel]**](JurisdictionModel.md) | List of all the qualified jurisdictions for the TaxRegionId. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


