# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class GuardPubkeyStatus(str, Enum):
    """
    The status of a Cobo Guard public key binding. Possible values include:    - `New`: The binding is created.   - `ChangeNew`: A new binding is created    - `WaitSelfConfirm`: The binding is waiting for user confirmation on the old Cobo Guard.   - `WaitConfirm`: The binding is waiting for admin confirmation.   - `WaitActive`: The binding is waiting to become active.   - `Active`: The binding has come into effect.   - `Freeze`: The binding is frozen.   - `Invalid`: The binding is invalid. 
    """

    """
    allowed enum values
    """
    NEW = 'New'
    CHANGENEW = 'ChangeNew'
    WAITSELFCONFIRM = 'WaitSelfConfirm'
    WAITCONFIRM = 'WaitConfirm'
    WAITACTIVE = 'WaitActive'
    ACTIVE = 'Active'
    FREEZE = 'Freeze'
    INVALID = 'Invalid'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GuardPubkeyStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


