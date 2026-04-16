# Avalara.SDK - the Unified Python SDK for next gen Avalara services.

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
*CodeListsApi* | [**get_code_list**](docs/EInvoicing/V1/CodeListsApi.md#get_code_list) | **GET** /codelists/{codelistId} | Retrieves a code list by ID for a specific country
*CodeListsApi* | [**get_code_list_list**](docs/EInvoicing/V1/CodeListsApi.md#get_code_list_list) | **GET** /codelists | Returns a list of code lists for a specific country
*DataInputFieldsApi* | [**get_data_input_fields**](docs/EInvoicing/V1/DataInputFieldsApi.md#get_data_input_fields) | **GET** /data-input-fields | Returns the optionality of document fields for different country mandates
*DocumentsApi* | [**download_document**](docs/EInvoicing/V1/DocumentsApi.md#download_document) | **GET** /documents/{documentId}/$download | Returns a copy of the document
*DocumentsApi* | [**fetch_documents**](docs/EInvoicing/V1/DocumentsApi.md#fetch_documents) | **POST** /documents/$fetch | Fetch the inbound document from a tax authority
*DocumentsApi* | [**get_document_list**](docs/EInvoicing/V1/DocumentsApi.md#get_document_list) | **GET** /documents | Returns a summary of documents for a date range
*DocumentsApi* | [**get_document_status**](docs/EInvoicing/V1/DocumentsApi.md#get_document_status) | **GET** /documents/{documentId}/status | Checks the status of a document
*DocumentsApi* | [**submit_document**](docs/EInvoicing/V1/DocumentsApi.md#submit_document) | **POST** /documents | Submits a document to Avalara E-Invoicing API
*InteropApi* | [**submit_interop_document**](docs/EInvoicing/V1/InteropApi.md#submit_interop_document) | **POST** /interop/documents | Submit a document
*MandatesApi* | [**get_mandate_data_input_fields**](docs/EInvoicing/V1/MandatesApi.md#get_mandate_data_input_fields) | **GET** /mandates/{mandateId}/data-input-fields | Returns document field information for a country mandate, a selected document type, and its version
*MandatesApi* | [**get_mandates**](docs/EInvoicing/V1/MandatesApi.md#get_mandates) | **GET** /mandates | List country mandates that are supported by the Avalara E-Invoicing platform
*ReportsApi* | [**download_report**](docs/EInvoicing/V1/ReportsApi.md#download_report) | **GET** /reports/{reportId}/$download | Returns a pre-signed download URL for a report
*ReportsApi* | [**get_report_by_id**](docs/EInvoicing/V1/ReportsApi.md#get_report_by_id) | **GET** /reports/{reportId}/status | Retrieves a report by its unique ID
*ReportsApi* | [**get_reports**](docs/EInvoicing/V1/ReportsApi.md#get_reports) | **GET** /reports | Returns a list of reports
*SubscriptionsApi* | [**create_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#create_webhook_subscription) | **POST** /webhooks/subscriptions | Create a subscription to events
*SubscriptionsApi* | [**delete_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#delete_webhook_subscription) | **DELETE** /webhooks/subscriptions/{subscriptionId} | Unsubscribe from events
*SubscriptionsApi* | [**get_webhook_subscription**](docs/EInvoicing/V1/SubscriptionsApi.md#get_webhook_subscription) | **GET** /webhooks/subscriptions/{subscriptionId} | Get details of a subscription
*SubscriptionsApi* | [**list_webhook_subscriptions**](docs/EInvoicing/V1/SubscriptionsApi.md#list_webhook_subscriptions) | **GET** /webhooks/subscriptions | List all subscriptions
*TaxIdentifiersApi* | [**tax_identifier_schema_by_country**](docs/EInvoicing/V1/TaxIdentifiersApi.md#tax_identifier_schema_by_country) | **GET** /tax-identifiers/schema | Returns the tax identifier request and response schema for a specific country.
*TaxIdentifiersApi* | [**validate_tax_identifier**](docs/EInvoicing/V1/TaxIdentifiersApi.md#validate_tax_identifier) | **POST** /tax-identifiers/validate | Validates a tax identifier.
*TradingPartnersApi* | [**batch_search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#batch_search_participants) | **POST** /trading-partners/batch-searches | Handles batch search requests by uploading a file containing search parameters.
*TradingPartnersApi* | [**create_trading_partner**](docs/EInvoicing/V1/TradingPartnersApi.md#create_trading_partner) | **POST** /trading-partners | Creates a new trading partner.
*TradingPartnersApi* | [**create_trading_partners_batch**](docs/EInvoicing/V1/TradingPartnersApi.md#create_trading_partners_batch) | **POST** /trading-partners/batch | Creates a batch of multiple trading partners.
*TradingPartnersApi* | [**delete_trading_partner**](docs/EInvoicing/V1/TradingPartnersApi.md#delete_trading_partner) | **DELETE** /trading-partners/{id} | Deletes a trading partner using ID.
*TradingPartnersApi* | [**download_batch_search_report**](docs/EInvoicing/V1/TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Downloads batch search results in a csv file.
*TradingPartnersApi* | [**get_batch_search_detail**](docs/EInvoicing/V1/TradingPartnersApi.md#get_batch_search_detail) | **GET** /trading-partners/batch-searches/{id} | Returns the batch search details using ID.
*TradingPartnersApi* | [**list_batch_searches**](docs/EInvoicing/V1/TradingPartnersApi.md#list_batch_searches) | **GET** /trading-partners/batch-searches | Lists all batch searches that were previously submitted.
*TradingPartnersApi* | [**search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#search_participants) | **GET** /trading-partners | Returns a list of participants matching the input query.
*TradingPartnersApi* | [**update_trading_partner**](docs/EInvoicing/V1/TradingPartnersApi.md#update_trading_partner) | **PUT** /trading-partners/{id} | Updates a trading partner using ID.

<a name="documentation-for-models"></a>
## Documentation for Models

<a name="documentation-for-EInvoicing-V1-models"></a>
### EInvoicing V1 Model Documentation

 - [Avalara.SDK.models.EInvoicing.V1.Address](docs/EInvoicing/V1/Address.md)
 - [Avalara.SDK.models.EInvoicing.V1.BadDownloadRequest](docs/EInvoicing/V1/BadDownloadRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.BadRequest](docs/EInvoicing/V1/BadRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchErrorDetail](docs/EInvoicing/V1/BatchErrorDetail.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearch](docs/EInvoicing/V1/BatchSearch.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearchListResponse](docs/EInvoicing/V1/BatchSearchListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.BatchSearchParticipants202Response](docs/EInvoicing/V1/BatchSearchParticipants202Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.CodeListListResponse](docs/EInvoicing/V1/CodeListListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.CodeListResponse](docs/EInvoicing/V1/CodeListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.CodeListSummary](docs/EInvoicing/V1/CodeListSummary.md)
 - [Avalara.SDK.models.EInvoicing.V1.CodeListValue](docs/EInvoicing/V1/CodeListValue.md)
 - [Avalara.SDK.models.EInvoicing.V1.CodeListVersion](docs/EInvoicing/V1/CodeListVersion.md)
 - [Avalara.SDK.models.EInvoicing.V1.ConditionalForField](docs/EInvoicing/V1/ConditionalForField.md)
 - [Avalara.SDK.models.EInvoicing.V1.Consents](docs/EInvoicing/V1/Consents.md)
 - [Avalara.SDK.models.EInvoicing.V1.CreateTradingPartner201Response](docs/EInvoicing/V1/CreateTradingPartner201Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.CreateTradingPartnersBatch200Response](docs/EInvoicing/V1/CreateTradingPartnersBatch200Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.CreateTradingPartnersBatch200ResponseValueInner](docs/EInvoicing/V1/CreateTradingPartnersBatch200ResponseValueInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.CreateTradingPartnersBatchRequest](docs/EInvoicing/V1/CreateTradingPartnersBatchRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputField](docs/EInvoicing/V1/DataInputField.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldNotUsedFor](docs/EInvoicing/V1/DataInputFieldNotUsedFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldOptionalFor](docs/EInvoicing/V1/DataInputFieldOptionalFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldRequiredFor](docs/EInvoicing/V1/DataInputFieldRequiredFor.md)
 - [Avalara.SDK.models.EInvoicing.V1.DataInputFieldsResponse](docs/EInvoicing/V1/DataInputFieldsResponse.md)
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
 - [Avalara.SDK.models.EInvoicing.V1.Extension](docs/EInvoicing/V1/Extension.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequest](docs/EInvoicing/V1/FetchDocumentsRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequestDataInner](docs/EInvoicing/V1/FetchDocumentsRequestDataInner.md)
 - [Avalara.SDK.models.EInvoicing.V1.FetchDocumentsRequestMetadata](docs/EInvoicing/V1/FetchDocumentsRequestMetadata.md)
 - [Avalara.SDK.models.EInvoicing.V1.ForbiddenError](docs/EInvoicing/V1/ForbiddenError.md)
 - [Avalara.SDK.models.EInvoicing.V1.HmacSignature](docs/EInvoicing/V1/HmacSignature.md)
 - [Avalara.SDK.models.EInvoicing.V1.HmacSignatureValue](docs/EInvoicing/V1/HmacSignatureValue.md)
 - [Avalara.SDK.models.EInvoicing.V1.Id](docs/EInvoicing/V1/Id.md)
 - [Avalara.SDK.models.EInvoicing.V1.Identifier](docs/EInvoicing/V1/Identifier.md)
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
 - [Avalara.SDK.models.EInvoicing.V1.ReportDownloadResponse](docs/EInvoicing/V1/ReportDownloadResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.ReportItem](docs/EInvoicing/V1/ReportItem.md)
 - [Avalara.SDK.models.EInvoicing.V1.ReportListResponse](docs/EInvoicing/V1/ReportListResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.RequiredWhenField](docs/EInvoicing/V1/RequiredWhenField.md)
 - [Avalara.SDK.models.EInvoicing.V1.SearchParticipants200Response](docs/EInvoicing/V1/SearchParticipants200Response.md)
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
 - [Avalara.SDK.models.EInvoicing.V1.SupportedDocumentStatuses](docs/EInvoicing/V1/SupportedDocumentStatuses.md)
 - [Avalara.SDK.models.EInvoicing.V1.SupportedDocumentTypes](docs/EInvoicing/V1/SupportedDocumentTypes.md)
 - [Avalara.SDK.models.EInvoicing.V1.TaxIdentifierRequest](docs/EInvoicing/V1/TaxIdentifierRequest.md)
 - [Avalara.SDK.models.EInvoicing.V1.TaxIdentifierResponse](docs/EInvoicing/V1/TaxIdentifierResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.TaxIdentifierResponseValue](docs/EInvoicing/V1/TaxIdentifierResponseValue.md)
 - [Avalara.SDK.models.EInvoicing.V1.TaxIdentifierSchemaByCountry200Response](docs/EInvoicing/V1/TaxIdentifierSchemaByCountry200Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.TradingPartner](docs/EInvoicing/V1/TradingPartner.md)
 - [Avalara.SDK.models.EInvoicing.V1.UpdateTradingPartner200Response](docs/EInvoicing/V1/UpdateTradingPartner200Response.md)
 - [Avalara.SDK.models.EInvoicing.V1.ValidationError](docs/EInvoicing/V1/ValidationError.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhookInvocation](docs/EInvoicing/V1/WebhookInvocation.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhooksErrorInfo](docs/EInvoicing/V1/WebhooksErrorInfo.md)
 - [Avalara.SDK.models.EInvoicing.V1.WebhooksErrorResponse](docs/EInvoicing/V1/WebhooksErrorResponse.md)
 - [Avalara.SDK.models.EInvoicing.V1.WorkflowIds](docs/EInvoicing/V1/WorkflowIds.md)
