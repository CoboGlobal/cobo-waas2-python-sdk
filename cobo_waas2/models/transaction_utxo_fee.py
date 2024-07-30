# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class TransactionUtxoFee(BaseModel):
    """
    The transaction fee actually charged by the chain that uses the UTXO fee model, such as Bitcoin. The transaction fee is calculated by multiplying the fee rate by the transaction size. This can be expressed as: Transaction fee = fee rate * transaction size. 
    """  # noqa: E501
    fee_rate: Optional[StrictStr] = Field(default=None, description="The fee rate in sat/vByte. The fee rate represents the satoshis you are willing to pay for each byte of data that your transaction will consume on the blockchain.")
    fee_type: FeeType
    token_id: Optional[StrictStr] = Field(default=None, description="The token ID of the transaction fee.")
    fee_used: Optional[StrictStr] = Field(default=None, description="The transaction fee.")
    max_fee_amount: Optional[StrictStr] = Field(default=None, description="The maximum fee that you are willing to pay for the transaction. The transaction will fail if the transaction fee exceeds the maximum fee.")
    __properties: ClassVar[List[str]] = ["fee_rate", "fee_type", "token_id", "fee_used", "max_fee_amount"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionUtxoFee from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionUtxoFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fee_rate": obj.get("fee_rate"),
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id"),
            "fee_used": obj.get("fee_used"),
            "max_fee_amount": obj.get("max_fee_amount")
        })
        return _obj


