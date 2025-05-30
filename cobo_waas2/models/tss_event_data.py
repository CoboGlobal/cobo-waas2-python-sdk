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
from cobo_waas2.models.tss_key_gen_event_data import TSSKeyGenEventData
from cobo_waas2.models.tss_key_reshare_event_data import TSSKeyReshareEventData
from cobo_waas2.models.tss_key_share_sign_event_data import TSSKeyShareSignEventData
from cobo_waas2.models.tss_key_sign_event_data import TSSKeySignEventData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TSSEVENTDATA_ONE_OF_SCHEMAS = ["TSSKeyGenEventData", "TSSKeyReshareEventData", "TSSKeyShareSignEventData", "TSSKeySignEventData"]

class TSSEventData(BaseModel):
    """
    TSSEventData
    """
    # data type: TSSKeyGenEventData
    oneof_schema_1_validator: Optional[TSSKeyGenEventData] = None
    # data type: TSSKeyReshareEventData
    oneof_schema_2_validator: Optional[TSSKeyReshareEventData] = None
    # data type: TSSKeySignEventData
    oneof_schema_3_validator: Optional[TSSKeySignEventData] = None
    # data type: TSSKeyShareSignEventData
    oneof_schema_4_validator: Optional[TSSKeyShareSignEventData] = None
    actual_instance: Optional[Union[TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData]] = None
    one_of_schemas: Set[str] = { "TSSKeyGenEventData", "TSSKeyReshareEventData", "TSSKeyShareSignEventData", "TSSKeySignEventData" }

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
        instance = TSSEventData.model_construct()
        error_messages = []
        match = 0
        # validate data type: TSSKeyGenEventData
        if not isinstance(v, TSSKeyGenEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TSSKeyGenEventData`")
        else:
            match += 1
        # validate data type: TSSKeyReshareEventData
        if not isinstance(v, TSSKeyReshareEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TSSKeyReshareEventData`")
        else:
            match += 1
        # validate data type: TSSKeySignEventData
        if not isinstance(v, TSSKeySignEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TSSKeySignEventData`")
        else:
            match += 1
        # validate data type: TSSKeyShareSignEventData
        if not isinstance(v, TSSKeyShareSignEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TSSKeyShareSignEventData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TSSEventData with oneOf schemas: TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TSSEventData with oneOf schemas: TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData. Details: " + ", ".join(error_messages))
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
        _data_type = json.loads(json_str).get("data_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `data_type` in the input.")

        # check if data type is `TSSKeyGenEventData`
        if _data_type == "KeyGen":
            instance.actual_instance = TSSKeyGenEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeyReshareEventData`
        if _data_type == "KeyReshare":
            instance.actual_instance = TSSKeyReshareEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeyShareSignEventData`
        if _data_type == "KeyShareSign":
            instance.actual_instance = TSSKeyShareSignEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeySignEventData`
        if _data_type == "KeySign":
            instance.actual_instance = TSSKeySignEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeyGenEventData`
        if _data_type == "TSSKeyGenEventData":
            instance.actual_instance = TSSKeyGenEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeyReshareEventData`
        if _data_type == "TSSKeyReshareEventData":
            instance.actual_instance = TSSKeyReshareEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeyShareSignEventData`
        if _data_type == "TSSKeyShareSignEventData":
            instance.actual_instance = TSSKeyShareSignEventData.from_json(json_str)
            return instance

        # check if data type is `TSSKeySignEventData`
        if _data_type == "TSSKeySignEventData":
            instance.actual_instance = TSSKeySignEventData.from_json(json_str)
            return instance

        return instance
        # deserialize data into TSSKeyGenEventData
        try:
            instance.actual_instance = TSSKeyGenEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TSSKeyReshareEventData
        try:
            instance.actual_instance = TSSKeyReshareEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TSSKeySignEventData
        try:
            instance.actual_instance = TSSKeySignEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TSSKeyShareSignEventData
        try:
            instance.actual_instance = TSSKeyShareSignEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TSSEventData with oneOf schemas: TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into TSSEventData with oneOf schemas: TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TSSKeyGenEventData, TSSKeyReshareEventData, TSSKeyShareSignEventData, TSSKeySignEventData]]:
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


