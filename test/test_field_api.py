# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.1

    qTest Manager API Version 8.6 - 9.1

    OpenAPI spec version: 8.6 - 9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.field_api import FieldApi


class TestFieldApi(unittest.TestCase):
    """ FieldApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.field_api.FieldApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Creates a Custom Field of an Object Type
        """
        pass

    def test_get_fields(self):
        """
        Test case for get_fields

        Gets all Fields of an Object Type
        """
        pass


if __name__ == '__main__':
    unittest.main()