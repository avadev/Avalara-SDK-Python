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

    Avalara E-Invoicing API
    An API that supports sending data for an E-Invoicing compliance use-case. 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    26.4.0
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ReportItem(BaseModel):
    """
    Represents a single report with full details including metadata and associated transaction IDs.
    """ # noqa: E501
    report_id: Optional[StrictStr] = Field(default=None, description="The unique ID for this report.", alias="reportId")
    job_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the job that generated this report.", alias="jobId")
    report_generate_date: Optional[datetime] = Field(default=None, description="The date and time when the report was generated.", alias="reportGenerateDate")
    report_from: Optional[date] = Field(default=None, description="The start date of the reporting period.", alias="reportFrom")
    report_to: Optional[date] = Field(default=None, description="The end date of the reporting period.", alias="reportTo")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-letter ISO-3166 country code for which this report was generated.", alias="countryCode")
    country_mandate: Optional[StrictStr] = Field(default=None, description="The e-invoicing mandate for the specified country.", alias="countryMandate")
    document_type: Optional[StrictStr] = Field(default=None, description="The type of document covered by this report.", alias="documentType")
    document_sub_type: Optional[StrictStr] = Field(default=None, description="The sub-type of the document.", alias="documentSubType")
    report_reference: Optional[StrictStr] = Field(default=None, description="An internal reference path for the report.", alias="reportReference")
    report_name: Optional[StrictStr] = Field(default=None, description="The name of the report file.", alias="reportName")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the report. Possible values include: PENDING, PROCESSING, COMPLETED, FAILED, SENT_TO_PPF, ERROR.")
    report_format_mimetypes: Optional[StrictStr] = Field(default=None, description="The MIME type of the report file.", alias="reportFormatMimetypes")
    tenant_id: Optional[StrictStr] = Field(default=None, description="The tenant identifier associated with this report.", alias="tenantId")
    ta_name: Optional[StrictStr] = Field(default=None, description="The name of the tax authority for this report.", alias="taName")
    tax_invoice_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total invoice amount covered by this report.", alias="taxInvoiceAmount")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total tax amount covered by this report.", alias="totalTaxAmount")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional report metadata (free-form JSON). Contents vary by country mandate.")
    transaction_ids: Optional[List[StrictStr]] = Field(default=None, description="List of transaction IDs associated with this report.", alias="transactionIds")
    __properties: ClassVar[List[str]] = ["reportId", "jobId", "reportGenerateDate", "reportFrom", "reportTo", "countryCode", "countryMandate", "documentType", "documentSubType", "reportReference", "reportName", "status", "reportFormatMimetypes", "tenantId", "taName", "taxInvoiceAmount", "totalTaxAmount", "metadata", "transactionIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReportItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if job_id (nullable) is None
        # and model_fields_set contains the field
        if self.job_id is None and "job_id" in self.model_fields_set:
            _dict['jobId'] = None

        # set to None if report_from (nullable) is None
        # and model_fields_set contains the field
        if self.report_from is None and "report_from" in self.model_fields_set:
            _dict['reportFrom'] = None

        # set to None if report_to (nullable) is None
        # and model_fields_set contains the field
        if self.report_to is None and "report_to" in self.model_fields_set:
            _dict['reportTo'] = None

        # set to None if document_type (nullable) is None
        # and model_fields_set contains the field
        if self.document_type is None and "document_type" in self.model_fields_set:
            _dict['documentType'] = None

        # set to None if document_sub_type (nullable) is None
        # and model_fields_set contains the field
        if self.document_sub_type is None and "document_sub_type" in self.model_fields_set:
            _dict['documentSubType'] = None

        # set to None if report_reference (nullable) is None
        # and model_fields_set contains the field
        if self.report_reference is None and "report_reference" in self.model_fields_set:
            _dict['reportReference'] = None

        # set to None if tax_invoice_amount (nullable) is None
        # and model_fields_set contains the field
        if self.tax_invoice_amount is None and "tax_invoice_amount" in self.model_fields_set:
            _dict['taxInvoiceAmount'] = None

        # set to None if total_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_tax_amount is None and "total_tax_amount" in self.model_fields_set:
            _dict['totalTaxAmount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reportId": obj.get("reportId"),
            "jobId": obj.get("jobId"),
            "reportGenerateDate": obj.get("reportGenerateDate"),
            "reportFrom": obj.get("reportFrom"),
            "reportTo": obj.get("reportTo"),
            "countryCode": obj.get("countryCode"),
            "countryMandate": obj.get("countryMandate"),
            "documentType": obj.get("documentType"),
            "documentSubType": obj.get("documentSubType"),
            "reportReference": obj.get("reportReference"),
            "reportName": obj.get("reportName"),
            "status": obj.get("status"),
            "reportFormatMimetypes": obj.get("reportFormatMimetypes"),
            "tenantId": obj.get("tenantId"),
            "taName": obj.get("taName"),
            "taxInvoiceAmount": obj.get("taxInvoiceAmount"),
            "totalTaxAmount": obj.get("totalTaxAmount"),
            "metadata": obj.get("metadata"),
            "transactionIds": obj.get("transactionIds")
        })
        return _obj


