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


class OrderStatus(str, Enum):
    """
    The current status of the pay-in order: - `Pending`: The order has been created and is awaiting payment. No incoming transaction has been detected. - `Processing`: An incoming transaction has been detected at the recipient address. - `Completed`: The payment has been fully received and is now complete. - `Expired`: The order has reached its expiration time without receiving any payment, or the order has been cancelled by the [Update pay-in order](https://www.cobo.com/developers/v2/api-references/payment/update-pay-in-order) operation. - `Underpaid`: The order has reached its expiration time. A payment was received but the amount is less than the order's required amount. 
    """

    """
    allowed enum values
    """
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    EXPIRED = 'Expired'
    UNDERPAID = 'Underpaid'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


