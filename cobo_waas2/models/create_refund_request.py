# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.refund_type import RefundType
from typing import Optional, Set
from typing_extensions import Self


class CreateRefundRequest(BaseModel):
    """
    CreateRefundRequest
    """  # noqa: E501
    request_id: StrictStr = Field(description="The request ID that is used to track a refund request. The request ID is provided by you and must be unique.")
    merchant_id: Optional[StrictStr] = Field(default=None, description="The merchant ID.")
    payable_amount: StrictStr = Field(description="The amount to refund in cryptocurrency.")
    to_address: StrictStr = Field(description="The address where the refunded cryptocurrency will be sent.")
    token_id: StrictStr = Field(description="The ID of the cryptocurrency used for refund. Supported values:    - USDC: `ETH_USDC`, `ARBITRUM_USDC`, `SOL_USDC`, `BASE_USDC`, `MATIC_USDC`, `BSC_USDC`   - USDT: `TRON_USDT`, `ETH_USDT`, `ARBITRUM_USDT`, `SOL_USDT`, `BASE_USDT`, `MATIC_USDT`, `BSC_USDT` ")
    refund_type: RefundType
    order_id: Optional[StrictStr] = Field(default=None, description="The ID of the original pay-in order associated with this refund. Use this to track refunds against specific payments.")
    charge_merchant_fee: Optional[StrictBool] = Field(default=None, description="Indicates whether the merchant should bear the transaction fee for the refund.  If true, the fee will be deducted from merchant's account balance. ")
    merchant_fee_amount: Optional[StrictStr] = Field(default=None, description="The amount of the transaction fee that the merchant will bear for the refund.  This is only applicable if `charge_merchant_fee` is set to true. ")
    merchant_fee_token_id: Optional[StrictStr] = Field(default=None, description="The ID of the cryptocurrency used for the transaction fee.  This is only applicable if `charge_merchant_fee` is set to true. ")
    __properties: ClassVar[List[str]] = ["request_id", "merchant_id", "payable_amount", "to_address", "token_id", "refund_type", "order_id", "charge_merchant_fee", "merchant_fee_amount", "merchant_fee_token_id"]

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
        """Create an instance of CreateRefundRequest from a JSON string"""
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
        """Create an instance of CreateRefundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_id": obj.get("request_id"),
            "merchant_id": obj.get("merchant_id"),
            "payable_amount": obj.get("payable_amount"),
            "to_address": obj.get("to_address"),
            "token_id": obj.get("token_id"),
            "refund_type": obj.get("refund_type"),
            "order_id": obj.get("order_id"),
            "charge_merchant_fee": obj.get("charge_merchant_fee"),
            "merchant_fee_amount": obj.get("merchant_fee_amount"),
            "merchant_fee_token_id": obj.get("merchant_fee_token_id")
        })
        return _obj


