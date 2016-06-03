# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Solution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Solution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'costs': 'int',
            'distance': 'int',
            'time': 'int',
            'no_unassigned': 'int',
            'routes': 'list[Route]',
            'unassigned': 'object'
        }

        self.attribute_map = {
            'costs': 'costs',
            'distance': 'distance',
            'time': 'time',
            'no_unassigned': 'no_unassigned',
            'routes': 'routes',
            'unassigned': 'unassigned'
        }

        self._costs = None
        self._distance = None
        self._time = None
        self._no_unassigned = None
        self._routes = None
        self._unassigned = None

    @property
    def costs(self):
        """
        Gets the costs of this Solution.
        overall costs of solution

        :return: The costs of this Solution.
        :rtype: int
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """
        Sets the costs of this Solution.
        overall costs of solution

        :param costs: The costs of this Solution.
        :type: int
        """
        self._costs = costs

    @property
    def distance(self):
        """
        Gets the distance of this Solution.
        overall travel distance in meters

        :return: The distance of this Solution.
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """
        Sets the distance of this Solution.
        overall travel distance in meters

        :param distance: The distance of this Solution.
        :type: int
        """
        self._distance = distance

    @property
    def time(self):
        """
        Gets the time of this Solution.
        overall travel time in ms

        :return: The time of this Solution.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this Solution.
        overall travel time in ms

        :param time: The time of this Solution.
        :type: int
        """
        self._time = time

    @property
    def no_unassigned(self):
        """
        Gets the no_unassigned of this Solution.
        number of jobs that could not be assigned to final solution

        :return: The no_unassigned of this Solution.
        :rtype: int
        """
        return self._no_unassigned

    @no_unassigned.setter
    def no_unassigned(self, no_unassigned):
        """
        Sets the no_unassigned of this Solution.
        number of jobs that could not be assigned to final solution

        :param no_unassigned: The no_unassigned of this Solution.
        :type: int
        """
        self._no_unassigned = no_unassigned

    @property
    def routes(self):
        """
        Gets the routes of this Solution.
        An array of routes

        :return: The routes of this Solution.
        :rtype: list[Route]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """
        Sets the routes of this Solution.
        An array of routes

        :param routes: The routes of this Solution.
        :type: list[Route]
        """
        self._routes = routes

    @property
    def unassigned(self):
        """
        Gets the unassigned of this Solution.


        :return: The unassigned of this Solution.
        :rtype: object
        """
        return self._unassigned

    @unassigned.setter
    def unassigned(self, unassigned):
        """
        Sets the unassigned of this Solution.


        :param unassigned: The unassigned of this Solution.
        :type: object
        """
        self._unassigned = unassigned

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
