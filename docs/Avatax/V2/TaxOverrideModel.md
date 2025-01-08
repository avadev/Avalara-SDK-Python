# TaxOverrideModel

Represents a tax override for a transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identifies the type of tax override | [optional] 
**tax_amount** | **float** | Indicates a total override of the calculated tax on the document.  AvaTax will distribute  the override across all the lines.                Tax will be distributed on a best effort basis.  It may not always be possible to override all taxes.  Please consult  your account manager for information about overrides. | [optional] 
**tax_date** | **date** | The override tax date to use                This is used when the tax has been previously calculated  as in the case of a layaway, return or other reason indicated by the Reason element.  If the date is not overridden, then it should be set to the same as the DocDate. | [optional] 
**reason** | **str** | This provides the reason for a tax override for audit purposes.  It is required for types 2-4.                Typical reasons include:  \&quot;Return\&quot;  \&quot;Layaway\&quot; | [optional] 
**tax_amount_by_tax_types** | [**[TransactionLineTaxAmountByTaxTypeModel]**](TransactionLineTaxAmountByTaxTypeModel.md) | Indicates a total override of the calculated tax on the line with TaxType.  AvaTax will distribute the override across all the line details for that TaxType.                TaxAmountByTaxType can be used only at the Line level. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


