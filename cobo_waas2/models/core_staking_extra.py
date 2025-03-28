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
from typing import Any, ClassVar, Dict, List
from cobo_waas2.models.staking_pool_type import StakingPoolType
from typing import Optional, Set
from typing_extensions import Self


class CoreStakingExtra(BaseModel):
    """
    CoreStakingExtra
    """  # noqa: E501
    pool_type: StakingPoolType
    pos_chain: StrictStr = Field(description="The Proof-of-Stake (PoS) chain.")
    staker_address: StrictStr = Field(description="The staker's Bitcoin address.")
    validator_address: StrictStr = Field(description="The validator's EVM address.")
    reward_address: StrictStr = Field(description="The EVM address to receive staking rewards.")
    timelock: StrictInt = Field(description="The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal.")
    __properties: ClassVar[List[str]] = ["pool_type", "pos_chain", "staker_address", "validator_address", "reward_address", "timelock"]

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
        """Create an instance of CoreStakingExtra from a JSON string"""
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
        """Create an instance of CoreStakingExtra from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pool_type": obj.get("pool_type"),
            "pos_chain": obj.get("pos_chain"),
            "staker_address": obj.get("staker_address"),
            "validator_address": obj.get("validator_address"),
            "reward_address": obj.get("reward_address"),
            "timelock": obj.get("timelock")
        })
        return _obj


