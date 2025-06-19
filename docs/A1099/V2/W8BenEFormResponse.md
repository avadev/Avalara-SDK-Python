# W8BenEFormResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the individual or entity associated with the form. | [optional] 
**citizenship_country** | **str** | The country of citizenship. | [optional] 
**disregarded_entity** | **str** | The name of the disregarded entity receiving the payment (if applicable). | [optional] 
**entity_type** | **str** | The entity type. | [optional] 
**making_treaty_claim** | **bool** | Indicates whether the entity is making a treaty claim. | [optional] 
**fatca_status** | **str** | The FATCA status. | [optional] 
**residence_address** | **str** | The residential address of the individual or entity. | [optional] 
**residence_city** | **str** | The city of residence. | [optional] 
**residence_state** | **str** | The state of residence. | [optional] 
**residence_zip** | **str** | The ZIP code of the residence. | [optional] 
**residence_country** | **str** | The country of residence. | [optional] 
**residence_is_mailing** | **bool** | Indicates whether the residence address is also the mailing address. | [optional] 
**mailing_address** | **str** | The mailing address. | [optional] 
**mailing_city** | **str** | The city of the mailing address. | [optional] 
**mailing_state** | **str** | The state of the mailing address. | [optional] 
**mailing_zip** | **str** | The ZIP code of the mailing address. | [optional] 
**mailing_country** | **str** | The country of the mailing address. | [optional] 
**tin_type** | **str** | The type of TIN provided. | [optional] 
**tin** | **str** | The taxpayer identification number (TIN). | [optional] 
**giin** | **str** | The global intermediary identification number (GIIN). | [optional] 
**foreign_tin_not_required** | **bool** | Indicates whether a foreign TIN is not required. | [optional] 
**foreign_tin** | **str** | The foreign taxpayer identification number (TIN). | [optional] 
**reference_number** | **str** | A reference number for the form. | [optional] 
**disregarded_entity_fatca_status** | **str** | The FATCA status of disregarded entity or branch receiving payment. | [optional] 
**disregarded_address** | **str** | The address for disregarded entities. | [optional] 
**disregarded_city** | **str** | The city for disregarded entities. | [optional] 
**disregarded_state** | **str** | The state for disregarded entities. | [optional] 
**disregarded_zip** | **str** | The ZIP code for disregarded entities. | [optional] 
**disregarded_country** | **str** | The country for disregarded entities. | [optional] 
**disregarded_entity_giin** | **str** | The GIIN for disregarded entities. | [optional] 
**treaty_country_certification** | **bool** | Certifies the beneficial owner&#39;s country under the U.S. tax treaty. | [optional] 
**treaty_country** | **str** | The treaty country of the beneficial owner. | [optional] 
**benefit_limitation_certification** | **bool** | Certifies that the beneficial owner is eligible for treaty benefits and meets any limitation on benefits requirements. | [optional] 
**benefit_limitation** | **str** | The benefit limitation for tax treaty claims. | [optional] 
**qualified_resident_status_certification** | **bool** | Certifies that the beneficial owner claims treaty benefits and meets the qualified resident status for specific U.S. source income. | [optional] 
**treaty_article** | **str** | Indicates the specific article and paragraph of the tax treaty under which the beneficial owner is claiming benefits. | [optional] 
**withholding_rate** | **str** | Specifies the reduced withholding rate claimed under the applicable tax treaty. | [optional] 
**income_type** | **str** | Specifies the type of income for which the reduced treaty withholding rate is being claimed. | [optional] 
**treaty_reasons** | **str** | The additional conditions in the article the beneficial owner meets to be eligible for the rate of withholding. | [optional] 
**ffi_sponsoring_entity** | **str** | The name of the entity that sponsors the foreign financial institution (FFI). | [optional] 
**investment_entity_certification** | **bool** | Certifies that the entity is an investment entity, not a QI, WP, or WT, and has an agreement with a sponsoring entity. | [optional] 
**controlled_foreign_corporation_certification** | **bool** | Certifies that the entity is a controlled foreign corporation sponsored by a U.S. financial institution, not a QI, WP, or WT,  and shares a common electronic account system for full transparency. | [optional] 
**compliant_nonregistering_local_bank_certification** | **bool** | Certifies that the FFI operates solely as a limited bank or credit union within its country, meets asset thresholds,  and has no foreign operations or affiliations outside its country of organization. | [optional] 
**compliant_ffi_low_value_accounts_certification** | **bool** | Certifies that the FFI is not primarily engaged in investment activities, maintains only low-value accounts,  and has limited total assets within its group. | [optional] 
**sponsored_closely_held_entity_sponsoring_entity** | **str** | The name of sponsoring entity for a certified deemed-compliant, closely held investment vehicle. | [optional] 
**sponsored_closely_held_investment_vehicle_certification** | **bool** | Certifies that the entity is a sponsored investment entity with 20 or fewer individual owners,  and that all compliance obligations are fulfilled by the sponsoring entity. | [optional] 
**compliant_limited_life_debt_entity_certification** | **bool** | Certifies that the entity qualifies as a limited life debt investment entity based on its formation date, issuance terms,  and compliance with regulatory requirements. | [optional] 
**investment_entity_no_financial_accounts_certification** | **bool** | Certifies that the entity is a financial institution solely because it is an investment entity under regulations  and the entity does not maintain financial accounts. | [optional] 
**owner_documented_ffi_certification** | **bool** | Certifies that the FFI meets all requirements to qualify as an owner-documented FFI, including restrictions on activities,  ownership, and account relationships. | [optional] 
**owner_documented_ffi_reporting_statement_certification** | **bool** | Certifies that the FFI will provide a complete owner reporting statement  and required documentation for each relevant owner or debt holder. | [optional] 
**owner_documented_ffi_auditor_letter_certification** | **bool** | Certifies that the FFI will provide an auditor’s letter and required owner reporting documentation  to confirm its status as an owner-documented FFI. | [optional] 
**owner_documented_ffi_trust_beneficiaries_certification** | **bool** | Certifies that the trust has no contingent or unidentified beneficiaries or designated classes of beneficiaries. | [optional] 
**restricted_distributor_certification** | **bool** | Certifies that the entity qualifies as a restricted distributor based on its operations, customer base, regulatory compliance,  and financial and geographic limitations. | [optional] 
**restricted_distributor_agreement_certification** | **bool** | Certifies that the entity is, and has been, bound by distribution agreements prohibiting sales of fund interests to  specified U.S. persons and certain non-U.S. entities. | [optional] 
**restricted_distributor_preexisting_sales_compliance_certification** | **bool** | Certifies that the entity complies with distribution restrictions for U.S.-linked investors  and has addressed any preexisting sales in accordance with FATCA regulations. | [optional] 
**nonreporting_iga_ffi_certification** | **bool** | Certifies that the entity meets the requirements to be considered a nonreporting financial institution to an applicable IGA. | [optional] 
**iga_country** | **str** | The country for the applicable IGA with the United States. | [optional] 
**iga_model** | **str** | The applicable IGA model. | [optional] 
**iga_legal_status_treatment** | **str** | Specifies how the applicable IGA is treated under the IGA provisions or Treasury regulations. | [optional] 
**iga_ffi_trustee_or_sponsor** | **str** | The trustee or sponsor name for the nonreporting IGA FFI. | [optional] 
**iga_ffi_trustee_is_foreign** | **bool** | Indicates whether the trustee for the nonreporting IGA FFI is foreign. | [optional] 
**non_commercial_financial_activity_certification** | **bool** | Certifies that the entity is the beneficial owner and is not engaged in commercial financial activities related  to the specified payments, accounts or obligations for which this form is submitted. | [optional] 
**internation_organization_certification** | **bool** | Certifies that the entity is an international organization described in section 7701(a)(18). | [optional] 
**intergovernmental_organization_certification** | **bool** | Certifies that the entity is an intergovernmental or supranational organization primarily comprised of foreign governments,  is the beneficial owner, and is not engaged in commercial financial activities. | [optional] 
**treaty_qualified_pension_fund_certification** | **bool** | Certifies that the entity is a pension or retirement fund established in a treaty country  and is entitled to treaty benefits on U.S. source income. | [optional] 
**qualified_retirement_fund_certification** | **bool** | Certifies that the entity is a government-regulated retirement fund meeting specific requirements for contributions, tax exemption,  beneficiary limits, and distribution restrictions. | [optional] 
**narrow_participation_retirement_fund_certification** | **bool** | Certifies that the entity is a government-regulated retirement fund with fewer than 50 participants, limited foreign ownership,  and employer sponsorship that is not from investment entities or passive NFFEs. | [optional] 
**section401_a_equivalent_pension_plan_certification** | **bool** | Certifies that the entity is formed under a pension plan meeting section 401(a) requirements, except for being U.S.-trust funded. | [optional] 
**investment_entity_for_retirement_funds_certification** | **bool** | Certifies that the entity is established solely to earn income for the benefit of qualifying retirement funds  or accounts under applicable FATCA regulations or IGAs. | [optional] 
**exempt_beneficial_owner_sponsored_retirement_fund_certification** | **bool** | Certifies that the entity is established and sponsored by a qualifying exempt beneficial owner to provide retirement, disability,  or death benefits to individuals based on services performed for the sponsor. | [optional] 
**exempt_beneficial_owner_owned_investment_entity_certification** | **bool** | Certifies that the entity is an investment entity wholly owned by exempt beneficial owners and has provided complete ownership  and documentation details as required under FATCA regulations. | [optional] 
**territory_financial_institution_certification** | **bool** | Certifies that the entity is a financial institution (other than an investment entity) that is incorporated  or organized under the laws of a possession of the United States. | [optional] 
**excepted_nonfinancial_group_entity_certification** | **bool** | Certifies that the entity is a holding company, treasury center, or captive finance company operating within a nonfinancial group  and not functioning as an investment or financial institution. | [optional] 
**excepted_nonfinancial_start_up_certification** | **bool** | Certifies that the entity is a recently formed startup NFFE investing in a non-financial business  and is not operating as or presenting itself as an investment fund. | [optional] 
**startup_formation_or_resolution_date** | **datetime** | The date the start-up company was formed on (or, in case of new line of business, the date of board resolution approving the  new line of business). | [optional] 
**excepted_nonfinancial_entity_in_liquidation_or_bankruptcy_certification** | **bool** | Certifies that the entity is in liquidation, reorganization, or bankruptcy and intends to operate as a nonfinancial entity,  with supporting documentation available if the process exceeds three years. | [optional] 
**nonfinancial_entity_filing_date** | **datetime** | The filed date for a plan of reorganization, liquidation or bankruptcy. | [optional] 
**section501_c_organization_certification** | **bool** | Certifies that the entity is a section 501(c) organization based on a valid IRS determination letter  or a legal opinion from U.S. counsel. | [optional] 
**determination_letter_date** | **datetime** | The date of the IRS determination letter confirming the entity’s section 501(c) status. | [optional] 
**nonprofit_organization_certification** | **bool** | Certifies that the entity is a nonprofit organization established for charitable or similar purposes, exempt from income tax,  and restricted in the use and distribution of its assets under applicable law. | [optional] 
**publicly_traded_nffe_certification** | **bool** | Certifies that the entity is a foreign corporation that is not a financial institution  and whose stock is regularly traded on an established securities market. | [optional] 
**publicly_traded_nffe_securities_market** | **str** | The name of the securities market where the corporation&#39;s stock is regularly traded. | [optional] 
**nffe_affiliate_of_publicly_traded_entity_certification** | **bool** | Certifies that the entity is a foreign corporation that is not a financial institution  and is affiliated with a publicly traded entity within the same expanded affiliated group. | [optional] 
**publicly_traded_entity** | **str** | The name of the affiliated entity whose stock is regularly traded on an established securities market. | [optional] 
**nffe_affiliate_of_publicly_traded_entity_securities_market** | **str** | The name of the established securities market where the affiliated entity&#39;s stock is traded. | [optional] 
**excepted_territory_nffe_certification** | **bool** | Certifies that the entity is organized in a U.S. possession, is not engaged in financial activities,  and is entirely owned by bona fide residents of that possession. | [optional] 
**active_nffe_certification** | **bool** | Certifies that the entity is a foreign non-financial institution with less than 50% passive income  and less than 50% of its assets producing or held to produce passive income. | [optional] 
**passive_nffe_certification** | **bool** | Certifies that the entity is a foreign non-financial entity that does not qualify for any other NFFE category  and is not a financial institution. | [optional] 
**passive_nffe_no_substantial_us_owners_certification** | **bool** | Certifies that the passive NFFE has no substantial U.S. owners or controlling U.S. persons. | [optional] 
**passive_nffe_substantial_us_owners_provided_certification** | **bool** | Certifies that the passive NFFE has provided the name, address, and TIN of each substantial U.S. owner or controlling U.S. person. | [optional] 
**excepted_inter_affiliate_ffi_certification** | **bool** | Certifies that the entity is an inter-affiliate FFI meeting all conditions for exemption,  including limited account activity and payment interactions within its expanded affiliated group. | [optional] 
**sponsored_direct_reporting_nffe_certification** | **bool** | Certifies that the entity is a sponsored direct reporting NFFE. | [optional] 
**direct_reporting_nffe_sponsoring_entity** | **str** | The name of the entity that sponsors the direct reporting NFFE. | [optional] 
**substantial_us_owners** | [**List[SubstantialUsOwnerResponse]**](SubstantialUsOwnerResponse.md) | The list of substantial U.S. owners of passive NFFE. | [optional] 
**signer_name** | **str** | The name of the signer. | [optional] 
**capacity_to_sign_certification** | **bool** | Certifies signer has the capacity to sign for the beneficial owner. | [optional] 
**id** | **str** | The unique identifier for the form. | [optional] 
**type** | **str** | The form type. | [optional] 
**entry_status** | **str** | The form status. | [optional] 
**entry_status_date** | **datetime** | The timestamp for the latest status update. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**company_id** | **str** | The ID of the associated company. | [optional] 
**display_name** | **str** | The display name associated with the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 
**archived** | **bool** | Indicates whether the form is archived. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**signed_date** | **datetime** | The date the form was signed. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**created_at** | **datetime** | The creation date of the form. | [optional] 
**updated_at** | **datetime** | The last updated date of the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.w8_ben_e_form_response import W8BenEFormResponse

# TODO update the JSON string below
json = "{}"
# create an instance of W8BenEFormResponse from a JSON string
w8_ben_e_form_response_instance = W8BenEFormResponse.from_json(json)
# print the JSON string representation of the object
print(W8BenEFormResponse.to_json())

# convert the object into a dict
w8_ben_e_form_response_dict = w8_ben_e_form_response_instance.to_dict()
# create an instance of W8BenEFormResponse from a dict
w8_ben_e_form_response_from_dict = W8BenEFormResponse.from_dict(w8_ben_e_form_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


