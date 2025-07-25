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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cobo_waas2.models.webhook_event_data import WebhookEventData
from cobo_waas2.models.webhook_event_status import WebhookEventStatus
from cobo_waas2.models.webhook_event_type import WebhookEventType
from typing import Optional, Set
from typing_extensions import Self


class WebhookEvent(BaseModel):
    """
    The webhook event payload.
    """  # noqa: E501
    event_id: Optional[StrictStr] = Field(default=None, description="The event ID.")
    url: Annotated[str, Field(strict=True, max_length=500)] = Field(description="The webhook endpoint URL.")
    created_timestamp: StrictInt = Field(description="The time when the event was triggered, in Unix timestamp format (milliseconds). - The value remains unchanged across retries. - The default webhook timeout is 2 seconds. ")
    type: WebhookEventType
    data: WebhookEventData
    status: Optional[WebhookEventStatus] = None
    next_retry_timestamp: Optional[StrictInt] = Field(default=None, description="The timestamp indicating the next scheduled retry to deliver this event, in Unix timestamp format, measured in milliseconds. This field is only present if the event status is `Retrying`. ")
    retries_left: Optional[StrictInt] = Field(default=None, description="The number of retries left. This field is only present if the event status is `Retrying`.")
    __properties: ClassVar[List[str]] = ["event_id", "url", "created_timestamp", "type", "data", "status", "next_retry_timestamp", "retries_left"]

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
        """Create an instance of WebhookEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "url": obj.get("url"),
            "created_timestamp": obj.get("created_timestamp"),
            "type": obj.get("type"),
            "data": WebhookEventData.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "status": obj.get("status"),
            "next_retry_timestamp": obj.get("next_retry_timestamp"),
            "retries_left": obj.get("retries_left")
        })
        return _obj


