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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from cobo_waas2.models.cobo_safe_delegate_type import CoboSafeDelegateType
from typing import Optional, Set
from typing_extensions import Self


class MPCDelegate(BaseModel):
    """
    The information about the MPC Wallet as the Delegate. You can call the [List Delegates](https://www.cobo.com/developers/v2/api-references/wallets--smart-contract-wallets/list-delegates) operation to retrieve the applicable Delegates.
    """  # noqa: E501
    delegate_type: CoboSafeDelegateType
    wallet_id: StrictStr = Field(description="The wallet ID of the Delegate. This is required when initiating a transfer or contract call from Smart Contract Wallets (Safe{Wallet}).")
    address: StrictStr = Field(description="The wallet address of the Delegate. This is required when initiating a transfer or contract call from Smart Contract Wallets (Safe{Wallet}).")
    __properties: ClassVar[List[str]] = ["delegate_type", "wallet_id", "address"]

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
        """Create an instance of MPCDelegate from a JSON string"""
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
        """Create an instance of MPCDelegate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delegate_type": obj.get("delegate_type"),
            "wallet_id": obj.get("wallet_id"),
            "address": obj.get("address")
        })
        return _obj


