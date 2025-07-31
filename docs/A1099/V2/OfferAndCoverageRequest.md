# OfferAndCoverageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **str** | Month of coverage | [optional] 
**offer_code** | **str** | Offer of coverage code | [optional] 
**share** | **float** | Employee required contribution share | [optional] 
**safe_harbor_code** | **str** | Safe harbor code | [optional] 
**zip_code** | **str** | ZIP code for coverage area | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.offer_and_coverage_request import OfferAndCoverageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OfferAndCoverageRequest from a JSON string
offer_and_coverage_request_instance = OfferAndCoverageRequest.from_json(json)
# print the JSON string representation of the object
print(OfferAndCoverageRequest.to_json())

# convert the object into a dict
offer_and_coverage_request_dict = offer_and_coverage_request_instance.to_dict()
# create an instance of OfferAndCoverageRequest from a dict
offer_and_coverage_request_from_dict = OfferAndCoverageRequest.from_dict(offer_and_coverage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


