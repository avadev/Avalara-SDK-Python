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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class OfferAndCoverage(BaseModel):
    """
    Offer and coverage information for health coverage forms
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Id")
    month: Optional[StrictStr] = Field(default=None, description="Month of coverage.  Available values:  - All: All months  - January: January  - February: February  - March: March  - April: April  - May: May  - June: June  - July: July  - August: August  - September: September  - October: October  - November: November  - December: December")
    offer_code: Optional[StrictStr] = Field(default=None, description="Offer of Coverage Code. Required if Share has a value, including zero.  Available values:    Pre-ICHRA Codes (available before 2020):  - 1A: Qualifying offer: minimum essential coverage providing minimum value offered to full-time employee with employee required contribution ≤ 9.5% (as adjusted) of mainland single federal poverty line and at least minimum essential coverage offered to spouse and dependent(s)  - 1B: Minimum essential coverage providing minimum value offered to employee only  - 1C: Minimum essential coverage providing minimum value offered to employee and at least minimum essential coverage offered to dependent(s) (not spouse)  - 1D: Minimum essential coverage providing minimum value offered to employee and at least minimum essential coverage offered to spouse (not dependent(s))  - 1E: Minimum essential coverage providing minimum value offered to employee and at least minimum essential coverage offered to dependent(s) and spouse  - 1F: Minimum essential coverage NOT providing minimum value offered to employee; employee and spouse or dependent(s); or employee, spouse, and dependents  - 1G: Offer of coverage to an individual who was not an employee or not a full-time employee and who enrolled in self-insured coverage  - 1H: No offer of coverage (employee not offered any health coverage or employee offered coverage that is not minimum essential coverage)  - 1J: Minimum essential coverage providing minimum value offered to employee and at least minimum essential coverage conditionally offered to spouse; minimum essential coverage not offered to dependent(s)  - 1K: Minimum essential coverage providing minimum value offered to employee; at least minimum essential coverage offered to dependents; and at least minimum essential coverage conditionally offered to spouse                ICHRA Codes (introduced 2020, require ZIP code):  - 1L: Individual coverage HRA offered to employee only  - 1M: Individual coverage HRA offered to employee and dependent(s) (not spouse)  - 1N: Individual coverage HRA offered to employee, spouse, and dependent(s)  - 1O: Individual coverage HRA offered to employee only using employment site ZIP code affordability safe harbor  - 1P: Individual coverage HRA offered to employee and dependent(s) (not spouse) using employment site ZIP code affordability safe harbor  - 1Q: Individual coverage HRA offered to employee, spouse, and dependent(s) using employment site ZIP code affordability safe harbor  - 1R: Individual coverage HRA that is NOT affordable  - 1S: Individual coverage HRA offered to an individual who was not a full-time employee  - 1T: Individual coverage HRA offered to employee and spouse (not dependents)  - 1U: Individual coverage HRA offered to employee and spouse (not dependents) using employment site ZIP code affordability safe harbor    Note: Codes 1B, 1C, 1D, 1E, 1J, 1K, 1L, 1M, 1N, 1O, 1P, 1Q, 1T, 1U require employee share amount (0.00 is a valid value).", alias="offerCode")
    share: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Employee required contribution share - Employee Share of Lowest Cost Monthly Premium, for Self-Only Minimum Value Coverage - May not exceed 3499.99")
    safe_harbor_code: Optional[StrictStr] = Field(default=None, description="Safe harbor code - Applicable Section 4980H Safe Harbor Code.  Available values:  - 2A: Form W-2 safe harbor  - 2B: Federal poverty line safe harbor  - 2C: Rate of pay safe harbor  - 2D: Part-time employee safe harbor for employees who were not full-time for any month of the year  - 2E: Multiemployer interim rule relief  - 2F: Qualifying offer method  - 2G: Qualifying offer transition relief  - 2H: Other affordability safe harbor", alias="safeHarborCode")
    zip_code: Optional[StrictStr] = Field(default=None, description="ZIP/postal code. For coverage area (optional, unless codes 1L to 1U are used).", alias="zipCode")
    __properties: ClassVar[List[str]] = ["id", "month", "offerCode", "share", "safeHarborCode", "zipCode"]

    @field_validator('month')
    def month_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['All', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']):
            raise ValueError("must be one of enum values ('All', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')")
        return value

    @field_validator('offer_code')
    def offer_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1J', '1K', '1L', '1M', '1N', '1O', '1P', '1Q', '1R', '1S', '1T', '1U']):
            raise ValueError("must be one of enum values ('1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1J', '1K', '1L', '1M', '1N', '1O', '1P', '1Q', '1R', '1S', '1T', '1U')")
        return value

    @field_validator('safe_harbor_code')
    def safe_harbor_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H']):
            raise ValueError("must be one of enum values ('2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H')")
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
        """Create an instance of OfferAndCoverage from a JSON string"""
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

        # set to None if month (nullable) is None
        # and model_fields_set contains the field
        if self.month is None and "month" in self.model_fields_set:
            _dict['month'] = None

        # set to None if offer_code (nullable) is None
        # and model_fields_set contains the field
        if self.offer_code is None and "offer_code" in self.model_fields_set:
            _dict['offerCode'] = None

        # set to None if share (nullable) is None
        # and model_fields_set contains the field
        if self.share is None and "share" in self.model_fields_set:
            _dict['share'] = None

        # set to None if safe_harbor_code (nullable) is None
        # and model_fields_set contains the field
        if self.safe_harbor_code is None and "safe_harbor_code" in self.model_fields_set:
            _dict['safeHarborCode'] = None

        # set to None if zip_code (nullable) is None
        # and model_fields_set contains the field
        if self.zip_code is None and "zip_code" in self.model_fields_set:
            _dict['zipCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OfferAndCoverage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "month": obj.get("month"),
            "offerCode": obj.get("offerCode"),
            "share": obj.get("share"),
            "safeHarborCode": obj.get("safeHarborCode"),
            "zipCode": obj.get("zipCode")
        })
        return _obj


