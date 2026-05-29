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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CoveredIndividual(BaseModel):
    """
    Covered individual information for health coverage forms
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Covered individual's ID")
    first_name: Optional[StrictStr] = Field(description="Covered individual's first name", alias="firstName")
    middle_name: Optional[StrictStr] = Field(default=None, description="Covered individual's middle name", alias="middleName")
    last_name: Optional[StrictStr] = Field(description="Covered individual's last name", alias="lastName")
    name_suffix: Optional[StrictStr] = Field(default=None, description="Covered individual's name suffix", alias="nameSuffix")
    tin: Optional[StrictStr] = Field(default=None, description="Covered individual's Federal Tax Identification Number (TIN).. SSN or ITIN. Required unless unavailable.")
    birth_date: Optional[date] = Field(default=None, description="Covered individual's date of birth - Required when SSN is missing.", alias="birthDate")
    covered_january: Optional[StrictBool] = Field(default=None, description="Coverage indicator for January", alias="coveredJanuary")
    covered_february: Optional[StrictBool] = Field(default=None, description="Coverage indicator for February", alias="coveredFebruary")
    covered_march: Optional[StrictBool] = Field(default=None, description="Coverage indicator for March", alias="coveredMarch")
    covered_april: Optional[StrictBool] = Field(default=None, description="Coverage indicator for April", alias="coveredApril")
    covered_may: Optional[StrictBool] = Field(default=None, description="Coverage indicator for May", alias="coveredMay")
    covered_june: Optional[StrictBool] = Field(default=None, description="Coverage indicator for June", alias="coveredJune")
    covered_july: Optional[StrictBool] = Field(default=None, description="Coverage indicator for July", alias="coveredJuly")
    covered_august: Optional[StrictBool] = Field(default=None, description="Coverage indicator for August", alias="coveredAugust")
    covered_september: Optional[StrictBool] = Field(default=None, description="Coverage indicator for September", alias="coveredSeptember")
    covered_october: Optional[StrictBool] = Field(default=None, description="Coverage indicator for October", alias="coveredOctober")
    covered_november: Optional[StrictBool] = Field(default=None, description="Coverage indicator for November", alias="coveredNovember")
    covered_december: Optional[StrictBool] = Field(default=None, description="Coverage indicator for December", alias="coveredDecember")
    __properties: ClassVar[List[str]] = ["id", "firstName", "middleName", "lastName", "nameSuffix", "tin", "birthDate", "coveredJanuary", "coveredFebruary", "coveredMarch", "coveredApril", "coveredMay", "coveredJune", "coveredJuly", "coveredAugust", "coveredSeptember", "coveredOctober", "coveredNovember", "coveredDecember"]

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
        """Create an instance of CoveredIndividual from a JSON string"""
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
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

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

        # set to None if name_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.name_suffix is None and "name_suffix" in self.model_fields_set:
            _dict['nameSuffix'] = None

        # set to None if tin (nullable) is None
        # and model_fields_set contains the field
        if self.tin is None and "tin" in self.model_fields_set:
            _dict['tin'] = None

        # set to None if birth_date (nullable) is None
        # and model_fields_set contains the field
        if self.birth_date is None and "birth_date" in self.model_fields_set:
            _dict['birthDate'] = None

        # set to None if covered_january (nullable) is None
        # and model_fields_set contains the field
        if self.covered_january is None and "covered_january" in self.model_fields_set:
            _dict['coveredJanuary'] = None

        # set to None if covered_february (nullable) is None
        # and model_fields_set contains the field
        if self.covered_february is None and "covered_february" in self.model_fields_set:
            _dict['coveredFebruary'] = None

        # set to None if covered_march (nullable) is None
        # and model_fields_set contains the field
        if self.covered_march is None and "covered_march" in self.model_fields_set:
            _dict['coveredMarch'] = None

        # set to None if covered_april (nullable) is None
        # and model_fields_set contains the field
        if self.covered_april is None and "covered_april" in self.model_fields_set:
            _dict['coveredApril'] = None

        # set to None if covered_may (nullable) is None
        # and model_fields_set contains the field
        if self.covered_may is None and "covered_may" in self.model_fields_set:
            _dict['coveredMay'] = None

        # set to None if covered_june (nullable) is None
        # and model_fields_set contains the field
        if self.covered_june is None and "covered_june" in self.model_fields_set:
            _dict['coveredJune'] = None

        # set to None if covered_july (nullable) is None
        # and model_fields_set contains the field
        if self.covered_july is None and "covered_july" in self.model_fields_set:
            _dict['coveredJuly'] = None

        # set to None if covered_august (nullable) is None
        # and model_fields_set contains the field
        if self.covered_august is None and "covered_august" in self.model_fields_set:
            _dict['coveredAugust'] = None

        # set to None if covered_september (nullable) is None
        # and model_fields_set contains the field
        if self.covered_september is None and "covered_september" in self.model_fields_set:
            _dict['coveredSeptember'] = None

        # set to None if covered_october (nullable) is None
        # and model_fields_set contains the field
        if self.covered_october is None and "covered_october" in self.model_fields_set:
            _dict['coveredOctober'] = None

        # set to None if covered_november (nullable) is None
        # and model_fields_set contains the field
        if self.covered_november is None and "covered_november" in self.model_fields_set:
            _dict['coveredNovember'] = None

        # set to None if covered_december (nullable) is None
        # and model_fields_set contains the field
        if self.covered_december is None and "covered_december" in self.model_fields_set:
            _dict['coveredDecember'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CoveredIndividual from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstName": obj.get("firstName"),
            "middleName": obj.get("middleName"),
            "lastName": obj.get("lastName"),
            "nameSuffix": obj.get("nameSuffix"),
            "tin": obj.get("tin"),
            "birthDate": obj.get("birthDate"),
            "coveredJanuary": obj.get("coveredJanuary"),
            "coveredFebruary": obj.get("coveredFebruary"),
            "coveredMarch": obj.get("coveredMarch"),
            "coveredApril": obj.get("coveredApril"),
            "coveredMay": obj.get("coveredMay"),
            "coveredJune": obj.get("coveredJune"),
            "coveredJuly": obj.get("coveredJuly"),
            "coveredAugust": obj.get("coveredAugust"),
            "coveredSeptember": obj.get("coveredSeptember"),
            "coveredOctober": obj.get("coveredOctober"),
            "coveredNovember": obj.get("coveredNovember"),
            "coveredDecember": obj.get("coveredDecember")
        })
        return _obj


