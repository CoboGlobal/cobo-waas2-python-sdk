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
from cobo_waas2.models.transaction_deposit_to_address_destination import TransactionDepositToAddressDestination
from cobo_waas2.models.transaction_deposit_to_wallet_destination import TransactionDepositToWalletDestination
from cobo_waas2.models.transaction_evm_contract_destination import TransactionEvmContractDestination
from cobo_waas2.models.transaction_message_sign_eip191_destination import TransactionMessageSignEIP191Destination
from cobo_waas2.models.transaction_message_sign_eip712_destination import TransactionMessageSignEIP712Destination
from cobo_waas2.models.transaction_raw_message_sign_destination import TransactionRawMessageSignDestination
from cobo_waas2.models.transaction_transfer_to_address_destination import TransactionTransferToAddressDestination
from cobo_waas2.models.transaction_transfer_to_wallet_destination import TransactionTransferToWalletDestination
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSACTIONDESTINATION_ONE_OF_SCHEMAS = ["TransactionDepositToAddressDestination", "TransactionDepositToWalletDestination", "TransactionEvmContractDestination", "TransactionMessageSignEIP191Destination", "TransactionMessageSignEIP712Destination", "TransactionRawMessageSignDestination", "TransactionTransferToAddressDestination", "TransactionTransferToWalletDestination"]

class TransactionDestination(BaseModel):
    """
    TransactionDestination
    """
    # data type: TransactionTransferToAddressDestination
    oneof_schema_1_validator: Optional[TransactionTransferToAddressDestination] = None
    # data type: TransactionTransferToWalletDestination
    oneof_schema_2_validator: Optional[TransactionTransferToWalletDestination] = None
    # data type: TransactionEvmContractDestination
    oneof_schema_3_validator: Optional[TransactionEvmContractDestination] = None
    # data type: TransactionMessageSignEIP191Destination
    oneof_schema_4_validator: Optional[TransactionMessageSignEIP191Destination] = None
    # data type: TransactionMessageSignEIP712Destination
    oneof_schema_5_validator: Optional[TransactionMessageSignEIP712Destination] = None
    # data type: TransactionRawMessageSignDestination
    oneof_schema_6_validator: Optional[TransactionRawMessageSignDestination] = None
    # data type: TransactionDepositToAddressDestination
    oneof_schema_7_validator: Optional[TransactionDepositToAddressDestination] = None
    # data type: TransactionDepositToWalletDestination
    oneof_schema_8_validator: Optional[TransactionDepositToWalletDestination] = None
    actual_instance: Optional[Union[TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination]] = None
    one_of_schemas: Set[str] = { "TransactionDepositToAddressDestination", "TransactionDepositToWalletDestination", "TransactionEvmContractDestination", "TransactionMessageSignEIP191Destination", "TransactionMessageSignEIP712Destination", "TransactionRawMessageSignDestination", "TransactionTransferToAddressDestination", "TransactionTransferToWalletDestination" }

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
        instance = TransactionDestination.model_construct()
        error_messages = []
        match = 0
        # validate data type: TransactionTransferToAddressDestination
        if not isinstance(v, TransactionTransferToAddressDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionTransferToAddressDestination`")
        else:
            match += 1
        # validate data type: TransactionTransferToWalletDestination
        if not isinstance(v, TransactionTransferToWalletDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionTransferToWalletDestination`")
        else:
            match += 1
        # validate data type: TransactionEvmContractDestination
        if not isinstance(v, TransactionEvmContractDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionEvmContractDestination`")
        else:
            match += 1
        # validate data type: TransactionMessageSignEIP191Destination
        if not isinstance(v, TransactionMessageSignEIP191Destination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMessageSignEIP191Destination`")
        else:
            match += 1
        # validate data type: TransactionMessageSignEIP712Destination
        if not isinstance(v, TransactionMessageSignEIP712Destination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMessageSignEIP712Destination`")
        else:
            match += 1
        # validate data type: TransactionRawMessageSignDestination
        if not isinstance(v, TransactionRawMessageSignDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionRawMessageSignDestination`")
        else:
            match += 1
        # validate data type: TransactionDepositToAddressDestination
        if not isinstance(v, TransactionDepositToAddressDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionDepositToAddressDestination`")
        else:
            match += 1
        # validate data type: TransactionDepositToWalletDestination
        if not isinstance(v, TransactionDepositToWalletDestination):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionDepositToWalletDestination`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransactionDestination with oneOf schemas: TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransactionDestination with oneOf schemas: TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination. Details: " + ", ".join(error_messages))
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
        _data_type = json.loads(json_str).get("destination_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `destination_type` in the input.")

        # check if data type is `TransactionTransferToAddressDestination`
        if _data_type == "Address":
            instance.actual_instance = TransactionTransferToAddressDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositToAddressDestination`
        if _data_type == "DepositToAddress":
            instance.actual_instance = TransactionDepositToAddressDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositToWalletDestination`
        if _data_type == "DepositToWallet":
            instance.actual_instance = TransactionDepositToWalletDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionEvmContractDestination`
        if _data_type == "EVM_Contract":
            instance.actual_instance = TransactionEvmContractDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionMessageSignEIP191Destination`
        if _data_type == "EVM_EIP_191_Signature":
            instance.actual_instance = TransactionMessageSignEIP191Destination.from_json(json_str)
            return instance

        # check if data type is `TransactionMessageSignEIP712Destination`
        if _data_type == "EVM_EIP_712_Signature":
            instance.actual_instance = TransactionMessageSignEIP712Destination.from_json(json_str)
            return instance

        # check if data type is `TransactionTransferToWalletDestination`
        if _data_type == "ExchangeWallet":
            instance.actual_instance = TransactionTransferToWalletDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionRawMessageSignDestination`
        if _data_type == "Raw_Message_Signature":
            instance.actual_instance = TransactionRawMessageSignDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositToAddressDestination`
        if _data_type == "TransactionDepositToAddressDestination":
            instance.actual_instance = TransactionDepositToAddressDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionDepositToWalletDestination`
        if _data_type == "TransactionDepositToWalletDestination":
            instance.actual_instance = TransactionDepositToWalletDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionEvmContractDestination`
        if _data_type == "TransactionEvmContractDestination":
            instance.actual_instance = TransactionEvmContractDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionMessageSignEIP191Destination`
        if _data_type == "TransactionMessageSignEIP191Destination":
            instance.actual_instance = TransactionMessageSignEIP191Destination.from_json(json_str)
            return instance

        # check if data type is `TransactionMessageSignEIP712Destination`
        if _data_type == "TransactionMessageSignEIP712Destination":
            instance.actual_instance = TransactionMessageSignEIP712Destination.from_json(json_str)
            return instance

        # check if data type is `TransactionRawMessageSignDestination`
        if _data_type == "TransactionRawMessageSignDestination":
            instance.actual_instance = TransactionRawMessageSignDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionTransferToAddressDestination`
        if _data_type == "TransactionTransferToAddressDestination":
            instance.actual_instance = TransactionTransferToAddressDestination.from_json(json_str)
            return instance

        # check if data type is `TransactionTransferToWalletDestination`
        if _data_type == "TransactionTransferToWalletDestination":
            instance.actual_instance = TransactionTransferToWalletDestination.from_json(json_str)
            return instance

        # deserialize data into TransactionTransferToAddressDestination
        try:
            instance.actual_instance = TransactionTransferToAddressDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionTransferToWalletDestination
        try:
            instance.actual_instance = TransactionTransferToWalletDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionEvmContractDestination
        try:
            instance.actual_instance = TransactionEvmContractDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMessageSignEIP191Destination
        try:
            instance.actual_instance = TransactionMessageSignEIP191Destination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMessageSignEIP712Destination
        try:
            instance.actual_instance = TransactionMessageSignEIP712Destination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionRawMessageSignDestination
        try:
            instance.actual_instance = TransactionRawMessageSignDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionDepositToAddressDestination
        try:
            instance.actual_instance = TransactionDepositToAddressDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionDepositToWalletDestination
        try:
            instance.actual_instance = TransactionDepositToWalletDestination.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionDestination with oneOf schemas: TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into TransactionDestination with oneOf schemas: TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionDepositToAddressDestination, TransactionDepositToWalletDestination, TransactionEvmContractDestination, TransactionMessageSignEIP191Destination, TransactionMessageSignEIP712Destination, TransactionRawMessageSignDestination, TransactionTransferToAddressDestination, TransactionTransferToWalletDestination]]:
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


