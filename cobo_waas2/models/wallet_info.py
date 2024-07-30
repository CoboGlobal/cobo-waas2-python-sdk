# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.custodial_wallet_info import CustodialWalletInfo
from cobo_waas2.models.exchange_wallet_info import ExchangeWalletInfo
from cobo_waas2.models.mpc_wallet_info import MPCWalletInfo
from cobo_waas2.models.smart_contract_wallet_info import SmartContractWalletInfo
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

WALLETINFO_ONE_OF_SCHEMAS = ["CustodialWalletInfo", "ExchangeWalletInfo", "MPCWalletInfo", "SmartContractWalletInfo"]

class WalletInfo(BaseModel):
    """
    WalletInfo
    """
    # data type: CustodialWalletInfo
    oneof_schema_1_validator: Optional[CustodialWalletInfo] = None
    # data type: MPCWalletInfo
    oneof_schema_2_validator: Optional[MPCWalletInfo] = None
    # data type: SmartContractWalletInfo
    oneof_schema_3_validator: Optional[SmartContractWalletInfo] = None
    # data type: ExchangeWalletInfo
    oneof_schema_4_validator: Optional[ExchangeWalletInfo] = None
    actual_instance: Optional[Union[CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo]] = None
    one_of_schemas: Set[str] = { "CustodialWalletInfo", "ExchangeWalletInfo", "MPCWalletInfo", "SmartContractWalletInfo" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = WalletInfo.model_construct()
        error_messages = []
        match = 0
        # validate data type: CustodialWalletInfo
        if not isinstance(v, CustodialWalletInfo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustodialWalletInfo`")
        else:
            match += 1
        # validate data type: MPCWalletInfo
        if not isinstance(v, MPCWalletInfo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MPCWalletInfo`")
        else:
            match += 1
        # validate data type: SmartContractWalletInfo
        if not isinstance(v, SmartContractWalletInfo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SmartContractWalletInfo`")
        else:
            match += 1
        # validate data type: ExchangeWalletInfo
        if not isinstance(v, ExchangeWalletInfo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExchangeWalletInfo`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in WalletInfo with oneOf schemas: CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in WalletInfo with oneOf schemas: CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("wallet_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `wallet_type` in the input.")

        # check if data type is `CustodialWalletInfo`
        if _data_type == "Custodial":
            instance.actual_instance = CustodialWalletInfo.from_json(json_str)
            return instance

        # check if data type is `ExchangeWalletInfo`
        if _data_type == "Exchange":
            instance.actual_instance = ExchangeWalletInfo.from_json(json_str)
            return instance

        # check if data type is `MPCWalletInfo`
        if _data_type == "MPC":
            instance.actual_instance = MPCWalletInfo.from_json(json_str)
            return instance

        # check if data type is `SmartContractWalletInfo`
        if _data_type == "SmartContract":
            instance.actual_instance = SmartContractWalletInfo.from_json(json_str)
            return instance

        # check if data type is `CustodialWalletInfo`
        if _data_type == "CustodialWalletInfo":
            instance.actual_instance = CustodialWalletInfo.from_json(json_str)
            return instance

        # check if data type is `ExchangeWalletInfo`
        if _data_type == "ExchangeWalletInfo":
            instance.actual_instance = ExchangeWalletInfo.from_json(json_str)
            return instance

        # check if data type is `MPCWalletInfo`
        if _data_type == "MPCWalletInfo":
            instance.actual_instance = MPCWalletInfo.from_json(json_str)
            return instance

        # check if data type is `SmartContractWalletInfo`
        if _data_type == "SmartContractWalletInfo":
            instance.actual_instance = SmartContractWalletInfo.from_json(json_str)
            return instance

        # deserialize data into CustodialWalletInfo
        try:
            instance.actual_instance = CustodialWalletInfo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MPCWalletInfo
        try:
            instance.actual_instance = MPCWalletInfo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SmartContractWalletInfo
        try:
            instance.actual_instance = SmartContractWalletInfo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExchangeWalletInfo
        try:
            instance.actual_instance = ExchangeWalletInfo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into WalletInfo with oneOf schemas: CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into WalletInfo with oneOf schemas: CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CustodialWalletInfo, ExchangeWalletInfo, MPCWalletInfo, SmartContractWalletInfo]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


