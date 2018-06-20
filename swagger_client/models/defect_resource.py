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


class DefectResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, properties=None, attachments=None, id=None, pid=None, submitted_date=None, last_modified_date=None, submitter_id=None, last_modified_user_id=None, web_url=None):
        """
        DefectResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'properties': 'list[PropertyResource]',
            'attachments': 'list[AttachmentResource]',
            'id': 'int',
            'pid': 'str',
            'submitted_date': 'datetime',
            'last_modified_date': 'datetime',
            'submitter_id': 'int',
            'last_modified_user_id': 'int',
            'web_url': 'str'
        }

        self.attribute_map = {
            'links': 'links',
            'properties': 'properties',
            'attachments': 'attachments',
            'id': 'id',
            'pid': 'pid',
            'submitted_date': 'submitted_date',
            'last_modified_date': 'last_modified_date',
            'submitter_id': 'submitter_id',
            'last_modified_user_id': 'last_modified_user_id',
            'web_url': 'web_url'
        }

        self._links = links
        self._properties = properties
        self._attachments = attachments
        self._id = id
        self._pid = pid
        self._submitted_date = submitted_date
        self._last_modified_date = last_modified_date
        self._submitter_id = submitter_id
        self._last_modified_user_id = last_modified_user_id
        self._web_url = web_url

    @property
    def links(self):
        """
        Gets the links of this DefectResource.

        :return: The links of this DefectResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this DefectResource.

        :param links: The links of this DefectResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def properties(self):
        """
        Gets the properties of this DefectResource.
        Properties of the Defect

        :return: The properties of this DefectResource.
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DefectResource.
        Properties of the Defect

        :param properties: The properties of this DefectResource.
        :type: list[PropertyResource]
        """

        self._properties = properties

    @property
    def attachments(self):
        """
        Gets the attachments of this DefectResource.
        Attachments of the Defect

        :return: The attachments of this DefectResource.
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this DefectResource.
        Attachments of the Defect

        :param attachments: The attachments of this DefectResource.
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def id(self):
        """
        Gets the id of this DefectResource.
        ID of the Defect

        :return: The id of this DefectResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DefectResource.
        ID of the Defect

        :param id: The id of this DefectResource.
        :type: int
        """

        self._id = id

    @property
    def pid(self):
        """
        Gets the pid of this DefectResource.
        PID of the Defect

        :return: The pid of this DefectResource.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this DefectResource.
        PID of the Defect

        :param pid: The pid of this DefectResource.
        :type: str
        """

        self._pid = pid

    @property
    def submitted_date(self):
        """
        Gets the submitted_date of this DefectResource.
        The date Defect was created

        :return: The submitted_date of this DefectResource.
        :rtype: datetime
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """
        Sets the submitted_date of this DefectResource.
        The date Defect was created

        :param submitted_date: The submitted_date of this DefectResource.
        :type: datetime
        """

        self._submitted_date = submitted_date

    @property
    def last_modified_date(self):
        """
        Gets the last_modified_date of this DefectResource.
        Last modified date

        :return: The last_modified_date of this DefectResource.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """
        Sets the last_modified_date of this DefectResource.
        Last modified date

        :param last_modified_date: The last_modified_date of this DefectResource.
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def submitter_id(self):
        """
        Gets the submitter_id of this DefectResource.
        ID of the User who create the Defect

        :return: The submitter_id of this DefectResource.
        :rtype: int
        """
        return self._submitter_id

    @submitter_id.setter
    def submitter_id(self, submitter_id):
        """
        Sets the submitter_id of this DefectResource.
        ID of the User who create the Defect

        :param submitter_id: The submitter_id of this DefectResource.
        :type: int
        """

        self._submitter_id = submitter_id

    @property
    def last_modified_user_id(self):
        """
        Gets the last_modified_user_id of this DefectResource.
        Last ID of the User who updated the Defect

        :return: The last_modified_user_id of this DefectResource.
        :rtype: int
        """
        return self._last_modified_user_id

    @last_modified_user_id.setter
    def last_modified_user_id(self, last_modified_user_id):
        """
        Sets the last_modified_user_id of this DefectResource.
        Last ID of the User who updated the Defect

        :param last_modified_user_id: The last_modified_user_id of this DefectResource.
        :type: int
        """

        self._last_modified_user_id = last_modified_user_id

    @property
    def web_url(self):
        """
        Gets the web_url of this DefectResource.
        Web url to the Defect

        :return: The web_url of this DefectResource.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """
        Sets the web_url of this DefectResource.
        Web url to the Defect

        :param web_url: The web_url of this DefectResource.
        :type: str
        """

        self._web_url = web_url

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
        if not isinstance(other, DefectResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
