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
    ## 🔐 Authentication  Use **username/password** or generate a **license key** from: *Avalara Portal → Settings → License and API Keys*.  [More on authentication methods](https://developer.avalara.com/avatax-dm-combined-erp/common-setup/authentication/authentication-methods/)  [Test your credentials](https://developer.avalara.com/avatax/test-credentials/)  ## 📘 API & SDK Documentation  [Avalara SDK (.NET) on GitHub](https://github.com/avadev/Avalara-SDK-DotNet#avalarasdk--the-unified-c-library-for-next-gen-avalara-services)  [Code Examples – 1099 API](https://github.com/avadev/Avalara-SDK-DotNet/blob/main/docs/A1099/V2/Class1099IssuersApi.md#call1099issuersget) 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    25.7.2
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IssuerCommand(BaseModel):
    """
    IssuerCommand
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Legal name, not DBA")
    name_dba: Optional[StrictStr] = Field(default=None, description="Optional DBA name or continuation of a long legal name", alias="nameDba")
    tin: Optional[StrictStr] = Field(default=None, description="Tax identification number")
    reference_id: Optional[StrictStr] = Field(default=None, description="Optional identifier for your reference, never shown to any agency or recipient.  We will also prefix download filenames with this value, if present.  Can only include letters, numbers, dashes, underscores and spaces.", alias="referenceId")
    telephone: Optional[StrictStr] = Field(default=None, description="Telephone number")
    tax_year: Optional[StrictInt] = Field(default=None, description="Tax year", alias="taxYear")
    country_code: Optional[StrictStr] = Field(default=None, description="If there is a transfer agent, use the shipping address of the transfer agent.", alias="countryCode")
    email: Optional[StrictStr] = Field(default=None, description="Email address")
    address: Optional[StrictStr] = Field(default=None, description="Address")
    city: Optional[StrictStr] = Field(default=None, description="City")
    state: Optional[StrictStr] = Field(default=None, description="State")
    zip: Optional[StrictStr] = Field(default=None, description="Zip code")
    foreign_province: Optional[StrictStr] = Field(default=None, description="Foreign province", alias="foreignProvince")
    transfer_agent_name: Optional[StrictStr] = Field(default=None, description="Transfer Agent's Name", alias="transferAgentName")
    last_filing: Optional[StrictBool] = Field(default=None, description="Last year of filing for this payer", alias="lastFiling")
    __properties: ClassVar[List[str]] = ["name", "nameDba", "tin", "referenceId", "telephone", "taxYear", "countryCode", "email", "address", "city", "state", "zip", "foreignProvince", "transferAgentName", "lastFiling"]

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
        """Create an instance of IssuerCommand from a JSON string"""
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
        # set to None if name_dba (nullable) is None
        # and model_fields_set contains the field
        if self.name_dba is None and "name_dba" in self.model_fields_set:
            _dict['nameDba'] = None

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
        """Create an instance of IssuerCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "nameDba": obj.get("nameDba"),
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


