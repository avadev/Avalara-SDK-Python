# DocumentStatusResponse

Returns the current document ID and status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for this document | [optional] 
**status** | **str** | Status of the transaction: &lt;br&gt; &#39;Pending&#39; &lt;br&gt; &#39;Failed&#39; &lt;br&gt; &#39;Complete&#39; | [optional] 
**events** | [**[StatusEvent]**](StatusEvent.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


