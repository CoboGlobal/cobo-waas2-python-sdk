# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cobo_waas2.models.smart_contract_initiator import SmartContractInitiator
from cobo_waas2.models.smart_contract_wallet_type import SmartContractWalletType
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
from typing import Optional, Set
from typing_extensions import Self


class SafeWallet(BaseModel):
    """
    SafeWallet
    """  # noqa: E501
    wallet_id: StrictStr = Field(description="The wallet ID.")
    wallet_type: WalletType
    wallet_subtype: WalletSubtype
    name: StrictStr = Field(description="The wallet name.")
    org_id: StrictStr = Field(description="The ID of the owning organization.")
    chain_id: Optional[StrictStr] = Field(default=None, description="The ID of the chain on which the wallet operates.")
    smart_contract_wallet_type: SmartContractWalletType
    safe_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The Smart Contract Wallet address.")
    signers: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="The signers of the Smart Contract Wallet.")
    threshold: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The minimum number of confirmations required for the Smart Contract Wallet. ")
    cobo_safe_address: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The address of Cobo Safe.")
    initiator: Optional[SmartContractInitiator] = None
    __properties: ClassVar[List[str]] = ["wallet_id", "wallet_type", "wallet_subtype", "name", "org_id", "chain_id", "smart_contract_wallet_type", "safe_address", "signers", "threshold", "cobo_safe_address", "initiator"]

    @field_validator('safe_address')
    def safe_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
        return value

    @field_validator('cobo_safe_address')
    def cobo_safe_address_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
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
        """Create an instance of SafeWallet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of initiator
        if self.initiator:
            _dict['initiator'] = self.initiator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SafeWallet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "wallet_id": obj.get("wallet_id"),
            "wallet_type": obj.get("wallet_type"),
            "wallet_subtype": obj.get("wallet_subtype"),
            "name": obj.get("name"),
            "org_id": obj.get("org_id"),
            "chain_id": obj.get("chain_id"),
            "smart_contract_wallet_type": obj.get("smart_contract_wallet_type"),
            "safe_address": obj.get("safe_address"),
            "signers": obj.get("signers"),
            "threshold": obj.get("threshold"),
            "cobo_safe_address": obj.get("cobo_safe_address"),
            "initiator": SmartContractInitiator.from_dict(obj["initiator"]) if obj.get("initiator") is not None else None
        })
        return _obj


