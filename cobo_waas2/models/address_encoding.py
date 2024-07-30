# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddressEncoding(str, Enum):
    """
    The address encoding formats. This property only applies to blockchains that have a similar architecture to Bitcoin.
    """

    """
    allowed enum values
    """
    ENCODING_P2_PKH = 'ENCODING_P2PKH'
    ENCODING_P2_SH_P2_WPKH = 'ENCODING_P2SH_P2WPKH'
    ENCODING_BECH32 = 'ENCODING_BECH32'
    ENCODING_P2_PKH_UNCOMPRESSED = 'ENCODING_P2PKH_UNCOMPRESSED'
    ENCODING_P2_SH_P2_MS = 'ENCODING_P2SH_P2MS'
    ENCODING_P2_SH_P2_WSH_P2_MS = 'ENCODING_P2SH_P2WSH_P2MS'
    ENCODING_P2_TR = 'ENCODING_P2TR'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddressEncoding from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


