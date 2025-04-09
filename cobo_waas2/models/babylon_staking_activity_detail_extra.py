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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cobo_waas2.models.staking_pool_type import StakingPoolType
from typing import Optional, Set
from typing_extensions import Self


class BabylonStakingActivityDetailExtra(BaseModel):
    """
    BabylonStakingActivityDetailExtra
    """  # noqa: E501
    pool_type: StakingPoolType
    finality_provider_public_key: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The public key of the finality provider.")
    stake_block_time: Optional[StrictInt] = Field(default=None, description="The number of blocks that need to be processed before the locked tokens are unlocked and become accessible.")
    auto_broadcast: Optional[StrictBool] = Field(default=None, description="Whether to automatically broadcast the transaction.  - `true`: Automatically broadcast the transaction. - `false`: The transaction will not be submitted to the blockchain automatically. You can call [Broadcast signed transactions](https://www.cobo.com/developers/v2/api-references/transactions/broadcast-signed-transactions) to broadcast the transaction to the blockchain, or retrieve the signed raw transaction data `raw_tx` by calling [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information) and broadcast it yourself. ")
    __properties: ClassVar[List[str]] = ["pool_type", "finality_provider_public_key", "stake_block_time", "auto_broadcast"]

    @field_validator('finality_provider_public_key')
    def finality_provider_public_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{64}$/")
        return value

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
        """Create an instance of BabylonStakingActivityDetailExtra from a JSON string"""
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
        """Create an instance of BabylonStakingActivityDetailExtra from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pool_type": obj.get("pool_type"),
            "finality_provider_public_key": obj.get("finality_provider_public_key"),
            "stake_block_time": obj.get("stake_block_time"),
            "auto_broadcast": obj.get("auto_broadcast")
        })
        return _obj


