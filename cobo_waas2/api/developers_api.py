# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from cobo_waas2.models.get_api_key_info200_response import GetApiKeyInfo200Response

from cobo_waas2.api_client import ApiClient, RequestSerialized
from cobo_waas2.api_response import ApiResponse
from cobo_waas2.rest import RESTResponseType


class DevelopersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client: ApiClient = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_api_key_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> GetApiKeyInfo200Response:
        """Get API key information

        This operation retrieves the details of the API key that you are using.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_api_key_info_serialize(
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetApiKeyInfo200Response",
            '4XX': "ErrorResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_api_key_info_with_http_info(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> ApiResponse[GetApiKeyInfo200Response]:
        """Get API key information

        This operation retrieves the details of the API key that you are using.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_api_key_info_serialize(
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetApiKeyInfo200Response",
            '4XX': "ErrorResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_api_key_info_without_preload_content(
        self,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> RESTResponseType:
        """Get API key information

        This operation retrieves the details of the API key that you are using.

        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_api_key_info_serialize(
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "GetApiKeyInfo200Response",
            '4XX': "ErrorResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_api_key_info_serialize(
        self,
    ) -> RequestSerialized:
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/developers/api_key_info',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
        )