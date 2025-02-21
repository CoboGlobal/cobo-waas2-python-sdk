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
from cobo_waas2.models.babylon_registration_request_status import BabylonRegistrationRequestStatus
from cobo_waas2.models.staking_source import StakingSource
from typing import Optional, Set
from typing_extensions import Self


class BabylonStakingRegistration(BaseModel):
    """
    The babylon staking registration.
    """  # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for tracking the staking registration")
    staking_id: Optional[StrictStr] = Field(default=None, description="The staking ID that is registered for Babylon staking.")
    babylon_address: Optional[StakingSource] = None
    btc_address: Optional[StakingSource] = None
    status: Optional[BabylonRegistrationRequestStatus] = None
    staked_amount: Optional[StrictStr] = Field(default=None, description="The amount of BTC that is staked.")
    error_message: Optional[StrictStr] = Field(default=None, description="The error message of the airdrop claim request.")
    created_timestamp: Optional[StrictInt] = Field(default=None, description="The timestamp when the registration was created")
    updated_timestamp: Optional[StrictInt] = Field(default=None, description="The timestamp when the registration was updated")
    __properties: ClassVar[List[str]] = ["id", "staking_id", "babylon_address", "btc_address", "status", "staked_amount", "error_message", "created_timestamp", "updated_timestamp"]

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
        """Create an instance of BabylonStakingRegistration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of babylon_address
        if self.babylon_address:
            _dict['babylon_address'] = self.babylon_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of btc_address
        if self.btc_address:
            _dict['btc_address'] = self.btc_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BabylonStakingRegistration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "staking_id": obj.get("staking_id"),
            "babylon_address": StakingSource.from_dict(obj["babylon_address"]) if obj.get("babylon_address") is not None else None,
            "btc_address": StakingSource.from_dict(obj["btc_address"]) if obj.get("btc_address") is not None else None,
            "status": obj.get("status"),
            "staked_amount": obj.get("staked_amount"),
            "error_message": obj.get("error_message"),
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp")
        })
        return _obj


