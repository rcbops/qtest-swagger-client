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
from swagger_client.apis.release_api import ReleaseApi


class TestReleaseApi(unittest.TestCase):
    """ ReleaseApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.release_api.ReleaseApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Creates a Release
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Delete a release
        """
        pass

    def test_get(self):
        """
        Test case for get

        Gets a Release
        """
        pass

    def test_get_all(self):
        """
        Test case for get_all

        Gets multiple Releases
        """
        pass

    def test_update(self):
        """
        Test case for update

        Updates a Release
        """
        pass


if __name__ == '__main__':
    unittest.main()
