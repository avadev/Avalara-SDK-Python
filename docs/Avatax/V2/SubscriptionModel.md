# SubscriptionModel

Represents a service that this account has subscribed to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID number of this subscription. | [optional] [readonly] 
**account_id** | **int** | The unique ID number of the account this subscription belongs to. | [optional] [readonly] 
**subscription_type_id** | **int** | The unique ID number of the service that the account is subscribed to. If this is provided, subscription description is ignored. | [optional] 
**subscription_description** | **str** | A friendly description of the service that the account is subscribed to. You can either provide the subscription type Id or this but not both. If  subscription type Id is provided, then this information is ignored and this field will be updated with the information from subscription type id. | [optional] 
**effective_date** | **date** | The date when the subscription began. | [optional] 
**end_date** | **date** | If the subscription has ended or will end, this date indicates when the subscription ends. | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**created_user_id** | **int** | The User ID of the user who created this record. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The user ID of the user who last modified this record. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


