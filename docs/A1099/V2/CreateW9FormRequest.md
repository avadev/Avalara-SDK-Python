# CreateW9FormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The form type. | [optional] [readonly] 
**name** | **str** | The name of the individual or entity associated with the form. | 
**business_name** | **str** | The name of the business associated with the form. | [optional] 
**business_classification** | **str** | The classification of the business.  Available values:  - Individual: Individual/sole proprietor  - C Corporation: C Corporation  - S Corporation: S Corporation  - Partnership: Partnership  - Trust/estate: Trust/estate  - LLC-C: Limited liability company (C Corporation)  - LLC-S: Limited liability company (S Corporation)  - LLC-P: Limited liability company (Partnership)  - Other: Other (requires BusinessOther field to be populated) | 
**business_other** | **str** | The classification description when \&quot;businessClassification\&quot; is \&quot;Other\&quot;. | [optional] 
**foreign_partner_owner_or_beneficiary** | **bool** | Indicates whether the individual is a foreign partner, owner, or beneficiary. | [optional] 
**exempt_payee_code** | **str** | The exempt payee code. | [optional] 
**exempt_fatca_code** | **str** | The exemption from FATCA reporting code. | [optional] 
**foreign_country_indicator** | **bool** | Indicates whether the individual or entity is in a foreign country. | [optional] 
**address** | **str** | The address of the employee. Required unless exempt. | 
**foreign_address** | **str** | The foreign address of the individual or entity. | [optional] 
**city** | **str** | The city of residence of the employee. Required unless exempt. | 
**state** | **str** | The state of residence of the employee. Required unless exempt. | 
**zip** | **str** | The ZIP code of residence of the employee. Required unless exempt. | 
**account_number** | **str** | The account number associated with the form. | [optional] 
**tin_type** | **str** | Tax Identification Number (TIN) type. | 
**tin** | **str** | The taxpayer identification number (TIN). | 
**backup_withholding** | **bool** | Indicates whether backup withholding applies. | [optional] 
**is1099able** | **bool** | Indicates whether the individual or entity should be issued a 1099 form. | [optional] 
**e_delivery_consented_at** | **datetime** | The date when e-delivery was consented. | [optional] 
**signature** | **str** | The signature of the form. | [optional] 
**company_id** | **str** | The ID of the associated company. Required when creating a form. | [optional] 
**reference_id** | **str** | A reference identifier for the form. | [optional] 
**email** | **str** | The email address of the individual associated with the form. | [optional] 
**citizenship_country** | **str** | The country of citizenship. | 
**disregarded_entity** | **str** | The name of the disregarded entity receiving the payment (if applicable). | [optional] 
**entity_type** | **str** | The entity type.  Available values:  - 1: Corporation  - 2: Disregarded entity  - 3: Partnership  - 4: Simple trust  - 5: Grantor trust  - 6: Complex trust  - 7: Estate  - 8: Foreign Government - Controlled Entity  - 9: Central Bank of Issue  - 10: Tax-exempt organization  - 11: Private foundation  - 12: International organization  - 13: Foreign Government - Controlled Integral Part | 
**fatca_status** | **str** | The FATCA status.  Available values:  - 1: Nonparticipating FFI (including a limited FFI or an FFI related to a Reporting IGA FFI other than a deemed-compliant FFI, participating FFI, or exempt beneficial owner)  - 2: Participating FFI  - 3: Reporting Model 1 FFI  - 4: Reporting Model 2 FFI  - 5: Registered deemed-compliant FFI (other than a reporting Model 1 FFI, sponsored FFI, or nonreporting IGA FFI covered in Part XII)  - 6: Sponsored FFI that has not obtained a GIIN  - 7: Certified deemed-compliant nonregistering local bank  - 8: Certified deemed-compliant FFI with only low-value accounts  - 9: Certified deemed-compliant sponsored, closely held investment vehicle  - 10: Certified deemed-compliant limited life debt investment entity  - 11: Certified deemed-compliant investment advisors and investment managers  - 12: Owner-documented FFI  - 13: Restricted distributor  - 14: Nonreporting IGA FFI  - 15: Foreign government, government of a U.S. possession, or foreign central bank of issue  - 16: International organization  - 17: Exempt retirement plans  - 18: Entity wholly owned by exempt beneficial owners  - 19: Territory financial institution  - 20: Nonfinancial group entity  - 21: Excepted nonfinancial start-up company  - 22: Excepted nonfinancial entity in liquidation or bankruptcy  - 23: 501(c) organization  - 24: Nonprofit organization  - 25: Publicly traded NFFE or NFFE affiliate of a publicly traded corporation  - 26: Excepted territory NFFE  - 27: Active NFFE  - 28: Passive NFFE  - 29: Excepted inter-affiliate FFI  - 30: Direct reporting NFFE  - 31: Sponsored direct reporting NFFE  - 32: Account that is not a financial account | 
**residence_address** | **str** | The residential address of the individual or entity. | [optional] 
**residence_city** | **str** | The city of residence. | [optional] 
**residence_state** | **str** | The state of residence. | [optional] 
**residence_zip** | **str** | The ZIP code of the residence. | [optional] 
**residence_country** | **str** | The country of residence. | 
**residence_is_mailing** | **bool** | Indicates whether the residence address is the mailing address. | [optional] 
**mailing_address** | **str** | The mailing address. | [optional] 
**mailing_city** | **str** | The city of the mailing address. | [optional] 
**mailing_state** | **str** | The state of the mailing address. | [optional] 
**mailing_zip** | **str** | The ZIP code of the mailing address. | [optional] 
**mailing_country** | **str** | The country of the mailing address. | 
**giin** | **str** | The global intermediary identification number (GIIN). | [optional] 
**foreign_tin** | **str** | The foreign taxpayer identification number (TIN). | [optional] 
**reference_number** | **str** | A reference number for the form. | [optional] 
**disregarded_entity_fatca_status** | **str** | The FATCA status of disregarded entity or branch receiving payment.  Available values:  - 1: Limited Branch  - 2: U.S. Branch  - 3: Participating FFI  - 4: Reporting Model 1 FFI  - 5: Reporting Model 2 FFI | [optional] 
**disregarded_address** | **str** | The address for disregarded entities. | [optional] 
**disregarded_city** | **str** | The city for disregarded entities. | [optional] 
**disregarded_state** | **str** | The state for disregarded entities. | [optional] 
**disregarded_zip** | **str** | The ZIP code for disregarded entities. | [optional] 
**disregarded_country** | **str** | The country for disregarded entities. | [optional] 
**disregarded_entity_giin** | **str** | The GIIN for disregarded entities. | [optional] 
**qualified_intermediary_certification** | **bool** | Certifies that the entity is a Qualified Intermediary (QI) acting in accordance with its QI Agreement,  providing required withholding statements and documentation for relevant tax withholding purposes. | [optional] 
**qi_primary_withholding_responsibility_certification** | **bool** | Certifies that the Qualified Intermediary assumes primary withholding responsibility  under chapters 3 and 4 for the specified accounts. | [optional] 
**qi_withholding_responsibility_for_ptp_sales_certification** | **bool** | Certifies that the Qualified Intermediary assumes primary withholding and reporting responsibility under section 1446(f)  for amounts realized from sales of interests in publicly traded partnerships. | [optional] 
**qi_nominee_withholding_responsibility_for_ptp_distributions_certification** | **bool** | Certifies that the Qualified Intermediary assumes primary withholding responsibility as a nominee  under Regulations section 1.1446-4(b)(3) for publicly traded partnership distributions. | [optional] 
**qi_securities_lender_substitute_dividend_withholding_certification** | **bool** | Certifies that the Qualified Intermediary is acting as a qualified securities lender and assumes primary withholding  and reporting responsibilities for U.S. source substitute dividend payments. | [optional] 
**qi_withholding_and1099_reporting_responsibility_certification** | **bool** | Certifies that the Qualified Intermediary assumes primary withholding under chapters 3 and 4, and primary Form 1099 reporting  and backup withholding responsibility for U.S. source interest and substitute interest payments. | [optional] 
**qi_form1099_or_fatca_reporting_responsibility_certification** | **bool** | Certifies that the Qualified Intermediary assumes Form 1099 reporting and backup withholding responsibility,  or FATCA reporting responsibility as a participating or registered deemed-compliant FFI,  for accounts held by specified U.S. persons. | [optional] 
**qi_opt_out_of_form1099_reporting_certification** | **bool** | Certifies that the Qualified Intermediary does not assume primary Form 1099 reporting  and backup withholding responsibility for the accounts associated with this form. | [optional] 
**qi_withholding_rate_pool_certification** | **bool** | Certifies that the Qualified Intermediary meets the requirements for allocating payments  to a chapter 4 withholding rate pool of U.S. payees under Regulations section 1.6049-4(c)(4)(iii). | [optional] 
**qi_intermediary_or_flow_through_entity_documentation_certification** | **bool** | Certifies that the Qualified Intermediary has obtained or will obtain documentation confirming the status of any intermediary  or flow-through entity as a participating FFI, registered deemed-compliant FFI,  or QI for U.S. payees in a chapter 4 withholding rate pool. | [optional] 
**qualified_derivatives_dealer_certification** | **bool** | Certifies that the Qualified Derivatives Dealer (QDD) is approved by the IRS and assumes primary withholding  and reporting responsibilities for payments related to potential section 871(m) transactions. | [optional] 
**qdd_corporation** | **bool** | Indicates QDD classification is Corporation. | [optional] 
**qdd_partnership** | **bool** | Indicates QDD classification is Partnership. | [optional] 
**qdd_disregarded_entity** | **bool** | Indicates QDD classification is Disregarded Entity. | [optional] 
**nonqualified_intermediary_certification** | **bool** | Certifies that the entity is not acting as a Qualified Intermediary  and is not acting for its own account for the accounts covered by this form. | [optional] 
**nqi_withholding_statement_transmission_certification** | **bool** | Certifies that the nonqualified intermediary is submitting this form to transmit withholding certificates  and/or other required documentation along with a withholding statement. | [optional] 
**nqi_withholding_rate_pool_compliance_certification** | **bool** | Certifies that the nonqualified intermediary meets the requirements of Regulations section 1.6049-4(c)(4)(iii)  for U.S. payees included in a withholding rate pool, excluding publicly traded partnership distributions. | [optional] 
**nqi_qualified_securities_lender_certification** | **bool** | Certifies that the nonqualified intermediary is acting as a qualified securities lender (not as a QI)  and assumes primary withholding and reporting responsibilities for U.S. source substitute dividend payments. | [optional] 
**nqi_alternative_withholding_statement_verification_certification** | **bool** | Certifies that the nonqualified intermediary has verified, or will verify,  all information on alternative withholding statements for consistency with account data to determine the correct withholding rate,  as required under sections 1441 or 1471. | [optional] 
**territory_financial_institution_certification** | **bool** | Certifies that the entity is a financial institution (other than an investment entity) that is incorporated  or organized under the laws of a possession of the United States. | [optional] 
**tfi_treated_as_us_person_certification** | **bool** | Certifies that the territory financial institution agrees to be treated as a U.S. person  for chapters 3 and 4 purposes concerning reportable amounts and withholdable payments. | [optional] 
**tfi_withholding_statement_transmission_certification** | **bool** | Certifies that the territory financial institution is transmitting withholding certificates or other required documentation  and has provided or will provide a withholding statement for reportable or withholdable payments. | [optional] 
**tfi_treated_as_us_person_for_ptp_sales_certification** | **bool** | Certifies that the territory financial institution agrees to be treated as a U.S. person  under Regulations section 1.1446(f)-4(a)(2)(i)(B) for amounts realized from sales of publicly traded partnership interests. | [optional] 
**tfi_nominee_us_person_for_ptp_distributions_certification** | **bool** | Certifies that the territory financial institution agrees to be treated as a U.S. person  and as a nominee for purposes of publicly traded partnership distributions under the applicable regulations. | [optional] 
**tfi_not_nominee_for_ptp_distributions_certification** | **bool** | Certifies that the territory financial institution is not acting as a nominee for publicly traded partnership distributions  and is providing withholding statements for those distributions. | [optional] 
**us_branch_non_effectively_connected_income_certification** | **bool** | Certifies that the U.S. branch is receiving reportable or withholdable payments  that are not effectively connected income, PTP distributions, or proceeds from PTP sales. | [optional] 
**us_branch_agreement_to_be_treated_as_us_person_certification** | **bool** | Certifies that the U.S. branch of a foreign bank or insurance company agrees to be treated as a U.S. person  for reportable amounts or withholdable payments under the applicable regulations. | [optional] 
**us_branch_withholding_statement_and_compliance_certification** | **bool** | Certifies that the U.S. branch is transmitting required documentation  and withholding statements for reportable or withholdable payments and is applying the appropriate FATCA regulations. | [optional] 
**us_branch_acting_as_us_person_for_ptp_sales_certification** | **bool** | Certifies that the U.S. branch is acting as a U.S. person  for purposes of amounts realized from sales of publicly traded partnership interests under the applicable regulations. | [optional] 
**us_branch_nominee_for_ptp_distributions_certification** | **bool** | Certifies that the U.S. branch is treated as a U.S. person  and as a nominee for publicly traded partnership distributions under the applicable regulations. | [optional] 
**us_branch_not_nominee_for_ptp_distributions_certification** | **bool** | Certifies that the U.S. branch is not acting as a nominee for publicly traded partnership distributions  and is providing the required withholding statements. | [optional] 
**withholding_foreign_partnership_or_trust_certification** | **bool** | Certifies that the entity is a withholding foreign partnership (WP) or a withholding foreign trust (WT)  that is compliant with the terms of its WP or WT agreement. | [optional] 
**nonwithholding_foreign_entity_withholding_statement_certification** | **bool** | Certifies that the entity is a nonwithholding foreign partnership or trust,  providing the form for non-effectively connected payments and transmitting required withholding documentation for chapters 3 and 4. | [optional] 
**foreign_entity_partner_in_lower_tier_partnership_certification** | **bool** | Certifies that the entity is a foreign partnership or grantor trust acting as a partner in a lower-tier partnership  and is submitting the form for purposes of section 1446(a). | [optional] 
**foreign_partnership_amount_realized_section1446_f_certification** | **bool** | Certifies that the entity is a foreign partnership receiving an amount realized  from the transfer of a partnership interest for purposes of section 1446(f). | [optional] 
**foreign_partnership_modified_amount_realized_certification** | **bool** | Certifies that the foreign partnership is providing a withholding statement for a modified amount realized  from the transfer of a partnership interest, when applicable. | [optional] 
**foreign_grantor_trust_amount_realized_allocation_certification** | **bool** | Certifies that the foreign grantor trust is submitting the form on behalf of each grantor or owner  and providing a withholding statement to allocate the amount realized in accordance with the regulations. | [optional] 
**alternative_withholding_statement_reliance_certification** | **bool** | Certifies that the entity may rely on the information in all associated withholding certificates  under the applicable standards of knowledge in sections 1441 or 1471 when providing an alternative withholding statement. | [optional] 
**np_ffi_with_exempt_beneficial_owners_certification** | **bool** | Certifies that the nonparticipating FFI is transmitting withholding documentation  and providing a statement allocating payment portions to exempt beneficial owners. | [optional] 
**ffi_sponsoring_entity** | **str** | The name of the entity that sponsors the foreign financial institution (FFI). | [optional] 
**investment_entity_certification** | **bool** | Certifies that the entity is an investment entity, not a QI, WP, or WT, and has an agreement with a sponsoring entity. | [optional] 
**controlled_foreign_corporation_certification** | **bool** | Certifies that the entity is a controlled foreign corporation sponsored by a U.S. financial institution, not a QI, WP, or WT,  and shares a common electronic account system for full transparency. | [optional] 
**owner_documented_ffi_certification** | **bool** | Certifies that the FFI meets all requirements to qualify as an owner-documented FFI, including restrictions on activities,  ownership, and account relationships. | [optional] 
**owner_documented_ffi_reporting_statement_certification** | **bool** | Certifies that the FFI will provide a complete owner reporting statement  and required documentation for each relevant owner or debt holder. | [optional] 
**owner_documented_ffi_auditor_letter_certification** | **bool** | Certifies that the FFI will provide an auditor’s letter and required owner reporting documentation  to confirm its status as an owner-documented FFI. | [optional] 
**compliant_nonregistering_local_bank_certification** | **bool** | Certifies that the FFI operates solely as a limited bank or credit union within its country, meets asset thresholds,  and has no foreign operations or affiliations outside its country of organization. | [optional] 
**compliant_ffi_low_value_accounts_certification** | **bool** | Certifies that the FFI is not primarily engaged in investment activities, maintains only low-value accounts,  and has limited total assets within its group. | [optional] 
**sponsored_closely_held_entity_sponsoring_entity** | **str** | The name of sponsoring entity for a certified deemed-compliant, closely held investment vehicle. | [optional] 
**sponsored_closely_held_investment_vehicle_certification** | **bool** | Certifies that the entity is a sponsored investment entity with 20 or fewer individual owners,  and that all compliance obligations are fulfilled by the sponsoring entity. | [optional] 
**compliant_limited_life_debt_entity_certification** | **bool** | Certifies that the entity qualifies as a limited life debt investment entity based on its formation date, issuance terms,  and compliance with regulatory requirements. | [optional] 
**investment_entity_no_financial_accounts_certification** | **bool** | Certifies that the entity is a financial institution solely because it is an investment entity under regulations  and the entity does not maintain financial accounts. | [optional] 
**restricted_distributor_certification** | **bool** | Certifies that the entity qualifies as a restricted distributor based on its operations, customer base, regulatory compliance,  and financial and geographic limitations. | [optional] 
**restricted_distributor_agreement_certification** | **bool** | Certifies that the entity is, and has been, bound by distribution agreements prohibiting sales of fund interests to  specified U.S. persons and certain non-U.S. entities. | [optional] 
**restricted_distributor_preexisting_sales_compliance_certification** | **bool** | Certifies that the entity complies with distribution restrictions for U.S.-linked investors  and has addressed any preexisting sales in accordance with FATCA regulations. | [optional] 
**foreign_central_bank_of_issue_certification** | **bool** | Certifies that the entity is treated as the beneficial owner of the payment solely  for purposes of chapter 4 under Regulations section 1.1471-6(d)(4). | [optional] 
**nonreporting_iga_ffi_certification** | **bool** | Certifies that the entity meets the requirements to be considered a nonreporting financial institution to an applicable IGA. | [optional] 
**iga_country** | **str** | The country for the applicable IGA with the United States. | [optional] 
**iga_model** | **str** | The applicable IGA model.  Available values:  - 1: Model 1 IGA  - 2: Model 2 IGA | [optional] 
**iga_legal_status_treatment** | **str** | Specifies how the applicable IGA is treated under the IGA provisions or Treasury regulations. | [optional] 
**iga_ffi_trustee_or_sponsor** | **str** | The trustee or sponsor name for the nonreporting IGA FFI. | [optional] 
**iga_ffi_trustee_is_foreign** | **bool** | Indicates whether the trustee for the nonreporting IGA FFI is foreign. | [optional] 
**treaty_qualified_pension_fund_certification** | **bool** | Certifies that the entity is a pension or retirement fund established in a treaty country  and is entitled to treaty benefits on U.S. source income. | [optional] 
**qualified_retirement_fund_certification** | **bool** | Certifies that the entity is a government-regulated retirement fund meeting specific requirements for contributions, tax exemption,  beneficiary limits, and distribution restrictions. | [optional] 
**narrow_participation_retirement_fund_certification** | **bool** | Certifies that the entity is a government-regulated retirement fund with fewer than 50 participants, limited foreign ownership,  and employer sponsorship that is not from investment entities or passive NFFEs. | [optional] 
**section401_a_equivalent_pension_plan_certification** | **bool** | Certifies that the entity is formed under a pension plan meeting section 401(a) requirements, except for being U.S.-trust funded. | [optional] 
**investment_entity_for_retirement_funds_certification** | **bool** | Certifies that the entity is established solely to earn income for the benefit of qualifying retirement funds  or accounts under applicable FATCA regulations or IGAs. | [optional] 
**exempt_beneficial_owner_sponsored_retirement_fund_certification** | **bool** | Certifies that the entity is established and sponsored by a qualifying exempt beneficial owner to provide retirement, disability,  or death benefits to individuals based on services performed for the sponsor. | [optional] 
**excepted_nonfinancial_group_entity_certification** | **bool** | Certifies that the entity is a holding company, treasury center, or captive finance company operating within a nonfinancial group  and not functioning as an investment or financial institution. | [optional] 
**excepted_nonfinancial_start_up_certification** | **bool** | Certifies that the entity is a recently formed startup NFFE investing in a non-financial business  and is not operating as or presenting itself as an investment fund. | [optional] 
**startup_formation_or_resolution_date** | **date** | The date the start-up company was formed on (or, in case of new line of business, the date of board resolution approving the  new line of business). | [optional] 
**excepted_nonfinancial_entity_in_liquidation_or_bankruptcy_certification** | **bool** | Certifies that the entity is in liquidation, reorganization, or bankruptcy and intends to operate as a nonfinancial entity,  with supporting documentation available if the process exceeds three years. | [optional] 
**nonfinancial_entity_filing_date** | **date** | The filed date for a plan of reorganization, liquidation or bankruptcy. | [optional] 
**publicly_traded_nffe_certification** | **bool** | Certifies that the entity is a foreign corporation that is not a financial institution  and whose stock is regularly traded on an established securities market. | [optional] 
**publicly_traded_nffe_securities_market** | **str** | The name of the securities market where the corporation&#39;s stock is regularly traded. | [optional] 
**nffe_affiliate_of_publicly_traded_entity_certification** | **bool** | Certifies that the entity is a foreign corporation that is not a financial institution  and is affiliated with a publicly traded entity within the same expanded affiliated group. | [optional] 
**publicly_traded_entity** | **str** | The name of the affiliated entity whose stock is regularly traded on an established securities market. | [optional] 
**nffe_affiliate_of_publicly_traded_entity_securities_market** | **str** | The name of the established securities market where the affiliated entity&#39;s stock is traded. | [optional] 
**excepted_territory_nffe_certification** | **bool** | Certifies that the entity is organized in a U.S. possession, is not engaged in financial activities,  and is entirely owned by bona fide residents of that possession. | [optional] 
**active_nffe_certification** | **bool** | Certifies that the entity is a foreign non-financial institution with less than 50% passive income  and less than 50% of its assets producing or held to produce passive income. | [optional] 
**passive_nffe_certification** | **bool** | Certifies that the entity is a foreign non-financial entity that does not qualify for any other NFFE category  and is not a financial institution. | [optional] 
**sponsored_direct_reporting_nffe_certification** | **bool** | Certifies that the entity is a sponsored direct reporting NFFE. | [optional] 
**direct_reporting_nffe_sponsoring_entity** | **str** | The name of the entity that sponsors the direct reporting NFFE. | [optional] 
**signer_name** | **str** | The name of the signer of the form. | [optional] 
**making_treaty_claim** | **bool** | Indicates whether the entity is making a treaty claim. | [optional] 
**foreign_tin_not_required** | **bool** | Indicates whether a foreign TIN is not legally required. | [optional] 
**treaty_country_certification** | **bool** | Certifies the beneficial owner&#39;s country under the U.S. tax treaty. | [optional] 
**treaty_country** | **str** | The country for which the treaty applies. | [optional] 
**benefit_limitation_certification** | **bool** | Certifies that the beneficial owner is eligible for treaty benefits and meets any limitation on benefits requirements. | [optional] 
**benefit_limitation** | **str** | The benefit limitation for tax treaty claims.  Available values:  - 1: Government  - 2: Tax exempt pension trust or pension fund  - 3: Other tax exempt organization  - 4: Publicly traded corporation  - 5: Subsidiary of a publicly traded corporation  - 6: Company that meets the ownership and base erosion test  - 7: Company that meets the derivative benefits test  - 8: Company with an item of income that meets active trade or business test  - 9: Favorable discretionary determination by the U.S. competent authority received  - 10: Other | [optional] 
**qualified_resident_status_certification** | **bool** | Certifies that the beneficial owner claims treaty benefits and meets the qualified resident status for specific U.S. source income. | [optional] 
**treaty_article** | **str** | The specific article of the treaty being claimed. | [optional] 
**withholding_rate** | **str** | The withholding rate applied as per the treaty. | [optional] 
**income_type** | **str** | The type of income covered by the treaty. | [optional] 
**treaty_reasons** | **str** | The reasons for claiming treaty benefits. | [optional] 
**owner_documented_ffi_trust_beneficiaries_certification** | **bool** | Certifies that the trust has no contingent or unidentified beneficiaries or designated classes of beneficiaries. | [optional] 
**non_commercial_financial_activity_certification** | **bool** | Certifies that the entity is the beneficial owner and is not engaged in commercial financial activities related  to the specified payments, accounts or obligations for which this form is submitted. | [optional] 
**internation_organization_certification** | **bool** | Certifies that the entity is an international organization described in section 7701(a)(18). | [optional] 
**intergovernmental_organization_certification** | **bool** | Certifies that the entity is an intergovernmental or supranational organization primarily comprised of foreign governments,  is the beneficial owner, and is not engaged in commercial financial activities. | [optional] 
**exempt_beneficial_owner_owned_investment_entity_certification** | **bool** | Certifies that the entity is an investment entity wholly owned by exempt beneficial owners and has provided complete ownership  and documentation details as required under FATCA regulations. | [optional] 
**section501_c_organization_certification** | **bool** | Certifies that the entity is a section 501(c) organization based on a valid IRS determination letter  or a legal opinion from U.S. counsel. | [optional] 
**determination_letter_date** | **date** | The date of the IRS determination letter confirming the entity’s section 501(c) status. | [optional] 
**nonprofit_organization_certification** | **bool** | Certifies that the entity is a nonprofit organization established for charitable or similar purposes, exempt from income tax,  and restricted in the use and distribution of its assets under applicable law. | [optional] 
**passive_nffe_no_substantial_us_owners_certification** | **bool** | Certifies that the passive NFFE has no substantial U.S. owners or controlling U.S. persons. | [optional] 
**passive_nffe_substantial_us_owners_provided_certification** | **bool** | Certifies that the passive NFFE has provided the name, address, and TIN of each substantial U.S. owner or controlling U.S. person. | [optional] 
**excepted_inter_affiliate_ffi_certification** | **bool** | Certifies that the entity is an inter-affiliate FFI meeting all conditions for exemption,  including limited account activity and payment interactions within its expanded affiliated group. | [optional] 
**substantial_us_owners** | [**List[SubstantialUsOwnerRequest]**](SubstantialUsOwnerRequest.md) | The list of substantial U.S. owners of passive NFFE. | [optional] 
**capacity_to_sign_certification** | **bool** | Certifies signer has the capacity to sign for the beneficial owner. | [optional] 
**birthday** | **date** | The birthday of the individual associated with the form. | [optional] 
**employee_first_name** | **str** | The first name of the employee. | 
**employee_middle_name** | **str** | The middle name of the employee. | [optional] 
**employee_last_name** | **str** | The last name of the employee. | 
**employee_name_suffix** | **str** | The name suffix of the employee. | [optional] 
**marital_status** | **str** | The marital status of the employee. Required unless exempt.  Available values:  - Single: Single or Married filing separately  - Married: Married filing jointly or qualifying surviving spouse  - MarriedBut: Head of household. Check only if you&#39;re unmarried and pay more than half the costs of keeping up a home for yourself and a qualifying individual. | [optional] 
**last_name_differs** | **bool** | Indicates whether the last name differs from prior records. | [optional] 
**num_allowances** | **int** | The number of allowances claimed by the employee. | [optional] 
**other_dependents** | **int** | The number of dependents other than allowances. | [optional] 
**non_job_income** | **float** | The amount of non-job income. | [optional] 
**deductions** | **float** | The amount of deductions claimed. | [optional] 
**additional_withheld** | **float** | The additional amount withheld. | [optional] 
**exempt_from_withholding** | **bool** | Indicates whether the employee is exempt from withholding. | [optional] 
**office_code** | **str** | The office code associated with the form. | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.create_w9_form_request import CreateW9FormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateW9FormRequest from a JSON string
create_w9_form_request_instance = CreateW9FormRequest.from_json(json)
# print the JSON string representation of the object
print(CreateW9FormRequest.to_json())

# convert the object into a dict
create_w9_form_request_dict = create_w9_form_request_instance.to_dict()
# create an instance of CreateW9FormRequest from a dict
create_w9_form_request_from_dict = CreateW9FormRequest.from_dict(create_w9_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


