# CertificateAttributeModel

A certificate attribute can be thought of as a feature or flag that is applied to a certificate.  A single certificate can be linked to zero, one, or many certificate attributes.  The full list of  attributes can be obtained by calling the `ListCertificateAttributes` API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique ID number representing this certificate attribute. | [optional] 
**name** | **str** | A friendly readable name for this certificate attribute. | [optional] 
**description** | **str** | A full help text description of the certificate attribute. | [optional] 
**is_system_code** | **bool** | This value is true if this is a system-defined certificate attribute.  System-defined attributes  cannot be modified or deleted on the CertCapture website. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


