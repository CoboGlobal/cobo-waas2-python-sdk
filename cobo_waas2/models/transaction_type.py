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


class TransactionType(str, Enum):
    """
    The transaction type. Possible values include:    - `Deposit`: A deposit transaction.   - `Withdrawal`: A withdrawal transaction.   - `ContractCall`: A transaction that interacts with a smart contract.   - `MessageSign`: A transaction that signs a message.    - `ExternalSafeTx`: A transaction to a Smart Contract Wallet (Safe{Wallet}) that requires one or multiple signatures to be executed.   - `Stake`: A transaction that creates a staking request.   - `Unstake`: A transaction that creates a unstaking request. 
    """

    """
    allowed enum values
    """
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'
    CONTRACTCALL = 'ContractCall'
    MESSAGESIGN = 'MessageSign'
    EXTERNALSAFETX = 'ExternalSafeTx'
    STAKE = 'Stake'
    UNSTAKE = 'Unstake'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


