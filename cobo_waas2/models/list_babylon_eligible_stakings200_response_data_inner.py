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
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.babylon_registration_status import BabylonRegistrationStatus
from cobo_waas2.models.staking_source import StakingSource
from typing import Optional, Set
from typing_extensions import Self


class ListBabylonEligibleStakings200ResponseDataInner(BaseModel):
    """
    The babylon staking position eligible for Phase-2 registration.
    """  # noqa: E501
    staking_id: Optional[StrictStr] = Field(default=None, description="The ID of the Phase-1 BTC staking position.")
    btc_address: Optional[StakingSource] = None
    babylon_address: Optional[StakingSource] = None
    staked_amount: Optional[StrictStr] = Field(default=None, description="The current amount of BTC staked.")
    status: Optional[BabylonRegistrationStatus] = None
    __properties: ClassVar[List[str]] = ["staking_id", "btc_address", "babylon_address", "staked_amount", "status"]

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
        """Create an instance of ListBabylonEligibleStakings200ResponseDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of btc_address
        if self.btc_address:
            _dict['btc_address'] = self.btc_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of babylon_address
        if self.babylon_address:
            _dict['babylon_address'] = self.babylon_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListBabylonEligibleStakings200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "staking_id": obj.get("staking_id"),
            "btc_address": StakingSource.from_dict(obj["btc_address"]) if obj.get("btc_address") is not None else None,
            "babylon_address": StakingSource.from_dict(obj["babylon_address"]) if obj.get("babylon_address") is not None else None,
            "staked_amount": obj.get("staked_amount"),
            "status": obj.get("status")
        })
        return _obj


