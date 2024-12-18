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
from cobo_waas2.models.auto_fuel_type import AutoFuelType
from cobo_waas2.models.transaction_request_fee import TransactionRequestFee
from cobo_waas2.models.transfer_destination import TransferDestination
from cobo_waas2.models.transfer_source import TransferSource
from typing import Optional, Set
from typing_extensions import Self


class TransferParams(BaseModel):
    """
    The information about a token transfer.
    """  # noqa: E501
    request_id: StrictStr = Field(description="The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization.")
    source: TransferSource
    token_id: StrictStr = Field(description="The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). For transfers from Exchange Wallets, this property value represents the asset ID.")
    destination: TransferDestination
    category_names: Optional[List[StrictStr]] = Field(default=None, description="The custom category for you to identify your transactions.")
    description: Optional[StrictStr] = Field(default=None, description="The description of the transfer.")
    fee: Optional[TransactionRequestFee] = None
    auto_fuel: Optional[AutoFuelType] = None
    __properties: ClassVar[List[str]] = ["request_id", "source", "token_id", "destination", "category_names", "description", "fee", "auto_fuel"]

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
        """Create an instance of TransferParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransferParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_id": obj.get("request_id"),
            "source": TransferSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "token_id": obj.get("token_id"),
            "destination": TransferDestination.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "category_names": obj.get("category_names"),
            "description": obj.get("description"),
            "fee": TransactionRequestFee.from_dict(obj["fee"]) if obj.get("fee") is not None else None,
            "auto_fuel": obj.get("auto_fuel")
        })
        return _obj


