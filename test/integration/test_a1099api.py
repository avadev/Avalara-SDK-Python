from math import fabs
import unittest
import pytest
import ssl
import time
import os
from dotenv import load_dotenv
import uuid

# Import Configuration, ApiClient, and exceptions
from Avalara.SDK.configuration import Configuration
from Avalara.SDK.api_client import ApiClient
from Avalara.SDK.exceptions import ApiException

# Import the specific A1099 APIs
from Avalara.SDK.api.A1099.V2.issuers1099_api import Issuers1099Api
from Avalara.SDK.api.A1099.V2.companies_w9_api import CompaniesW9Api
from Avalara.SDK.api.A1099.V2.forms1099_api import Forms1099Api

class TestA1099Api(unittest.TestCase):
    """A1099Api unit test stubs"""

    def setUp(self):
        load_dotenv()

        bearer_token = os.getenv('BEARER_TOKEN_A1099')
        # Configure with the A1099 bearer token
        configuration = Configuration(
            environment="sandbox",
            access_token=bearer_token
        )

        # Create an API client for all tests
        self.api_client = ApiClient(configuration)
        self.issuers_api = Issuers1099Api(self.api_client)
        self.companies_api = CompaniesW9Api(self.api_client)
        self.forms_api = Forms1099Api(self.api_client)

    def tearDown(self):
        pass

    def test_get_issuers(self):
        """Test the GetIssuers endpoint returns data"""
        try:
            correlation_id = str(uuid.uuid4())
            result = self.issuers_api.get_issuers("2.0", correlation_id)
            print(result)
            assert result is not None, "Expected non-null issuers list"
        except ApiException as e:
            print(f"Exception when calling Issuers1099Api->get_issuers: {e}\n")
            assert False
        print("Completed get_issuers test")

    def test_get_companies(self):
        """Test the GetCompanies endpoint returns data"""
        try:
            correlation_id = str(uuid.uuid4())
            result = self.companies_api.get_companies("2.0", correlation_id)
            print(result)
            assert result is not None, "Expected non-null companies list"
        except ApiException as e:
            print(f"Exception when calling CompaniesW9Api->get_companies: {e}\n")
            assert False
        print("Completed get_companies test")

    def test_list_1099_forms(self):
        """Test the List1099Forms endpoint returns data"""
        try:
            correlation_id = str(uuid.uuid4())
            result = self.forms_api.list1099_forms("2.0", correlation_id)
            print(result)
            assert result is not None, "Expected non-null 1099 forms list"
        except ApiException as e:
            print(f"Exception when calling Forms1099Api->list_1099_forms: {e}\n")
            assert False
        print("Completed list_1099_forms test")

if __name__ == '__main__':
    unittest.main()
