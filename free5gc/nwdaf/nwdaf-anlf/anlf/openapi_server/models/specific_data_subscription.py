# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.data_subscription import DataSubscription
from openapi_server import util

from openapi_server.models.data_subscription import DataSubscription  # noqa: E501

class SpecificDataSubscription(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subscription_id=None, producer_id=None, producer_set_id=None, data_sub=None):  # noqa: E501
        """SpecificDataSubscription - a model defined in OpenAPI

        :param subscription_id: The subscription_id of this SpecificDataSubscription.  # noqa: E501
        :type subscription_id: str
        :param producer_id: The producer_id of this SpecificDataSubscription.  # noqa: E501
        :type producer_id: str
        :param producer_set_id: The producer_set_id of this SpecificDataSubscription.  # noqa: E501
        :type producer_set_id: str
        :param data_sub: The data_sub of this SpecificDataSubscription.  # noqa: E501
        :type data_sub: DataSubscription
        """
        self.openapi_types = {
            'subscription_id': str,
            'producer_id': str,
            'producer_set_id': str,
            'data_sub': DataSubscription
        }

        self.attribute_map = {
            'subscription_id': 'subscriptionId',
            'producer_id': 'producerId',
            'producer_set_id': 'producerSetId',
            'data_sub': 'dataSub'
        }

        self.subscription_id = subscription_id
        self.producer_id = producer_id
        self.producer_set_id = producer_set_id
        self.data_sub = data_sub

    @classmethod
    def from_dict(cls, dikt) -> 'SpecificDataSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpecificDataSubscription of this SpecificDataSubscription.  # noqa: E501
        :rtype: SpecificDataSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SpecificDataSubscription.


        :return: The subscription_id of this SpecificDataSubscription.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SpecificDataSubscription.


        :param subscription_id: The subscription_id of this SpecificDataSubscription.
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def producer_id(self):
        """Gets the producer_id of this SpecificDataSubscription.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :return: The producer_id of this SpecificDataSubscription.
        :rtype: str
        """
        return self._producer_id

    @producer_id.setter
    def producer_id(self, producer_id):
        """Sets the producer_id of this SpecificDataSubscription.

        String uniquely identifying a NF instance. The format of the NF Instance ID shall be a  Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122.    # noqa: E501

        :param producer_id: The producer_id of this SpecificDataSubscription.
        :type producer_id: str
        """

        self._producer_id = producer_id

    @property
    def producer_set_id(self):
        """Gets the producer_set_id of this SpecificDataSubscription.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :return: The producer_set_id of this SpecificDataSubscription.
        :rtype: str
        """
        return self._producer_set_id

    @producer_set_id.setter
    def producer_set_id(self, producer_set_id):
        """Sets the producer_set_id of this SpecificDataSubscription.

        NF Set Identifier (see clause 28.12 of 3GPP TS 23.003), formatted as the following string \"set<Set ID>.<nftype>set.5gc.mnc<MNC>.mcc<MCC>\", or  \"set<SetID>.<NFType>set.5gc.nid<NID>.mnc<MNC>.mcc<MCC>\" with  <MCC> encoded as defined in clause 5.4.2 (\"Mcc\" data type definition)  <MNC> encoding the Mobile Network Code part of the PLMN, comprising 3 digits.    If there are only 2 significant digits in the MNC, one \"0\" digit shall be inserted    at the left side to fill the 3 digits coding of MNC.  Pattern: '^[0-9]{3}$' <NFType> encoded as a value defined in Table 6.1.6.3.3-1 of 3GPP TS 29.510 but    with lower case characters <Set ID> encoded as a string of characters consisting of    alphabetic characters (A-Z and a-z), digits (0-9) and/or the hyphen (-) and that    shall end with either an alphabetic character or a digit.    # noqa: E501

        :param producer_set_id: The producer_set_id of this SpecificDataSubscription.
        :type producer_set_id: str
        """

        self._producer_set_id = producer_set_id

    @property
    def data_sub(self):
        """Gets the data_sub of this SpecificDataSubscription.


        :return: The data_sub of this SpecificDataSubscription.
        :rtype: DataSubscription
        """
        return self._data_sub

    @data_sub.setter
    def data_sub(self, data_sub):
        """Sets the data_sub of this SpecificDataSubscription.


        :param data_sub: The data_sub of this SpecificDataSubscription.
        :type data_sub: DataSubscription
        """

        self._data_sub = data_sub