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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from Avalara.SDK.models.A1099.V2.form1042_s import Form1042S
from Avalara.SDK.models.A1099.V2.form1095_b import Form1095B
from Avalara.SDK.models.A1099.V2.form1095_c import Form1095C
from Avalara.SDK.models.A1099.V2.form1099_div import Form1099Div
from Avalara.SDK.models.A1099.V2.form1099_int import Form1099Int
from Avalara.SDK.models.A1099.V2.form1099_k import Form1099K
from Avalara.SDK.models.A1099.V2.form1099_misc import Form1099Misc
from Avalara.SDK.models.A1099.V2.form1099_nec import Form1099Nec
from Avalara.SDK.models.A1099.V2.form1099_r import Form1099R
from Avalara.SDK.models.A1099.V2.form1099_w2 import Form1099W2
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GET1099FORM200RESPONSE_ONE_OF_SCHEMAS = ["Form1042S", "Form1095B", "Form1095C", "Form1099Div", "Form1099Int", "Form1099K", "Form1099Misc", "Form1099Nec", "Form1099R", "Form1099W2"]

class Get1099Form200Response(BaseModel):
    """
    Get1099Form200Response
    """
    # data type: Form1042S
    oneof_schema_1_validator: Optional[Form1042S] = None
    # data type: Form1095B
    oneof_schema_2_validator: Optional[Form1095B] = None
    # data type: Form1095C
    oneof_schema_3_validator: Optional[Form1095C] = None
    # data type: Form1099Div
    oneof_schema_4_validator: Optional[Form1099Div] = None
    # data type: Form1099Int
    oneof_schema_5_validator: Optional[Form1099Int] = None
    # data type: Form1099K
    oneof_schema_6_validator: Optional[Form1099K] = None
    # data type: Form1099Misc
    oneof_schema_7_validator: Optional[Form1099Misc] = None
    # data type: Form1099Nec
    oneof_schema_8_validator: Optional[Form1099Nec] = None
    # data type: Form1099R
    oneof_schema_9_validator: Optional[Form1099R] = None
    # data type: Form1099W2
    oneof_schema_10_validator: Optional[Form1099W2] = None
    actual_instance: Optional[Union[Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2]] = None
    one_of_schemas: Set[str] = { "Form1042S", "Form1095B", "Form1095C", "Form1099Div", "Form1099Int", "Form1099K", "Form1099Misc", "Form1099Nec", "Form1099R", "Form1099W2" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

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
        instance = Get1099Form200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: Form1042S
        if not isinstance(v, Form1042S):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1042S`")
        else:
            match += 1
        # validate data type: Form1095B
        if not isinstance(v, Form1095B):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1095B`")
        else:
            match += 1
        # validate data type: Form1095C
        if not isinstance(v, Form1095C):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1095C`")
        else:
            match += 1
        # validate data type: Form1099Div
        if not isinstance(v, Form1099Div):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099Div`")
        else:
            match += 1
        # validate data type: Form1099Int
        if not isinstance(v, Form1099Int):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099Int`")
        else:
            match += 1
        # validate data type: Form1099K
        if not isinstance(v, Form1099K):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099K`")
        else:
            match += 1
        # validate data type: Form1099Misc
        if not isinstance(v, Form1099Misc):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099Misc`")
        else:
            match += 1
        # validate data type: Form1099Nec
        if not isinstance(v, Form1099Nec):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099Nec`")
        else:
            match += 1
        # validate data type: Form1099R
        if not isinstance(v, Form1099R):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099R`")
        else:
            match += 1
        # validate data type: Form1099W2
        if not isinstance(v, Form1099W2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Form1099W2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Get1099Form200Response with oneOf schemas: Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Get1099Form200Response with oneOf schemas: Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2. Details: " + ", ".join(error_messages))
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

        # deserialize data into Form1042S
        try:
            instance.actual_instance = Form1042S.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1095B
        try:
            instance.actual_instance = Form1095B.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1095C
        try:
            instance.actual_instance = Form1095C.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099Div
        try:
            instance.actual_instance = Form1099Div.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099Int
        try:
            instance.actual_instance = Form1099Int.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099K
        try:
            instance.actual_instance = Form1099K.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099Misc
        try:
            instance.actual_instance = Form1099Misc.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099Nec
        try:
            instance.actual_instance = Form1099Nec.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099R
        try:
            instance.actual_instance = Form1099R.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Form1099W2
        try:
            instance.actual_instance = Form1099W2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Get1099Form200Response with oneOf schemas: Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Get1099Form200Response with oneOf schemas: Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], Form1042S, Form1095B, Form1095C, Form1099Div, Form1099Int, Form1099K, Form1099Misc, Form1099Nec, Form1099R, Form1099W2]]:
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


