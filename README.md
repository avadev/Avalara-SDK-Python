# Avalara.SDK - the Unified Java SDK for next gen Avalara services.

Unified SDK consists of services on top of which the Avalara Compliance Cloud platform is built. These services are foundational and provide functionality such as einvoicing.

## Requirements.

Python >= 3.6

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install Avalara.SDK==24.12.1
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

### Running SDK unit tests

```sh
pip install -r test-requirements.txt
pytest
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
from Avalara.SDK.configuration import Configuration
from Avalara.SDK.api_client import ApiClient
from Avalara.SDK.exceptions import ApiException
from Avalara.SDK.api.EInvoicing.V1.mandates_api import MandatesApi  # noqa: E501
from pprint import pprint

# Define configuration object with parameters specified to your application.
configuration = Configuration(
    app_name='test app',
    app_version='1.0',
    machine_name='some machine',
    access_token='',
    environment='sandbox'
)
# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MandatesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve geolocation information for a specified address
        api_response = api_instance.get_mandates(avalara_version="1.2", x_avalara_client=x_avalara_client)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MandatesApi->get_mandates: %s\n" % e)
```

## Documentation for API Endpoints

<a name="documentation-for-EInvoicing-V1-api-endpoints"></a>

### EInvoicing V1 API Documentation

| Class                | Method                                                                                                    | HTTP request                                                    | Description                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| _DataInputFieldsApi_ | [**get_data_input_fields**](docs/EInvoicing/V1/DataInputFieldsApi.md#get_data_input_fields)               | **GET** /data-input-fields                                      | Returns the optionality of document fields for different country mandates                               |
| _DocumentsApi_       | [**download_document**](docs/EInvoicing/V1/DocumentsApi.md#download_document)                             | **GET** /documents/{documentId}/$download                       | Returns a copy of the document                                                                          |
| _DocumentsApi_       | [**fetch_documents**](docs/EInvoicing/V1/DocumentsApi.md#fetch_documents)                                 | **POST** /documents/$fetch                                      | Fetch the inbound document from a tax authority                                                         |
| _DocumentsApi_       | [**get_document_list**](docs/EInvoicing/V1/DocumentsApi.md#get_document_list)                             | **GET** /documents                                              | Returns a summary of documents for a date range                                                         |
| _DocumentsApi_       | [**get_document_status**](docs/EInvoicing/V1/DocumentsApi.md#get_document_status)                         | **GET** /documents/{documentId}/status                          | Checks the status of a document                                                                         |
| _DocumentsApi_       | [**submit_document**](docs/EInvoicing/V1/DocumentsApi.md#submit_document)                                 | **POST** /documents                                             | Submits a document to Avalara E-Invoicing API                                                           |
| _InteropApi_         | [**submit_interop_document**](docs/EInvoicing/V1/InteropApi.md#submit_interop_document)                   | **POST** /interop/documents                                     | Submit a document                                                                                       |
| _MandatesApi_        | [**get_mandate_data_input_fields**](docs/EInvoicing/V1/MandatesApi.md#get_mandate_data_input_fields)      | **GET** /mandates/{mandateId}/data-input-fields                 | Returns document field information for a country mandate, a selected document type, and its version     |
| _MandatesApi_        | [**get_mandates**](docs/EInvoicing/V1/MandatesApi.md#get_mandates)                                        | **GET** /mandates                                               | List country mandates that are supported by the Avalara E-Invoicing platform                            |
| _TradingPartnersApi_ | [**batch_search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#batch_search_participants)       | **POST** /trading-partners/batch-searches                       | Creates a batch search and performs a batch search in the directory for participants in the background. |
| _TradingPartnersApi_ | [**download_batch_search_report**](docs/EInvoicing/V1/TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Download batch search results in a csv file.                                                            |
| _TradingPartnersApi_ | [**get_batch_search_detail**](docs/EInvoicing/V1/TradingPartnersApi.md#get_batch_search_detail)           | **GET** /trading-partners/batch-searches/{id}                   | Get the batch search details for a given id.                                                            |
| _TradingPartnersApi_ | [**list_batch_searches**](docs/EInvoicing/V1/TradingPartnersApi.md#list_batch_searches)                   | **GET** /trading-partners/batch-searches                        | List all batch searches that were previously submitted.                                                 |
| _TradingPartnersApi_ | [**search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#search_participants)                   | **GET** /trading-partners                                       | Returns a list of participants matching the input query.                                                |

<a name="documentation-for-models"></a>

## Documentation for Models

<a name="documentation-for-EInvoicing-V1-models"></a>

### EInvoicing V1 Model Documentation

- [Avalara.SDK.models.EInvoicing.V1.BadDownloadRequest](docs/EInvoicing/V1/BadDownloadRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.BadRequest](docs/EInvoicing/V1/BadRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.BatchSearch](docs/EInvoicing/V1/BatchSearch.md)
- [Avalara.SDK.models.EInvoicing.V1.BatchSearchListResponse](docs/EInvoicing/V1/BatchSearchListResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.ConditionalForField](docs/EInvoicing/V1/ConditionalForField.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputField](docs/EInvoicing/V1/DataInputField.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldNotUsedFor](docs/EInvoicing/V1/DataInputFieldNotUsedFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldOptionalFor](docs/EInvoicing/V1/DataInputFieldOptionalFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldRequiredFor](docs/EInvoicing/V1/DataInputFieldRequiredFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldsResponse](docs/EInvoicing/V1/DataInputFieldsResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponse](docs/EInvoicing/V1/DirectorySearchResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInner](docs/EInvoicing/V1/DirectorySearchResponseValueInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerAddressesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerAddressesInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerIdentifiersInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerIdentifiersInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerSupportedDocumentTypesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerSupportedDocumentTypesInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetch](docs/EInvoicing/V1/DocumentFetch.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequest](docs/EInvoicing/V1/DocumentFetchRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequestDataInner](docs/EInvoicing/V1/DocumentFetchRequestDataInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequestMetadata](docs/EInvoicing/V1/DocumentFetchRequestMetadata.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentListResponse](docs/EInvoicing/V1/DocumentListResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentStatusResponse](docs/EInvoicing/V1/DocumentStatusResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSubmissionError](docs/EInvoicing/V1/DocumentSubmissionError.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSubmitResponse](docs/EInvoicing/V1/DocumentSubmitResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSummary](docs/EInvoicing/V1/DocumentSummary.md)
- [Avalara.SDK.models.EInvoicing.V1.ErrorResponse](docs/EInvoicing/V1/ErrorResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.ForbiddenError](docs/EInvoicing/V1/ForbiddenError.md)
- [Avalara.SDK.models.EInvoicing.V1.InputDataFormats](docs/EInvoicing/V1/InputDataFormats.md)
- [Avalara.SDK.models.EInvoicing.V1.InternalServerError](docs/EInvoicing/V1/InternalServerError.md)
- [Avalara.SDK.models.EInvoicing.V1.Mandate](docs/EInvoicing/V1/Mandate.md)
- [Avalara.SDK.models.EInvoicing.V1.MandateDataInputField](docs/EInvoicing/V1/MandateDataInputField.md)
- [Avalara.SDK.models.EInvoicing.V1.MandateDataInputFieldNamespace](docs/EInvoicing/V1/MandateDataInputFieldNamespace.md)
- [Avalara.SDK.models.EInvoicing.V1.MandatesResponse](docs/EInvoicing/V1/MandatesResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.NotFoundError](docs/EInvoicing/V1/NotFoundError.md)
- [Avalara.SDK.models.EInvoicing.V1.NotUsedForField](docs/EInvoicing/V1/NotUsedForField.md)
- [Avalara.SDK.models.EInvoicing.V1.RequiredWhenField](docs/EInvoicing/V1/RequiredWhenField.md)
- [Avalara.SDK.models.EInvoicing.V1.StatusEvent](docs/EInvoicing/V1/StatusEvent.md)
- [Avalara.SDK.models.EInvoicing.V1.SubmitDocumentMetadata](docs/EInvoicing/V1/SubmitDocumentMetadata.md)
- [Avalara.SDK.models.EInvoicing.V1.SubmitInteropDocument202Response](docs/EInvoicing/V1/SubmitInteropDocument202Response.md)
- [Avalara.SDK.models.EInvoicing.V1.WorkflowIds](docs/EInvoicing/V1/WorkflowIds.md)
<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

<a name="documentation-for-EInvoicing-V1-api-endpoints"></a>
### EInvoicing V1 API Documentation

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataInputFieldsApi* | [**get_data_input_fields**](docs/EInvoicing/V1/DataInputFieldsApi.md#get_data_input_fields) | **GET** /data-input-fields | Returns the optionality of document fields for different country mandates
*DocumentsApi* | [**download_document**](docs/EInvoicing/V1/DocumentsApi.md#download_document) | **GET** /documents/{documentId}/$download | Returns a copy of the document
*DocumentsApi* | [**fetch_documents**](docs/EInvoicing/V1/DocumentsApi.md#fetch_documents) | **POST** /documents/$fetch | Fetch the inbound document from a tax authority
*DocumentsApi* | [**get_document_list**](docs/EInvoicing/V1/DocumentsApi.md#get_document_list) | **GET** /documents | Returns a summary of documents for a date range
*DocumentsApi* | [**get_document_status**](docs/EInvoicing/V1/DocumentsApi.md#get_document_status) | **GET** /documents/{documentId}/status | Checks the status of a document
*DocumentsApi* | [**submit_document**](docs/EInvoicing/V1/DocumentsApi.md#submit_document) | **POST** /documents | Submits a document to Avalara E-Invoicing API
*InteropApi* | [**submit_interop_document**](docs/EInvoicing/V1/InteropApi.md#submit_interop_document) | **POST** /interop/documents | Submit a document
*MandatesApi* | [**get_mandate_data_input_fields**](docs/EInvoicing/V1/MandatesApi.md#get_mandate_data_input_fields) | **GET** /mandates/{mandateId}/data-input-fields | Returns document field information for a country mandate, a selected document type, and its version
*MandatesApi* | [**get_mandates**](docs/EInvoicing/V1/MandatesApi.md#get_mandates) | **GET** /mandates | List country mandates that are supported by the Avalara E-Invoicing platform
*SubscriptionsApi* | [**create_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#create_webhook_subscription) | **POST** /webhooks/subscriptions | Create a subscription to events
*SubscriptionsApi* | [**delete_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /webhooks/subscriptions/{subscription-id} | Unsubscribe from events
*SubscriptionsApi* | [**get_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#get_webhook_subscription) | **GET** /webhooks/subscriptions/{subscription-id} | Get details of a subscription
*SubscriptionsApi* | [**list_webhook_subscriptions**](docs/EInvoicing/V1/SubscriptionsApi.md#list_webhook_subscriptions) | **GET** /webhooks/subscriptions | List all subscriptions
*TradingPartnersApi* | [**batch_search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#batch_search_participants) | **POST** /trading-partners/batch-searches | Creates a batch search and performs a batch search in the directory for participants in the background.
*TradingPartnersApi* | [**download_batch_search_report**](docs/EInvoicing/V1/TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Download batch search results in a csv file.
*TradingPartnersApi* | [**get_batch_search_detail**](docs/EInvoicing/V1/TradingPartnersApi.md#get_batch_search_detail) | **GET** /trading-partners/batch-searches/{id} | Get the batch search details for a given id.
*TradingPartnersApi* | [**list_batch_searches**](docs/EInvoicing/V1/TradingPartnersApi.md#list_batch_searches) | **GET** /trading-partners/batch-searches | List all batch searches that were previously submitted.
*TradingPartnersApi* | [**search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#search_participants) | **GET** /trading-partners | Returns a list of participants matching the input query.

<a name="documentation-for-A1099-V2-api-endpoints"></a>
### A1099 V2 API Documentation

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompaniesW9Api* | [**create_company**](docs/A1099/V2/CompaniesW9Api.md#create_company) | **POST** /w9/companies | Creates a new company
*CompaniesW9Api* | [**delete_company**](docs/A1099/V2/CompaniesW9Api.md#delete_company) | **DELETE** /w9/companies/{id} | Deletes a company
*CompaniesW9Api* | [**get_companies**](docs/A1099/V2/CompaniesW9Api.md#get_companies) | **GET** /w9/companies | List companies
*CompaniesW9Api* | [**get_company**](docs/A1099/V2/CompaniesW9Api.md#get_company) | **GET** /w9/companies/{id} | Retrieve a company
*CompaniesW9Api* | [**update_company**](docs/A1099/V2/CompaniesW9Api.md#update_company) | **PUT** /w9/companies/{id} | Update a company
*Forms1099Api* | [**bulk_upsert1099_forms**](docs/A1099/V2/Forms1099Api.md#bulk_upsert1099_forms) | **POST** /1099/forms/$bulk-upsert | Creates or updates multiple 1099 forms.
*Forms1099Api* | [**create1099_form**](docs/A1099/V2/Forms1099Api.md#create1099_form) | **POST** /1099/forms | Creates a 1099 form.
*Forms1099Api* | [**delete1099_form**](docs/A1099/V2/Forms1099Api.md#delete1099_form) | **DELETE** /1099/forms/{id} | Deletes a 1099 form.
*Forms1099Api* | [**get1099_form**](docs/A1099/V2/Forms1099Api.md#get1099_form) | **GET** /1099/forms/{id} | Retrieves a 1099 form.
*Forms1099Api* | [**get1099_form_pdf**](docs/A1099/V2/Forms1099Api.md#get1099_form_pdf) | **GET** /1099/forms/{id}/pdf | Retrieves the PDF file for a single 1099 by form id.
*Forms1099Api* | [**list1099_forms**](docs/A1099/V2/Forms1099Api.md#list1099_forms) | **GET** /1099/forms | Retrieves a list of 1099 forms based on query parameters.
*Forms1099Api* | [**update1099_form**](docs/A1099/V2/Forms1099Api.md#update1099_form) | **PUT** /1099/forms/{id} | Updates a 1099 form.
*FormsW9Api* | [**create_w9_form**](docs/A1099/V2/FormsW9Api.md#create_w9_form) | **POST** /w9/forms | Create a W9/W4/W8 form
*FormsW9Api* | [**delete_w9_form**](docs/A1099/V2/FormsW9Api.md#delete_w9_form) | **DELETE** /w9/forms/{id} | Delete a form
*FormsW9Api* | [**get_w9_form**](docs/A1099/V2/FormsW9Api.md#get_w9_form) | **GET** /w9/forms/{id} | Retrieve a W9/W4/W8 form
*FormsW9Api* | [**list_w9_forms**](docs/A1099/V2/FormsW9Api.md#list_w9_forms) | **GET** /w9/forms | List W9/W4/W8 forms.
*FormsW9Api* | [**send_w9_form_email**](docs/A1099/V2/FormsW9Api.md#send_w9_form_email) | **POST** /w9/forms/{id}/$send-email | Sends a W9 email request to a vendor/payee
*FormsW9Api* | [**update_w9_form**](docs/A1099/V2/FormsW9Api.md#update_w9_form) | **PUT** /w9/forms/{id} | Update a W9/W4/W8 form
*FormsW9Api* | [**upload_w9_files**](docs/A1099/V2/FormsW9Api.md#upload_w9_files) | **PUT** /w9/forms/{id}/attachment | Upload files for a W9/W4/W8 form
*Issuers1099Api* | [**create_issuer**](docs/A1099/V2/Issuers1099Api.md#create_issuer) | **POST** /1099/issuers | Create an issuer
*Issuers1099Api* | [**delete_issuer**](docs/A1099/V2/Issuers1099Api.md#delete_issuer) | **DELETE** /1099/issuers/{id} | Delete an issuer
*Issuers1099Api* | [**get_issuer**](docs/A1099/V2/Issuers1099Api.md#get_issuer) | **GET** /1099/issuers/{id} | Get an issuer
*Issuers1099Api* | [**get_issuers**](docs/A1099/V2/Issuers1099Api.md#get_issuers) | **GET** /1099/issuers | List issuers
*Issuers1099Api* | [**update_issuer**](docs/A1099/V2/Issuers1099Api.md#update_issuer) | **PUT** /1099/issuers/{id} | Update an issuer
*Jobs1099Api* | [**get_job**](docs/A1099/V2/Jobs1099Api.md#get_job) | **GET** /1099/jobs/{id} | Retrieves information about the job

<a name="documentation-for-models"></a>
## Documentation for Models

<a name="documentation-for-EInvoicing-V1-models"></a>
### EInvoicing V1 Model Documentation

 - [Avalara.SDK.models.EInvoicing.V1.BadDownloadRequest](docs/EInvoicing/V1/BadDownloadRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.BadRequest](docs/EInvoicing/V1/BadRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearch](docs/EInvoicing/V1/BatchSearch.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearchListResponse](docs/EInvoicing/V1/BatchSearchListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearchParticipants202Response](docs/EInvoicing/V1/BatchSearchParticipants202Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.ConditionalForField](docs/EInvoicing/V1/ConditionalForField.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputField](docs/EInvoicing/V1/DataInputField.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldNotUsedFor](docs/EInvoicing/V1/DataInputFieldNotUsedFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldOptionalFor](docs/EInvoicing/V1/DataInputFieldOptionalFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldRequiredFor](docs/EInvoicing/V1/DataInputFieldRequiredFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldsResponse](docs/EInvoicing/V1/DataInputFieldsResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponse](docs/EInvoicing/V1/DirectorySearchResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInner](docs/EInvoicing/V1/DirectorySearchResponseValueInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerAddressesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerAddressesInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerIdentifiersInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerIdentifiersInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerSupportedDocumentTypesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerSupportedDocumentTypesInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentFetch](docs/EInvoicing/V1/DocumentFetch.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentListResponse](docs/EInvoicing/V1/DocumentListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentStatusResponse](docs/EInvoicing/V1/DocumentStatusResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentSubmissionError](docs/EInvoicing/V1/DocumentSubmissionError.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentSubmitResponse](docs/EInvoicing/V1/DocumentSubmitResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.DocumentSummary](docs/EInvoicing/V1/DocumentSummary.md)
 - [Avalara.SDK.models.EInvoicing.V1.ErrorResponse](docs/EInvoicing/V1/ErrorResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.EventId](docs/EInvoicing/V1/EventId.md)
 - [Avalara.SDK.models.EInvoicing.V1.EventMessage](docs/EInvoicing/V1/EventMessage.md)
 - [Avalara.SDK.models.EInvoicing.V1.EventPayload](docs/EInvoicing/V1/EventPayload.md)
 - [Avalara.SDK.models.EInvoicing.V1.EventSubscription](docs/EInvoicing/V1/EventSubscription.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequest](docs/EInvoicing/V1/FetchDocumentsRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequestDataInner](docs/EInvoicing/V1/FetchDocumentsRequestDataInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequestMetadata](docs/EInvoicing/V1/FetchDocumentsRequestMetadata.md)
 - [Avalara.SDK.models.EInvoicing.V1.ForbiddenError](docs/EInvoicing/V1/ForbiddenError.md)
 - [Avalara.SDK.models.EInvoicing.V1.HmacSignature](docs/EInvoicing/V1/HmacSignature.md)
 - [Avalara.SDK.models.EInvoicing.V1.HmacSignatureValue](docs/EInvoicing/V1/HmacSignatureValue.md)
 - [Avalara.SDK.models.EInvoicing.V1.Id](docs/EInvoicing/V1/Id.md)
 - [Avalara.SDK.models.EInvoicing.V1.InputDataFormats](docs/EInvoicing/V1/InputDataFormats.md)
 - [Avalara.SDK.models.EInvoicing.V1.InternalServerError](docs/EInvoicing/V1/InternalServerError.md)
 - [Avalara.SDK.models.EInvoicing.V1.Mandate](docs/EInvoicing/V1/Mandate.md)
 - [Avalara.SDK.models.EInvoicing.V1.MandateDataInputField](docs/EInvoicing/V1/MandateDataInputField.md)
 - [Avalara.SDK.models.EInvoicing.V1.MandateDataInputFieldNamespace](docs/EInvoicing/V1/MandateDataInputFieldNamespace.md)
 - [Avalara.SDK.models.EInvoicing.V1.MandatesResponse](docs/EInvoicing/V1/MandatesResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.NotFoundError](docs/EInvoicing/V1/NotFoundError.md)
 - [Avalara.SDK.models.EInvoicing.V1.NotUsedForField](docs/EInvoicing/V1/NotUsedForField.md)
 - [Avalara.SDK.models.EInvoicing.V1.OutputDataFormats](docs/EInvoicing/V1/OutputDataFormats.md)
 - [Avalara.SDK.models.EInvoicing.V1.Pagination](docs/EInvoicing/V1/Pagination.md)
 - [Avalara.SDK.models.EInvoicing.V1.RequiredWhenField](docs/EInvoicing/V1/RequiredWhenField.md)
 - [Avalara.SDK.models.EInvoicing.V1.Signature](docs/EInvoicing/V1/Signature.md)
 - [Avalara.SDK.models.EInvoicing.V1.SignatureSignature](docs/EInvoicing/V1/SignatureSignature.md)
 - [Avalara.SDK.models.EInvoicing.V1.SignatureValue](docs/EInvoicing/V1/SignatureValue.md)
 - [Avalara.SDK.models.EInvoicing.V1.SignatureValueSignature](docs/EInvoicing/V1/SignatureValueSignature.md)
 - [Avalara.SDK.models.EInvoicing.V1.StatusEvent](docs/EInvoicing/V1/StatusEvent.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubmitDocumentMetadata](docs/EInvoicing/V1/SubmitDocumentMetadata.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubmitInteropDocument202Response](docs/EInvoicing/V1/SubmitInteropDocument202Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubscriptionCommon](docs/EInvoicing/V1/SubscriptionCommon.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubscriptionDetail](docs/EInvoicing/V1/SubscriptionDetail.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubscriptionListResponse](docs/EInvoicing/V1/SubscriptionListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.SubscriptionRegistration](docs/EInvoicing/V1/SubscriptionRegistration.md)
 - [Avalara.SDK.models.EInvoicing.V1.SuccessResponse](docs/EInvoicing/V1/SuccessResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhookInvocation](docs/EInvoicing/V1/WebhookInvocation.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhooksErrorInfo](docs/EInvoicing/V1/WebhooksErrorInfo.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhooksErrorResponse](docs/EInvoicing/V1/WebhooksErrorResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.WorkflowIds](docs/EInvoicing/V1/WorkflowIds.md)


<a name="documentation-for-A1099-V2-models"></a>
### A1099 V2 Model Documentation

 - [Avalara.SDK.models.A1099.V2.Attribute](docs/A1099/V2/Attribute.md)
 - [Avalara.SDK.models.A1099.V2.AuthorizedApiRequestModel](docs/A1099/V2/AuthorizedApiRequestModel.md)
 - [Avalara.SDK.models.A1099.V2.AuthorizedApiRequestV2DataModel](docs/A1099/V2/AuthorizedApiRequestV2DataModel.md)
 - [Avalara.SDK.models.A1099.V2.BaseCompanyModel](docs/A1099/V2/BaseCompanyModel.md)
 - [Avalara.SDK.models.A1099.V2.BaseFormListRequest](docs/A1099/V2/BaseFormListRequest.md)
 - [Avalara.SDK.models.A1099.V2.BulkUpsert1099FormsRequest](docs/A1099/V2/BulkUpsert1099FormsRequest.md)
 - [Avalara.SDK.models.A1099.V2.CompanyCreateUpdateRequestModel](docs/A1099/V2/CompanyCreateUpdateRequestModel.md)
 - [Avalara.SDK.models.A1099.V2.CompanyModel](docs/A1099/V2/CompanyModel.md)
 - [Avalara.SDK.models.A1099.V2.CompanyResponse](docs/A1099/V2/CompanyResponse.md)
 - [Avalara.SDK.models.A1099.V2.CompanyResponseModel](docs/A1099/V2/CompanyResponseModel.md)
 - [Avalara.SDK.models.A1099.V2.CoveredIndividualReference](docs/A1099/V2/CoveredIndividualReference.md)
 - [Avalara.SDK.models.A1099.V2.CoveredIndividualRequest](docs/A1099/V2/CoveredIndividualRequest.md)
 - [Avalara.SDK.models.A1099.V2.Data](docs/A1099/V2/Data.md)
 - [Avalara.SDK.models.A1099.V2.ErrorModel](docs/A1099/V2/ErrorModel.md)
 - [Avalara.SDK.models.A1099.V2.ErrorResponse](docs/A1099/V2/ErrorResponse.md)
 - [Avalara.SDK.models.A1099.V2.ErrorResponseErrorsInner](docs/A1099/V2/ErrorResponseErrorsInner.md)
 - [Avalara.SDK.models.A1099.V2.Form1095B](docs/A1099/V2/Form1095B.md)
 - [Avalara.SDK.models.A1099.V2.Form1095BList](docs/A1099/V2/Form1095BList.md)
 - [Avalara.SDK.models.A1099.V2.Form1095BListItem](docs/A1099/V2/Form1095BListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1095BRequest](docs/A1099/V2/Form1095BRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099Base](docs/A1099/V2/Form1099Base.md)
 - [Avalara.SDK.models.A1099.V2.Form1099DivList](docs/A1099/V2/Form1099DivList.md)
 - [Avalara.SDK.models.A1099.V2.Form1099DivListItem](docs/A1099/V2/Form1099DivListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1099DivRequest](docs/A1099/V2/Form1099DivRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099DivResponse](docs/A1099/V2/Form1099DivResponse.md)
 - [Avalara.SDK.models.A1099.V2.Form1099K](docs/A1099/V2/Form1099K.md)
 - [Avalara.SDK.models.A1099.V2.Form1099KList](docs/A1099/V2/Form1099KList.md)
 - [Avalara.SDK.models.A1099.V2.Form1099KListItem](docs/A1099/V2/Form1099KListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1099KRequest](docs/A1099/V2/Form1099KRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099List](docs/A1099/V2/Form1099List.md)
 - [Avalara.SDK.models.A1099.V2.Form1099Misc](docs/A1099/V2/Form1099Misc.md)
 - [Avalara.SDK.models.A1099.V2.Form1099MiscList](docs/A1099/V2/Form1099MiscList.md)
 - [Avalara.SDK.models.A1099.V2.Form1099MiscListItem](docs/A1099/V2/Form1099MiscListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1099MiscRequest](docs/A1099/V2/Form1099MiscRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099MiscResponse](docs/A1099/V2/Form1099MiscResponse.md)
 - [Avalara.SDK.models.A1099.V2.Form1099Nec](docs/A1099/V2/Form1099Nec.md)
 - [Avalara.SDK.models.A1099.V2.Form1099NecList](docs/A1099/V2/Form1099NecList.md)
 - [Avalara.SDK.models.A1099.V2.Form1099NecListItem](docs/A1099/V2/Form1099NecListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1099NecRequest](docs/A1099/V2/Form1099NecRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099NecResponse](docs/A1099/V2/Form1099NecResponse.md)
 - [Avalara.SDK.models.A1099.V2.Form1099ProccessResult](docs/A1099/V2/Form1099ProccessResult.md)
 - [Avalara.SDK.models.A1099.V2.Form1099R](docs/A1099/V2/Form1099R.md)
 - [Avalara.SDK.models.A1099.V2.Form1099RList](docs/A1099/V2/Form1099RList.md)
 - [Avalara.SDK.models.A1099.V2.Form1099RListItem](docs/A1099/V2/Form1099RListItem.md)
 - [Avalara.SDK.models.A1099.V2.Form1099RRequest](docs/A1099/V2/Form1099RRequest.md)
 - [Avalara.SDK.models.A1099.V2.Form1099StatusDetail](docs/A1099/V2/Form1099StatusDetail.md)
 - [Avalara.SDK.models.A1099.V2.FormRequestBase](docs/A1099/V2/FormRequestBase.md)
 - [Avalara.SDK.models.A1099.V2.FormRequestCsvBase](docs/A1099/V2/FormRequestCsvBase.md)
 - [Avalara.SDK.models.A1099.V2.FormResponseBase](docs/A1099/V2/FormResponseBase.md)
 - [Avalara.SDK.models.A1099.V2.FormSingleRequestBase](docs/A1099/V2/FormSingleRequestBase.md)
 - [Avalara.SDK.models.A1099.V2.Get1099Form200Response](docs/A1099/V2/Get1099Form200Response.md)
 - [Avalara.SDK.models.A1099.V2.HttpValidationProblemDetails](docs/A1099/V2/HttpValidationProblemDetails.md)
 - [Avalara.SDK.models.A1099.V2.ICreateForm1099Request](docs/A1099/V2/ICreateForm1099Request.md)
 - [Avalara.SDK.models.A1099.V2.IUpdateForm1099Request](docs/A1099/V2/IUpdateForm1099Request.md)
 - [Avalara.SDK.models.A1099.V2.IW9FormDataModelsOneOf](docs/A1099/V2/IW9FormDataModelsOneOf.md)
 - [Avalara.SDK.models.A1099.V2.IncludedBase](docs/A1099/V2/IncludedBase.md)
 - [Avalara.SDK.models.A1099.V2.IssuerCommand](docs/A1099/V2/IssuerCommand.md)
 - [Avalara.SDK.models.A1099.V2.IssuerResponse](docs/A1099/V2/IssuerResponse.md)
 - [Avalara.SDK.models.A1099.V2.JobResult](docs/A1099/V2/JobResult.md)
 - [Avalara.SDK.models.A1099.V2.Link](docs/A1099/V2/Link.md)
 - [Avalara.SDK.models.A1099.V2.PaginatedQueryResultModel](docs/A1099/V2/PaginatedQueryResultModel.md)
 - [Avalara.SDK.models.A1099.V2.PaginatedQueryResultModelCompanyResponse](docs/A1099/V2/PaginatedQueryResultModelCompanyResponse.md)
 - [Avalara.SDK.models.A1099.V2.PaginatedQueryResultModelIssuerResponse](docs/A1099/V2/PaginatedQueryResultModelIssuerResponse.md)
 - [Avalara.SDK.models.A1099.V2.PaginatedW9FormsModel](docs/A1099/V2/PaginatedW9FormsModel.md)
 - [Avalara.SDK.models.A1099.V2.ProblemDetails](docs/A1099/V2/ProblemDetails.md)
 - [Avalara.SDK.models.A1099.V2.StateAndLocalWithholding](docs/A1099/V2/StateAndLocalWithholding.md)
 - [Avalara.SDK.models.A1099.V2.StateAndLocalWithholdingRequest](docs/A1099/V2/StateAndLocalWithholdingRequest.md)
 - [Avalara.SDK.models.A1099.V2.StateAndLocalWithholdingResponse](docs/A1099/V2/StateAndLocalWithholdingResponse.md)
 - [Avalara.SDK.models.A1099.V2.StateEfileStatusDetail](docs/A1099/V2/StateEfileStatusDetail.md)
 - [Avalara.SDK.models.A1099.V2.StateEfileStatusDetailApp](docs/A1099/V2/StateEfileStatusDetailApp.md)
 - [Avalara.SDK.models.A1099.V2.StatusDetail](docs/A1099/V2/StatusDetail.md)
 - [Avalara.SDK.models.A1099.V2.SubstantialUsOwnerResponse](docs/A1099/V2/SubstantialUsOwnerResponse.md)
 - [Avalara.SDK.models.A1099.V2.Update1099Form200Response](docs/A1099/V2/Update1099Form200Response.md)
 - [Avalara.SDK.models.A1099.V2.ValidationError](docs/A1099/V2/ValidationError.md)
 - [Avalara.SDK.models.A1099.V2.ValidationErrorApp](docs/A1099/V2/ValidationErrorApp.md)
 - [Avalara.SDK.models.A1099.V2.W4FormDataModel](docs/A1099/V2/W4FormDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W4FormResponse](docs/A1099/V2/W4FormResponse.md)
 - [Avalara.SDK.models.A1099.V2.W8BenEFormResponse](docs/A1099/V2/W8BenEFormResponse.md)
 - [Avalara.SDK.models.A1099.V2.W8BenESubstantialUsOwnerDataModel](docs/A1099/V2/W8BenESubstantialUsOwnerDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W8BenFormDataModel](docs/A1099/V2/W8BenFormDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W8BenFormResponse](docs/A1099/V2/W8BenFormResponse.md)
 - [Avalara.SDK.models.A1099.V2.W8BeneFormDataModel](docs/A1099/V2/W8BeneFormDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W8ImyFormDataModel](docs/A1099/V2/W8ImyFormDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W8ImyFormResponse](docs/A1099/V2/W8ImyFormResponse.md)
 - [Avalara.SDK.models.A1099.V2.W9FormBaseResponse](docs/A1099/V2/W9FormBaseResponse.md)
 - [Avalara.SDK.models.A1099.V2.W9FormDataModel](docs/A1099/V2/W9FormDataModel.md)
 - [Avalara.SDK.models.A1099.V2.W9FormResponse](docs/A1099/V2/W9FormResponse.md)
