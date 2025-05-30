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
from cobo_waas2.models.transaction_cosmos_message import TransactionCosmosMessage
from cobo_waas2.models.transaction_destination_type import TransactionDestinationType
from typing import Optional, Set
from typing_extensions import Self


class TransactionCosmosContractDestination(BaseModel):
    """
    Information about the transaction destination type `COSMOS_Contract`. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Switch between the tabs to display the properties for different transaction destinations. 
    """  # noqa: E501
    destination_type: TransactionDestinationType
    cosmos_messages: List[TransactionCosmosMessage]
    value: Optional[StrictStr] = Field(default=None, description="The transfer amount. For example, if you trade 1.5 ETH, then the value is `1.5`. ")
    __properties: ClassVar[List[str]] = ["destination_type", "cosmos_messages", "value"]

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
        """Create an instance of TransactionCosmosContractDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cosmos_messages (list)
        _items = []
        if self.cosmos_messages:
            for _item in self.cosmos_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cosmos_messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionCosmosContractDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_type": obj.get("destination_type"),
            "cosmos_messages": [TransactionCosmosMessage.from_dict(_item) for _item in obj["cosmos_messages"]] if obj.get("cosmos_messages") is not None else None,
            "value": obj.get("value")
        })
        return _obj


