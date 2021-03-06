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


class Profile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, is_readonly=False, is_admin=False):
        """
        Profile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'is_readonly': 'bool',
            'is_admin': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'is_readonly': 'is_readonly',
            'is_admin': 'is_admin'
        }

        self._id = id
        self._name = name
        self._is_readonly = is_readonly
        self._is_admin = is_admin

    @property
    def id(self):
        """
        Gets the id of this Profile.
        ID of Profile

        :return: The id of this Profile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Profile.
        ID of Profile

        :param id: The id of this Profile.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Profile.
        Name of Profile

        :return: The name of this Profile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Profile.
        Name of Profile

        :param name: The name of this Profile.
        :type: str
        """

        self._name = name

    @property
    def is_readonly(self):
        """
        Gets the is_readonly of this Profile.
        Is readonly or not

        :return: The is_readonly of this Profile.
        :rtype: bool
        """
        return self._is_readonly

    @is_readonly.setter
    def is_readonly(self, is_readonly):
        """
        Sets the is_readonly of this Profile.
        Is readonly or not

        :param is_readonly: The is_readonly of this Profile.
        :type: bool
        """

        self._is_readonly = is_readonly

    @property
    def is_admin(self):
        """
        Gets the is_admin of this Profile.
        Is admin profile or not

        :return: The is_admin of this Profile.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this Profile.
        Is admin profile or not

        :param is_admin: The is_admin of this Profile.
        :type: bool
        """

        self._is_admin = is_admin

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
        if not isinstance(other, Profile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
