# JobResponse

Response model for job operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the job | [optional] 
**type** | **str** | Job type identifier. Will always be \&quot;update_job\&quot; for bulk upsert operations | [optional] 
**status** | **str** | Current status of the job (e.g., Success, Failed, InProgress) | [optional] 
**error_message** | **str** | Error message if the job failed, null otherwise | [optional] 
**total_processed** | **int** | Total number of forms processed. Value can be 0 or another value based on what the job has available | [optional] 
**total_rows** | **int** | Total number of forms in the request. Value can be 0 or another value based on what the job has available | [optional] 
**updated_valid** | **int** | Number of forms updated and valid for e-filing and e-delivery. Value can be 0 or another value based on what the job has available | [optional] 
**updated_no_email** | **int** | Number of forms updated and valid for e-filing but missing email or email is undeliverable. Value can be 0 or another value based on what the job has available | [optional] 
**updated_invalid** | **int** | Number of forms updated but invalid for e-filing. Value can be 0 or another value based on what the job has available | [optional] 
**skipped_duplicate** | **int** | Number of forms skipped because they would have updated a record already updated once in the request. Value can be 0 or another value based on what the job has available | [optional] 
**skipped_invalid** | **int** | Number of forms skipped because they would have made a form invalid and the form is already e-filed or scheduled for e-filing. Value can be 0 or another value based on what the job has available | [optional] 
**skipped_multiple_matches** | **int** | Number of forms skipped because they matched multiple forms. Value can be 0 or another value based on what the job has available | [optional] 
**not_found** | **int** | Number of forms skipped because no matching form or issuer could be found. Value can be 0 or another value based on what the job has available | [optional] 
**created_invalid** | **int** | Number of new forms created because no matching form could be found (and &#x60;upsert&#x60; was true) - with errors. Value can be 0 or another value based on what the job has available | [optional] 
**created_no_email** | **int** | Number of new forms created because no matching form could be found (and &#x60;upsert&#x60; was true) - valid for e-filing but missing email or email is undeliverable. Value can be 0 or another value based on what the job has available | [optional] 
**created_valid** | **int** | Number of new forms created because no matching form could be found (and &#x60;upsert&#x60; was true) - valid for e-filing and e-delivery. Value can be 0 or another value based on what the job has available | [optional] 
**dry_run** | **bool** | Dry run. If &#x60;true&#x60;, this job only simulates the changes but doesn&#39;t actually persist them. | [optional] 
**upsert** | **bool** | Upsert. If &#x60;true&#x60;, this job will first attempt to update existing records if matches can be found. Matches are done in the following order: Form ID, Form Reference ID and tax year, Form TIN and tax year. | [optional] 
**link** | **str** | Link to access the job details | [optional] 
**processed_forms** | [**List[Get1099Form200Response]**](Get1099Form200Response.md) | List of processed forms returned when bulk-upsert processes ≤1000 records. Same format as GET /1099/forms response. Only available in bulk-upsert endpoint responses. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


