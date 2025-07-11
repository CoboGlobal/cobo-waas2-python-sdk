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
from cobo_waas2.models.acquiring_type import AcquiringType
from typing import Optional, Set
from typing_extensions import Self


class SettlementInfo(BaseModel):
    """
    SettlementInfo
    """  # noqa: E501
    merchant_id: Optional[StrictStr] = Field(default=None, description="The merchant ID. For developer balance, this field will be empty.")
    token_id: Optional[StrictStr] = Field(default=None, description="The ID of the cryptocurrency.")
    available_amount: StrictStr = Field(description="The amount available for settlement or refund, in the specified cryptocurrency.")
    available_currency_balance: Optional[StrictStr] = Field(default=None, description="The amount available for settlement or refund, in the specified fiat currency.")
    pending_amount: Optional[StrictStr] = Field(default=None, description="The amount unavailable for settlement or refund, in the specified cryptocurrency.")
    pending_currency_balance: Optional[StrictStr] = Field(default=None, description="The amount unavailable for settlement or refund, in the specified fiat currency.")
    settled_amount: Optional[StrictStr] = Field(default=None, description="The amount already settled, in the specified cryptocurrency.")
    acquiring_type: Optional[AcquiringType] = None
    created_timestamp: Optional[StrictInt] = Field(default=None, description="The creation time of the settlement, represented as a UNIX timestamp in seconds.")
    updated_timestamp: Optional[StrictInt] = Field(default=None, description="The last update time of the settlement, represented as a UNIX timestamp in seconds.")
    __properties: ClassVar[List[str]] = ["merchant_id", "token_id", "available_amount", "available_currency_balance", "pending_amount", "pending_currency_balance", "settled_amount", "acquiring_type", "created_timestamp", "updated_timestamp"]

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
        """Create an instance of SettlementInfo from a JSON string"""
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
        """Create an instance of SettlementInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "merchant_id": obj.get("merchant_id"),
            "token_id": obj.get("token_id"),
            "available_amount": obj.get("available_amount"),
            "available_currency_balance": obj.get("available_currency_balance"),
            "pending_amount": obj.get("pending_amount"),
            "pending_currency_balance": obj.get("pending_currency_balance"),
            "settled_amount": obj.get("settled_amount"),
            "acquiring_type": obj.get("acquiring_type"),
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp")
        })
        return _obj


