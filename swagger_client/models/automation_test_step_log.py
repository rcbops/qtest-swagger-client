# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.1

    qTest Manager API Version 8.6 - 9.1

    OpenAPI spec version: 8.6 - 9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AutomationTestStepLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, expected_result=None, actual_result=None, order=None, status=None, attachments=None, defects=None):
        """
        AutomationTestStepLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'expected_result': 'str',
            'actual_result': 'str',
            'order': 'int',
            'status': 'str',
            'attachments': 'list[AttachmentResource]',
            'defects': 'list[LinkedDefectResource]'
        }

        self.attribute_map = {
            'description': 'description',
            'expected_result': 'expected_result',
            'actual_result': 'actual_result',
            'order': 'order',
            'status': 'status',
            'attachments': 'attachments',
            'defects': 'defects'
        }

        self._description = description
        self._expected_result = expected_result
        self._actual_result = actual_result
        self._order = order
        self._status = status
        self._attachments = attachments
        self._defects = defects

    @property
    def description(self):
        """
        Gets the description of this AutomationTestStepLog.
        Test Step Log's description

        :return: The description of this AutomationTestStepLog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AutomationTestStepLog.
        Test Step Log's description

        :param description: The description of this AutomationTestStepLog.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def expected_result(self):
        """
        Gets the expected_result of this AutomationTestStepLog.
        Test Step Log's expected result

        :return: The expected_result of this AutomationTestStepLog.
        :rtype: str
        """
        return self._expected_result

    @expected_result.setter
    def expected_result(self, expected_result):
        """
        Sets the expected_result of this AutomationTestStepLog.
        Test Step Log's expected result

        :param expected_result: The expected_result of this AutomationTestStepLog.
        :type: str
        """
        if expected_result is None:
            raise ValueError("Invalid value for `expected_result`, must not be `None`")

        self._expected_result = expected_result

    @property
    def actual_result(self):
        """
        Gets the actual_result of this AutomationTestStepLog.
        Test Step Log's actual result

        :return: The actual_result of this AutomationTestStepLog.
        :rtype: str
        """
        return self._actual_result

    @actual_result.setter
    def actual_result(self, actual_result):
        """
        Sets the actual_result of this AutomationTestStepLog.
        Test Step Log's actual result

        :param actual_result: The actual_result of this AutomationTestStepLog.
        :type: str
        """

        self._actual_result = actual_result

    @property
    def order(self):
        """
        Gets the order of this AutomationTestStepLog.
        Test Step Log's order

        :return: The order of this AutomationTestStepLog.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AutomationTestStepLog.
        Test Step Log's order

        :param order: The order of this AutomationTestStepLog.
        :type: int
        """

        self._order = order

    @property
    def status(self):
        """
        Gets the status of this AutomationTestStepLog.
        Test Step Log's status

        :return: The status of this AutomationTestStepLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AutomationTestStepLog.
        Test Step Log's status

        :param status: The status of this AutomationTestStepLog.
        :type: str
        """

        self._status = status

    @property
    def attachments(self):
        """
        Gets the attachments of this AutomationTestStepLog.

        :return: The attachments of this AutomationTestStepLog.
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this AutomationTestStepLog.

        :param attachments: The attachments of this AutomationTestStepLog.
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def defects(self):
        """
        Gets the defects of this AutomationTestStepLog.

        :return: The defects of this AutomationTestStepLog.
        :rtype: list[LinkedDefectResource]
        """
        return self._defects

    @defects.setter
    def defects(self, defects):
        """
        Sets the defects of this AutomationTestStepLog.

        :param defects: The defects of this AutomationTestStepLog.
        :type: list[LinkedDefectResource]
        """

        self._defects = defects

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AutomationTestStepLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
