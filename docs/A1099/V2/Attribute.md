# Attribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**upsert** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**total_processed** | **int** |  | [optional] 
**total_rows** | **int** |  | [optional] 
**updated_valid** | **int** |  | [optional] 
**updated_no_email** | **int** |  | [optional] 
**updated_invalid** | **int** |  | [optional] 
**skipped_duplicate** | **int** |  | [optional] 
**skipped_invalid** | **int** |  | [optional] 
**skipped_multiple_matches** | **int** |  | [optional] 
**not_found** | **int** |  | [optional] 
**created_invalid** | **int** |  | [optional] 
**created_no_email** | **int** |  | [optional] 
**created_valid** | **int** |  | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print(Attribute.to_json())

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_from_dict = Attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


