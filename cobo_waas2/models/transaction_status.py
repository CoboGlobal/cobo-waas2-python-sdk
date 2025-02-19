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


class TransactionStatus(str, Enum):
    """
    The transaction status. For more details including sub-statuses, please refer to [Transaction statuses and sub-statuses](https://www.cobo.com/developers/v2/guides/transactions/status). 
    """

    """
    allowed enum values
    """
    SUBMITTED = 'Submitted'
    PENDINGSCREENING = 'PendingScreening'
    PENDINGAUTHORIZATION = 'PendingAuthorization'
    PENDINGSIGNATURE = 'PendingSignature'
    BROADCASTING = 'Broadcasting'
    CONFIRMING = 'Confirming'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    REJECTED = 'Rejected'
    PENDING = 'Pending'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


