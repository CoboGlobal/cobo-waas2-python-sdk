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

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from cobo_waas2.models.list_address_books200_response import ListAddressBooks200Response

from cobo_waas2.api_client import ApiClient, RequestSerialized
from cobo_waas2.api_response import ApiResponse
from cobo_waas2.rest import RESTResponseType


class AddressBooksApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client: ApiClient = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def list_address_books(
        self,
        chain_id: Annotated[StrictStr, Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains).")],
        address: Annotated[Optional[StrictStr], Field(description="The wallet address.")] = None,
        label: Annotated[Optional[StrictStr], Field(description="The address label.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of objects to return. For most operations, the value range is [1, 50].")] = None,
        before: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. ")] = None,
        after: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> ListAddressBooks200Response:
        """List address book entries

        This operation retrieves a list of addresses from your address book. 

        :param chain_id: The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). (required)
        :type chain_id: str
        :param address: The wallet address.
        :type address: str
        :param label: The address label.
        :type label: str
        :param limit: The maximum number of objects to return. For most operations, the value range is [1, 50].
        :type limit: int
        :param before: This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. 
        :type before: str
        :param after: This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. 
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._list_address_books_serialize(
            chain_id=chain_id,
            address=address,
            label=label,
            limit=limit,
            before=before,
            after=after,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAddressBooks200Response",
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
    def list_address_books_with_http_info(
        self,
        chain_id: Annotated[StrictStr, Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains).")],
        address: Annotated[Optional[StrictStr], Field(description="The wallet address.")] = None,
        label: Annotated[Optional[StrictStr], Field(description="The address label.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of objects to return. For most operations, the value range is [1, 50].")] = None,
        before: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. ")] = None,
        after: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> ApiResponse[ListAddressBooks200Response]:
        """List address book entries

        This operation retrieves a list of addresses from your address book. 

        :param chain_id: The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). (required)
        :type chain_id: str
        :param address: The wallet address.
        :type address: str
        :param label: The address label.
        :type label: str
        :param limit: The maximum number of objects to return. For most operations, the value range is [1, 50].
        :type limit: int
        :param before: This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. 
        :type before: str
        :param after: This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. 
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._list_address_books_serialize(
            chain_id=chain_id,
            address=address,
            label=label,
            limit=limit,
            before=before,
            after=after,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAddressBooks200Response",
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
    def list_address_books_without_preload_content(
        self,
        chain_id: Annotated[StrictStr, Field(description="The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains).")],
        address: Annotated[Optional[StrictStr], Field(description="The wallet address.")] = None,
        label: Annotated[Optional[StrictStr], Field(description="The address label.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="The maximum number of objects to return. For most operations, the value range is [1, 50].")] = None,
        before: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. ")] = None,
        after: Annotated[Optional[StrictStr], Field(description="This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. ")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
    ) -> RESTResponseType:
        """List address book entries

        This operation retrieves a list of addresses from your address book. 

        :param chain_id: The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). (required)
        :type chain_id: str
        :param address: The wallet address.
        :type address: str
        :param label: The address label.
        :type label: str
        :param limit: The maximum number of objects to return. For most operations, the value range is [1, 50].
        :type limit: int
        :param before: This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set `before` to the ID of Object C (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object A.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. - If you set it to `infinity`, the last page of data is returned. 
        :type before: str
        :param after: This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set `after` to the ID of Object A (`RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk`), the response will include Object B and Object C.    **Notes**:   - If you set both `after` and `before`, an error will occur. - If you leave both `before` and `after` empty, the first page of data is returned. 
        :type after: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._list_address_books_serialize(
            chain_id=chain_id,
            address=address,
            label=label,
            limit=limit,
            before=before,
            after=after,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAddressBooks200Response",
            '4XX': "ErrorResponse",
            '5XX': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response

    def _list_address_books_serialize(
        self,
        chain_id,
        address,
        label,
        limit,
        before,
        after,
    ) -> RequestSerialized:
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if chain_id is not None:
            
            _query_params.append(('chain_id', chain_id))
            
        if address is not None:
            
            _query_params.append(('address', address))
            
        if label is not None:
            
            _query_params.append(('label', label))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if before is not None:
            
            _query_params.append(('before', before))
            
        if after is not None:
            
            _query_params.append(('after', after))
            
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
            resource_path='/address_books',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
        )
