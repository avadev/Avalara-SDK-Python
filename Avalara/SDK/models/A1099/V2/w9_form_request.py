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
    ## Authentication  #### Step 1: Generate API Credentials  Generate a *client ID* and *client secret* from your [Avalara1099 account](https://sbx.track1099.com/api_tokens): *Your Profile → API*.  #### Step 2: Get an Identity Token  Send a `POST` request to the **Identity Token URL** with your *client ID* and *client secret* from Step 1 as form-encoded parameters:  ```http POST https://identity.avalara.com/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials client_id=<your client ID> client_secret=<your client secret> ```  **Body parameters** - `grant_type` — Always `client_credentials` - `client_id` — Your *client ID* from Step 1 - `client_secret` — Your *client secret* from Step 1  **Successful response**  ```json {   \"access_token\": \"eyJhbGci...\",   \"expires_in\": 3600,   \"token_type\": \"Bearer\" } ```  Use the `access_token` as a bearer token in the `Authorization` header on every A1099 API request:  ```http Authorization: Bearer <access_token> ```  ---  For more on authenticating requests, see the [A1099 authentication guide](https://developer.avalara.com/1099-and-w-9/kny2997001535374/).  ---  ## Environments  #### Production - **Avalara 1099 API URL:** [`https://api.avalara.com/avalara1099`](https://api.avalara.com/avalara1099) - **Identity Token URL:** [`https://identity.avalara.com/connect/token`](https://identity.avalara.com/connect/token)  #### Sandbox - **Avalara 1099 API URL:** [`https://api.sbx.avalara.com/avalara1099`](https://api.sbx.avalara.com/avalara1099) - **Identity Token URL:** [`https://ai-sbx.avlr.sh/connect/token`](https://ai-sbx.avlr.sh/connect/token)  ---  ## API & SDK Documentation  [Avalara 1099 API Reference](https://developer.avalara.com/api-reference/avalara1099/avalara1099/)  [Avalara SDKs](https://developer.avalara.com/sdk/)  [Swagger](https://api.avalara.com/avalara1099/swagger/index.html?api-version=2.0) 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    26.5.0
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class W9FormRequest(BaseModel):
    """
    W9FormRequest
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="The form type (always \"w9\" for this model).")
    name: StrictStr = Field(description="The name of the individual or entity associated with the form.")
    business_name: Optional[StrictStr] = Field(default=None, description="The name of the business associated with the form.", alias="businessName")
    business_classification: StrictStr = Field(description="The classification of the business.  Available values:  - Individual: Individual/sole proprietor  - C Corporation: C Corporation  - S Corporation: S Corporation  - Partnership: Partnership  - Trust/estate: Trust/estate  - LLC-C: Limited liability company (C Corporation)  - LLC-S: Limited liability company (S Corporation)  - LLC-P: Limited liability company (Partnership)  - Other: Other (requires BusinessOther field to be populated)", alias="businessClassification")
    business_other: Optional[StrictStr] = Field(default=None, description="The classification description when \"businessClassification\" is \"Other\".", alias="businessOther")
    foreign_partner_owner_or_beneficiary: Optional[StrictBool] = Field(default=None, description="Indicates whether the individual is a foreign partner, owner, or beneficiary.", alias="foreignPartnerOwnerOrBeneficiary")
    exempt_payee_code: Optional[StrictStr] = Field(default=None, description="The exempt payee code. Allowed values (1–13):  - 1 — Organization exempt under §501(a) or IRA; custodial account under §403(b)(7)  - 2 — U.S. government or its agencies/instrumentalities  - 3 — U.S. state, DC, U.S. territory/possession, or their political subdivisions/agencies/instrumentalities  - 4 — Foreign government or its political subdivisions/agencies/instrumentalities  - 5 — Corporation  - 6 — Dealer in securities or commodities required to register in the U.S., DC, or U.S. territory/possession  - 7 — Futures commission merchant registered with the CFTC  - 8 — Real estate investment trust (REIT)  - 9 — Entity registered at all times during the tax year under the Investment Company Act of 1940  - 10 — Common trust fund operated by a bank under §584(a)  - 11 — Financial institution (see §581)  - 12 — Broker (nominee/custodian)  - 13 — Trust exempt under §664 or described in §4947", alias="exemptPayeeCode")
    exempt_fatca_code: Optional[StrictStr] = Field(default=None, description="The exemption from FATCA reporting code. Allowed values (A–M):  - A — Tax‑exempt organization under §501(a) or IRA (§7701(a)(37))  - B — U.S. government or any of its agencies/instrumentalities  - C — U.S. state, DC, territory/possession, or their political subdivisions/instrumentalities  - D — Corporation whose stock is regularly traded on an established securities market  - E — Corporation that is a member of the same expanded affiliated group as a D corporation  - F — Registered dealer in securities/commodities/derivatives  - G — REIT (Real Estate Investment Trust)  - H — Regulated investment company (§851) or entity registered all year under the Investment Company Act of 1940  - I — Common trust fund (§584(a))  - J — Bank (§581)  - K — Broker  - L — Charitable remainder trust (§664) or trust described in §4947(a)(1)  - M — Trust under §403(b) plan or §457(g) plan", alias="exemptFatcaCode")
    foreign_country_indicator: Optional[StrictBool] = Field(default=None, description="Indicates whether the individual or entity is in a foreign country.", alias="foreignCountryIndicator")
    address: StrictStr = Field(description="The address of the individual or entity.")
    foreign_address: Optional[StrictStr] = Field(default=None, description="The foreign address of the individual or entity.", alias="foreignAddress")
    city: Optional[StrictStr] = Field(description="The city of the address.")
    state: Optional[StrictStr] = Field(description="The state of the address.")
    zip: Optional[StrictStr] = Field(description="The ZIP code of the address.")
    account_number: Optional[StrictStr] = Field(default=None, description="The account number associated with the form.", alias="accountNumber")
    tin_type: StrictStr = Field(description="Tax Identification Number (TIN) type. SSN/ITIN (for individuals) and EIN (for businesses).", alias="tinType")
    tin: StrictStr = Field(description="The taxpayer identification number (TIN).")
    backup_withholding: Optional[StrictBool] = Field(default=None, description="Indicates whether backup withholding applies.", alias="backupWithholding")
    is1099able: Optional[StrictBool] = Field(default=None, description="Indicates whether the individual or entity should be issued a 1099 form.")
    e_delivery_consented_at: Optional[datetime] = Field(default=None, description="The date when e-delivery was consented.", alias="eDeliveryConsentedAt")
    signature: Optional[StrictStr] = Field(default=None, description="The signature of the form.")
    company_id: Optional[StrictStr] = Field(default=None, description="The ID of the associated company. Required when creating a form.", alias="companyId")
    reference_id: Optional[StrictStr] = Field(default=None, description="A reference identifier for the form.", alias="referenceId")
    email: Optional[StrictStr] = Field(default=None, description="The email address of the individual associated with the form.")
    __properties: ClassVar[List[str]] = ["eDeliveryConsentedAt", "signature", "type", "companyId", "referenceId", "email"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['W4', 'W8Ben', 'W8BenE', 'W8Imy', 'W9']):
            raise ValueError("must be one of enum values ('W4', 'W8Ben', 'W8BenE', 'W8Imy', 'W9')")
        return value

    @field_validator('business_classification')
    def business_classification_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Individual', 'CCorporation', 'SCorporation', 'Partnership', 'TrustEstate', 'LlcC', 'LlcS', 'LlcP', 'Other']):
            raise ValueError("must be one of enum values ('Individual', 'CCorporation', 'SCorporation', 'Partnership', 'TrustEstate', 'LlcC', 'LlcS', 'LlcP', 'Other')")
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
        """Create an instance of W9FormRequest from a JSON string"""
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
        # set to None if e_delivery_consented_at (nullable) is None
        # and model_fields_set contains the field
        if self.e_delivery_consented_at is None and "e_delivery_consented_at" in self.model_fields_set:
            _dict['eDeliveryConsentedAt'] = None

        # set to None if signature (nullable) is None
        # and model_fields_set contains the field
        if self.signature is None and "signature" in self.model_fields_set:
            _dict['signature'] = None

        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['referenceId'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of W9FormRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eDeliveryConsentedAt": obj.get("eDeliveryConsentedAt"),
            "signature": obj.get("signature"),
            "type": obj.get("type"),
            "companyId": obj.get("companyId"),
            "referenceId": obj.get("referenceId"),
            "email": obj.get("email")
        })
        return _obj


