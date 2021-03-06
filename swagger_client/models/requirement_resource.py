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


class RequirementResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, name=None, order=None, pid=None, created_date=None, last_modified_date=None, properties=None, web_url=None, parent_id=None):
        """
        RequirementResource - a model defined in Swagger

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
            'web_url': 'str',
            'parent_id': 'int'
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
            'web_url': 'web_url',
            'parent_id': 'parent_id'
        }

        self._links = links
        self._id = id
        self._name = name
        self._order = order
        self._pid = pid
        self._created_date = created_date
        self._last_modified_date = last_modified_date
        self._properties = properties
        self._web_url = web_url
        self._parent_id = parent_id

    @property
    def links(self):
        """
        Gets the links of this RequirementResource.

        :return: The links of this RequirementResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this RequirementResource.

        :param links: The links of this RequirementResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this RequirementResource.

        :return: The id of this RequirementResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RequirementResource.

        :param id: The id of this RequirementResource.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RequirementResource.

        :return: The name of this RequirementResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RequirementResource.

        :param name: The name of this RequirementResource.
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
        Gets the order of this RequirementResource.

        :return: The order of this RequirementResource.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this RequirementResource.

        :param order: The order of this RequirementResource.
        :type: int
        """

        self._order = order

    @property
    def pid(self):
        """
        Gets the pid of this RequirementResource.

        :return: The pid of this RequirementResource.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this RequirementResource.

        :param pid: The pid of this RequirementResource.
        :type: str
        """

        self._pid = pid

    @property
    def created_date(self):
        """
        Gets the created_date of this RequirementResource.

        :return: The created_date of this RequirementResource.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this RequirementResource.

        :param created_date: The created_date of this RequirementResource.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def last_modified_date(self):
        """
        Gets the last_modified_date of this RequirementResource.

        :return: The last_modified_date of this RequirementResource.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """
        Sets the last_modified_date of this RequirementResource.

        :param last_modified_date: The last_modified_date of this RequirementResource.
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def properties(self):
        """
        Gets the properties of this RequirementResource.

        :return: The properties of this RequirementResource.
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this RequirementResource.

        :param properties: The properties of this RequirementResource.
        :type: list[PropertyResource]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def web_url(self):
        """
        Gets the web_url of this RequirementResource.

        :return: The web_url of this RequirementResource.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """
        Sets the web_url of this RequirementResource.

        :param web_url: The web_url of this RequirementResource.
        :type: str
        """

        self._web_url = web_url

    @property
    def parent_id(self):
        """
        Gets the parent_id of this RequirementResource.

        :return: The parent_id of this RequirementResource.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this RequirementResource.

        :param parent_id: The parent_id of this RequirementResource.
        :type: int
        """

        self._parent_id = parent_id

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
        if not isinstance(other, RequirementResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
