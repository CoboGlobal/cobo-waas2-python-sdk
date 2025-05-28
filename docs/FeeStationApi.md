# cobo_waas2.FeeStationApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_fee_station_fee**](FeeStationApi.md#estimate_fee_station_fee) | **POST** /fee_station/transactions/estimate_fee | Estimate fee for Fee Station transaction
[**get_fee_station_transaction_by_id**](FeeStationApi.md#get_fee_station_transaction_by_id) | **GET** /fee_station/transactions/{transaction_id} | Get Fee Station transaction information
[**list_fee_station_addresses**](FeeStationApi.md#list_fee_station_addresses) | **GET** /fee_station/addresses | List Fee Station addresses
[**list_fee_station_transactions**](FeeStationApi.md#list_fee_station_transactions) | **GET** /fee_station/transactions | List all Fee Station transactions
[**list_token_balances_for_fee_station**](FeeStationApi.md#list_token_balances_for_fee_station) | **GET** /fee_station/tokens | List Fee Station token balances


# **estimate_fee_station_fee**
> EstimatedFixedFee estimate_fee_station_fee(fee_station_transfer=fee_station_transfer)

Estimate fee for Fee Station transaction

This operation estimates the gas fee required for a top-up transaction sent by [Fee Station](https://manuals.cobo.com/en/portal/fee-station/introduction) to provide gas to the sender of the original transaction.  You need to provide the token ID and transfer amount.  For more information about transaction fee models and how fees are calculated, refer to [Estimate transaction fee](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.estimated_fixed_fee import EstimatedFixedFee
from cobo_waas2.models.fee_station_transfer import FeeStationTransfer
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
    api_instance = cobo_waas2.FeeStationApi(api_client)
    fee_station_transfer = cobo_waas2.FeeStationTransfer()

    try:
        # Estimate fee for Fee Station transaction
        api_response = api_instance.estimate_fee_station_fee(fee_station_transfer=fee_station_transfer)
        print("The response of FeeStationApi->estimate_fee_station_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeStationApi->estimate_fee_station_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fee_station_transfer** | [**FeeStationTransfer**](FeeStationTransfer.md)| The information about a Fee Station top-up transaction. | [optional] 

### Return type

[**EstimatedFixedFee**](EstimatedFixedFee.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_station_transaction_by_id**
> TransactionDetail get_fee_station_transaction_by_id(transaction_id)

Get Fee Station transaction information

This operation retrieves detailed information about a specified Fee Station transaction record, such as the transaction status, source address, destination address, and timestamp. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.transaction_detail import TransactionDetail
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
    api_instance = cobo_waas2.FeeStationApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get Fee Station transaction information
        api_response = api_instance.get_fee_station_transaction_by_id(transaction_id)
        print("The response of FeeStationApi->get_fee_station_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeStationApi->get_fee_station_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 

### Return type

[**TransactionDetail**](TransactionDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about a transaction. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_station_addresses**
> ListAddresses200Response list_fee_station_addresses(chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)

List Fee Station addresses

This operation retrieves a list of deposit addresses of your Fee Station, including the chain ID, address, and additional information. You can filter the result by chain ID and address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_addresses200_response import ListAddresses200Response
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
    api_instance = cobo_waas2.FeeStationApi(api_client)
    chain_ids = 'BTC,ETH'
    addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Fee Station addresses
        api_response = api_instance.list_fee_station_addresses(chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)
        print("The response of FeeStationApi->list_fee_station_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeStationApi->list_fee_station_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **addresses** | **str**| A list of wallet addresses, separated by comma. For addresses requiring a memo, append the memo after the address using the &#39;|&#39; separator (e.g., \&quot;address|memo\&quot;). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListAddresses200Response**](ListAddresses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed addresses |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_station_transactions**
> ListTransactions200Response list_fee_station_transactions(request_id=request_id, cobo_ids=cobo_ids, transaction_ids=transaction_ids, transaction_hashes=transaction_hashes, types=types, statuses=statuses, chain_ids=chain_ids, token_ids=token_ids, asset_ids=asset_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)

List all Fee Station transactions

This operation retrieves all Fee Station transactions under your organization.  You can filter the results by request ID, Cobo ID, transaction ID, transaction hash, type, status, and timestamp. You can also paginate and sort your query results. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_transactions200_response import ListTransactions200Response
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
    api_instance = cobo_waas2.FeeStationApi(api_client)
    request_id = 'web_send_by_user_327_1610444045047'
    cobo_ids = '20231213122855000000000000000000,20231213122955000000000000000000'
    transaction_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,557918d2-632a-4fe1-932f-315711f05fe3'
    transaction_hashes = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28'
    types = 'Deposit,Withdrawal'
    statuses = 'Completed,Failed'
    chain_ids = 'BTC,ETH'
    token_ids = 'ETH_USDT,ETH_USDC'
    asset_ids = 'USDT,USDC'
    min_created_timestamp = 1635744000000
    max_created_timestamp = 1635744000000
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    direction = ''

    try:
        # List all Fee Station transactions
        api_response = api_instance.list_fee_station_transactions(request_id=request_id, cobo_ids=cobo_ids, transaction_ids=transaction_ids, transaction_hashes=transaction_hashes, types=types, statuses=statuses, chain_ids=chain_ids, token_ids=token_ids, asset_ids=asset_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)
        print("The response of FeeStationApi->list_fee_station_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeStationApi->list_fee_station_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
 **cobo_ids** | **str**| A list of Cobo IDs, separated by comma. A Cobo ID can be used to track a transaction. | [optional] 
 **transaction_ids** | **str**| A list of transaction IDs, separated by comma. | [optional] 
 **transaction_hashes** | **str**| A list of transaction hashes, separated by comma. | [optional] 
 **types** | **str**| A list of transaction types for Fee Station, separated by comma. Possible values include:    - &#x60;Deposit&#x60;: A deposit transaction.   - &#x60;Withdrawal&#x60;: A withdrawal transaction.  | [optional] 
 **statuses** | **str**| A list of transaction statuses, separated by comma. Possible values include:    - &#x60;Submitted&#x60;: The transaction is submitted.   - &#x60;PendingScreening&#x60;: The transaction is pending screening by Risk Control.    - &#x60;PendingAuthorization&#x60;: The transaction is pending approvals.   - &#x60;PendingSignature&#x60;: The transaction is pending signature.    - &#x60;Broadcasting&#x60;: The transaction is being broadcast.   - &#x60;Confirming&#x60;: The transaction is waiting for the required number of confirmations.   - &#x60;Completed&#x60;: The transaction is completed.   - &#x60;Failed&#x60;: The transaction failed.   - &#x60;Rejected&#x60;: The transaction is rejected.   - &#x60;Pending&#x60;: The transaction is waiting to be included in the next block of the blockchain.  | [optional] 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **asset_ids** | **str**| (This concept applies to Exchange Wallets only) A list of asset IDs, separated by comma. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
 **min_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or after the specified time.  If not provided, the default value is 90 days before the current time. This default value is subject to change.  | [optional] 
 **max_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or before the specified time.  If not provided, the default value is the current time. This default value is subject to change.  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;&#39;]

### Return type

[**ListTransactions200Response**](ListTransactions200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the transactions. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_balances_for_fee_station**
> ListTokenBalancesForFeeStation200Response list_token_balances_for_fee_station(token_ids=token_ids, limit=limit, before=before, after=after)

List Fee Station token balances

The operation retrieves a list of token balances within your Fee Station. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_token_balances_for_fee_station200_response import ListTokenBalancesForFeeStation200Response
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
    api_instance = cobo_waas2.FeeStationApi(api_client)
    token_ids = 'ETH_USDT,ETH_USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Fee Station token balances
        api_response = api_instance.list_token_balances_for_fee_station(token_ids=token_ids, limit=limit, before=before, after=after)
        print("The response of FeeStationApi->list_token_balances_for_fee_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeStationApi->list_token_balances_for_fee_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListTokenBalancesForFeeStation200Response**](ListTokenBalancesForFeeStation200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

