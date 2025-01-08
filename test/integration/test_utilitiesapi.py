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
class TestUtilitiesApi(unittest.TestCase):
    """UtilitiesApi unit test stubs"""

    def setUp(self):
        load_dotenv()
        # ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
        configuration = Avalara.SDK.Configuration(
            # access_token="",
            # api_key="",
            environment="qa",
            client_id="",
            client_secret="",
            access_token=os.getenv('BEARER_TOKEN')
        )
        with Avalara.SDK.ApiClient(configuration) as api_client:
            self.api = UtilitiesApi(api_client)

    def tearDown(self):
        pass

    def test_ping_utility(self):
        try:

            # thread = self.api.ping(async_req=True)
            # result = thread.get()
            result = self.api.ping(async_req=False)
            assert result.authenticated == True
        except Avalara.SDK.ApiException as e:
            print("Exception when calling UtilitiesApi->ping: %s\n" % e)
            assert False

        print("Completed")
        pass


if __name__ == '__main__':
    unittest.main()
