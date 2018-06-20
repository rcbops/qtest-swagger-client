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


class TestStepLogResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, test_step_id=None, test_step_log_id=None, user_id=None, status=None, actual_result=None, called_test_case_id=None, called_test_case_name=None, order=None, group=None, test_step=None, defects=None, called_test_case_log=None, parent_test_step_id=None):
        """
        TestStepLogResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'test_step_id': 'int',
            'test_step_log_id': 'int',
            'user_id': 'int',
            'status': 'StatusResource',
            'actual_result': 'str',
            'called_test_case_id': 'int',
            'called_test_case_name': 'str',
            'order': 'int',
            'group': 'int',
            'test_step': 'TestStepResource',
            'defects': 'list[LinkedDefectResource]',
            'called_test_case_log': 'TestLogResource',
            'parent_test_step_id': 'int'
        }

        self.attribute_map = {
            'links': 'links',
            'test_step_id': 'test_step_id',
            'test_step_log_id': 'test_step_log_id',
            'user_id': 'user_id',
            'status': 'status',
            'actual_result': 'actual_result',
            'called_test_case_id': 'called_test_case_id',
            'called_test_case_name': 'called_test_case_name',
            'order': 'order',
            'group': 'group',
            'test_step': 'test_step',
            'defects': 'defects',
            'called_test_case_log': 'called_test_case_log',
            'parent_test_step_id': 'parent_test_step_id'
        }

        self._links = links
        self._test_step_id = test_step_id
        self._test_step_log_id = test_step_log_id
        self._user_id = user_id
        self._status = status
        self._actual_result = actual_result
        self._called_test_case_id = called_test_case_id
        self._called_test_case_name = called_test_case_name
        self._order = order
        self._group = group
        self._test_step = test_step
        self._defects = defects
        self._called_test_case_log = called_test_case_log
        self._parent_test_step_id = parent_test_step_id

    @property
    def links(self):
        """
        Gets the links of this TestStepLogResource.

        :return: The links of this TestStepLogResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TestStepLogResource.

        :param links: The links of this TestStepLogResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def test_step_id(self):
        """
        Gets the test_step_id of this TestStepLogResource.

        :return: The test_step_id of this TestStepLogResource.
        :rtype: int
        """
        return self._test_step_id

    @test_step_id.setter
    def test_step_id(self, test_step_id):
        """
        Sets the test_step_id of this TestStepLogResource.

        :param test_step_id: The test_step_id of this TestStepLogResource.
        :type: int
        """

        self._test_step_id = test_step_id

    @property
    def test_step_log_id(self):
        """
        Gets the test_step_log_id of this TestStepLogResource.

        :return: The test_step_log_id of this TestStepLogResource.
        :rtype: int
        """
        return self._test_step_log_id

    @test_step_log_id.setter
    def test_step_log_id(self, test_step_log_id):
        """
        Sets the test_step_log_id of this TestStepLogResource.

        :param test_step_log_id: The test_step_log_id of this TestStepLogResource.
        :type: int
        """

        self._test_step_log_id = test_step_log_id

    @property
    def user_id(self):
        """
        Gets the user_id of this TestStepLogResource.

        :return: The user_id of this TestStepLogResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this TestStepLogResource.

        :param user_id: The user_id of this TestStepLogResource.
        :type: int
        """

        self._user_id = user_id

    @property
    def status(self):
        """
        Gets the status of this TestStepLogResource.

        :return: The status of this TestStepLogResource.
        :rtype: StatusResource
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TestStepLogResource.

        :param status: The status of this TestStepLogResource.
        :type: StatusResource
        """

        self._status = status

    @property
    def actual_result(self):
        """
        Gets the actual_result of this TestStepLogResource.

        :return: The actual_result of this TestStepLogResource.
        :rtype: str
        """
        return self._actual_result

    @actual_result.setter
    def actual_result(self, actual_result):
        """
        Sets the actual_result of this TestStepLogResource.

        :param actual_result: The actual_result of this TestStepLogResource.
        :type: str
        """

        self._actual_result = actual_result

    @property
    def called_test_case_id(self):
        """
        Gets the called_test_case_id of this TestStepLogResource.

        :return: The called_test_case_id of this TestStepLogResource.
        :rtype: int
        """
        return self._called_test_case_id

    @called_test_case_id.setter
    def called_test_case_id(self, called_test_case_id):
        """
        Sets the called_test_case_id of this TestStepLogResource.

        :param called_test_case_id: The called_test_case_id of this TestStepLogResource.
        :type: int
        """

        self._called_test_case_id = called_test_case_id

    @property
    def called_test_case_name(self):
        """
        Gets the called_test_case_name of this TestStepLogResource.

        :return: The called_test_case_name of this TestStepLogResource.
        :rtype: str
        """
        return self._called_test_case_name

    @called_test_case_name.setter
    def called_test_case_name(self, called_test_case_name):
        """
        Sets the called_test_case_name of this TestStepLogResource.

        :param called_test_case_name: The called_test_case_name of this TestStepLogResource.
        :type: str
        """

        self._called_test_case_name = called_test_case_name

    @property
    def order(self):
        """
        Gets the order of this TestStepLogResource.

        :return: The order of this TestStepLogResource.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this TestStepLogResource.

        :param order: The order of this TestStepLogResource.
        :type: int
        """

        self._order = order

    @property
    def group(self):
        """
        Gets the group of this TestStepLogResource.

        :return: The group of this TestStepLogResource.
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this TestStepLogResource.

        :param group: The group of this TestStepLogResource.
        :type: int
        """

        self._group = group

    @property
    def test_step(self):
        """
        Gets the test_step of this TestStepLogResource.

        :return: The test_step of this TestStepLogResource.
        :rtype: TestStepResource
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        """
        Sets the test_step of this TestStepLogResource.

        :param test_step: The test_step of this TestStepLogResource.
        :type: TestStepResource
        """

        self._test_step = test_step

    @property
    def defects(self):
        """
        Gets the defects of this TestStepLogResource.

        :return: The defects of this TestStepLogResource.
        :rtype: list[LinkedDefectResource]
        """
        return self._defects

    @defects.setter
    def defects(self, defects):
        """
        Sets the defects of this TestStepLogResource.

        :param defects: The defects of this TestStepLogResource.
        :type: list[LinkedDefectResource]
        """

        self._defects = defects

    @property
    def called_test_case_log(self):
        """
        Gets the called_test_case_log of this TestStepLogResource.

        :return: The called_test_case_log of this TestStepLogResource.
        :rtype: TestLogResource
        """
        return self._called_test_case_log

    @called_test_case_log.setter
    def called_test_case_log(self, called_test_case_log):
        """
        Sets the called_test_case_log of this TestStepLogResource.

        :param called_test_case_log: The called_test_case_log of this TestStepLogResource.
        :type: TestLogResource
        """

        self._called_test_case_log = called_test_case_log

    @property
    def parent_test_step_id(self):
        """
        Gets the parent_test_step_id of this TestStepLogResource.

        :return: The parent_test_step_id of this TestStepLogResource.
        :rtype: int
        """
        return self._parent_test_step_id

    @parent_test_step_id.setter
    def parent_test_step_id(self, parent_test_step_id):
        """
        Sets the parent_test_step_id of this TestStepLogResource.

        :param parent_test_step_id: The parent_test_step_id of this TestStepLogResource.
        :type: int
        """

        self._parent_test_step_id = parent_test_step_id

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
        if not isinstance(other, TestStepLogResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
