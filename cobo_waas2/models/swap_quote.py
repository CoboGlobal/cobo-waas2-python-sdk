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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class SwapQuote(BaseModel):
    """
    SwapQuote
    """  # noqa: E501
    quote_id: StrictStr = Field(description="The unique id of quote.")
    pay_token_id: StrictStr = Field(description="The token ID to pay.")
    pay_amount: StrictStr = Field(description="The amount of tokens to pay.")
    receive_token_id: StrictStr = Field(description="The token ID to receive.")
    receive_amount: StrictStr = Field(description="The amount of tokens to receive.")
    fee_token_id: StrictStr = Field(description="The token ID for the service fee.")
    fee_amount: StrictStr = Field(description="The amount of tokens for the service fee.")
    estimated_network_fee_amount: Optional[StrictStr] = Field(default=None, description="The estimated amount of tokens for the network fee.")
    min_receive_amount: Optional[StrictStr] = Field(default=None, description="The minimum amount of tokens to receive if the pay amount is specified.")
    max_pay_amount: Optional[StrictStr] = Field(default=None, description="The maximum amount of tokens to pay if the receive amount is specified.")
    quote_expired_timestamp: StrictInt = Field(description="The time when the quote will expire, in Unix timestamp format, measured in milliseconds.")
    __properties: ClassVar[List[str]] = ["quote_id", "pay_token_id", "pay_amount", "receive_token_id", "receive_amount", "fee_token_id", "fee_amount", "estimated_network_fee_amount", "min_receive_amount", "max_pay_amount", "quote_expired_timestamp"]

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
        """Create an instance of SwapQuote from a JSON string"""
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
        """Create an instance of SwapQuote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quote_id": obj.get("quote_id"),
            "pay_token_id": obj.get("pay_token_id"),
            "pay_amount": obj.get("pay_amount"),
            "receive_token_id": obj.get("receive_token_id"),
            "receive_amount": obj.get("receive_amount"),
            "fee_token_id": obj.get("fee_token_id"),
            "fee_amount": obj.get("fee_amount"),
            "estimated_network_fee_amount": obj.get("estimated_network_fee_amount"),
            "min_receive_amount": obj.get("min_receive_amount"),
            "max_pay_amount": obj.get("max_pay_amount"),
            "quote_expired_timestamp": obj.get("quote_expired_timestamp")
        })
        return _obj


