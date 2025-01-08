# SettingModel

This object is used to keep track of custom information about a company.                The company settings system is a metadata system that you can use to store extra information  about a company.  Your integration or connector could use this data storage to keep track of  preference information, reminders, or any other storage that would need to persist even if  the customer uninstalls your application.                A setting can refer to any type of data you need to remember about this company object.  When creating this object, you may define your own `set`, `name`, and `value` parameters.  To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID number of this setting. | 
**set** | **str** | A user-defined \&quot;set\&quot; containing this setting.                Avalara defines some sets that cannot be changed.  To create your own set, choose a set  name that begins with &#x60;X-&#x60; to indicate that this is an extension value.                We recommend that you choose a set name that clearly identifies your application, and then  store data within name/value pairs within that set.  For example, if you were creating an  application called MyApp, you might choose to create a set named &#x60;X-MyCompany-MyApp&#x60;. | 
**name** | **str** | A user-defined \&quot;name\&quot; for this name-value pair. | 
**company_id** | **int** | The unique ID number of the company this setting refers to. | [optional] [readonly] 
**value** | **str** | The value of this name-value pair. | [optional] 
**modified_date** | **datetime** | The value when the entry was last modified. | [optional] [readonly] 
**modified_user_id** | **int** | The value identifying who last modified the entry. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


