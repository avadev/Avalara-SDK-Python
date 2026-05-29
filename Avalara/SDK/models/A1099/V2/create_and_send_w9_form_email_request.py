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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from Avalara.SDK.models.A1099.V2.w4_form_minimal_request import W4FormMinimalRequest
from Avalara.SDK.models.A1099.V2.w8_ben_e_form_minimal_request import W8BenEFormMinimalRequest
from Avalara.SDK.models.A1099.V2.w8_ben_form_minimal_request import W8BenFormMinimalRequest
from Avalara.SDK.models.A1099.V2.w8_imy_form_minimal_request import W8ImyFormMinimalRequest
from Avalara.SDK.models.A1099.V2.w9_form_minimal_request import W9FormMinimalRequest
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CREATEANDSENDW9FORMEMAILREQUEST_ONE_OF_SCHEMAS = ["W4FormMinimalRequest", "W8BenEFormMinimalRequest", "W8BenFormMinimalRequest", "W8ImyFormMinimalRequest", "W9FormMinimalRequest"]

class CreateAndSendW9FormEmailRequest(BaseModel):
    """
    CreateAndSendW9FormEmailRequest
    """
    # data type: W4FormMinimalRequest
    oneof_schema_1_validator: Optional[W4FormMinimalRequest] = None
    # data type: W8BenEFormMinimalRequest
    oneof_schema_2_validator: Optional[W8BenEFormMinimalRequest] = None
    # data type: W8BenFormMinimalRequest
    oneof_schema_3_validator: Optional[W8BenFormMinimalRequest] = None
    # data type: W8ImyFormMinimalRequest
    oneof_schema_4_validator: Optional[W8ImyFormMinimalRequest] = None
    # data type: W9FormMinimalRequest
    oneof_schema_5_validator: Optional[W9FormMinimalRequest] = None
    actual_instance: Optional[Union[W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest]] = None
    one_of_schemas: Set[str] = { "W4FormMinimalRequest", "W8BenEFormMinimalRequest", "W8BenFormMinimalRequest", "W8ImyFormMinimalRequest", "W9FormMinimalRequest" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CreateAndSendW9FormEmailRequest.model_construct()
        error_messages = []
        match = 0
        # validate data type: W4FormMinimalRequest
        if not isinstance(v, W4FormMinimalRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `W4FormMinimalRequest`")
        else:
            match += 1
        # validate data type: W8BenEFormMinimalRequest
        if not isinstance(v, W8BenEFormMinimalRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `W8BenEFormMinimalRequest`")
        else:
            match += 1
        # validate data type: W8BenFormMinimalRequest
        if not isinstance(v, W8BenFormMinimalRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `W8BenFormMinimalRequest`")
        else:
            match += 1
        # validate data type: W8ImyFormMinimalRequest
        if not isinstance(v, W8ImyFormMinimalRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `W8ImyFormMinimalRequest`")
        else:
            match += 1
        # validate data type: W9FormMinimalRequest
        if not isinstance(v, W9FormMinimalRequest):
            error_messages.append(f"Error! Input type `{type(v)}` is not `W9FormMinimalRequest`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateAndSendW9FormEmailRequest with oneOf schemas: W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateAndSendW9FormEmailRequest with oneOf schemas: W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into W4FormMinimalRequest
        try:
            instance.actual_instance = W4FormMinimalRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into W8BenEFormMinimalRequest
        try:
            instance.actual_instance = W8BenEFormMinimalRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into W8BenFormMinimalRequest
        try:
            instance.actual_instance = W8BenFormMinimalRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into W8ImyFormMinimalRequest
        try:
            instance.actual_instance = W8ImyFormMinimalRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into W9FormMinimalRequest
        try:
            instance.actual_instance = W9FormMinimalRequest.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateAndSendW9FormEmailRequest with oneOf schemas: W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateAndSendW9FormEmailRequest with oneOf schemas: W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], W4FormMinimalRequest, W8BenEFormMinimalRequest, W8BenFormMinimalRequest, W8ImyFormMinimalRequest, W9FormMinimalRequest]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


