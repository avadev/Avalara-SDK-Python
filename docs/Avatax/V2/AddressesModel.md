# AddressesModel

Information about all the addresses involved in this transaction.                For a physical in-person transaction at a retail point-of-sale location, please specify only one address using  the `singleLocation` field.                For a transaction that was shipped, delivered, or provided from an origin location such as a warehouse to  a destination location such as a customer, please specify the `shipFrom` and `shipTo` addresses.                In the United States, some jurisdictions recognize the address types `pointOfOrderOrigin` and `pointOfOrderAcceptance`.  These address types affect the sourcing models of some transactions.                If latitude and longitude information is provided for any of these addresses along with line, city, region, country and postal code information,  we will be using only latitude and longitude and will discard line, city, region, country and postal code information for the transaction.  Please ensure that you have the correct latitude/longitude information for the addresses prior to using the API.  If you provide either latitude or longitude information but not both, we will be using the line, city, region, country and postal code information for the addresses.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**single_location** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**ship_from** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**ship_to** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**point_of_order_origin** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**point_of_order_acceptance** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**goods_place_or_service_rendered** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**_import** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**bill_to** | [**AddressLocationInfo**](AddressLocationInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


