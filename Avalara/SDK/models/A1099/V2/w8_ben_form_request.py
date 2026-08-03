# coding: utf-8

"""
AvaTax Software Development Kit for Python.

   Copyright 2022 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

    Avalara 1099 & W-9 API Definition
    > **Note:** You must have an active Avalara 1099 & W-9 subscription to authenticate and use these APIs. If you don't have a subscription, please contact our [Sales team](https://www.avalara.com/us/en/products/1099/request-a-demo.html).  ## Authentication  The Avalara 1099 & W-9 API uses **Bearer Token Authentication**. To authenticate, acquire a bearer token using a **Client ID** and **Client Secret** that you generate in the Avalara 1099 & W-9 web application.  The sample cURL commands below use **production** URLs. For **sandbox**, replace them with the sandbox URLs listed in the Sandbox Environment table.  ### Option 1 — Client ID and Client Secret (recommended)  **Step 1: Create API credentials in the Avalara 1099 & W-9 web app**  For a full walkthrough, see the [Avalara 1099 & W-9 integration guide](https://developer.avalara.com/products/avalara-1099-and-w9/integration-guides/1099-and-w-9/siu2796410674799/).  > **Note:** To enable credential creation you must first enter a valid company address in **Account Settings > Account** and enable two-factor authentication in **Account Settings > Security**.  1. In Avalara 1099 & W-9, open **Account Settings** (gear icon, top-right of any page) and select **API**. 2. Click **Create new credentials** (a valid company address and 2FA are required). 3. Copy your **Client Id** and **Client Secret** securely — they will not be shown again after you leave the screen.  **Step 2: Request a bearer token**  ```bash curl -X POST 'https://identity.avalara.com/connect/token' \\   --header 'Content-Type: application/x-www-form-urlencoded' \\   --data-urlencode 'grant_type=client_credentials' \\   --data-urlencode 'client_id={{client_id}}' \\   --data-urlencode 'client_secret={{client_secret}}' ```  ### Option 2 — Account ID and License Key  If your organization already uses other Avalara products (AvaTax, CertCapture) and has access to the logged-in area of Avalara.com, you can generate the bearer token using your **Account ID** and **License Key**.  > **Note:** If you already have a license key for other Avalara products you can reuse it. Generating a new key will reset any previously created key.  1. Log in to Avalara.com. 2. Go to **Settings → License and API Keys**. 3. Click **Generate New Key**. 4. Note your **Account ID** from the Account menu.  ```bash curl -X POST 'https://identity.avalara.com/connect/token' \\   --header 'Content-Type: application/x-www-form-urlencoded' \\   --data-urlencode 'grant_type=client_credentials' \\   --data-urlencode 'client_id={{accountId}}' \\   --data-urlencode 'client_secret={{licenseKey}}' ```  ### Using and renewing the bearer token  Include the token in the `Authorization` header on every request:  ```http Authorization: Bearer {access_token} ```  Tokens expire after the number of seconds in the `expires_in` field of the token response. Your integration must renew the token before it expires.  **Example token response**  ```json {   \"access_token\": \"eyJhbGciOiJIUzI1NiIsInR5cCI...\",   \"expires_in\": 3600,   \"token_type\": \"Bearer\",   \"scope\": \"avatax_api iam-ds\" } ```  ### Sandbox Environment  Use the same steps as production, replacing the base URLs:  | Purpose | Production | Sandbox | | --- | --- | --- | | Account & License Key management (web) | `https://www.avalara.com` | `https://sandbox.admin.avalara.com` | | Account & License Key management (API) | `https://rest.avatax.com` | `https://sandbox-rest.avatax.com` | | Token generation | `https://identity.avalara.com` | `https://ai-sbx.avlr.sh` |  ## Environments  #### Production - **Avalara 1099 API URL:** [`https://api.avalara.com/avalara1099`](https://api.avalara.com/avalara1099) - **Identity Token URL:** [`https://identity.avalara.com/connect/token`](https://identity.avalara.com/connect/token)  #### Sandbox - **Avalara 1099 API URL:** [`https://api.sbx.avalara.com/avalara1099`](https://api.sbx.avalara.com/avalara1099) - **Identity Token URL:** [`https://ai-sbx.avlr.sh/connect/token`](https://ai-sbx.avlr.sh/connect/token)  ---  ## API & SDK Documentation  [Avalara 1099 API Reference](https://developer.avalara.com/api-reference/avalara1099/avalara1099/)  [Avalara SDKs](https://developer.avalara.com/sdk/)  [Swagger](https://api.avalara.com/avalara1099/swagger/index.html?api-version=2.0) 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    26.7.0
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class W8BenFormRequest(BaseModel):
    """
    W8BenFormRequest
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="The form type (always \"w8ben\" for this model).")
    name: StrictStr = Field(description="The name of the individual or entity associated with the form.")
    citizenship_country: StrictStr = Field(description="The country of citizenship.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more)", alias="citizenshipCountry")
    residence_address: Optional[StrictStr] = Field(default=None, description="The residential address of the individual or entity.", alias="residenceAddress")
    residence_city: Optional[StrictStr] = Field(default=None, description="The city of residence.", alias="residenceCity")
    residence_state: Optional[StrictStr] = Field(default=None, description="The state of residence. Required for US and Canada.. Allowed values: AA, AE, AK, AL, AP, AR, AS, AZ, CA, CO (and 65 more)", alias="residenceState")
    residence_zip: Optional[StrictStr] = Field(default=None, description="The ZIP code of the residence.", alias="residenceZip")
    residence_country: StrictStr = Field(description="The country of residence.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more)", alias="residenceCountry")
    residence_is_mailing: Optional[StrictBool] = Field(default=None, description="Indicates whether the residence address is the mailing address.", alias="residenceIsMailing")
    mailing_address: Optional[StrictStr] = Field(default=None, description="The mailing address.", alias="mailingAddress")
    mailing_city: Optional[StrictStr] = Field(default=None, description="The city of the mailing address.", alias="mailingCity")
    mailing_state: Optional[StrictStr] = Field(default=None, description="The state of the mailing address. Required for US and Canada.. Allowed values: AA, AE, AK, AL, AP, AR, AS, AZ, CA, CO (and 65 more)", alias="mailingState")
    mailing_zip: Optional[StrictStr] = Field(default=None, description="The ZIP code of the mailing address.", alias="mailingZip")
    mailing_country: Optional[StrictStr] = Field(description="The country of the mailing address.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more)", alias="mailingCountry")
    tin: Optional[StrictStr] = Field(default=None, description="The taxpayer identification number (TIN).")
    foreign_tin_not_required: Optional[StrictBool] = Field(default=None, description="Indicates whether a foreign TIN is not legally required.", alias="foreignTinNotRequired")
    foreign_tin: Optional[StrictStr] = Field(default=None, description="The foreign taxpayer identification number (TIN).", alias="foreignTin")
    reference_number: Optional[StrictStr] = Field(default=None, description="A reference number for the form.", alias="referenceNumber")
    birthday: Optional[date] = Field(default=None, description="The birthday of the individual associated with the form.")
    treaty_country: Optional[StrictStr] = Field(default=None, description="The country for which the treaty applies.. Allowed values: US, AF, AX, AL, AG, AQ, AN, AO, AV, AY (and 248 more)", alias="treatyCountry")
    treaty_article: Optional[StrictStr] = Field(default=None, description="The specific article of the treaty being claimed.", alias="treatyArticle")
    treaty_reasons: Optional[StrictStr] = Field(default=None, description="The reasons for claiming treaty benefits.", alias="treatyReasons")
    withholding_rate: Optional[StrictStr] = Field(default=None, description="The withholding rate applied as per the treaty. Must be a percentage with up to two decimals (e.g., 12.50, 0).. Allowed values: 0, 0.0, 0.00, 5, 5.5, 10, 12.50, 15, 20, 25 (and 1 more)", alias="withholdingRate")
    income_type: Optional[StrictStr] = Field(default=None, description="The type of income covered by the treaty.", alias="incomeType")
    signer_name: Optional[StrictStr] = Field(default=None, description="The name of the signer of the form.", alias="signerName")
    company_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated company. Required when creating a form.", alias="companyId")
    reference_id: Optional[StrictStr] = Field(default=None, description="A reference identifier for the form.", alias="referenceId")
    email: Optional[StrictStr] = Field(default=None, description="The email address of the individual associated with the form.")
    e_delivery_consented_at: Optional[datetime] = Field(default=None, description="The date when e-delivery was consented.", alias="eDeliveryConsentedAt")
    signature: Optional[StrictStr] = Field(default=None, description="The signature of the form.")
    __properties: ClassVar[List[str]] = ["type", "companyId", "referenceId", "email", "eDeliveryConsentedAt", "signature"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['W4', 'W8Ben', 'W8BenE', 'W8Imy', 'W9']):
            raise ValueError("must be one of enum values ('W4', 'W8Ben', 'W8BenE', 'W8Imy', 'W9')")
        return value

    @field_validator('citizenship_country')
    def citizenship_country_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI']):
            raise ValueError("must be one of enum values ('US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI')")
        return value

    @field_validator('residence_state')
    def residence_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'FM', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MH', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']):
            raise ValueError("must be one of enum values ('AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'FM', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MH', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')")
        return value

    @field_validator('residence_country')
    def residence_country_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI']):
            raise ValueError("must be one of enum values ('US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI')")
        return value

    @field_validator('mailing_state')
    def mailing_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'FM', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MH', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']):
            raise ValueError("must be one of enum values ('AA', 'AE', 'AK', 'AL', 'AP', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'FM', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MH', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'PW', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')")
        return value

    @field_validator('mailing_country')
    def mailing_country_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI']):
            raise ValueError("must be one of enum values ('US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI')")
        return value

    @field_validator('treaty_country')
    def treaty_country_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI']):
            raise ValueError("must be one of enum values ('US', 'AF', 'AX', 'AL', 'AG', 'AQ', 'AN', 'AO', 'AV', 'AY', 'AC', 'AR', 'AM', 'AA', 'AT', 'AS', 'AU', 'AJ', 'BF', 'BA', 'FQ', 'BG', 'BB', 'BO', 'BE', 'BH', 'BN', 'BD', 'BT', 'BL', 'BK', 'BC', 'BV', 'BR', 'IO', 'VI', 'BX', 'BU', 'UV', 'BM', 'BY', 'CB', 'CM', 'CA', 'CV', 'CJ', 'CT', 'CD', 'CI', 'CH', 'KT', 'IP', 'CK', 'CO', 'CN', 'CF', 'CG', 'CW', 'CR', 'CS', 'IV', 'HR', 'CU', 'UC', 'CY', 'EZ', 'DA', 'DX', 'DJ', 'DO', 'DR', 'TT', 'EC', 'EG', 'ES', 'EK', 'ER', 'EN', 'ET', 'FK', 'FO', 'FM', 'FJ', 'FI', 'FR', 'FP', 'FS', 'GB', 'GA', 'GG', 'GM', 'GH', 'GI', 'GR', 'GL', 'GJ', 'GQ', 'GT', 'GK', 'GV', 'PU', 'GY', 'HA', 'HM', 'VT', 'HO', 'HK', 'HQ', 'HU', 'IC', 'IN', 'ID', 'IR', 'IZ', 'EI', 'IS', 'IT', 'JM', 'JN', 'JA', 'DQ', 'JE', 'JQ', 'JO', 'KZ', 'KE', 'KQ', 'KR', 'KN', 'KS', 'KV', 'KU', 'KG', 'LA', 'LG', 'LE', 'LT', 'LI', 'LY', 'LS', 'LH', 'LU', 'MC', 'MK', 'MA', 'MI', 'MY', 'MV', 'ML', 'MT', 'IM', 'RM', 'MR', 'MP', 'MX', 'MQ', 'MD', 'MN', 'MG', 'MJ', 'MH', 'MO', 'MZ', 'WA', 'NR', 'BQ', 'NP', 'NL', 'NC', 'NZ', 'NU', 'NG', 'NI', 'NE', 'NF', 'CQ', 'NO', 'MU', 'OC', 'PK', 'PS', 'LQ', 'PM', 'PP', 'PF', 'PA', 'PE', 'RP', 'PC', 'PL', 'PO', 'RQ', 'QA', 'RO', 'RS', 'RW', 'TB', 'RN', 'WS', 'SM', 'TP', 'SA', 'SG', 'RI', 'SE', 'SL', 'SN', 'NN', 'LO', 'SI', 'BP', 'SO', 'SF', 'SX', 'SP', 'PG', 'CE', 'SH', 'SC', 'ST', 'SB', 'VC', 'SU', 'NS', 'SV', 'WZ', 'SW', 'SZ', 'SY', 'TW', 'TI', 'TZ', 'TH', 'TO', 'TL', 'TN', 'TD', 'TS', 'TU', 'TX', 'TK', 'TV', 'UG', 'UP', 'AE', 'UK', 'UY', 'UZ', 'NH', 'VE', 'VM', 'VQ', 'WQ', 'WF', 'WI', 'YM', 'ZA', 'ZI')")
        return value

    @field_validator('withholding_rate')
    def withholding_rate_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['0', '0.0', '0.00', '5', '5.5', '10', '12.50', '15', '20', '25', '30']):
            raise ValueError("must be one of enum values ('0', '0.0', '0.00', '5', '5.5', '10', '12.50', '15', '20', '25', '30')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of W8BenFormRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['referenceId'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if e_delivery_consented_at (nullable) is None
        # and model_fields_set contains the field
        if self.e_delivery_consented_at is None and "e_delivery_consented_at" in self.model_fields_set:
            _dict['eDeliveryConsentedAt'] = None

        # set to None if signature (nullable) is None
        # and model_fields_set contains the field
        if self.signature is None and "signature" in self.model_fields_set:
            _dict['signature'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of W8BenFormRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "companyId": obj.get("companyId"),
            "referenceId": obj.get("referenceId"),
            "email": obj.get("email"),
            "eDeliveryConsentedAt": obj.get("eDeliveryConsentedAt"),
            "signature": obj.get("signature")
        })
        return _obj


