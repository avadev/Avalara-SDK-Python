# ExposureZoneModel

Information about a physical area or zone in which a certificate can apply.  An exposure zone for an exemption certificate will generally be a tax authority such  as a state, country, or local government entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique ID number representing this exposure zone. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the AvaTax company that recorded this customer. | [optional] 
**name** | **str** | The short name of this exposure zone, suitable for use in a drop-down list. | [optional] 
**tag** | **str** | A tag indicating | [optional] 
**description** | **str** | A more complete description of this exposure zone, suitable for use as a tooltip or help text. | [optional] 
**created** | **datetime** | The date when this record was created. | [optional] 
**modified** | **datetime** | The date/time when this record was last modified. | [optional] 
**region** | **str** | Two or three character ISO 3166 region, province, or state name of this exposure zone. | [optional] [readonly] 
**country** | **str** | Two character ISO 3166 county code for the country component of this exposure zone. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


