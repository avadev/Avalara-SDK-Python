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

    AvaTax API
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator) 

@author     Sachin Baijal <sachin.baijal@avalara.com>
@author     Jonathan Wenger <jonathan.wenger@avalara.com>
@copyright  2022 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    0.1.1
@link       https://github.com/avadev/AvaTax-REST-V3-Python-SDK
"""

import re  # noqa: F401
import sys  # noqa: F401

from Avalara.SDK.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from Avalara.SDK.exceptions import ApiAttributeError



class ContactModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('contact_code',): {
            'max_length': 25,
            'min_length': 0,
        },
        ('first_name',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('middle_name',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('last_name',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('title',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('line1',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('line2',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('line3',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('city',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('postal_code',): {
            'max_length': 10,
            'min_length': 0,
        },
        ('email',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('phone',): {
            'max_length': 25,
            'min_length': 0,
        },
        ('mobile',): {
            'max_length': 25,
            'min_length': 0,
        },
        ('fax',): {
            'max_length': 25,
            'min_length': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'contact_code': (str,),  # noqa: E501
            'id': (int,),  # noqa: E501
            'company_id': (int,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'middle_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'line1': (str,),  # noqa: E501
            'line2': (str,),  # noqa: E501
            'line3': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'mobile': (str,),  # noqa: E501
            'fax': (str,),  # noqa: E501
            'created_date': (datetime,),  # noqa: E501
            'created_user_id': (int,),  # noqa: E501
            'modified_date': (datetime,),  # noqa: E501
            'modified_user_id': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'contact_code': 'contactCode',  # noqa: E501
        'id': 'id',  # noqa: E501
        'company_id': 'companyId',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'middle_name': 'middleName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'title': 'title',  # noqa: E501
        'line1': 'line1',  # noqa: E501
        'line2': 'line2',  # noqa: E501
        'line3': 'line3',  # noqa: E501
        'city': 'city',  # noqa: E501
        'region': 'region',  # noqa: E501
        'postal_code': 'postalCode',  # noqa: E501
        'country': 'country',  # noqa: E501
        'email': 'email',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'mobile': 'mobile',  # noqa: E501
        'fax': 'fax',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'created_user_id': 'createdUserId',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'modified_user_id': 'modifiedUserId',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'company_id',  # noqa: E501
        'created_date',  # noqa: E501
        'created_user_id',  # noqa: E501
        'modified_date',  # noqa: E501
        'modified_user_id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, contact_code, *args, **kwargs):  # noqa: E501
        """ContactModel - a model defined in OpenAPI

        Args:
            contact_code (str): A unique code for this contact.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): The unique ID number of this contact.. [optional]  # noqa: E501
            company_id (int): The unique ID number of the company to which this contact belongs.. [optional]  # noqa: E501
            first_name (str): The first or given name of this contact.. [optional]  # noqa: E501
            middle_name (str): The middle name of this contact.. [optional]  # noqa: E501
            last_name (str): The last or family name of this contact.. [optional]  # noqa: E501
            title (str): Professional title of this contact.. [optional]  # noqa: E501
            line1 (str): The first line of the postal mailing address of this contact.. [optional]  # noqa: E501
            line2 (str): The second line of the postal mailing address of this contact.. [optional]  # noqa: E501
            line3 (str): The third line of the postal mailing address of this contact.. [optional]  # noqa: E501
            city (str): The city of the postal mailing address of this contact.. [optional]  # noqa: E501
            region (str): Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API `ListRegions`.. [optional]  # noqa: E501
            postal_code (str): The postal code or zip code of the postal mailing address of this contact.. [optional]  # noqa: E501
            country (str): Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API `ListCountries`.. [optional]  # noqa: E501
            email (str): The email address of this contact.. [optional]  # noqa: E501
            phone (str): The main phone number for this contact.. [optional]  # noqa: E501
            mobile (str): The mobile phone number for this contact.. [optional]  # noqa: E501
            fax (str): The facsimile phone number for this contact.. [optional]  # noqa: E501
            created_date (datetime): The date when this record was created.. [optional]  # noqa: E501
            created_user_id (int): The User ID of the user who created this record.. [optional]  # noqa: E501
            modified_date (datetime): The date/time when this record was last modified.. [optional]  # noqa: E501
            modified_user_id (int): The user ID of the user who last modified this record.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.contact_code = contact_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, contact_code, *args, **kwargs):  # noqa: E501
        """ContactModel - a model defined in OpenAPI

        Args:
            contact_code (str): A unique code for this contact.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): The unique ID number of this contact.. [optional]  # noqa: E501
            company_id (int): The unique ID number of the company to which this contact belongs.. [optional]  # noqa: E501
            first_name (str): The first or given name of this contact.. [optional]  # noqa: E501
            middle_name (str): The middle name of this contact.. [optional]  # noqa: E501
            last_name (str): The last or family name of this contact.. [optional]  # noqa: E501
            title (str): Professional title of this contact.. [optional]  # noqa: E501
            line1 (str): The first line of the postal mailing address of this contact.. [optional]  # noqa: E501
            line2 (str): The second line of the postal mailing address of this contact.. [optional]  # noqa: E501
            line3 (str): The third line of the postal mailing address of this contact.. [optional]  # noqa: E501
            city (str): The city of the postal mailing address of this contact.. [optional]  # noqa: E501
            region (str): Name or ISO 3166 code identifying the region within the country.                This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions                For a full list of all supported codes and names, please see the Definitions API `ListRegions`.. [optional]  # noqa: E501
            postal_code (str): The postal code or zip code of the postal mailing address of this contact.. [optional]  # noqa: E501
            country (str): Name or ISO 3166 code identifying the country.                This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries                For a full list of all supported codes and names, please see the Definitions API `ListCountries`.. [optional]  # noqa: E501
            email (str): The email address of this contact.. [optional]  # noqa: E501
            phone (str): The main phone number for this contact.. [optional]  # noqa: E501
            mobile (str): The mobile phone number for this contact.. [optional]  # noqa: E501
            fax (str): The facsimile phone number for this contact.. [optional]  # noqa: E501
            created_date (datetime): The date when this record was created.. [optional]  # noqa: E501
            created_user_id (int): The User ID of the user who created this record.. [optional]  # noqa: E501
            modified_date (datetime): The date/time when this record was last modified.. [optional]  # noqa: E501
            modified_user_id (int): The user ID of the user who last modified this record.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.contact_code = contact_code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")