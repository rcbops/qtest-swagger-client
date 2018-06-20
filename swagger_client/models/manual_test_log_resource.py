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


class ManualTestLogResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, test_case_version_id=None, exe_start_date=None, exe_end_date=None, note=None, attachments=None, name=None, planned_exe_time=None, actual_exe_time=None, build_number=None, build_url=None, properties=None, status=None, result_number=None, test_step_logs=None, defects=None):
        """
        ManualTestLogResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'id': 'int',
            'test_case_version_id': 'int',
            'exe_start_date': 'datetime',
            'exe_end_date': 'datetime',
            'note': 'str',
            'attachments': 'list[AttachmentResource]',
            'name': 'str',
            'planned_exe_time': 'int',
            'actual_exe_time': 'int',
            'build_number': 'str',
            'build_url': 'str',
            'properties': 'list[PropertyResource]',
            'status': 'StatusResource',
            'result_number': 'int',
            'test_step_logs': 'list[TestStepLogResource]',
            'defects': 'list[LinkedDefectResource]'
        }

        self.attribute_map = {
            'links': 'links',
            'id': 'id',
            'test_case_version_id': 'test_case_version_id',
            'exe_start_date': 'exe_start_date',
            'exe_end_date': 'exe_end_date',
            'note': 'note',
            'attachments': 'attachments',
            'name': 'name',
            'planned_exe_time': 'planned_exe_time',
            'actual_exe_time': 'actual_exe_time',
            'build_number': 'build_number',
            'build_url': 'build_url',
            'properties': 'properties',
            'status': 'status',
            'result_number': 'result_number',
            'test_step_logs': 'test_step_logs',
            'defects': 'defects'
        }

        self._links = links
        self._id = id
        self._test_case_version_id = test_case_version_id
        self._exe_start_date = exe_start_date
        self._exe_end_date = exe_end_date
        self._note = note
        self._attachments = attachments
        self._name = name
        self._planned_exe_time = planned_exe_time
        self._actual_exe_time = actual_exe_time
        self._build_number = build_number
        self._build_url = build_url
        self._properties = properties
        self._status = status
        self._result_number = result_number
        self._test_step_logs = test_step_logs
        self._defects = defects

    @property
    def links(self):
        """
        Gets the links of this ManualTestLogResource.

        :return: The links of this ManualTestLogResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ManualTestLogResource.

        :param links: The links of this ManualTestLogResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this ManualTestLogResource.

        :return: The id of this ManualTestLogResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManualTestLogResource.

        :param id: The id of this ManualTestLogResource.
        :type: int
        """

        self._id = id

    @property
    def test_case_version_id(self):
        """
        Gets the test_case_version_id of this ManualTestLogResource.
        ID of the Test Case Version

        :return: The test_case_version_id of this ManualTestLogResource.
        :rtype: int
        """
        return self._test_case_version_id

    @test_case_version_id.setter
    def test_case_version_id(self, test_case_version_id):
        """
        Sets the test_case_version_id of this ManualTestLogResource.
        ID of the Test Case Version

        :param test_case_version_id: The test_case_version_id of this ManualTestLogResource.
        :type: int
        """

        self._test_case_version_id = test_case_version_id

    @property
    def exe_start_date(self):
        """
        Gets the exe_start_date of this ManualTestLogResource.
        Execution start date

        :return: The exe_start_date of this ManualTestLogResource.
        :rtype: datetime
        """
        return self._exe_start_date

    @exe_start_date.setter
    def exe_start_date(self, exe_start_date):
        """
        Sets the exe_start_date of this ManualTestLogResource.
        Execution start date

        :param exe_start_date: The exe_start_date of this ManualTestLogResource.
        :type: datetime
        """
        if exe_start_date is None:
            raise ValueError("Invalid value for `exe_start_date`, must not be `None`")

        self._exe_start_date = exe_start_date

    @property
    def exe_end_date(self):
        """
        Gets the exe_end_date of this ManualTestLogResource.
        Execution end date

        :return: The exe_end_date of this ManualTestLogResource.
        :rtype: datetime
        """
        return self._exe_end_date

    @exe_end_date.setter
    def exe_end_date(self, exe_end_date):
        """
        Sets the exe_end_date of this ManualTestLogResource.
        Execution end date

        :param exe_end_date: The exe_end_date of this ManualTestLogResource.
        :type: datetime
        """
        if exe_end_date is None:
            raise ValueError("Invalid value for `exe_end_date`, must not be `None`")

        self._exe_end_date = exe_end_date

    @property
    def note(self):
        """
        Gets the note of this ManualTestLogResource.
        Note

        :return: The note of this ManualTestLogResource.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this ManualTestLogResource.
        Note

        :param note: The note of this ManualTestLogResource.
        :type: str
        """

        self._note = note

    @property
    def attachments(self):
        """
        Gets the attachments of this ManualTestLogResource.
        Test Log attachments

        :return: The attachments of this ManualTestLogResource.
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this ManualTestLogResource.
        Test Log attachments

        :param attachments: The attachments of this ManualTestLogResource.
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def name(self):
        """
        Gets the name of this ManualTestLogResource.
        Test Run's name

        :return: The name of this ManualTestLogResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManualTestLogResource.
        Test Run's name

        :param name: The name of this ManualTestLogResource.
        :type: str
        """

        self._name = name

    @property
    def planned_exe_time(self):
        """
        Gets the planned_exe_time of this ManualTestLogResource.

        :return: The planned_exe_time of this ManualTestLogResource.
        :rtype: int
        """
        return self._planned_exe_time

    @planned_exe_time.setter
    def planned_exe_time(self, planned_exe_time):
        """
        Sets the planned_exe_time of this ManualTestLogResource.

        :param planned_exe_time: The planned_exe_time of this ManualTestLogResource.
        :type: int
        """
        if planned_exe_time is not None and planned_exe_time > 9999999:
            raise ValueError("Invalid value for `planned_exe_time`, must be a value less than or equal to `9999999`")
        if planned_exe_time is not None and planned_exe_time < 0:
            raise ValueError("Invalid value for `planned_exe_time`, must be a value greater than or equal to `0`")

        self._planned_exe_time = planned_exe_time

    @property
    def actual_exe_time(self):
        """
        Gets the actual_exe_time of this ManualTestLogResource.

        :return: The actual_exe_time of this ManualTestLogResource.
        :rtype: int
        """
        return self._actual_exe_time

    @actual_exe_time.setter
    def actual_exe_time(self, actual_exe_time):
        """
        Sets the actual_exe_time of this ManualTestLogResource.

        :param actual_exe_time: The actual_exe_time of this ManualTestLogResource.
        :type: int
        """

        self._actual_exe_time = actual_exe_time

    @property
    def build_number(self):
        """
        Gets the build_number of this ManualTestLogResource.
        Jenkins jobs build number

        :return: The build_number of this ManualTestLogResource.
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """
        Sets the build_number of this ManualTestLogResource.
        Jenkins jobs build number

        :param build_number: The build_number of this ManualTestLogResource.
        :type: str
        """

        self._build_number = build_number

    @property
    def build_url(self):
        """
        Gets the build_url of this ManualTestLogResource.
        Jenkins jobs build URL

        :return: The build_url of this ManualTestLogResource.
        :rtype: str
        """
        return self._build_url

    @build_url.setter
    def build_url(self, build_url):
        """
        Sets the build_url of this ManualTestLogResource.
        Jenkins jobs build URL

        :param build_url: The build_url of this ManualTestLogResource.
        :type: str
        """

        self._build_url = build_url

    @property
    def properties(self):
        """
        Gets the properties of this ManualTestLogResource.

        :return: The properties of this ManualTestLogResource.
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ManualTestLogResource.

        :param properties: The properties of this ManualTestLogResource.
        :type: list[PropertyResource]
        """

        self._properties = properties

    @property
    def status(self):
        """
        Gets the status of this ManualTestLogResource.
        Test Log status

        :return: The status of this ManualTestLogResource.
        :rtype: StatusResource
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ManualTestLogResource.
        Test Log status

        :param status: The status of this ManualTestLogResource.
        :type: StatusResource
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def result_number(self):
        """
        Gets the result_number of this ManualTestLogResource.

        :return: The result_number of this ManualTestLogResource.
        :rtype: int
        """
        return self._result_number

    @result_number.setter
    def result_number(self, result_number):
        """
        Sets the result_number of this ManualTestLogResource.

        :param result_number: The result_number of this ManualTestLogResource.
        :type: int
        """

        self._result_number = result_number

    @property
    def test_step_logs(self):
        """
        Gets the test_step_logs of this ManualTestLogResource.
        Arrays of Test Step Log,   With called test steps, the \"called_test_case_id\" and \"parent_test_step_id\" must be included in request body.

        :return: The test_step_logs of this ManualTestLogResource.
        :rtype: list[TestStepLogResource]
        """
        return self._test_step_logs

    @test_step_logs.setter
    def test_step_logs(self, test_step_logs):
        """
        Sets the test_step_logs of this ManualTestLogResource.
        Arrays of Test Step Log,   With called test steps, the \"called_test_case_id\" and \"parent_test_step_id\" must be included in request body.

        :param test_step_logs: The test_step_logs of this ManualTestLogResource.
        :type: list[TestStepLogResource]
        """

        self._test_step_logs = test_step_logs

    @property
    def defects(self):
        """
        Gets the defects of this ManualTestLogResource.
        Array of Defect

        :return: The defects of this ManualTestLogResource.
        :rtype: list[LinkedDefectResource]
        """
        return self._defects

    @defects.setter
    def defects(self, defects):
        """
        Sets the defects of this ManualTestLogResource.
        Array of Defect

        :param defects: The defects of this ManualTestLogResource.
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
        if not isinstance(other, ManualTestLogResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
