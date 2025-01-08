from math import fabs
import unittest
import pytest
import ssl
import time
import Avalara.SDK
from Avalara.SDK import api_client
from Avalara.SDK.api.Avatax.V2.utilities_api import UtilitiesApi  # noqa: E501
from Avalara.SDK.oauth_helper import AvalaraOauth2Client

import os
from dotenv import load_dotenv

# @pytest.mark.usefixtures("params")
class TestOAuthDevice(unittest.TestCase):
    """OAuthDevice unit test stubs"""

    def setUp(self):
        load_dotenv()
        # ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
        configuration = Avalara.SDK.Configuration(
            # access_token="",
            # api_key="",
            environment="qa",
            client_id=os.getenv('CLIENT_ID'),
            client_secret="",
        )
        with Avalara.SDK.ApiClient(configuration) as api_client:
            self.api = UtilitiesApi(api_client)

    def tearDown(self):
        pass

    def test_device_flow(self):
        outh2_client = self.api.api_client.configuration.outh2_client
        device_auth_info = outh2_client.initiate_device_authorization_flow()
        access_token_info = outh2_client.get_access_token_for_device_flow(
            device_auth_info["device_code"]
        )
        assert access_token_info["error"] == "authorization_pending"


if __name__ == '__main__':
    unittest.main()