# CreateTransactionModel

Create a transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**[LineItemModel]**](LineItemModel.md) | A list of line items that will appear on this transaction. | 
**date** | **date** | Transaction Date - The date on the invoice, purchase order, etc.                By default, this date will be used to calculate the tax rates for the transaction.  If you wish to use a  different date to calculate tax rates, please specify a &#x60;taxOverride&#x60; of type &#x60;taxDate&#x60;. | 
**customer_code** | **str** | Customer Code - The client application customer reference code.  Note: This field is case sensitive. To have exemption certificates apply, this value should  be the same as the one passed to create a customer. | 
**code** | **str** | The internal reference code used by the client application.  This is used for operations such as  Get, Adjust, Settle, and Void.  If you leave the transaction code blank, a GUID will be assigned to each transaction. | [optional] 
**type** | **str** | Specifies the type of document to create.  A document type ending with &#x60;Invoice&#x60; is a permanent transaction  that will be recorded in AvaTax.  A document type ending with &#x60;Order&#x60; is a temporary estimate that will not  be preserved.                If you omit this value, the API will assume you want to create a &#x60;SalesOrder&#x60;. | [optional] 
**company_code** | **str** | Company Code - Specify the code of the company creating this transaction here.  If you leave this value null,  your account&#39;s default company will be used instead. | [optional] 
**salesperson_code** | **str** | Salesperson Code - The client application salesperson reference code. | [optional] 
**customer_usage_type** | **str** | DEPRECATED - Date: 10/16/2017, Version: 17.11, Message: Please use entityUseCode instead.  Customer Usage Type - The client application customer or usage type. | [optional] 
**entity_use_code** | **str** | Entity Use Code - The client application customer or usage type.  For a list of  available usage types, use [ListEntityUseCodes](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Definitions/ListEntityUseCodes/) API. | [optional] 
**discount** | **float** | Discount - The discount amount to apply to the document.  This value will be applied only to lines  that have the &#x60;discounted&#x60; flag set to true.  If no lines have &#x60;discounted&#x60; set to true, this discount  cannot be applied. | [optional] 
**purchase_order_no** | **str** | Purchase Order Number for this document.                This is required for single use exemption certificates to match the order and invoice with the certificate. | [optional] 
**exemption_no** | **str** | Exemption Number for this document.                If you specify an exemption number for this document, this document will be considered exempt, and you  may be asked to provide proof of this exemption certificate in the event that you are asked by an auditor  to verify your exemptions.  Note: This is same as &#39;exemptNo&#39; in TransactionModel. | [optional] 
**addresses** | [**AddressesModel**](AddressesModel.md) |  | [optional] 
**parameters** | [**[TransactionParameterModel]**](TransactionParameterModel.md) | Special parameters for this transaction.                To get a full list of available parameters, please use the [ListParameters](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Definitions/ListParameters/) endpoint. | [optional] 
**user_defined_fields** | [**[TransactionUserDefinedFieldModel]**](TransactionUserDefinedFieldModel.md) | Custom user fields/flex fields for this transaction. | [optional] 
**reference_code** | **str** | Customer-provided Reference Code with information about this transaction.                This field could be used to reference the original document for a return invoice, or for any other  reference purpose. | [optional] 
**reporting_location_code** | **str** | Sets the sale location code (Outlet ID) for reporting this document to the tax authority.                This value is used by Avalara Managed Returns to group documents together by reporting locations  for tax authorities that require location-based reporting. | [optional] 
**commit** | **bool** | Causes the document to be committed if true.  This option is only applicable for invoice document  types, not orders. | [optional] 
**batch_code** | **str** | BatchCode for batch operations. | [optional] 
**tax_override** | [**TaxOverrideModel**](TaxOverrideModel.md) |  | [optional] 
**currency_code** | **str** | The three-character ISO 4217 currency code for this transaction. | [optional] 
**service_mode** | **str** | Specifies whether the tax calculation is handled Local, Remote, or Automatic (default).  This only  applies when using an AvaLocal server. | [optional] 
**exchange_rate** | **float** | Currency exchange rate from this transaction to the company base currency.                This only needs to be set if the transaction currency is different than the company base currency.  It defaults to 1.0. | [optional] 
**exchange_rate_effective_date** | **date** | Effective date of the exchange rate. | [optional] 
**exchange_rate_currency_code** | **str** | Optional three-character ISO 4217 reporting exchange rate currency code for this transaction. The default value is USD. | [optional] 
**pos_lane_code** | **str** | Sets the Point of Sale Lane Code sent by the User for this document. | [optional] 
**business_identification_no** | **str** | VAT business identification number for the customer for this transaction.  This number will be used for all lines  in the transaction, except for those lines where you have defined a different business identification number.                If you specify a VAT business identification number for the customer in this transaction and you have also set up  a business identification number for your company during company setup, this transaction will be treated as a  business-to-business transaction for VAT purposes and it will be calculated according to VAT tax rules. | [optional] 
**is_seller_importer_of_record** | **bool** | Specifies if the transaction should have value-added and cross-border taxes calculated with the seller as the importer of record.                Some taxes only apply if the seller is the importer of record for a product.  In cases where companies are working together to  ship products, there may be mutual agreement as to which company is the entity designated as importer of record.  The importer  of record will then be the company designated to pay taxes marked as being obligated to the importer of record.                Set this value to &#x60;true&#x60; to consider your company as the importer of record and collect these taxes.                This value may also be set at the Nexus level.  See &#x60;NexusModel&#x60; for more information. | [optional] 
**description** | **str** | User-supplied description for this transaction. | [optional] 
**email** | **str** | User-supplied email address relevant for this transaction. | [optional] 
**debug_level** | **str** | If the user wishes to request additional debug information from this transaction, specify a level higher than &#x60;normal&#x60;. | [optional] 
**customer_supplier_name** | **str** | The name of the supplier / exporter / seller.  For sales doctype enter the name of your own company for which you are reporting.  For purchases doctype enter the name of the supplier you have purchased from. | [optional] 
**data_source_id** | **int** | The Id of the datasource from which this transaction originated.  This value will be overridden by the system to take the datasource Id from the call header. | [optional] 
**delivery_terms** | **str** | The Delivery Terms is a field used in conjunction with Importer of Record to influence whether AvaTax includes Import Duty and Tax values in the transaction totals or not.  Delivered at Place (DAP) and Delivered Duty Paid (DDP) are two delivery terms that  indicate that Import Duty and Tax should be included in the transaction total.  This field is also used for reports.  This field is used for future feature support. This field is not currently in use. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


