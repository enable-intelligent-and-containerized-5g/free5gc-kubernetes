# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LocationFilterAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    TAI = "TAI"
    CELL_ID = "CELL_ID"
    RAN_NODE = "RAN_NODE"
    N3IWF = "N3IWF"
    UE_IP = "UE_IP"
    UDP_PORT = "UDP_PORT"
    TNAP_ID = "TNAP_ID"
    GLI = "GLI"
    TWAP_ID = "TWAP_ID"
    def __init__(self):  # noqa: E501
        """LocationFilterAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'LocationFilterAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocationFilter_anyOf of this LocationFilterAnyOf.  # noqa: E501
        :rtype: LocationFilterAnyOf
        """
        return util.deserialize_model(dikt, cls)