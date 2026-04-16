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

    Avalara E-Invoicing API
    An API that supports sending data for an E-Invoicing compliance use-case. 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    26.4.0
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from Avalara.SDK.models.EInvoicing.V1.code_list_value import CodeListValue
from typing import Optional, Set
from typing_extensions import Self

class CodeListVersion(BaseModel):
    """
    Represents a versioned definition of a code list for a specific jurisdiction and date range
    """ # noqa: E501
    version_reasons: Optional[List[StrictStr]] = Field(default=None, description="List of free-text reasons explaining why this version of the code list exists (for example, initial introduction, regulatory update, addition/deprecation of codes). Useful for audit and change tracking.", alias="versionReasons")
    juris_effective_date: Optional[date] = Field(default=None, description="Date from which this version of the code list becomes legally or operationally effective in the jurisdiction. Typically corresponds to a go-live, mandate, or release date.", alias="jurisEffectiveDate")
    juris_sunset_date: Optional[date] = Field(default=None, description="Date after which this version of the code list must no longer be used in the jurisdiction. Use a far-future date (e.g., 9999-12-31) when the sunset is not yet known.", alias="jurisSunsetDate")
    locale: Optional[StrictStr] = Field(default=None, description="Language–region locale identifier indicating the language and regional variant for descriptions in this version of the code list. Follows BCP-47 format such as en-US, fr-FR, de-DE.")
    values: Optional[List[CodeListValue]] = Field(default=None, description="Array of code entries defined in this version of the code list. Each entry contains the machine-readable code value and its human-readable description in the given locale.")
    __properties: ClassVar[List[str]] = ["versionReasons", "jurisEffectiveDate", "jurisSunsetDate", "locale", "values"]

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
        """Create an instance of CodeListVersion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeListVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "versionReasons": obj.get("versionReasons"),
            "jurisEffectiveDate": obj.get("jurisEffectiveDate"),
            "jurisSunsetDate": obj.get("jurisSunsetDate"),
            "locale": obj.get("locale"),
            "values": [CodeListValue.from_dict(_item) for _item in obj["values"]] if obj.get("values") is not None else None
        })
        return _obj


