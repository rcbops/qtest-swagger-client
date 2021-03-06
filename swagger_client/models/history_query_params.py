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


class HistoryQueryParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, object_type=None, fields=None, query=None, object_query=None):
        """
        HistoryQueryParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'object_type': 'str',
            'fields': 'list[str]',
            'query': 'str',
            'object_query': 'str'
        }

        self.attribute_map = {
            'object_type': 'object_type',
            'fields': 'fields',
            'query': 'query',
            'object_query': 'object_query'
        }

        self._object_type = object_type
        self._fields = fields
        self._query = query
        self._object_query = object_query

    @property
    def object_type(self):
        """
        Gets the object_type of this HistoryQueryParams.

        :return: The object_type of this HistoryQueryParams.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HistoryQueryParams.

        :param object_type: The object_type of this HistoryQueryParams.
        :type: str
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")

        self._object_type = object_type

    @property
    def fields(self):
        """
        Gets the fields of this HistoryQueryParams.

        :return: The fields of this HistoryQueryParams.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this HistoryQueryParams.

        :param fields: The fields of this HistoryQueryParams.
        :type: list[str]
        """

        self._fields = fields

    @property
    def query(self):
        """
        Gets the query of this HistoryQueryParams.
        Specify a structured query to retrieve history of objects specified in attribute object_query above  Only these 2 criteria are supported:   created: it can be used for querying by updated date of the object.   Its values need to be in ISO Date format. Applicable operator include: =, <>, <= and >=   author:it can be used for querying by Id of the users who made the update. Applicable operators include: = and <>  You can use operators and and or to combine an unlimited number of criteria above

        :return: The query of this HistoryQueryParams.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this HistoryQueryParams.
        Specify a structured query to retrieve history of objects specified in attribute object_query above  Only these 2 criteria are supported:   created: it can be used for querying by updated date of the object.   Its values need to be in ISO Date format. Applicable operator include: =, <>, <= and >=   author:it can be used for querying by Id of the users who made the update. Applicable operators include: = and <>  You can use operators and and or to combine an unlimited number of criteria above

        :param query: The query of this HistoryQueryParams.
        :type: str
        """

        self._query = query

    @property
    def object_query(self):
        """
        Gets the object_query of this HistoryQueryParams.
        Specify a structured query to search for qTest objects. Refer to attribute query in the request body of Query Objects API

        :return: The object_query of this HistoryQueryParams.
        :rtype: str
        """
        return self._object_query

    @object_query.setter
    def object_query(self, object_query):
        """
        Sets the object_query of this HistoryQueryParams.
        Specify a structured query to search for qTest objects. Refer to attribute query in the request body of Query Objects API

        :param object_query: The object_query of this HistoryQueryParams.
        :type: str
        """

        self._object_query = object_query

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
        if not isinstance(other, HistoryQueryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
