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

class CompanyCreateUpdateRequestModel(BaseModel):
    """
    CompanyCreateUpdateRequestModel
    """ # noqa: E501
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    telephone: Optional[StrictStr] = None
    tin: Optional[StrictStr] = None
    dba_name: Optional[StrictStr] = Field(default=None, alias="dbaName")
    reference_id: Optional[StrictStr] = Field(default=None, alias="referenceId")
    do_tin_match: Optional[StrictBool] = Field(default=None, alias="doTinMatch")
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    foreign_province: Optional[StrictStr] = Field(default=None, alias="foreignProvince")
    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    resend_requests: Optional[StrictBool] = Field(default=None, alias="resendRequests")
    resend_interval_days: Optional[StrictInt] = Field(default=None, alias="resendIntervalDays")
    max_reminder_attempts: Optional[StrictInt] = Field(default=None, alias="maxReminderAttempts")
    __properties: ClassVar[List[str]] = ["name", "email", "address", "city", "state", "zip", "telephone", "tin", "dbaName", "referenceId", "doTinMatch", "groupName", "foreignProvince", "countryCode", "resendRequests", "resendIntervalDays", "maxReminderAttempts"]

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
        """Create an instance of CompanyCreateUpdateRequestModel from a JSON string"""
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
        # set to None if resend_interval_days (nullable) is None
        # and model_fields_set contains the field
        if self.resend_interval_days is None and "resend_interval_days" in self.model_fields_set:
            _dict['resendIntervalDays'] = None

        # set to None if max_reminder_attempts (nullable) is None
        # and model_fields_set contains the field
        if self.max_reminder_attempts is None and "max_reminder_attempts" in self.model_fields_set:
            _dict['maxReminderAttempts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompanyCreateUpdateRequestModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip": obj.get("zip"),
            "telephone": obj.get("telephone"),
            "tin": obj.get("tin"),
            "dbaName": obj.get("dbaName"),
            "referenceId": obj.get("referenceId"),
            "doTinMatch": obj.get("doTinMatch"),
            "groupName": obj.get("groupName"),
            "foreignProvince": obj.get("foreignProvince"),
            "countryCode": obj.get("countryCode"),
            "resendRequests": obj.get("resendRequests"),
            "resendIntervalDays": obj.get("resendIntervalDays"),
            "maxReminderAttempts": obj.get("maxReminderAttempts")
        })
        return _obj


