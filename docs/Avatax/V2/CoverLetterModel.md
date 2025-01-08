# CoverLetterModel

The CoverLetter model represents a message sent along with an invitation to use CertExpress to  upload certificates.  An invitation allows customers to use CertExpress to upload their exemption  certificates directly; this cover letter explains why the invitation was sent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique ID number representing a cover letter sent with a CertExpress invitation. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the AvaTax company that received this certificate. | [optional] 
**title** | **str** | The title used when sending the cover letter. | [optional] 
**subject** | **str** | The subject message used when sending the cover letter via email. | [optional] 
**description** | **str** | A full description of the cover letter&#39;s contents and message. | [optional] 
**created_date** | **datetime** | The date when this record was created. | [optional] [readonly] 
**modified_date** | **datetime** | The date/time when this record was last modified. | [optional] [readonly] 
**active** | **bool** | Is this cover letter active | [optional] 
**page_count** | **int** | How many pages this cover letter encompasses | [optional] [readonly] 
**template_filename** | **str** | The file name of the cover letter template | [optional] 
**version** | **int** | The version number of the template | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


