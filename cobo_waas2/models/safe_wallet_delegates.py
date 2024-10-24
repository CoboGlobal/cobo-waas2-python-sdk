# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.safe_wallet_delegates_contract_call import SafeWalletDelegatesContractCall
from cobo_waas2.models.safe_wallet_delegates_transfer import SafeWalletDelegatesTransfer
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SAFEWALLETDELEGATES_ONE_OF_SCHEMAS = ["SafeWalletDelegatesContractCall", "SafeWalletDelegatesTransfer"]

class SafeWalletDelegates(BaseModel):
    """
    SafeWalletDelegates
    """
    # data type: SafeWalletDelegatesContractCall
    oneof_schema_1_validator: Optional[SafeWalletDelegatesContractCall] = None
    # data type: SafeWalletDelegatesTransfer
    oneof_schema_2_validator: Optional[SafeWalletDelegatesTransfer] = None
    actual_instance: Optional[Union[SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer]] = None
    one_of_schemas: Set[str] = { "SafeWalletDelegatesContractCall", "SafeWalletDelegatesTransfer" }

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
        instance = SafeWalletDelegates.model_construct()
        error_messages = []
        match = 0
        # validate data type: SafeWalletDelegatesContractCall
        if not isinstance(v, SafeWalletDelegatesContractCall):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SafeWalletDelegatesContractCall`")
        else:
            match += 1
        # validate data type: SafeWalletDelegatesTransfer
        if not isinstance(v, SafeWalletDelegatesTransfer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SafeWalletDelegatesTransfer`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SafeWalletDelegates with oneOf schemas: SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SafeWalletDelegates with oneOf schemas: SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer. Details: " + ", ".join(error_messages))
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
        _data_type = json.loads(json_str).get("request_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `request_type` in the input.")

        # check if data type is `SafeWalletDelegatesContractCall`
        if _data_type == "ContractCall":
            instance.actual_instance = SafeWalletDelegatesContractCall.from_json(json_str)
            return instance

        # check if data type is `SafeWalletDelegatesTransfer`
        if _data_type == "Transfer":
            instance.actual_instance = SafeWalletDelegatesTransfer.from_json(json_str)
            return instance

        # check if data type is `SafeWalletDelegatesContractCall`
        if _data_type == "SafeWalletDelegatesContractCall":
            instance.actual_instance = SafeWalletDelegatesContractCall.from_json(json_str)
            return instance

        # check if data type is `SafeWalletDelegatesTransfer`
        if _data_type == "SafeWalletDelegatesTransfer":
            instance.actual_instance = SafeWalletDelegatesTransfer.from_json(json_str)
            return instance

        # deserialize data into SafeWalletDelegatesContractCall
        try:
            instance.actual_instance = SafeWalletDelegatesContractCall.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SafeWalletDelegatesTransfer
        try:
            instance.actual_instance = SafeWalletDelegatesTransfer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SafeWalletDelegates with oneOf schemas: SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into SafeWalletDelegates with oneOf schemas: SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], SafeWalletDelegatesContractCall, SafeWalletDelegatesTransfer]]:
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

