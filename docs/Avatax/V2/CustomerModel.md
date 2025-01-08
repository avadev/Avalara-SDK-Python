# CustomerModel

Represents a customer to whom you sell products and/or services.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The unique ID number of the AvaTax company that recorded this customer. | 
**customer_code** | **str** | The unique code identifying this customer.  Must be unique within your company.                This code should be used in the &#x60;customerCode&#x60; field of any call that creates or adjusts a transaction  in order to ensure that all exemptions that apply to this customer are correctly considered.                Note: This field is case sensitive. | 
**name** | **str** | A friendly name identifying this customer. | 
**line1** | **str** | First line of the street address of this customer. | 
**city** | **str** | City component of the street address of this customer. | 
**postal_code** | **str** | Postal Code / Zip Code component of the address of this customer. | 
**country** | **str** | Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API &#x60;ListCountries&#x60;. | 
**id** | **int** | Unique ID number of this customer. | [optional] [readonly] 
**alternate_id** | **str** | A customer-configurable alternate ID number for this customer.  You may set this value to match any  other system that would like to reference this customer record. | [optional] 
**attn_name** | **str** | Indicates the \&quot;Attn:\&quot; component of the address for this customer, if this customer requires mailings to be shipped  to the attention of a specific person or department name. | [optional] 
**line2** | **str** | Second line of the street address of this customer. | [optional] 
**phone_number** | **str** | The main phone number for this customer. | [optional] 
**fax_number** | **str** | The fax phone number for this customer, if any. | [optional] 
**email_address** | **str** | The main email address for this customer. | [optional] 
**contact_name** | **str** | The name of the main contact person for this customer. | [optional] 
**last_transaction** | **datetime** | Date when this customer last executed a transaction. | [optional] [readonly] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**region** | **str** | ISO 3166 code identifying the region within the country.  Two and three character ISO 3166 region codes.  This is a required field if the country is US or CA. For other countries, this is an optional field.  For a full list of all supported codes, please see the Definitions API &#x60;ListRegions&#x60;. | [optional] 
**is_bill** | **bool** | True if this customer record is specifically used for bill-to purposes. | [optional] 
**is_ship** | **bool** | True if this customer record is specifically used for ship-to purposes. | [optional] 
**taxpayer_id_number** | **str** | For customers in the United States, this field is the federal taxpayer ID number.  For businesses, this is  a Federal Employer Identification Number.  For individuals, this will be a Social Security Number. | [optional] 
**certificates** | [**[CertificateModel]**](CertificateModel.md) | A list of exemption certficates that apply to this customer.  You can fetch this data by specifying  &#x60;$include&#x3D;certificates&#x60; when calling a customer fetch API. | [optional] 
**custom_fields** | [**[CustomFieldModel]**](CustomFieldModel.md) | A list of custom fields defined on this customer.                For more information about custom fields, see the [Avalara Help Center article about custom fields](https://help.avalara.com/0021_Avalara_CertCapture/All_About_CertCapture/Edit_or_Remove_Details_about_Customers). | [optional] 
**exposure_zones** | [**[ExposureZoneModel]**](ExposureZoneModel.md) | A list of exposure zones where you do business with this customer.                To keep track of certificates that are needed for each customer, set this value to a list of all exposure zones where you  sell products to this customer.  You can find a list of exposure zones by calling &#x60;ListExposureZones&#x60;.                This field is often called \&quot;Ship-To States\&quot; or \&quot;Ship-To Zones\&quot;, since it generally refers to locations where you ship products  when this customer makes a purchase.                This field is useful for audit purposes since it helps you ensure you have the necessary certificates for each customer. | [optional] 
**ship_tos** | [**[CustomerModel]**](CustomerModel.md) | A list of ship-to customer records that are connected to this bill-to customer.                Customer records represent businesses or individuals who can provide exemption certificates.  Some customers  may have certificates that are linked to their shipping address or their billing address.  To group these  customer records together, you may link multiple bill-to and ship-to addresses together to represent a single  entity that has multiple different addresses of different kinds. | [optional] 
**attributes** | [**[CustomerAttributeModel]**](CustomerAttributeModel.md) | A list of attributes that apply to this customer.                You can fetch this data by specifying &#x60;$include&#x3D;attributes&#x60; when calling a customer fetch API. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


