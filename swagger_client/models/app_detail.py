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


class AppDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, logo_url=None, display_order=None, url=None, redirect_url=None):
        """
        AppDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'logo_url': 'str',
            'display_order': 'int',
            'url': 'str',
            'redirect_url': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'logo_url': 'logo_url',
            'display_order': 'display_order',
            'url': 'url',
            'redirect_url': 'redirect_url'
        }

        self._name = name
        self._logo_url = logo_url
        self._display_order = display_order
        self._url = url
        self._redirect_url = redirect_url

    @property
    def name(self):
        """
        Gets the name of this AppDetail.
        Manager

        :return: The name of this AppDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppDetail.
        Manager

        :param name: The name of this AppDetail.
        :type: str
        """

        self._name = name

    @property
    def logo_url(self):
        """
        Gets the logo_url of this AppDetail.
        <link to qTest application logo>

        :return: The logo_url of this AppDetail.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this AppDetail.
        <link to qTest application logo>

        :param logo_url: The logo_url of this AppDetail.
        :type: str
        """

        self._logo_url = logo_url

    @property
    def display_order(self):
        """
        Gets the display_order of this AppDetail.
        Display order of qTest application

        :return: The display_order of this AppDetail.
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """
        Sets the display_order of this AppDetail.
        Display order of qTest application

        :param display_order: The display_order of this AppDetail.
        :type: int
        """

        self._display_order = display_order

    @property
    def url(self):
        """
        Gets the url of this AppDetail.
        URL to qTest application

        :return: The url of this AppDetail.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this AppDetail.
        URL to qTest application

        :param url: The url of this AppDetail.
        :type: str
        """

        self._url = url

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this AppDetail.

        :return: The redirect_url of this AppDetail.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this AppDetail.

        :param redirect_url: The redirect_url of this AppDetail.
        :type: str
        """

        self._redirect_url = redirect_url

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
        if not isinstance(other, AppDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
