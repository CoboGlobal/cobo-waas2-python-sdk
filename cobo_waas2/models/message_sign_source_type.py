# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MessageSignSourceType(str, Enum):
    """
    The wallet subtype. Possible values include: - `Org-Controlled`: MPC Wallets (Organization-Controlled). - `User-Controlled`: MPC Wallets (User-Controlled). 
    """

    """
    allowed enum values
    """
    ORG_MINUS_CONTROLLED = 'Org-Controlled'
    USER_MINUS_CONTROLLED = 'User-Controlled'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageSignSourceType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


