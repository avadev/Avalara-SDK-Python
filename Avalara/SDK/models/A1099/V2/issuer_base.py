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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IssuerBase(BaseModel):
    """
    IssuerBase
    """ # noqa: E501
    business_name: Optional[StrictStr] = Field(description="Business name. Required when the recipient of the form is a business; should only be used for businesses.", alias="businessName")
    business_name2: Optional[StrictStr] = Field(default=None, description="Business name line 2. Should only be used for businesses. Use either this or 'transferAgentName'.", alias="businessName2")
    name: Optional[StrictStr] = Field(default=None, description="Legal name. Not the DBA name. Deprecated alias for 'businessName'.")
    dba_name: Optional[StrictStr] = Field(default=None, description="Doing Business As (DBA) name or continuation of a long legal name. Deprecated alias for 'businessName2'. Use either this or 'transferAgentName'.", alias="dbaName")
    tin_type: Optional[StrictStr] = Field(default=None, description="Recipient classification.  The platform is transitioning from tax identifier classifications to recipient entity classifications. New values represent recipient entity types and should be preferred. Deprecated values represent identifier formats and remain supported for backward compatibility only.  Available values: - INDIVIDUAL: Recipient is an individual - BUSINESS: Recipient is a business - UNKNOWN: Recipient classification is unknown - EIN: (Deprecated - use BUSINESS) Employer Identification Number - SSN: (Deprecated - use INDIVIDUAL) Social Security Number - ITIN: (Deprecated - use INDIVIDUAL) Individual Taxpayer Identification Number - ATIN: (Deprecated - use INDIVIDUAL) Adoption Taxpayer Identification Number", alias="tinType")
    first_name: Optional[StrictStr] = Field(default=None, description="First name. Required when the recipient of the form is an individual; should only be used for individuals.", alias="firstName")
    middle_name: Optional[StrictStr] = Field(default=None, description="Middle name. Should only be used for individuals.", alias="middleName")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name. Required when the recipient of the form is an individual; should only be used for individuals.", alias="lastName")
    suffix: Optional[StrictStr] = Field(default=None, description="Suffix name. Should only be used for individuals.")
    tin: Optional[StrictStr] = Field(default=None, description="Federal Tax Identification Number (TIN).")
    reference_id: Optional[StrictStr] = Field(default=None, description="Internal reference ID. Never shown to any agency or recipient. If present, it will prefix download filenames. Allowed characters: letters, numbers, dashes, underscores, and spaces.", alias="referenceId")
    telephone: Optional[StrictStr] = Field(description="Contact phone number (must contain at least 10 digits, max 15 characters). For recipient inquiries.")
    tax_year: Optional[StrictInt] = Field(description="Tax year for which the forms are being filed (e.g., 2024). Must be within current tax year and current tax year - 4. It's only required on creation, and cannot be modified on update.", alias="taxYear")
    country_code: Optional[StrictStr] = Field(description="Two-letter IRS country code (e.g., 'US', 'CA'), as defined at https://www.irs.gov/e-file-providers/country-codes. If there is a transfer agent, use the transfer agent's shipping address.", alias="countryCode")
    email: Optional[StrictStr] = Field(default=None, description="Contact email address. For recipient inquiries. Phone will be used on communications if you don't specify an email")
    address: Optional[StrictStr] = Field(description="Address.")
    city: Optional[StrictStr] = Field(description="City.")
    state: Optional[StrictStr] = Field(description="Two-letter US state or Canadian province code (required for US/CA addresses).")
    zip: Optional[StrictStr] = Field(description="ZIP/postal code.")
    foreign_province: Optional[StrictStr] = Field(default=None, description="Province or region for non-US/CA addresses.", alias="foreignProvince")
    transfer_agent_name: Optional[StrictStr] = Field(default=None, description="Name of the transfer agent, if applicable — optional; use either this or 'dbaName'.", alias="transferAgentName")
    last_filing: Optional[StrictBool] = Field(description="Indicates if this is the issuer's final year filing.", alias="lastFiling")
    __properties: ClassVar[List[str]] = ["businessName", "businessName2", "name", "dbaName", "tinType", "firstName", "middleName", "lastName", "suffix", "tin", "referenceId", "telephone", "taxYear", "countryCode", "email", "address", "city", "state", "zip", "foreignProvince", "transferAgentName", "lastFiling"]

    @field_validator('tin_type')
    def tin_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNKNOWN', 'INDIVIDUAL', 'BUSINESS']):
            raise ValueError("must be one of enum values ('UNKNOWN', 'INDIVIDUAL', 'BUSINESS')")
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
        """Create an instance of IssuerBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if business_name (nullable) is None
        # and model_fields_set contains the field
        if self.business_name is None and "business_name" in self.model_fields_set:
            _dict['businessName'] = None

        # set to None if business_name2 (nullable) is None
        # and model_fields_set contains the field
        if self.business_name2 is None and "business_name2" in self.model_fields_set:
            _dict['businessName2'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if dba_name (nullable) is None
        # and model_fields_set contains the field
        if self.dba_name is None and "dba_name" in self.model_fields_set:
            _dict['dbaName'] = None

        # set to None if tin_type (nullable) is None
        # and model_fields_set contains the field
        if self.tin_type is None and "tin_type" in self.model_fields_set:
            _dict['tinType'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if middle_name (nullable) is None
        # and model_fields_set contains the field
        if self.middle_name is None and "middle_name" in self.model_fields_set:
            _dict['middleName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if suffix (nullable) is None
        # and model_fields_set contains the field
        if self.suffix is None and "suffix" in self.model_fields_set:
            _dict['suffix'] = None

        # set to None if tin (nullable) is None
        # and model_fields_set contains the field
        if self.tin is None and "tin" in self.model_fields_set:
            _dict['tin'] = None

        # set to None if reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.reference_id is None and "reference_id" in self.model_fields_set:
            _dict['referenceId'] = None

        # set to None if telephone (nullable) is None
        # and model_fields_set contains the field
        if self.telephone is None and "telephone" in self.model_fields_set:
            _dict['telephone'] = None

        # set to None if tax_year (nullable) is None
        # and model_fields_set contains the field
        if self.tax_year is None and "tax_year" in self.model_fields_set:
            _dict['taxYear'] = None

        # set to None if country_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_code is None and "country_code" in self.model_fields_set:
            _dict['countryCode'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if zip (nullable) is None
        # and model_fields_set contains the field
        if self.zip is None and "zip" in self.model_fields_set:
            _dict['zip'] = None

        # set to None if foreign_province (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_province is None and "foreign_province" in self.model_fields_set:
            _dict['foreignProvince'] = None

        # set to None if transfer_agent_name (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_agent_name is None and "transfer_agent_name" in self.model_fields_set:
            _dict['transferAgentName'] = None

        # set to None if last_filing (nullable) is None
        # and model_fields_set contains the field
        if self.last_filing is None and "last_filing" in self.model_fields_set:
            _dict['lastFiling'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuerBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "businessName": obj.get("businessName"),
            "businessName2": obj.get("businessName2"),
            "name": obj.get("name"),
            "dbaName": obj.get("dbaName"),
            "tinType": obj.get("tinType"),
            "firstName": obj.get("firstName"),
            "middleName": obj.get("middleName"),
            "lastName": obj.get("lastName"),
            "suffix": obj.get("suffix"),
            "tin": obj.get("tin"),
            "referenceId": obj.get("referenceId"),
            "telephone": obj.get("telephone"),
            "taxYear": obj.get("taxYear"),
            "countryCode": obj.get("countryCode"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip": obj.get("zip"),
            "foreignProvince": obj.get("foreignProvince"),
            "transferAgentName": obj.get("transferAgentName"),
            "lastFiling": obj.get("lastFiling")
        })
        return _obj


