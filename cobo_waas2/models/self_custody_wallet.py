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
from cobo_waas2.models.destination_wallet_type import DestinationWalletType
from typing import Optional, Set
from typing_extensions import Self


class SelfCustodyWallet(BaseModel):
    """
    Required fields for `SELF_CUSTODY_WALLET`.
    """  # noqa: E501
    destination_wallet_type: DestinationWalletType
    self_custody_wallet_challenge: StrictStr = Field(description="The challenge obtained from a previous operation.")
    self_custody_wallet_address: StrictStr = Field(description="The address of the self-custodial wallet.")
    self_custody_wallet_sign: StrictStr = Field(description="The signed message from the self-custodial wallet.")
    __properties: ClassVar[List[str]] = ["destination_wallet_type", "self_custody_wallet_challenge", "self_custody_wallet_address", "self_custody_wallet_sign"]

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
        """Create an instance of SelfCustodyWallet from a JSON string"""
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
        """Create an instance of SelfCustodyWallet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_wallet_type": obj.get("destination_wallet_type"),
            "self_custody_wallet_challenge": obj.get("self_custody_wallet_challenge"),
            "self_custody_wallet_address": obj.get("self_custody_wallet_address"),
            "self_custody_wallet_sign": obj.get("self_custody_wallet_sign")
        })
        return _obj


