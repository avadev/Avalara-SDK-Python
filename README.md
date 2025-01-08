# Avalara.SDK
API for evaluating transactions against direct-to-consumer Beverage Alcohol shipping regulations.

This API is currently in beta.


- Package version: 2.4.29

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import Avalara.SDK
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import Avalara.SDK
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import Avalara.SDK
from Avalara.SDK.api import addresses_api
from Avalara.SDK.model.address_validation_info import AddressValidationInfo
from Avalara.SDK.model.address_resolution_model import AddressResolutionModel
from pprint import pprint
    
# Define configuration object with parameters specified to your application.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    client_id='<Your Avalara Identity Client Id>'
    client_secret='<Your Avalara Identity Client Secret>'
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = AddressValidationInfo(
        line1="2000 Main Street",
        text_case="Upper",
        line2="line2_example",
        line3="line3_example",
        city="Irvine",
        region="CA",
        country="US",
        postal_code="92614",
        latitude=3.14,
        longitude=3.14,
    ) # AddressValidationInfo | The address to resolve (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve geolocation information for a specified address
        api_response = api_instance.resolve_address_post(x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AddressesApi->resolve_address_post: %s\n" % e)
```

## Documentation For Authorization

Authentication schemes defined for the API:
<a name="OAuth Client Credentials Flow"></a>
### OAuth Client Credentials

- **Type**: OAuth
- **Flow**: client_credentials
- **Scopes**: 
  - avatax_api: avatax_api scope.

```python
import time
import Avalara.SDK
from Avalara.SDK.api import addresses_api
from Avalara.SDK.model.address_validation_info import AddressValidationInfo
from Avalara.SDK.model.address_resolution_model import AddressResolutionModel
from pprint import pprint
    
# Define configuration object with parameters specified to your application.
# Passing in client_id and client_secret will setup the OAuth Client Credentials flow to automatically be handled by the SDK for the caller.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    client_id='<Your Avalara Identity Client Id>'
    client_secret='<Your Avalara Identity Client Secret>'
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = AddressValidationInfo(
        line1="2000 Main Street",
        text_case="Upper",
        line2="line2_example",
        line3="line3_example",
        city="Irvine",
        region="CA",
        country="US",
        postal_code="92614",
        latitude=3.14,
        longitude=3.14,
    ) # AddressValidationInfo | The address to resolve (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # When the api call is made, the OAuth2 Token endpoint will automatically be called using
        # The client_id and client_secret from the configuration object and the bearer token will be
        # appended to the Authorization header in the request.
        api_response = api_instance.resolve_address_post(x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AddressesApi->resolve_address_post: %s\n" % e)
```

<a name="OAuth Device Code Flow"></a>
### OAuth Device Code

- **Type**: OAuth
- **Flow**: device_code
- **Scopes**: 
  - avatax_api: avatax_api scope.

```python
import time
import Avalara.SDK
from Avalara.SDK.api import addresses_api
from Avalara.SDK.model.address_validation_info import AddressValidationInfo
from Avalara.SDK.model.address_resolution_model import AddressResolutionModel
from pprint import pprint
    
# Define configuration object with parameters specified to your application.
# Passing in client_id will be used in the OAuth2 Device code flow to fetch the device token.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    client_id='<Your Avalara Identity Client Id>'
    environment='sandbox'
)
# Get a reference to the oauth2 client
outh2_client = self.api.api_client.configuration.outh2_client
# Initiate the device code flow (device_authorization endpoint call)
device_auth_info = outh2_client.initiate_device_authorization_flow()
# Use the device code to poll the token endpoint (this needs to be handled by the client application)
# as the user authenticating in the browser is an offline process.
# Until the user has completed, this call will return 'authorization_pending' as follows:
# access_token_info["error"] == "authorization_pending"
access_token_info = outh2_client.get_access_token_for_device_flow(
    device_auth_info["device_code"]
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"
    body = AddressValidationInfo(
        line1="2000 Main Street",
        text_case="Upper",
        line2="line2_example",
        line3="line3_example",
        city="Irvine",
        region="CA",
        country="US",
        postal_code="92614",
        latitude=3.14,
        longitude=3.14,
    ) # AddressValidationInfo | The address to resolve (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # When the api call is made, the OAuth2 Token endpoint will automatically be called using
        # The Bearer Token from the Device Code flow will automatically be appended into the Authorization Header
        # for the request once the offline user authentication in the browser is complete and the get_access_token_for_device_flow method
        # has been called successfully.
        api_response = api_instance.resolve_address_post(x_avalara_client=x_avalara_client, body=body)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling AddressesApi->resolve_address_post: %s\n" % e)
```

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

<a name="documentation-for-EInvoicing-V1-api-endpoints"></a>
### EInvoicing V1 API Documentation

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataInputFieldsApi* | [**get_data_input_fields**](docs/EInvoicing/V1/DataInputFieldsApi.md#get_data_input_fields) | **GET** /data-input-fields | Returns the mandatory and conditional invoice or creditnote input fields for different country mandates
*DocumentsApi* | [**download_document**](docs/EInvoicing/V1/DocumentsApi.md#download_document) | **GET** /documents/{documentId}/$download | Returns a copy of the document
*DocumentsApi* | [**get_document_list**](docs/EInvoicing/V1/DocumentsApi.md#get_document_list) | **GET** /documents | Returns a summary of documents for a date range
*DocumentsApi* | [**get_document_status**](docs/EInvoicing/V1/DocumentsApi.md#get_document_status) | **GET** /document/{documentId}/status | Checks the status of a document
*DocumentsApi* | [**submit_document**](docs/EInvoicing/V1/DocumentsApi.md#submit_document) | **POST** /documents | Submits a document to Avalara E-Invoicing API
*MandatesApi* | [**get_mandates**](docs/EInvoicing/V1/MandatesApi.md#get_mandates) | **GET** /mandates | List country mandates that are supported by the Avalara E-Invoicing platform

<a name="documentation-for-models"></a>
## Documentation for Models

<a name="documentation-for-EInvoicing-V1-models"></a>
### EInvoicing V1 Model Documentation

 - [Avalara.SDK.model.BadDownloadRequest](docs/EInvoicing/V1/BadDownloadRequest.md)
 - [Avalara.SDK.model.BadRequest](docs/EInvoicing/V1/BadRequest.md)
 - [Avalara.SDK.model.ConditionalForField](docs/EInvoicing/V1/ConditionalForField.md)
 - [Avalara.SDK.model.DataInputField](docs/EInvoicing/V1/DataInputField.md)
 - [Avalara.SDK.model.DataInputFieldNotUsedFor](docs/EInvoicing/V1/DataInputFieldNotUsedFor.md)
 - [Avalara.SDK.model.DataInputFieldOptionalFor](docs/EInvoicing/V1/DataInputFieldOptionalFor.md)
 - [Avalara.SDK.model.DataInputFieldRequiredFor](docs/EInvoicing/V1/DataInputFieldRequiredFor.md)
 - [Avalara.SDK.model.DataInputFieldsResponse](docs/EInvoicing/V1/DataInputFieldsResponse.md)
 - [Avalara.SDK.model.DocumentListResponse](docs/EInvoicing/V1/DocumentListResponse.md)
 - [Avalara.SDK.model.DocumentStatusResponse](docs/EInvoicing/V1/DocumentStatusResponse.md)
 - [Avalara.SDK.model.DocumentSubmissionError](docs/EInvoicing/V1/DocumentSubmissionError.md)
 - [Avalara.SDK.model.DocumentSubmitResponse](docs/EInvoicing/V1/DocumentSubmitResponse.md)
 - [Avalara.SDK.model.DocumentSummary](docs/EInvoicing/V1/DocumentSummary.md)
 - [Avalara.SDK.model.ForbiddenError](docs/EInvoicing/V1/ForbiddenError.md)
 - [Avalara.SDK.model.InputDataFormats](docs/EInvoicing/V1/InputDataFormats.md)
 - [Avalara.SDK.model.InternalServerError](docs/EInvoicing/V1/InternalServerError.md)
 - [Avalara.SDK.model.Mandate](docs/EInvoicing/V1/Mandate.md)
 - [Avalara.SDK.model.MandatesResponse](docs/EInvoicing/V1/MandatesResponse.md)
 - [Avalara.SDK.model.NotFoundError](docs/EInvoicing/V1/NotFoundError.md)
 - [Avalara.SDK.model.NotUsedForField](docs/EInvoicing/V1/NotUsedForField.md)
 - [Avalara.SDK.model.RequiredWhenField](docs/EInvoicing/V1/RequiredWhenField.md)
 - [Avalara.SDK.model.StatusEvent](docs/EInvoicing/V1/StatusEvent.md)
 - [Avalara.SDK.model.WorkflowIds](docs/EInvoicing/V1/WorkflowIds.md)
