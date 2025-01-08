# CustomerAttributeModel

A Customer's linked attribute denoting what features applied to the customer. A customer can  be linked to multiple customer attributes and vice versa.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique ID number representing this attribute. | [optional] 
**name** | **str** | A friendly readable name for this attribute. | [optional] 
**description** | **str** | A full help text description of the attribute. | [optional] 
**is_system_code** | **bool** | This value is true if this is a system-defined attribute.  System-defined attributes  cannot be modified or deleted on the CertCapture website. | [optional] 
**is_non_deliver** | **bool** | A flag denotes that future exemption certificate request won&#39;t be mailed to the customer | [optional] 
**is_changeable** | **bool** | A flag denotes that this attribute can&#39;t be removed/added to a customer record | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


