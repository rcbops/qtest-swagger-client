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


class BuildResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, name=None, order=None, pid=None, created_date=None, last_modified_date=None, properties=None, release=None):
        """
        BuildResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'id': 'int',
            'name': 'str',
            'order': 'int',
            'pid': 'str',
            'created_date': 'datetime',
            'last_modified_date': 'datetime',
            'properties': 'list[PropertyResource]',
            'release': 'ReleaseWithCustomFieldResource'
        }

        self.attribute_map = {
            'links': 'links',
            'id': 'id',
            'name': 'name',
            'order': 'order',
            'pid': 'pid',
            'created_date': 'created_date',
            'last_modified_date': 'last_modified_date',
            'properties': 'properties',
            'release': 'release'
        }

        self._links = links
        self._id = id
        self._name = name
        self._order = order
        self._pid = pid
        self._created_date = created_date
        self._last_modified_date = last_modified_date
        self._properties = properties
        self._release = release

    @property
    def links(self):
        """
        Gets the links of this BuildResource.

        :return: The links of this BuildResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this BuildResource.

        :param links: The links of this BuildResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this BuildResource.
        ID of the Build

        :return: The id of this BuildResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildResource.
        ID of the Build

        :param id: The id of this BuildResource.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildResource.
        Name of the Build

        :return: The name of this BuildResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildResource.
        Name of the Build

        :param name: The name of this BuildResource.
        :type: str
        """
        if name is not None and len(name) > 500:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `500`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def order(self):
        """
        Gets the order of this BuildResource.
        Order in left tree of the Build

        :return: The order of this BuildResource.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this BuildResource.
        Order in left tree of the Build

        :param order: The order of this BuildResource.
        :type: int
        """

        self._order = order

    @property
    def pid(self):
        """
        Gets the pid of this BuildResource.
        PID of the Build

        :return: The pid of this BuildResource.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this BuildResource.
        PID of the Build

        :param pid: The pid of this BuildResource.
        :type: str
        """

        self._pid = pid

    @property
    def created_date(self):
        """
        Gets the created_date of this BuildResource.

        :return: The created_date of this BuildResource.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this BuildResource.

        :param created_date: The created_date of this BuildResource.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """
        Gets the last_modified_date of this BuildResource.

        :return: The last_modified_date of this BuildResource.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """
        Sets the last_modified_date of this BuildResource.

        :param last_modified_date: The last_modified_date of this BuildResource.
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def properties(self):
        """
        Gets the properties of this BuildResource.
        Arrays property of the Build

        :return: The properties of this BuildResource.
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this BuildResource.
        Arrays property of the Build

        :param properties: The properties of this BuildResource.
        :type: list[PropertyResource]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def release(self):
        """
        Gets the release of this BuildResource.

        :return: The release of this BuildResource.
        :rtype: ReleaseWithCustomFieldResource
        """
        return self._release

    @release.setter
    def release(self, release):
        """
        Sets the release of this BuildResource.

        :param release: The release of this BuildResource.
        :type: ReleaseWithCustomFieldResource
        """

        self._release = release

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
        if not isinstance(other, BuildResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
