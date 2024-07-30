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
from cobo_waas2.models.create_custodial_wallet_params import CreateCustodialWalletParams
from cobo_waas2.models.create_exchange_wallet_params import CreateExchangeWalletParams
from cobo_waas2.models.create_mpc_wallet_params import CreateMpcWalletParams
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CREATEWALLETPARAMS_ONE_OF_SCHEMAS = ["CreateCustodialWalletParams", "CreateExchangeWalletParams", "CreateMpcWalletParams"]

class CreateWalletParams(BaseModel):
    """
    CreateWalletParams
    """
    # data type: CreateCustodialWalletParams
    oneof_schema_1_validator: Optional[CreateCustodialWalletParams] = None
    # data type: CreateMpcWalletParams
    oneof_schema_2_validator: Optional[CreateMpcWalletParams] = None
    # data type: CreateExchangeWalletParams
    oneof_schema_3_validator: Optional[CreateExchangeWalletParams] = None
    actual_instance: Optional[Union[CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams]] = None
    one_of_schemas: Set[str] = { "CreateCustodialWalletParams", "CreateExchangeWalletParams", "CreateMpcWalletParams" }

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
        instance = CreateWalletParams.model_construct()
        error_messages = []
        match = 0
        # validate data type: CreateCustodialWalletParams
        if not isinstance(v, CreateCustodialWalletParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateCustodialWalletParams`")
        else:
            match += 1
        # validate data type: CreateMpcWalletParams
        if not isinstance(v, CreateMpcWalletParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateMpcWalletParams`")
        else:
            match += 1
        # validate data type: CreateExchangeWalletParams
        if not isinstance(v, CreateExchangeWalletParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateExchangeWalletParams`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateWalletParams with oneOf schemas: CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateWalletParams with oneOf schemas: CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams. Details: " + ", ".join(error_messages))
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

        # check if data type is `CreateCustodialWalletParams`
        if _data_type == "Custodial":
            instance.actual_instance = CreateCustodialWalletParams.from_json(json_str)
            return instance

        # check if data type is `CreateExchangeWalletParams`
        if _data_type == "Exchange":
            instance.actual_instance = CreateExchangeWalletParams.from_json(json_str)
            return instance

        # check if data type is `CreateMpcWalletParams`
        if _data_type == "MPC":
            instance.actual_instance = CreateMpcWalletParams.from_json(json_str)
            return instance

        # check if data type is `CreateCustodialWalletParams`
        if _data_type == "CreateCustodialWalletParams":
            instance.actual_instance = CreateCustodialWalletParams.from_json(json_str)
            return instance

        # check if data type is `CreateExchangeWalletParams`
        if _data_type == "CreateExchangeWalletParams":
            instance.actual_instance = CreateExchangeWalletParams.from_json(json_str)
            return instance

        # check if data type is `CreateMpcWalletParams`
        if _data_type == "CreateMpcWalletParams":
            instance.actual_instance = CreateMpcWalletParams.from_json(json_str)
            return instance

        # deserialize data into CreateCustodialWalletParams
        try:
            instance.actual_instance = CreateCustodialWalletParams.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateMpcWalletParams
        try:
            instance.actual_instance = CreateMpcWalletParams.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateExchangeWalletParams
        try:
            instance.actual_instance = CreateExchangeWalletParams.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateWalletParams with oneOf schemas: CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into CreateWalletParams with oneOf schemas: CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], CreateCustodialWalletParams, CreateExchangeWalletParams, CreateMpcWalletParams]]:
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


