# CertExpressInvitationModel

Represents an invitation for a customer to use CertExpress to self-report their own certificates.  This invitation is delivered by your choice of method, or you can present a hyperlink to the user  directly in your connector.  Your customer will be redirected to https://app.certexpress.com/ where  they can follow a step-by-step guide to enter information about their exemption certificates.  The  certificates entered will be recorded and automatically linked to their customer record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique ID number representing this CertExpress invitation. | [optional] [readonly] 
**company_id** | **int** | The unique ID number of the AvaTax company that sent this invitation. | [optional] 
**recipient** | **str** | The email address to which this invitation was sent.  If this invitation was presented as a weblink, this value will be null. | [optional] 
**customer_code** | **str** | The unique code of the customer that received this invitation.  Note: This field is case sensitive. To have exemption certificates apply, this value should  be the same as the one passed to create a customer. | [optional] 
**customer** | [**CustomerModel**](CustomerModel.md) |  | [optional] 
**cover_letter** | [**CoverLetterModel**](CoverLetterModel.md) |  | [optional] 
**email_status** | **str** | The status of the emails associated with this invitation.  If this invitation was sent via email,  this value will change to &#x60;Sent&#x60; when the email message has been sent. | [optional] [readonly] 
**cover_letters_only** | **bool** | True if this invitation contained a cover letter only. | [optional] [readonly] 
**exposure_zones** | **[int]** | When an invitation is sent, it contains a list of exposure zones for which the customer is invited to upload  their exemption certificates.  This list contains the ID numbers of the exposure zones identified.                For a list of exposure zones, please call &#x60;ListCertificateExposureZones&#x60;. | [optional] 
**exempt_reasons** | **[int]** | The list of exemption reasons identified by this CertExpress invitation.                For a list of reason codes, please call &#x60;ListCertificateExemptReasons&#x60;. | [optional] 
**delivery_method** | **str** | Indicates the method that was used to deliver this CertExpress invitation. | [optional] 
**message** | **str** | The custom message delivered with this invitation. | [optional] 
**date** | **datetime** | The date of the invitation. | [optional] 
**request_link** | **str** | The web link (URL) that a customer can click on or visit to begin using this CertExpress invitation.                This value is only usable if the status of this invitation is &#x60;Ready&#x60; and the request was created with type &#x60;Download&#x60;.  NOTE: This link usually takes a few minutes to be available. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


