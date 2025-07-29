# BatchErrorDetail

Represents detailed error information for an individual entry in a batch request. Includes the index of the failed item and associated validation errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index of the request that caused the error in the batch. | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 

## Example

```python
from Avalara.SDK.models.EInvoicing.V1.batch_error_detail import BatchErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BatchErrorDetail from a JSON string
batch_error_detail_instance = BatchErrorDetail.from_json(json)
# print the JSON string representation of the object
print(BatchErrorDetail.to_json())

# convert the object into a dict
batch_error_detail_dict = batch_error_detail_instance.to_dict()
# create an instance of BatchErrorDetail from a dict
batch_error_detail_from_dict = BatchErrorDetail.from_dict(batch_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


