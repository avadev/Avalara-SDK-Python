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
from Avalara.SDK.api.EInvoicing.V1.documents_api import DocumentsApi  # noqa: E501


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        load_dotenv()

        # Use the Configuration from Avalara.SDK
        configuration = Configuration(
            environment="sandbox",
            access_token=os.getenv('BEARER_TOKEN')
        )

        # Create an API client using that configuration
        with ApiClient(configuration) as api_client:
            self.api = DocumentsApi(api_client)

    def tearDown(self):
        pass

    def test_get_documents(self):
        try:
            result = self.api.get_document_list("1.2")
            print(result)
            assert result is not None, "Result should not be None"
        except ApiException as e:
            print("Exception when calling DocumentsApi->get_document_list: %s\n" % e)
            assert False

        print("Completed")


if __name__ == '__main__':
    unittest.main()