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
from swagger_client.models.message import Message


class TestMessage(unittest.TestCase):
    """ Message unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessage(self):
        """
        Test Message
        """
        model = swagger_client.models.message.Message()


if __name__ == '__main__':
    unittest.main()
