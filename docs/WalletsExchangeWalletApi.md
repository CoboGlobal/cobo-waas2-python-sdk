# cobo_waas2.WalletsExchangeWalletApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_asset_balances_for_exchange_wallet**](WalletsExchangeWalletApi.md#list_asset_balances_for_exchange_wallet) | **GET** /wallets/{wallet_id}/exchanges/assets | List asset balances
[**list_exchanges**](WalletsExchangeWalletApi.md#list_exchanges) | **GET** /wallets/exchanges/settings | List supported exchanges
[**list_supported_assets_for_exchange**](WalletsExchangeWalletApi.md#list_supported_assets_for_exchange) | **GET** /wallets/exchanges/{exchange_id}/assets | List supported assets
[**list_supported_chains_for_exchange**](WalletsExchangeWalletApi.md#list_supported_chains_for_exchange) | **GET** /wallets/exchanges/{exchange_id}/assets/{asset_id}/chains | List supported chains


# **list_asset_balances_for_exchange_wallet**
> ListAssetBalancesForExchangeWallet200Response list_asset_balances_for_exchange_wallet(wallet_id, trading_account_types=trading_account_types, asset_ids=asset_ids, limit=limit, before=before, after=after)

List asset balances

This operation retrieves the asset balances in a specified Exchange Wallet. You can filter the results by trading account type or asset ID. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_asset_balances_for_exchange_wallet200_response import ListAssetBalancesForExchangeWallet200Response
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
    api_instance = cobo_waas2.WalletsExchangeWalletApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    trading_account_types = 'Trading,Funding'
    asset_ids = 'USDT,USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List asset balances
        api_response = api_instance.list_asset_balances_for_exchange_wallet(wallet_id, trading_account_types=trading_account_types, asset_ids=asset_ids, limit=limit, before=before, after=after)
        print("The response of WalletsExchangeWalletApi->list_asset_balances_for_exchange_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsExchangeWalletApi->list_asset_balances_for_exchange_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **trading_account_types** | **str**| A list of trading account types, separated by comma. You can get the the supported trading account types of an exchange by calling [List supported exchanges](/v2/api-references/wallets--exchange-wallet/list-supported-exchanges). | [optional] 
 **asset_ids** | **str**| (This concept applies to Exchange Wallets only) A list of asset IDs, separated by comma. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListAssetBalancesForExchangeWallet200Response**](ListAssetBalancesForExchangeWallet200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

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

# **list_exchanges**
> List[ListExchanges200ResponseInner] list_exchanges()

List supported exchanges

This operation retrieves the information about the exchanges supported by Cobo's Exchange Wallets, including exchange IDs and trading account types.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_exchanges200_response_inner import ListExchanges200ResponseInner
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
    api_instance = cobo_waas2.WalletsExchangeWalletApi(api_client)

    try:
        # List supported exchanges
        api_response = api_instance.list_exchanges()
        print("The response of WalletsExchangeWalletApi->list_exchanges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsExchangeWalletApi->list_exchanges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListExchanges200ResponseInner]**](ListExchanges200ResponseInner.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

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

# **list_supported_assets_for_exchange**
> ListSupportedAssetsForExchange200Response list_supported_assets_for_exchange(exchange_id, limit=limit, before=before, after=after)

List supported assets

This operation retrieves all the assets supported by a specified exchange.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.exchange_id import ExchangeId
from cobo_waas2.models.list_supported_assets_for_exchange200_response import ListSupportedAssetsForExchange200Response
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
    api_instance = cobo_waas2.WalletsExchangeWalletApi(api_client)
    exchange_id = cobo_waas2.ExchangeId()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List supported assets
        api_response = api_instance.list_supported_assets_for_exchange(exchange_id, limit=limit, before=before, after=after)
        print("The response of WalletsExchangeWalletApi->list_supported_assets_for_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsExchangeWalletApi->list_supported_assets_for_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | [**ExchangeId**](.md)| The ID of the exchange. Possible values include:   - &#x60;binance&#x60;: Binance.   - &#x60;okx&#x60;: OKX.   - &#x60;deribit&#x60;: Deribit.   - &#x60;bybit&#x60;: Bybit.   - &#x60;gate&#x60;: Gate.io   - &#x60;bitget&#39;&#x60;: Bitget  | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSupportedAssetsForExchange200Response**](ListSupportedAssetsForExchange200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

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

# **list_supported_chains_for_exchange**
> List[ChainInfo] list_supported_chains_for_exchange(exchange_id, asset_id)

List supported chains

This operation retrieves all the chains supported by a specified exchange for a given asset.   You can use this operation to confirm whether you can transfer an asset from or to your Exchange Wallet when using a specific chain. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.chain_info import ChainInfo
from cobo_waas2.models.exchange_id import ExchangeId
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
    api_instance = cobo_waas2.WalletsExchangeWalletApi(api_client)
    exchange_id = cobo_waas2.ExchangeId()
    asset_id = 'USDT'

    try:
        # List supported chains
        api_response = api_instance.list_supported_chains_for_exchange(exchange_id, asset_id)
        print("The response of WalletsExchangeWalletApi->list_supported_chains_for_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsExchangeWalletApi->list_supported_chains_for_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | [**ExchangeId**](.md)| The ID of the exchange. Possible values include:   - &#x60;binance&#x60;: Binance.   - &#x60;okx&#x60;: OKX.   - &#x60;deribit&#x60;: Deribit.   - &#x60;bybit&#x60;: Bybit.   - &#x60;gate&#x60;: Gate.io   - &#x60;bitget&#39;&#x60;: Bitget  | 
 **asset_id** | **str**| (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. You can get the ID of the assets supported by an exchanges by calling [List supported assets](/v2/api-references/wallets--exchange-wallet/list-supported-assets). | 

### Return type

[**List[ChainInfo]**](ChainInfo.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

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

