# LineItemModel

Represents one line item in a transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Total amount for this line.  The amount represents the net currency value that changed hands from the customer (represented by the &#x60;customerCode&#x60; field) to the company (represented by the &#x60;companyCode&#x60;) field.                For sale transactions, this value must be positive.  It indicates the amount of money paid by the customer to the company.                For refund or return transactions, this value must be negative. | 
**number** | **str** | The line number of this line within the document.  This can be any text that is useful to you, such as numeric line numbers, alphabetic line numbers, or other text. | [optional] 
**quantity** | **float** | Quantity of items in this line.  This quantity value should always be a positive value representing the quantity of product that changed hands, even when handling returns or refunds.                If not provided, or if set to zero, the quantity value is assumed to be one (1). | [optional] 
**addresses** | [**AddressesModel**](AddressesModel.md) |  | [optional] 
**tax_code** | **str** | Tax Code - System or Custom Tax Code.                You can use your own tax code mapping or standard Avalara tax codes.  For a full list of tax codes, see &#x60;ListTaxCodes&#x60;. | [optional] 
**customer_usage_type** | **str** | DEPRECATED - Date: 10/16/2017, Version: 17.11, Message: Please use &#x60;entityUseCode&#x60; instead.   | [optional] 
**entity_use_code** | **str** | Entity Use Code - The client application customer or usage type.  This field allows you to designate a type of usage that  may make this transaction considered exempt by reason of exempt usage.                For a list of entity use codes, see the Definitions API &#x60;ListEntityUseCodes&#x60;. | [optional] 
**item_code** | **str** | Item Code (SKU).  If you provide an &#x60;itemCode&#x60; field, the AvaTax API will look up the item you created with the &#x60;CreateItems&#x60; API call  and use all the information available about that item for this transaction. | [optional] 
**exemption_code** | **str** | The customer Tax Id Number (tax_number) associated with a certificate - Sales tax calculation requests first determine if there is an applicable  ECMS entry available, and will utilize it for exemption processing. If no applicable ECMS entry is available, the AvaTax service  will determine if an Exemption Number field is populated or an Entity/Use Code is included in the sales tax calculation request,  and will perform exemption processing using either of those two options.  Note: This is same as &#39;exemptNo&#39; in TransactionModel. | [optional] 
**discounted** | **bool** | True if the document discount should be applied to this line.  If this value is false, or not provided, discounts will not be  applied to this line even if they are specified on the root &#x60;discount&#x60; element. | [optional] 
**tax_included** | **bool** | Indicates whether the &#x60;amount&#x60; for this line already includes tax.                If this value is &#x60;true&#x60;, the final price of this line including tax will equal the value in &#x60;amount&#x60;.                If this value is &#x60;null&#x60; or &#x60;false&#x60;, the final price will equal &#x60;amount&#x60; plus whatever taxes apply to this line. | [optional] 
**revenue_account** | **str** | Revenue Account (Customer Defined Field).                This field is available for you to use to provide whatever information your implementation requires.  It does not affect tax calculation. | [optional] 
**ref1** | **str** | Ref1 (Customer Defined Field)                This field is available for you to use to provide whatever information your implementation requires.  It does not affect tax calculation. | [optional] 
**ref2** | **str** | Ref2 (Customer Defined Field)                This field is available for you to use to provide whatever information your implementation requires.  It does not affect tax calculation. | [optional] 
**description** | **str** | Item description.                For Streamlined Sales Tax (SST) customers, this field is required if an unmapped &#x60;itemCode&#x60; is used. | [optional] 
**business_identification_no** | **str** | VAT business identification number for the customer for this line item.  If you leave this field empty,  this line item will use whatever business identification number you provided at the transaction level.                If you specify a VAT business identification number for the customer in this transaction and you have also set up  a business identification number for your company during company setup, this transaction will be treated as a  business-to-business transaction for VAT purposes and it will be calculated according to VAT tax rules. | [optional] 
**tax_override** | [**TaxOverrideModel**](TaxOverrideModel.md) |  | [optional] 
**parameters** | [**[TransactionLineParameterModel]**](TransactionLineParameterModel.md) | Special parameters that apply to this line within this transaction.                To get a full list of available parameters, please use the &#x60;ListParameters&#x60; API. | [optional] 
**user_defined_fields** | [**[TransactionLineUserDefinedFieldModel]**](TransactionLineUserDefinedFieldModel.md) | Custom user fields/flex fields for this line. | [optional] 
**hs_code** | **str** | The Item code for Custom Duty / Global Import tax determination  Harmonized Tariff System code for this transaction.                For a list of harmonized tariff codes, see the Definitions API for harmonized tariff codes. | [optional] 
**merchant_seller_id** | **int** | DEPRECATED - Date: 04/15/2021, Version: 21.4, Message: Please use merchantSellerIdentifier instead.  ID of the merchant selling on the Marketplace. This field must be populated by Marketplace. | [optional] 
**merchant_seller_identifier** | **str** | ID of the merchant selling on the Marketplace. This field must be populated by Marketplace. | [optional] 
**marketplace_liability_type** | **str** | This field will identify who is remitting Marketplace or Seller. This field must be populated by Marketplace. | [optional] 
**origination_document_id** | **str** | The transaction&#39;s original ID in its origination system | [optional] 
**origination_site** | **str** | Synonym of Marketplace Origination. Name of the Marketplace where the transaction originated from. | [optional] 
**category** | **str** | Product category breadcrumbs. This is the full path to the category where item is included. Categories should be separated by “ &gt; “.  Multiple category paths per item are accepted. In this case, category paths should be separated by “;”. | [optional] 
**summary** | **str** | A long description of the product. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


