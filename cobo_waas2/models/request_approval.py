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
from cobo_waas2.models.app_workflow_field import AppWorkflowField
from typing import Optional, Set
from typing_extensions import Self


class RequestApproval(BaseModel):
    """
    The information about a approval request.
    """  # noqa: E501
    operation_id: StrictStr = Field(description="The unique ID of the approval workflow.")
    request_id: StrictStr = Field(description="An identifier provided by you to track this request.")
    initiator_email: StrictStr = Field(description="The email of the user who requested the approval.")
    fields: List[AppWorkflowField]
    guard_template: StrictStr = Field(description="The template of a Cobo Guard message. Please connect [help@cobo.com](mailto:help@cobo.com) to get the template content.")
    __properties: ClassVar[List[str]] = ["operation_id", "request_id", "initiator_email", "fields", "guard_template"]

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
        """Create an instance of RequestApproval from a JSON string"""
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
        """Create an instance of RequestApproval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operation_id": obj.get("operation_id"),
            "request_id": obj.get("request_id"),
            "initiator_email": obj.get("initiator_email"),
            "fields": [AppWorkflowField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "guard_template": obj.get("guard_template")
        })
        return _obj


