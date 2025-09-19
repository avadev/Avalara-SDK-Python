# Get1099Form200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tin_type** | **str** | Tax Identification Number (TIN) type.  Available values: - EIN: Employer Identification Number - SSN: Social Security Number - ITIN: Individual Taxpayer Identification Number - ATIN: Adoption Taxpayer Identification Number | [optional] 
**unique_form_id** | **str** | Unique form identifier | 
**recipient_date_of_birth** | **date** | Recipient&#39;s date of birth | [optional] 
**recipient_giin** | **str** | Recipient&#39;s Global Intermediary Identification Number (GIIN). A valid GIIN looks like &#39;XXXXXX.XXXXX.XX.XXX&#39;. | [optional] 
**recipient_foreign_tin** | **str** | Recipient&#39;s foreign TIN. Required if email is specified, must fill either this or Chap3StatusCode. | [optional] 
**lob_code** | **str** | Limitation on Benefits (LOB) code for tax treaty purposes.  Available values:  - 01: Individual (Deprecated - valid only for tax years prior to 2019)  - 02: Government - contracting state/political subdivision/local authority  - 03: Tax exempt pension trust/Pension fund  - 04: Tax exempt/Charitable organization  - 05: Publicly-traded corporation  - 06: Subsidiary of publicly-traded corporation  - 07: Company that meets the ownership and base erosion test  - 08: Company that meets the derivative benefits test  - 09: Company with an item of income that meets the active trade or business test  - 10: Discretionary determination  - 11: Other  - 12: No LOB article in treaty | [optional] 
**income_code** | **str** | Income code.  Available values:    Interest:  - 01: Interest paid by US obligors - general  - 02: Interest paid on real property mortgages  - 03: Interest paid to controlling foreign corporations  - 04: Interest paid by foreign corporations  - 05: Interest on tax-free covenant bonds  - 22: Interest paid on deposit with a foreign branch of a domestic corporation or partnership  - 29: Deposit interest  - 30: Original issue discount (OID)  - 31: Short-term OID  - 33: Substitute payment - interest  - 51: Interest paid on certain actively traded or publicly offered securities(1)  - 54: Substitute payments - interest from certain actively traded or publicly offered securities(1)    Dividend:  - 06: Dividends paid by U.S. corporations - general  - 07: Dividends qualifying for direct dividend rate  - 08: Dividends paid by foreign corporations  - 34: Substitute payment - dividends  - 40: Other dividend equivalents under IRC section 871(m) (formerly 871(l))  - 52: Dividends paid on certain actively traded or publicly offered securities(1)  - 53: Substitute payments - dividends from certain actively traded or publicly offered securities(1)  - 56: Dividend equivalents under IRC section 871(m) as a result of applying the combined transaction rules    Other:  - 09: Capital gains  - 10: Industrial royalties  - 11: Motion picture or television copyright royalties  - 12: Other royalties (for example, copyright, software, broadcasting, endorsement payments)  - 13: Royalties paid on certain publicly offered securities(1)  - 14: Real property income and natural resources royalties  - 15: Pensions, annuities, alimony, and/or insurance premiums  - 16: Scholarship or fellowship grants  - 17: Compensation for independent personal services(2)  - 18: Compensation for dependent personal services(2)  - 19: Compensation for teaching(2)  - 20: Compensation during studying and training(2)  - 23: Other income  - 24: Qualified investment entity (QIE) distributions of capital gains  - 25: Trust distributions subject to IRC section 1445  - 26: Unsevered growing crops and timber distributions by a trust subject to IRC section 1445  - 27: Publicly traded partnership distributions subject to IRC section 1446  - 28: Gambling winnings(3)  - 32: Notional principal contract income(4)  - 35: Substitute payment - other  - 36: Capital gains distributions  - 37: Return of capital  - 38: Eligible deferred compensation items subject to IRC section 877A(d)(1)  - 39: Distributions from a nongrantor trust subject to IRC section 877A(f)(1)  - 41: Guarantee of indebtedness  - 42: Earnings as an artist or athlete - no central withholding agreement(5)  - 43: Earnings as an artist or athlete - central withholding agreement(5)  - 44: Specified Federal procurement payments  - 50: Income previously reported under escrow procedure(6)  - 55: Taxable death benefits on life insurance contracts  - 57: Amount realized under IRC section 1446(f)  - 58: Publicly traded partnership distributions-undetermined | 
**gross_income** | **float** | Gross income | 
**withholding_indicator** | **str** | Withholding indicator  Available values:  - 3: Chapter 3  - 4: Chapter 4 | 
**tax_country_code** | **str** | Country code | 
**exemption_code_chap3** | **str** | Exemption code (Chapter 3). Required if WithholdingIndicator is 3 (Chapter 3). Required when using TaxRateChap3.  Available values:  - Empty: Tax rate is due to backup withholding  - 00: Not exempt  - 01: Effectively connected income  - 02: Exempt under IRC (other than portfolio interest)  - 03: Income is not from US sources  - 04: Exempt under tax treaty  - 05: Portfolio interest exempt under IRC  - 06: QI that assumes primary withholding responsibility  - 07: WFP or WFT  - 08: U.S. branch treated as U.S. Person  - 09: Territory FI treated as U.S. Person  - 10: QI represents that income is exempt  - 11: QSL that assumes primary withholding responsibility  - 12: Payee subjected to chapter 4 withholding  - 22: QDD that assumes primary withholding responsibility  - 23: Exempt under section 897(l)  - 24: Exempt under section 892 | [optional] 
**exemption_code_chap4** | **str** | Exemption code (Chapter 4). Required if WithholdingIndicator is 4 (Chapter 4).  Available values:  - 00: Not exempt  - 13: Grandfathered payment  - 14: Effectively connected income  - 15: Payee not subject to chapter 4 withholding  - 16: Excluded nonfinancial payment  - 17: Foreign Entity that assumes primary withholding responsibility  - 18: U.S. Payees - of participating FFI or registered deemed - compliant FFI  - 19: Exempt from withholding under IGA(6)  - 20: Dormant account(7)  - 21: Other - payment not subject to chapter 4 withholding | [optional] 
**tax_rate_chap3** | **str** | Tax rate (Chapter 3) - Required if WithholdingIndicator is 3 (Chapter 3).  Available values:  - 00.00: 0.00%  - 02.00: 2.00%  - 04.00: 4.00%  - 04.90: 4.90%  - 04.95: 4.95%  - 05.00: 5.00%  - 07.00: 7.00%  - 08.00: 8.00%  - 10.00: 10.00%  - 12.00: 12.00%  - 12.50: 12.50%  - 14.00: 14.00%  - 15.00: 15.00%  - 17.50: 17.50%  - 20.00: 20.00%  - 21.00: 21.00%  - 24.00: 24.00%  - 25.00: 25.00%  - 27.50: 27.50%  - 28.00: 28.00%  - 30.00: 30.00%  - 37.00: 37.00% | [optional] 
**withholding_allowance** | **float** | Withholding allowance | [optional] 
**federal_tax_withheld** | **float** | Federal tax withheld | [optional] 
**tax_not_deposited_indicator** | **bool** | Tax not deposited indicator | [optional] 
**academic_indicator** | **bool** | Academic indicator | [optional] 
**tax_withheld_other_agents** | **float** | Tax withheld by other agents | [optional] 
**amount_repaid** | **float** | Amount repaid to recipient | [optional] 
**tax_paid_agent** | **float** | Tax paid by withholding agent | [optional] 
**chap3_status_code** | **str** | Chapter 3 status code - Required if WithholdingIndicator is 3 (Chapter 3). Available values: - 01: U.S. Withholding Agent - FI (Deprecated - valid only for tax years prior to 2020) - 02: U.S. Withholding Agent - Other (Deprecated - valid only for tax years prior to 2020) - 03: Territory FI - treated as U.S. Person - 04: Territory FI - not treated as U.S. Person - 05: U.S. branch - treated as U.S. Person - 06: U.S. branch - not treated as U.S. Person - 07: U.S. branch - ECI presumption applied - 08: Partnership other than Withholding Foreign Partnership - 09: Withholding Foreign Partnership - 10: Trust other than Withholding Foreign Trust - 11: Withholding Foreign Trust - 12: Qualified Intermediary - 13: Qualified Securities Lender - Qualified Intermediary - 14: Qualified Securities Lender - Other - 15: Corporation - 16: Individual - 17: Estate - 18: Private Foundation - 19: Government or International Organization - 20: Tax Exempt Organization (Section 501(c) entities) - 21: Unknown Recipient - 22: Artist or Athlete - 23: Pension - 24: Foreign Central Bank of Issue - 25: Nonqualified Intermediary - 26: Hybrid entity making Treaty Claim - 27: Withholding Rate Pool - General - 28: Withholding Rate Pool - Exempt Organization - 29: PAI Withholding Rate Pool - General - 30: PAI Withholding Rate Pool - Exempt Organization - 31: Agency Withholding Rate Pool - General - 32: Agency Withholding Rate Pool - Exempt Organization - 34: U.S. Withholding Agent-Foreign branch of FI (Deprecated - valid only for tax years prior to 2020) - 35: Qualified Derivatives Dealer - 36: Foreign Government - Integral Part - 37: Foreign Government - Controlled Entity - 38: Publicly Traded Partnership - 39: Disclosing Qualified Intermediary | [optional] 
**chap4_status_code** | **str** | Chapter 4 status code. Required if WithholdingIndicator is 4 (Chapter 4). Required if email is specified, must fill either this or RecipientForeignTin. Available values: - 01: U.S. Withholding Agent - FI - 02: U.S. Withholding Agent - Other - 03: Territory FI - not treated as U.S. Person - 04: Territory FI - treated as U.S. Person - 05: Participating FFI - Other - 06: Participating FFI - Reporting Model 2 FFI - 07: Registered Deemed - Compliant FFI-Reporting Model 1 FFI - 08: Registered Deemed - Compliant FFI-Sponsored Entity - 09: Registered Deemed - Compliant FFI-Other - 10: Certified Deemed - Compliant FFI-Other - 11: Certified Deemed - Compliant FFI-FFI with Low Value Accounts - 12: Certified Deemed - Compliant FFI-Non-Registering Local Bank - 13: Certified Deemed - Compliant FFI-Sponsored Entity - 14: Certified Deemed - Compliant FFI-Investment Advisor or Investment Manager - 15: Nonparticipating FFI - 16: Owner-Documented FFI - 17: U.S. Branch - treated as U.S. person - 18: U.S. Branch - not treated as U.S. person (reporting under section 1471) - 19: Passive NFFE identifying Substantial U.S. Owners - 20: Passive NFFE with no Substantial U.S. Owners - 21: Publicly Traded NFFE or Affiliate of Publicly Traded NFFE - 22: Active NFFE - 23: Individual - 24: Section 501(c) Entities - 25: Excepted Territory NFFE - 26: Excepted NFFE - Other - 27: Exempt Beneficial Owner - 28: Entity Wholly Owned by Exempt Beneficial Owners - 29: Unknown Recipient - 30: Recalcitrant Account Holder - 31: Nonreporting IGA FFI - 32: Direct reporting NFFE - 33: U.S. reportable account - 34: Non-consenting U.S. account - 35: Sponsored direct reporting NFFE - 36: Excepted Inter-affiliate FFI - 37: Undocumented Preexisting Obligation - 38: U.S. Branch - ECI presumption applied - 39: Account Holder of Excluded Financial Account - 40: Passive NFFE reported by FFI - 41: NFFE subject to 1472 withholding - 42: Recalcitrant Pool - No U.S. Indicia - 43: Recalcitrant Pool - U.S. Indicia - 44: Recalcitrant Pool - Dormant Account - 45: Recalcitrant Pool - U.S. Persons - 46: Recalcitrant Pool - Passive NFFEs - 47: Nonparticipating FFI Pool - 48: U.S. Payees Pool - 49: QI - Recalcitrant Pool-General - 50: U.S. Withholding Agent-Foreign branch of FI | [optional] 
**primary_withholding_agent** | [**PrimaryWithholdingAgent**](PrimaryWithholdingAgent.md) | Primary withholding agent information | [optional] 
**intermediary_or_flow_through** | [**IntermediaryOrFlowThrough**](IntermediaryOrFlowThrough.md) | Intermediary or flow-through entity information | [optional] 
**type** | **str** | Form type. | 
**id** | **str** | Form ID. Unique identifier set when the record is created. | [optional] [readonly] 
**issuer_id** | **str** | Issuer ID - only required when creating forms | [optional] 
**issuer_reference_id** | **str** | Issuer Reference ID - only required when creating forms via $bulk-upsert | [optional] 
**issuer_tin** | **str** | Issuer TIN - readonly | [optional] 
**tax_year** | **int** | Tax Year - only required when creating forms via $bulk-upsert | [optional] 
**reference_id** | **str** | Internal reference ID. Never shown to any agency or recipient. | [optional] 
**tin** | **str** | Recipient&#39;s Federal Tax Identification Number (TIN). | [optional] 
**recipient_name** | **str** | Recipient name | 
**recipient_second_name** | **str** | Recipient second name | [optional] 
**address** | **str** | Address. | 
**address2** | **str** | Address line 2. | [optional] 
**city** | **str** | City. | 
**state** | **str** | Two-letter US state or Canadian province code (required for US/CA addresses). | [optional] 
**zip** | **str** | ZIP/postal code. | [optional] 
**email** | **str** | Recipient&#39;s Contact email address. | [optional] 
**account_number** | **str** | Account number | [optional] 
**office_code** | **str** | Office code | [optional] 
**non_us_province** | **str** | Province or region for non-US/CA addresses. | [optional] 
**country_code** | **str** | Two-letter IRS country code (e.g., &#39;US&#39;, &#39;CA&#39;), as defined at https://www.irs.gov/e-file-providers/country-codes. | 
**federal_efile_date** | **date** | Date when federal e-filing should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**postal_mail** | **bool** | Boolean indicating that postal mailing to the recipient should be scheduled for this form | [optional] 
**state_efile_date** | **date** | Date when state e-filing should be scheduled. Must be on or after federalEfileDate. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**recipient_edelivery_date** | **date** | Date when recipient e-delivery should be scheduled. If set between current date and beginning of blackout period, scheduled to that date. If in the past or blackout period, scheduled to next available date. For blackout period information, see https://www.track1099.com/info/IRS_info. Set to null to leave unscheduled. | [optional] 
**tin_match** | **bool** | Boolean indicating that TIN Matching should be scheduled for this form | [optional] 
**no_tin** | **bool** | No TIN indicator | [optional] 
**address_verification** | **bool** | Boolean indicating that address verification should be scheduled for this form | [optional] 
**state_and_local_withholding** | [**StateAndLocalWithholding**](StateAndLocalWithholding.md) | State and local withholding information | [optional] 
**second_tin_notice** | **bool** | Second TIN notice | [optional] 
**federal_efile_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Federal e-file status.  Available values:  - unscheduled: Form has not been scheduled for federal e-filing  - scheduled: Form is scheduled for federal e-filing  - airlock: Form is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - sent: Form has been sent to the IRS  - accepted: Form was accepted by the IRS  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlock: Correction is in process of being uploaded to the IRS (forms exist in this state for a very short period and cannot be updated while in this state)  - corrected: A correction has been sent to the IRS  - corrected_accepted: Correction was accepted by the IRS  - rejected: Form was rejected by the IRS  - corrected_rejected: Correction was rejected by the IRS  - held: Form is held and will not be submitted to IRS (used for certain forms submitted only to states) | [optional] [readonly] 
**state_efile_status** | [**List[StateEfileStatusDetail]**](StateEfileStatusDetail.md) | State e-file status.  Available values:  - unscheduled: Form has not been scheduled for state e-filing  - scheduled: Form is scheduled for state e-filing  - airlocked: Form is in process of being uploaded to the state  - sent: Form has been sent to the state  - rejected: Form was rejected by the state  - accepted: Form was accepted by the state  - corrected_scheduled: Correction is scheduled to be sent  - corrected_airlocked: Correction is in process of being uploaded to the state  - corrected_sent: Correction has been sent to the state  - corrected_rejected: Correction was rejected by the state  - corrected_accepted: Correction was accepted by the state | [optional] [readonly] 
**postal_mail_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Postal mail to recipient status.  Available values:  - unscheduled: Postal mail has not been scheduled  - pending: Postal mail is pending to be sent  - sent: Postal mail has been sent  - delivered: Postal mail has been delivered | [optional] [readonly] 
**tin_match_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | TIN Match status.  Available values:  - none: TIN matching has not been performed  - pending: TIN matching request is pending  - matched: Name/TIN combination matches IRS records  - unknown: TIN is missing, invalid, or request contains errors  - rejected: Name/TIN combination does not match IRS records or TIN not currently issued | [optional] [readonly] 
**address_verification_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | Address verification status.  Available values:  - unknown: Address verification has not been checked  - pending: Address verification is in progress  - failed: Address verification failed  - incomplete: Address verification is incomplete  - unchanged: User declined address changes  - verified: Address has been verified and accepted | [optional] [readonly] 
**e_delivery_status** | [**Form1099StatusDetail**](Form1099StatusDetail.md) | EDelivery status.  Available values:  - unscheduled: E-delivery has not been scheduled  - scheduled: E-delivery is scheduled to be sent  - sent: E-delivery has been sent to recipient  - bounced: E-delivery bounced back (invalid email)  - refused: E-delivery was refused by recipient  - bad_verify: E-delivery failed verification  - accepted: E-delivery was accepted by recipient  - bad_verify_limit: E-delivery failed verification limit reached  - second_delivery: Second e-delivery attempt  - undelivered: E-delivery is undelivered (temporary state allowing resend) | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Validation errors | [optional] [readonly] 
**created_at** | **datetime** | Date time when the record was created. | [optional] [readonly] 
**updated_at** | **datetime** | Date time when the record was last updated. | [optional] [readonly] 
**employee_first_name** | **str** | Employee&#39;s first name | 
**employee_middle_name** | **str** | Employee&#39;s middle name | [optional] 
**employee_last_name** | **str** | Employee&#39;s last name | 
**employee_name_suffix** | **str** | Employee&#39;s name suffix | [optional] 
**employee_date_of_birth** | **date** | Employee&#39;s date of birth | [optional] 
**origin_of_health_coverage_code** | **str** | Origin of health coverage code.    Available values:  - A: Small Business Health Options Program (SHOP)  - B: Employer-sponsored coverage  - C: Government-sponsored program  - D: Individual market insurance  - E: Multiemployer plan  - F: Other designated minimum essential coverage  - G: Employer-sponsored coverage that is an individual coverage HRA (valid for tax years 2020 and later) | 
**covered_individuals** | [**List[CoveredIndividual]**](CoveredIndividual.md) | Covered individuals information | [optional] 
**plan_start_month** | **str** | Plan start month.  The calendar month during which the plan year begins of the health plan in which the employee is offered coverage (or would be offered coverage if the employee were eligible to participate in the plan).  Available values:  - 00: None  - 01: January  - 02: February  - 03: March  - 04: April  - 05: May  - 06: June  - 07: July  - 08: August  - 09: September  - 10: October  - 11: November  - 12: December | 
**employer_provided_si_coverage** | **bool** | Employer provided self-insured coverage | [optional] 
**offer_and_coverages** | [**List[OfferAndCoverage]**](OfferAndCoverage.md) | Offer and coverage information | 
**total_ordinary_dividends** | **float** | Total ordinary dividends | [optional] 
**qualified_dividends** | **float** | Qualified dividends | [optional] 
**total_capital_gain_distributions** | **float** | Total capital gain distributions | [optional] 
**unrecaptured_section1250_gain** | **float** | Unrecaptured Section 1250 gain | [optional] 
**section1202_gain** | **float** | Section 1202 gain | [optional] 
**collectibles_gain** | **float** | Collectibles (28%) gain | [optional] 
**section897_ordinary_dividends** | **float** | Section 897 ordinary dividends | [optional] 
**section897_capital_gain** | **float** | Section 897 capital gain | [optional] 
**nondividend_distributions** | **float** | Nondividend distributions | [optional] 
**federal_income_tax_withheld** | **float** | Federal income tax withheld | [optional] 
**section199_a_dividends** | **float** | Section 199A dividends | [optional] 
**investment_expenses** | **float** | Investment Expenses | [optional] 
**foreign_tax_paid** | **float** | Foreign tax paid | [optional] 
**foreign_country_or_us_possession** | **str** | Foreign country or U.S. possession | [optional] 
**cash_liquidation_distributions** | **float** | Cash liquidation distributions | [optional] 
**noncash_liquidation_distributions** | **float** | Noncash liquidation distributions | [optional] 
**exempt_interest_dividends** | **float** | Exempt-interest dividends | [optional] 
**specified_private_activity_bond_interest_dividends** | **float** | Specified private activity bond interest dividends | [optional] 
**fatca_filing_requirement** | **bool** | FATCA filing requirement. | [optional] 
**interest_income** | **float** | Interest Income | [optional] 
**early_withdrawal_penalty** | **float** | Early Withdrawal Penalty | [optional] 
**us_savings_bonds_interest** | **float** | Interest on U.S. Savings Bonds and Treasury obligations | [optional] 
**foreign_country** | **str** | Foreign country or U.S. possession | [optional] 
**tax_exempt_interest** | **float** | Tax-Exempt Interest | [optional] 
**specified_private_activity_bond_interest** | **float** | Specified Private activity | [optional] 
**market_discount** | **float** | Market Discount | [optional] 
**bond_premium** | **float** | Bond Premium | [optional] 
**bond_premium_on_treasury_obligations** | **float** | Bond Premium on Treasury obligations | [optional] 
**bond_premium_on_tax_exempt_bond** | **float** | Bond Premium on tax exempt bond | [optional] 
**tax_exempt_bond_cusip_number** | **str** | Tax exempt bond CUSIP no.   Enter VARIOUS if the tax-exempt interest is reported in the aggregate for multiple bonds or accounts. | [optional] 
**filer_type** | **str** | Filer type for tax reporting purposes.  Available values:  - PSE: Payment Settlement Entity  - EPF: Electronic Payment Facilitator or other third party | 
**payment_type** | **str** | Payment type for transaction classification.  Available values:  - PaymentCard: Payment card transactions  - ThirdPartyNetwork: Third party network transactions | 
**payment_settlement_entity_name_phone_number** | **str** | Payment settlement entity name and phone number, if different from Filer&#39;s | [optional] 
**gross_amount_payment_card** | **float** | Gross amount of payment card/third party network transactions. This value must equal the total of all monthly payment amounts (January through December). | 
**card_not_present_transactions** | **float** | Card not present transactions | [optional] 
**merchant_category_code** | **str** | Merchant category code (4 numbers) | [optional] 
**payment_transaction_number** | **float** | Number of payment transactions | 
**january** | **float** | January gross payments | [optional] 
**february** | **float** | February gross payments | [optional] 
**march** | **float** | March gross payments | [optional] 
**april** | **float** | April gross payments | [optional] 
**may** | **float** | May gross payments | [optional] 
**june** | **float** | June gross payments | [optional] 
**july** | **float** | July gross payments | [optional] 
**august** | **float** | August gross payments | [optional] 
**september** | **float** | September gross payments | [optional] 
**october** | **float** | October gross payments | [optional] 
**november** | **float** | November gross payments | [optional] 
**december** | **float** | December gross payments | [optional] 
**rents** | **float** | Rents | [optional] 
**royalties** | **float** | Royalties | [optional] 
**other_income** | **float** | Other income | [optional] 
**fishing_boat_proceeds** | **float** | Fishing boat proceeds | [optional] 
**medical_and_health_care_payments** | **float** | Medical and health care payments | [optional] 
**direct_sales_indicator** | **bool** | Payer made direct sales totaling $5,000 or more of consumer products to recipient for resale. Should be true if Nonemployee compensation is not provided. | [optional] 
**substitute_payments** | **float** | Substitute payments in lieu of dividends or interest | [optional] 
**crop_insurance_proceeds** | **float** | Crop insurance proceeds | [optional] 
**gross_proceeds_paid_to_attorney** | **float** | Gross proceeds paid to an attorney | [optional] 
**fish_purchased_for_resale** | **float** | Fish purchased for resale | [optional] 
**section409_a_deferrals** | **float** | Section 409A deferrals | [optional] 
**excess_golden_parachute_payments** | **float** | (Legacy field) Excess golden parachute payments | [optional] 
**nonqualified_deferred_compensation** | **float** | Nonqualified deferred compensation | [optional] 
**nonemployee_compensation** | **float** | Nonemployee compensation. Required if DirectSalesIndicator is false. | 
**gross_distribution** | **float** | Gross distribution | [optional] 
**taxable_amount** | **float** | Taxable amount | [optional] 
**taxable_amount_not_determined** | **bool** | Taxable amount not determined | [optional] 
**total_distribution_determined** | **bool** | Total distribution | [optional] 
**capital_gain** | **float** | Capital gain (included in Box 2a) | [optional] 
**employee_contributions_or_designated_roth_or_insurance_premiums** | **float** | Employee contributions/Designated Roth contributions or insurance premiums | [optional] 
**net_unrealized_appreciation_in_employer_securities** | **float** | Net unrealized appreciation in employer&#39;s securities | [optional] 
**distribution_code** | **str** | Distribution code.    Available values:  - 1: Early distribution, no known exception (in most cases, under age 59½)  - 2: Early distribution, exception applies (under age 59½)  - 3: Disability  - 4: Death  - 5: Prohibited transaction  - 6: Section 1035 exchange (a tax-free exchange of life insurance, annuity, qualified long-term care insurance, or endowment contracts)  - 7: Normal distribution  - 8: Excess contributions plus earnings/excess deferrals (and/or earnings) taxable in payment year  - 9: Cost of current life insurance protection (premiums paid by a trustee or custodian for current insurance protection)  - A: May be eligible for 10-year tax option  - B: Designated Roth account distribution  - C: Reportable Death Benefits Under Section 6050Y(c)  - D: Annuity payments from nonqualified annuity payments and distributions from life insurance contracts that may be subject to tax under section 1411  - E: Distribution under Employee Plans Compliance Resolution System (EPCRS)  - F: Charitable gift annuity  - G: Direct rollover and rollover contribution  - H: Direct rollover of distribution from a designated Roth account to a Roth IRA  - J: Early distribution from a Roth IRA (This code may be used with a Code 8 or P)  - K: Distribution of IRA Assets Not Having A Readily Available FMV  - L: Loans treated as deemed distributions under section 72(p)  - M: Qualified Plan Loan Offsets  - N: Recharacterized IRA contribution made for year following payment year  - P: Excess contributions plus earnings/excess deferrals taxable for year prior to payment year  - Q: Qualified distribution from a Roth IRA (Distribution from a Roth IRA when the 5-year holding period has been met, and the recipient has reached 59½, has died, or is disabled)  - R: Recharacterized IRA contribution made for year prior to payment year  - S: Early distribution from a SIMPLE IRA in first 2 years no known exceptions  - T: Roth IRA distribution exception applies because participant has reached 59½, died or is disabled, but it is unknown if the 5-year period has been met  - U: Distribution from ESOP under Section 404(k)  - W: Charges or payments for purchasing qualified long-term care insurance contracts under combined arrangements | 
**second_distribution_code** | **str** | Second distribution code. Must be a valid combination with the first distribution code.  See DistributionCode property documentation for code descriptions.    Valid combinations based on first distribution code:  - 1: _, 8, B, D, K, L, M, P  - 2: _, 8, B, D, K, L, M, P  - 3: _, D  - 4: _, 8, A, B, D, G, H, K, L, M, P  - 5: _  - 6: _, W  - 7: _, A, B, D, K, L, M  - 8: _, 1, 2, 4, B, J, K  - 9: _  - A: 4, 7  - B: _, 1, 2, 4, 7, 8, G, L, M, P, U  - C: _, D  - D: 1, 2, 3, 4, 7, C  - E: _  - F: _  - G: _, 4, B, K  - H: _, 4  - J: _, 8, P  - K: 1, 2, 4, 7, 8, G  - L: _, 1, 2, 4, 7, B  - M: _, 1, 2, 4, 7, B  - N: _  - P: _, 1, 2, 4, B, J  - Q: _  - R: _  - S: _  - T: _  - U: _, B  - W: _, 6                (_ indicates no second distribution code)    (format: firstDistributionCode: availableSecondDistributionCodes) | [optional] 
**ira_sep_simple** | **bool** | IRA/SEP/SIMPLE | [optional] 
**traditional_ira_sep_simple_or_roth_conversion_amount** | **float** | Traditional IRA/SEP/SIMPLE or Roth conversion amount | [optional] 
**other_amount** | **float** | Other amount | [optional] 
**other_percentage** | **str** | Other percentage | [optional] 
**total_distribution_percentage** | **str** | Total distribution percentage | [optional] 
**total_employee_contributions** | **float** | Total employee contributions | [optional] 
**amount_allocable_to_irr_within5_years** | **float** | Amount allocable to IRR within 5 years | [optional] 
**first_year_of_designated_roth_contribution** | **str** | First year of designated Roth contribution | [optional] 
**date_of_payment** | **date** | Date of payment | [optional] 

## Example

```python
from Avalara.SDK.models.A1099.V2.get1099_form200_response import Get1099Form200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Get1099Form200Response from a JSON string
get1099_form200_response_instance = Get1099Form200Response.from_json(json)
# print the JSON string representation of the object
print(Get1099Form200Response.to_json())

# convert the object into a dict
get1099_form200_response_dict = get1099_form200_response_instance.to_dict()
# create an instance of Get1099Form200Response from a dict
get1099_form200_response_from_dict = Get1099Form200Response.from_dict(get1099_form200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


