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
from cobo_waas2.models.fee_type import FeeType
from typing import Optional, Set
from typing_extensions import Self


class TransactionRequestSOLFee(BaseModel):
    """
    The preset properties to limit transaction fee.  In the SOL fee model, the calculation method for the fee is: fee = base_fee + compute_unit_price * compute_unit_limit + rent_amount, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify the compute_unit_price, compute_unit_limit.   Switch between the tabs to display the properties for different transaction fee models. 
    """  # noqa: E501
    compute_unit_price: StrictStr = Field(description="The cost per compute unit. Transactions consume computational resources measured in compute units, and this price helps determine the cost of executing transactions, especially complex ones involving smart contracts.")
    compute_unit_limit: StrictStr = Field(description="The maximum number of compute units allowed for a transaction. This limits the resources any single transaction can consume, preventing excessive resource usage that could impact network performance negatively.")
    fee_type: FeeType
    token_id: StrictStr = Field(description="The token ID of the transaction fee.")
    __properties: ClassVar[List[str]] = ["compute_unit_price", "compute_unit_limit", "fee_type", "token_id"]

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
        """Create an instance of TransactionRequestSOLFee from a JSON string"""
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
        """Create an instance of TransactionRequestSOLFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "compute_unit_price": obj.get("compute_unit_price"),
            "compute_unit_limit": obj.get("compute_unit_limit"),
            "fee_type": obj.get("fee_type"),
            "token_id": obj.get("token_id")
        })
        return _obj


