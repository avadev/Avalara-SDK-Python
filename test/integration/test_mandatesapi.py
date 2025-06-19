from math import fabs
import unittest
import pytest
import ssl
import time

import os
from dotenv import load_dotenv

# Import the specific classes/functions you need rather than `import Avalara.SDK`
from Avalara.SDK.configuration import Configuration
from Avalara.SDK.api_client import ApiClient
from Avalara.SDK.exceptions import ApiException

# Import your generated API module
from Avalara.SDK.api.EInvoicing.V1.mandates_api import MandatesApi  # noqa: E501

import os
from dotenv import load_dotenv

# @pytest.mark.usefixtures("params")
class TestMandatesApi(unittest.TestCase):
    """MandatesApi unit test stubs"""

    def setUp(self):
        load_dotenv()
        # ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
        configuration = Configuration(
            environment="sandbox",
            access_token=os.getenv('BEARER_TOKEN_EINVOICING')
        )
        with ApiClient(configuration) as api_client:
            self.api = MandatesApi(api_client)

    def tearDown(self):
        pass

    def test_get_documents(self):
        try:
            result = self.api.get_mandates("1.2")
            print(result)
            assert result is not None, "Result should not be None"
        except ApiException as e:
            print("Exception when calling MandatesApi->get_mandates: %s\n" % e)
            assert False

        print("Completed")
        pass


if __name__ == '__main__':
    unittest.main()