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
from cobo_waas2.models.amount_details_inner import AmountDetailsInner
from cobo_waas2.models.babylon_validator import BabylonValidator
from cobo_waas2.models.staking_pool_id import StakingPoolId
from cobo_waas2.models.stakings_extra import StakingsExtra
from typing import Optional, Set
from typing_extensions import Self


class Stakings(BaseModel):
    """
    The information about a staking position.
    """  # noqa: E501
    id: StrictStr = Field(description="The ID of the staking position.")
    wallet_id: StrictStr = Field(description="The staker's wallet ID.")
    address: StrictStr = Field(description="The staker's wallet address.")
    amounts: List[AmountDetailsInner] = Field(description="The details about the staking amount.")
    pool_id: StakingPoolId
    token_id: StrictStr = Field(description="The token ID.")
    rewards_info: Optional[Dict[str, Any]] = Field(default=None, description="The information about the staking rewards.")
    created_timestamp: StrictInt = Field(description="The time when the staking position was created.")
    updated_timestamp: StrictInt = Field(description="The time when the staking position was last updated.")
    validator_info: BabylonValidator
    extra: Optional[StakingsExtra] = None
    __properties: ClassVar[List[str]] = ["id", "wallet_id", "address", "amounts", "pool_id", "token_id", "rewards_info", "created_timestamp", "updated_timestamp", "validator_info", "extra"]

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
        """Create an instance of Stakings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in amounts (list)
        _items = []
        if self.amounts:
            for _item in self.amounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['amounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of validator_info
        if self.validator_info:
            _dict['validator_info'] = self.validator_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra
        if self.extra:
            _dict['extra'] = self.extra.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Stakings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "wallet_id": obj.get("wallet_id"),
            "address": obj.get("address"),
            "amounts": [AmountDetailsInner.from_dict(_item) for _item in obj["amounts"]] if obj.get("amounts") is not None else None,
            "pool_id": obj.get("pool_id"),
            "token_id": obj.get("token_id"),
            "rewards_info": obj.get("rewards_info"),
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp"),
            "validator_info": BabylonValidator.from_dict(obj["validator_info"]) if obj.get("validator_info") is not None else None,
            "extra": StakingsExtra.from_dict(obj["extra"]) if obj.get("extra") is not None else None
        })
        return _obj


