# CreateCertExpressInvitationModel

Represents an invitation for a customer to use CertExpress to self-report their own certificates.  This invitation is delivered by your choice of method, or you can present a hyperlink to the user  directly in your connector.  Your customer will be redirected to https://app.certexpress.com/ where  they can follow a step-by-step guide to enter information about their exemption certificates.  The  certificates entered will be recorded and automatically linked to their customer record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** | If the value of &#x60;deliveryMethod&#x60; is set to &#x60;Email&#x60;, please specify the email address of the recipient  for the request. | [optional] 
**cover_letter_title** | **str** | If this invitation is sent via email or download, please specify the cover letter to use when building this  invitation.  For a list of cover letters, please call &#x60;ListCoverLetters&#x60;. | [optional] 
**exposure_zones** | **[int]** | You may optionally specify a list of exposure zones to request in this CertExpress invitation.  If you list  more than one exposure zone, the customer will be prompted to provide an exemption certificate for each one.  If you do not provide a list of exposure zones, the customer will be prompted to select an exposure zone.                For a list of available exposure zones, please call &#x60;ListCertificateExposureZones&#x60;. | [optional] 
**exempt_reasons** | **[int]** | You may optionally specify a list of exemption reasons to pre-populate in this CertExpress invitation.  If you list exemption reasons, the customer will have part of their form already filled in when they visit  the CertExpress website.                For a list of available exemption reasons, please call &#x60;ListCertificateExemptReasons&#x60;. | [optional] 
**delivery_method** | **str** | Specify the type of invitation.  CertExpress invitations can be delivered via email, web link, or  facsimile.                * If you specify &#x60;Email&#x60;, the invitation will be delivered via email.  Please ask the customer to ensure that  * If you specify &#x60;Fax&#x60;, the invitation will be sent via fax to the customer&#39;s fax number on file.  * If you specify &#x60;Download&#x60;, the invitation will be prepared as a web link that you can display to the customer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


