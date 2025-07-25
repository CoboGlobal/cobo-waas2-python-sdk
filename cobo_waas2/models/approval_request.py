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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from cobo_waas2.models.app_workflow_field import AppWorkflowField
from cobo_waas2.models.approval_status import ApprovalStatus
from typing import Optional, Set
from typing_extensions import Self


class ApprovalRequest(BaseModel):
    """
    The information of an approval request.
    """  # noqa: E501
    approval_id: StrictStr = Field(description="The system-generated unique ID of the approval request.")
    request_id: StrictStr = Field(description="An identifier provided by you when requesting the approval.")
    fields: List[AppWorkflowField]
    status: ApprovalStatus
    initiated_timestamp: StrictInt = Field(description="The time when the approval was initiated, in Unix timestamp format, measured in milliseconds.")
    __properties: ClassVar[List[str]] = ["approval_id", "request_id", "fields", "status", "initiated_timestamp"]

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
        """Create an instance of ApprovalRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApprovalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approval_id": obj.get("approval_id"),
            "request_id": obj.get("request_id"),
            "fields": [AppWorkflowField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "status": obj.get("status"),
            "initiated_timestamp": obj.get("initiated_timestamp")
        })
        return _obj


