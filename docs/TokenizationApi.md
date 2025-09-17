# cobo_waas2.TokenizationApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**burn_tokenization**](TokenizationApi.md#burn_tokenization) | **POST** /tokenization/tokens/{token_id}/burn | Burn tokens
[**estimate_tokenization_fee**](TokenizationApi.md#estimate_tokenization_fee) | **POST** /tokenization/estimate_fee | Estimate tokenization operation fee
[**get_tokenization_activity**](TokenizationApi.md#get_tokenization_activity) | **GET** /tokenization/activities/{activity_id} | Get tokenization activity details
[**get_tokenization_allowlist_activation**](TokenizationApi.md#get_tokenization_allowlist_activation) | **GET** /tokenization/tokens/{token_id}/allowlist/activation | Get allowlist activation status
[**get_tokenization_info**](TokenizationApi.md#get_tokenization_info) | **GET** /tokenization/tokens/{token_id} | Get token details
[**issue_token**](TokenizationApi.md#issue_token) | **POST** /tokenization/tokens | Issue token
[**list_issued_tokens**](TokenizationApi.md#list_issued_tokens) | **GET** /tokenization/tokens | List issued tokens
[**list_tokenization_activities**](TokenizationApi.md#list_tokenization_activities) | **GET** /tokenization/activities | List tokenization activities
[**list_tokenization_allowlist_addresses**](TokenizationApi.md#list_tokenization_allowlist_addresses) | **GET** /tokenization/tokens/{token_id}/allowlist/addresses | List addresses on allowlist
[**list_tokenization_blocklist_addresses**](TokenizationApi.md#list_tokenization_blocklist_addresses) | **GET** /tokenization/tokens/{token_id}/blocklist/addresses | List addresses on blocklist
[**list_tokenization_holdings**](TokenizationApi.md#list_tokenization_holdings) | **GET** /tokenization/tokens/{token_id}/holdings | Get token holdings information
[**list_tokenization_supported_chains**](TokenizationApi.md#list_tokenization_supported_chains) | **GET** /tokenization/enabled_chains | List supported chains for tokenization
[**mint_tokenization**](TokenizationApi.md#mint_tokenization) | **POST** /tokenization/tokens/{token_id}/mint | Mint tokens
[**pause_tokenization**](TokenizationApi.md#pause_tokenization) | **POST** /tokenization/tokens/{token_id}/pause | Pause token contract
[**tokenization_contract_call**](TokenizationApi.md#tokenization_contract_call) | **POST** /tokenization/tokens/{token_id}/contract_call | Call token contract
[**unpause_tokenization**](TokenizationApi.md#unpause_tokenization) | **POST** /tokenization/tokens/{token_id}/unpause | Unpause token contract
[**update_tokenization_allowlist_activation**](TokenizationApi.md#update_tokenization_allowlist_activation) | **POST** /tokenization/tokens/{token_id}/allowlist/activation | Activate or deactivate allowlist
[**update_tokenization_allowlist_addresses**](TokenizationApi.md#update_tokenization_allowlist_addresses) | **POST** /tokenization/tokens/{token_id}/allowlist/addresses | Update addresses on allowlist
[**update_tokenization_blocklist_addresses**](TokenizationApi.md#update_tokenization_blocklist_addresses) | **POST** /tokenization/tokens/{token_id}/blocklist/addresses | Update addresses on blocklist


# **burn_tokenization**
> TokenizationOperationResponse burn_tokenization(token_id, tokenization_burn_token_request=tokenization_burn_token_request)

Burn tokens

This operation burns tokens from a specified address. Creates a burn transaction that will decrease the token supply. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_burn_token_request import TokenizationBurnTokenRequest
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_burn_token_request = cobo_waas2.TokenizationBurnTokenRequest()

    try:
        # Burn tokens
        api_response = api_instance.burn_tokenization(token_id, tokenization_burn_token_request=tokenization_burn_token_request)
        print("The response of TokenizationApi->burn_tokenization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->burn_tokenization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_burn_token_request** | [**TokenizationBurnTokenRequest**](TokenizationBurnTokenRequest.md)| The request body for burning tokens. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_tokenization_fee**
> EstimatedFee estimate_tokenization_fee(tokenization_estimate_fee_request)

Estimate tokenization operation fee

This operation estimates the fee required for tokenization operations. For EVM-based chains, this calculates the gas cost for the specified operation. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.estimated_fee import EstimatedFee
from cobo_waas2.models.tokenization_estimate_fee_request import TokenizationEstimateFeeRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    tokenization_estimate_fee_request = cobo_waas2.TokenizationEstimateFeeRequest()

    try:
        # Estimate tokenization operation fee
        api_response = api_instance.estimate_tokenization_fee(tokenization_estimate_fee_request)
        print("The response of TokenizationApi->estimate_tokenization_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->estimate_tokenization_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenization_estimate_fee_request** | [**TokenizationEstimateFeeRequest**](TokenizationEstimateFeeRequest.md)| The request body to estimate tokenization operation fee. | 

### Return type

[**EstimatedFee**](EstimatedFee.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully retrieved the estimated fee for token issuance. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokenization_activity**
> TokenizationActivityInfo get_tokenization_activity(activity_id)

Get tokenization activity details

This operation retrieves the detailed information for a specific tokenization activity by its ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_activity_info import TokenizationActivityInfo
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    activity_id = 'b7c8e9d0-f1a2-3b4c-5d6e-7f8a9b0c1d2e'

    try:
        # Get tokenization activity details
        api_response = api_instance.get_tokenization_activity(activity_id)
        print("The response of TokenizationApi->get_tokenization_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_tokenization_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| The ID of the activity. | 

### Return type

[**TokenizationActivityInfo**](TokenizationActivityInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved Activity details. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokenization_allowlist_activation**
> GetTokenizationAllowlistActivation200Response get_tokenization_allowlist_activation(token_id)

Get allowlist activation status

This operation retrieves the allowlist activation status of the token contract. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_tokenization_allowlist_activation200_response import GetTokenizationAllowlistActivation200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'

    try:
        # Get allowlist activation status
        api_response = api_instance.get_tokenization_allowlist_activation(token_id)
        print("The response of TokenizationApi->get_tokenization_allowlist_activation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_tokenization_allowlist_activation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 

### Return type

[**GetTokenizationAllowlistActivation200Response**](GetTokenizationAllowlistActivation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the allowlist activation status. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokenization_info**
> TokenizationTokenDetailInfo get_tokenization_info(token_id)

Get token details

This operation retrieves the detailed information for a specific issued token by its ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_token_detail_info import TokenizationTokenDetailInfo
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'

    try:
        # Get token details
        api_response = api_instance.get_tokenization_info(token_id)
        print("The response of TokenizationApi->get_tokenization_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_tokenization_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 

### Return type

[**TokenizationTokenDetailInfo**](TokenizationTokenDetailInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved token information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_token**
> TokenizationOperationResponse issue_token(tokenization_issued_token_request)

Issue token

This operation issues a new token contract. It supports various blockchain platforms.  For EVM-based chains, this involves issuing a new smart contract from a template. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_issued_token_request import TokenizationIssuedTokenRequest
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    tokenization_issued_token_request = cobo_waas2.TokenizationIssuedTokenRequest()

    try:
        # Issue token
        api_response = api_instance.issue_token(tokenization_issued_token_request)
        print("The response of TokenizationApi->issue_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->issue_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenization_issued_token_request** | [**TokenizationIssuedTokenRequest**](TokenizationIssuedTokenRequest.md)| The request body to issue a new token. | 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issued_tokens**
> TokenizationListTokenInfoResponse list_issued_tokens(chain_id=chain_id, token_id=token_id, token_standard=token_standard, status=status, limit=limit, before=before, after=after)

List issued tokens

This operation retrieves a list of tokens issued by the organization. Returns issued token information including total supply, holdings, and token status. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_list_token_info_response import TokenizationListTokenInfoResponse
from cobo_waas2.models.tokenization_status import TokenizationStatus
from cobo_waas2.models.tokenization_token_standard import TokenizationTokenStandard
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    chain_id = 'ETH'
    token_id = 'ETH_USDT'
    token_standard = cobo_waas2.TokenizationTokenStandard()
    status = cobo_waas2.TokenizationStatus()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List issued tokens
        api_response = api_instance.list_issued_tokens(chain_id=chain_id, token_id=token_id, token_standard=token_standard, status=status, limit=limit, before=before, after=after)
        print("The response of TokenizationApi->list_issued_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_issued_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **token_standard** | [**TokenizationTokenStandard**](.md)| Filter by token standard. | [optional] 
 **status** | [**TokenizationStatus**](.md)| Filter by token status. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**TokenizationListTokenInfoResponse**](TokenizationListTokenInfoResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with the list of token information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokenization_activities**
> TokenizationListActivitiesResponse list_tokenization_activities(token_id=token_id, activity_type=activity_type, activity_status=activity_status, limit=limit, after=after, before=before, direction=direction)

List tokenization activities

This operation retrieves a list of tokenization activities. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_activity_status import TokenizationActivityStatus
from cobo_waas2.models.tokenization_list_activities_response import TokenizationListActivitiesResponse
from cobo_waas2.models.tokenization_operation_type import TokenizationOperationType
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    activity_type = cobo_waas2.TokenizationOperationType()
    activity_status = cobo_waas2.TokenizationActivityStatus()
    limit = 10
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    direction = 'ASC'

    try:
        # List tokenization activities
        api_response = api_instance.list_tokenization_activities(token_id=token_id, activity_type=activity_type, activity_status=activity_status, limit=limit, after=after, before=before, direction=direction)
        print("The response of TokenizationApi->list_tokenization_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_tokenization_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **activity_type** | [**TokenizationOperationType**](.md)| Filter by tokenization activity type. | [optional] 
 **activity_status** | [**TokenizationActivityStatus**](.md)| Filter by tokenization activity status. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;ASC&#39;]

### Return type

[**TokenizationListActivitiesResponse**](TokenizationListActivitiesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of tokenization activities. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokenization_allowlist_addresses**
> TokenizationAllowlistAddressesResponse list_tokenization_allowlist_addresses(token_id, limit=limit, after=after, before=before, direction=direction)

List addresses on allowlist

This operation lists addresses on the allowlist. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_allowlist_addresses_response import TokenizationAllowlistAddressesResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    limit = 10
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    direction = 'ASC'

    try:
        # List addresses on allowlist
        api_response = api_instance.list_tokenization_allowlist_addresses(token_id, limit=limit, after=after, before=before, direction=direction)
        print("The response of TokenizationApi->list_tokenization_allowlist_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_tokenization_allowlist_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;ASC&#39;]

### Return type

[**TokenizationAllowlistAddressesResponse**](TokenizationAllowlistAddressesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved addresses on the allowlist. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokenization_blocklist_addresses**
> ListTokenizationBlocklistAddresses200Response list_tokenization_blocklist_addresses(token_id, limit=limit, after=after, before=before, direction=direction)

List addresses on blocklist

This operation lists addresses on the blocklist. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_tokenization_blocklist_addresses200_response import ListTokenizationBlocklistAddresses200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    limit = 10
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    direction = 'ASC'

    try:
        # List addresses on blocklist
        api_response = api_instance.list_tokenization_blocklist_addresses(token_id, limit=limit, after=after, before=before, direction=direction)
        print("The response of TokenizationApi->list_tokenization_blocklist_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_tokenization_blocklist_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListTokenizationBlocklistAddresses200Response**](ListTokenizationBlocklistAddresses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved addresses on the blocklist. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokenization_holdings**
> TokenizationListHoldingsResponse list_tokenization_holdings(token_id, limit=limit, before=before, after=after)

Get token holdings information

This operation retrieves the holdings information for a specific issued token, showing which wallets hold the token and their respective balances. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_list_holdings_response import TokenizationListHoldingsResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # Get token holdings information
        api_response = api_instance.list_tokenization_holdings(token_id, limit=limit, before=before, after=after)
        print("The response of TokenizationApi->list_tokenization_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_tokenization_holdings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**TokenizationListHoldingsResponse**](TokenizationListHoldingsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved token holdings information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokenization_supported_chains**
> TokenizationListEnabledChainsResponse list_tokenization_supported_chains(limit=limit, after=after, before=before)

List supported chains for tokenization

This operation retrieves a list of tokenization supported chains. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_list_enabled_chains_response import TokenizationListEnabledChainsResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    limit = 10
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'

    try:
        # List supported chains for tokenization
        api_response = api_instance.list_tokenization_supported_chains(limit=limit, after=after, before=before)
        print("The response of TokenizationApi->list_tokenization_supported_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->list_tokenization_supported_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 

### Return type

[**TokenizationListEnabledChainsResponse**](TokenizationListEnabledChainsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of tokenization supported chains. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_tokenization**
> TokenizationOperationResponse mint_tokenization(token_id, tokenization_mint_token_request)

Mint tokens

This operation mints new tokens to a specified address. Creates a mint transaction that will increase the token supply. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_mint_token_request import TokenizationMintTokenRequest
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_mint_token_request = cobo_waas2.TokenizationMintTokenRequest()

    try:
        # Mint tokens
        api_response = api_instance.mint_tokenization(token_id, tokenization_mint_token_request)
        print("The response of TokenizationApi->mint_tokenization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->mint_tokenization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_mint_token_request** | [**TokenizationMintTokenRequest**](TokenizationMintTokenRequest.md)| The request body for minting tokens. | 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_tokenization**
> TokenizationOperationResponse pause_tokenization(token_id, tokenization_pause_token_request=tokenization_pause_token_request)

Pause token contract

This operation pauses the token contract, temporarily halting token operations and transfers. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.models.tokenization_pause_token_request import TokenizationPauseTokenRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_pause_token_request = cobo_waas2.TokenizationPauseTokenRequest()

    try:
        # Pause token contract
        api_response = api_instance.pause_tokenization(token_id, tokenization_pause_token_request=tokenization_pause_token_request)
        print("The response of TokenizationApi->pause_tokenization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->pause_tokenization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_pause_token_request** | [**TokenizationPauseTokenRequest**](TokenizationPauseTokenRequest.md)| The request body for pausing tokens. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokenization_contract_call**
> TokenizationOperationResponse tokenization_contract_call(token_id, tokenization_contract_call_request=tokenization_contract_call_request)

Call token contract

This operation performs a contract call on the token contract. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_contract_call_request import TokenizationContractCallRequest
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_contract_call_request = cobo_waas2.TokenizationContractCallRequest()

    try:
        # Call token contract
        api_response = api_instance.tokenization_contract_call(token_id, tokenization_contract_call_request=tokenization_contract_call_request)
        print("The response of TokenizationApi->tokenization_contract_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->tokenization_contract_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_contract_call_request** | [**TokenizationContractCallRequest**](TokenizationContractCallRequest.md)| The request body for contract call. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpause_tokenization**
> TokenizationOperationResponse unpause_tokenization(token_id, tokenization_unpause_token_request=tokenization_unpause_token_request)

Unpause token contract

This operation unpauses the token contract, resuming token operations and transfers. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.models.tokenization_unpause_token_request import TokenizationUnpauseTokenRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_unpause_token_request = cobo_waas2.TokenizationUnpauseTokenRequest()

    try:
        # Unpause token contract
        api_response = api_instance.unpause_tokenization(token_id, tokenization_unpause_token_request=tokenization_unpause_token_request)
        print("The response of TokenizationApi->unpause_tokenization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->unpause_tokenization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_unpause_token_request** | [**TokenizationUnpauseTokenRequest**](TokenizationUnpauseTokenRequest.md)| The request body for unpausing tokens. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tokenization_allowlist_activation**
> TokenizationOperationResponse update_tokenization_allowlist_activation(token_id, tokenization_allowlist_activation_request=tokenization_allowlist_activation_request)

Activate or deactivate allowlist

This operation activates or deactivates the allowlist. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_allowlist_activation_request import TokenizationAllowlistActivationRequest
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_allowlist_activation_request = cobo_waas2.TokenizationAllowlistActivationRequest()

    try:
        # Activate or deactivate allowlist
        api_response = api_instance.update_tokenization_allowlist_activation(token_id, tokenization_allowlist_activation_request=tokenization_allowlist_activation_request)
        print("The response of TokenizationApi->update_tokenization_allowlist_activation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->update_tokenization_allowlist_activation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_allowlist_activation_request** | [**TokenizationAllowlistActivationRequest**](TokenizationAllowlistActivationRequest.md)| The request body for activating or deactivating the allowlist. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tokenization_allowlist_addresses**
> TokenizationOperationResponse update_tokenization_allowlist_addresses(token_id, tokenization_update_allowlist_addresses_request=tokenization_update_allowlist_addresses_request)

Update addresses on allowlist

This operation updates addresses on the allowlist. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.models.tokenization_update_allowlist_addresses_request import TokenizationUpdateAllowlistAddressesRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_update_allowlist_addresses_request = cobo_waas2.TokenizationUpdateAllowlistAddressesRequest()

    try:
        # Update addresses on allowlist
        api_response = api_instance.update_tokenization_allowlist_addresses(token_id, tokenization_update_allowlist_addresses_request=tokenization_update_allowlist_addresses_request)
        print("The response of TokenizationApi->update_tokenization_allowlist_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->update_tokenization_allowlist_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_update_allowlist_addresses_request** | [**TokenizationUpdateAllowlistAddressesRequest**](TokenizationUpdateAllowlistAddressesRequest.md)| The request body for adding or removing multiple addresses on the allowlist. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tokenization_blocklist_addresses**
> TokenizationOperationResponse update_tokenization_blocklist_addresses(token_id, tokenization_update_blocklist_addresses_request=tokenization_update_blocklist_addresses_request)

Update addresses on blocklist

This operation updates addresses on the blocklist. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tokenization_operation_response import TokenizationOperationResponse
from cobo_waas2.models.tokenization_update_blocklist_addresses_request import TokenizationUpdateBlocklistAddressesRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.TokenizationApi(api_client)
    token_id = 'ETH_USDT'
    tokenization_update_blocklist_addresses_request = cobo_waas2.TokenizationUpdateBlocklistAddressesRequest()

    try:
        # Update addresses on blocklist
        api_response = api_instance.update_tokenization_blocklist_addresses(token_id, tokenization_update_blocklist_addresses_request=tokenization_update_blocklist_addresses_request)
        print("The response of TokenizationApi->update_tokenization_blocklist_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->update_tokenization_blocklist_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **tokenization_update_blocklist_addresses_request** | [**TokenizationUpdateBlocklistAddressesRequest**](TokenizationUpdateBlocklistAddressesRequest.md)| The request body for adding or removing multiple addresses on the blocklist. | [optional] 

### Return type

[**TokenizationOperationResponse**](TokenizationOperationResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokenization operation transaction created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

