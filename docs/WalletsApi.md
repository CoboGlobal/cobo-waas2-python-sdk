# cobo_waas2.WalletsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_address_chains_validity**](WalletsApi.md#check_address_chains_validity) | **GET** /wallets/check_address_chains_validity | Check address validity across chains
[**check_address_validity**](WalletsApi.md#check_address_validity) | **GET** /wallets/check_address_validity | Check address validity
[**check_addresses_validity**](WalletsApi.md#check_addresses_validity) | **GET** /wallets/check_addresses_validity | Check addresses validity
[**create_address**](WalletsApi.md#create_address) | **POST** /wallets/{wallet_id}/addresses | Create addresses in wallet
[**create_wallet**](WalletsApi.md#create_wallet) | **POST** /wallets | Create wallet
[**delete_wallet_by_id**](WalletsApi.md#delete_wallet_by_id) | **POST** /wallets/{wallet_id}/delete | Delete wallet
[**get_chain_by_id**](WalletsApi.md#get_chain_by_id) | **GET** /wallets/chains/{chain_id} | Get chain information
[**get_max_transferable_value**](WalletsApi.md#get_max_transferable_value) | **GET** /wallets/{wallet_id}/max_transferable_value | Get maximum transferable value
[**get_token_by_id**](WalletsApi.md#get_token_by_id) | **GET** /wallets/tokens/{token_id} | Get token information
[**get_wallet_by_id**](WalletsApi.md#get_wallet_by_id) | **GET** /wallets/{wallet_id} | Get wallet information
[**list_address_balances_by_token**](WalletsApi.md#list_address_balances_by_token) | **GET** /wallets/{wallet_id}/tokens/{token_id} | List address balances by token
[**list_addresses**](WalletsApi.md#list_addresses) | **GET** /wallets/{wallet_id}/addresses | List wallet addresses
[**list_enabled_chains**](WalletsApi.md#list_enabled_chains) | **GET** /wallets/enabled_chains | List enabled chains
[**list_enabled_tokens**](WalletsApi.md#list_enabled_tokens) | **GET** /wallets/enabled_tokens | List enabled tokens
[**list_supported_chains**](WalletsApi.md#list_supported_chains) | **GET** /wallets/chains | List supported chains
[**list_supported_tokens**](WalletsApi.md#list_supported_tokens) | **GET** /wallets/tokens | List supported tokens
[**list_token_balances_for_address**](WalletsApi.md#list_token_balances_for_address) | **GET** /wallets/{wallet_id}/addresses/{address}/tokens | List token balances by address
[**list_token_balances_for_wallet**](WalletsApi.md#list_token_balances_for_wallet) | **GET** /wallets/{wallet_id}/tokens | List token balances by wallet
[**list_utxos**](WalletsApi.md#list_utxos) | **GET** /wallets/{wallet_id}/utxos | List UTXOs
[**list_wallets**](WalletsApi.md#list_wallets) | **GET** /wallets | List all wallets
[**lock_utxos**](WalletsApi.md#lock_utxos) | **POST** /wallets/{wallet_id}/utxos/lock | Lock UTXOs
[**refresh_address_balances_by_token**](WalletsApi.md#refresh_address_balances_by_token) | **PUT** /wallets/{wallet_id}/tokens/{token_id}/refresh_address_balances | refresh address balances by token
[**unlock_utxos**](WalletsApi.md#unlock_utxos) | **POST** /wallets/{wallet_id}/utxos/unlock | Unlock UTXOs
[**update_wallet_by_id**](WalletsApi.md#update_wallet_by_id) | **PUT** /wallets/{wallet_id} | Update wallet


# **check_address_chains_validity**
> List[CheckAddressChainsValidity200ResponseInner] check_address_chains_validity(address, chain_ids)

Check address validity across chains

This operation verifies if a given address is valid for a list of chains. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.check_address_chains_validity200_response_inner import CheckAddressChainsValidity200ResponseInner
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    chain_ids = 'BTC,ETH'

    try:
        # Check address validity across chains
        api_response = api_instance.check_address_chains_validity(address, chain_ids)
        print("The response of WalletsApi->check_address_chains_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->check_address_chains_validity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The wallet address. | 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 

### Return type

[**List[CheckAddressChainsValidity200ResponseInner]**](CheckAddressChainsValidity200ResponseInner.md)

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

# **check_address_validity**
> CheckAddressValidity200Response check_address_validity(chain_id, address)

Check address validity

This operation verifies if a given address is valid for a specific chain. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.check_address_validity200_response import CheckAddressValidity200Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    chain_id = 'ETH'
    address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'

    try:
        # Check address validity
        api_response = api_instance.check_address_validity(chain_id, address)
        print("The response of WalletsApi->check_address_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->check_address_validity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
 **address** | **str**| The wallet address. | 

### Return type

[**CheckAddressValidity200Response**](CheckAddressValidity200Response.md)

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

# **check_addresses_validity**
> List[CheckAddressesValidity200ResponseInner] check_addresses_validity(chain_id, addresses)

Check addresses validity

This operation verifies if given addresses are valid for a specific chain. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.check_addresses_validity200_response_inner import CheckAddressesValidity200ResponseInner
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    chain_id = 'ETH'
    addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'

    try:
        # Check addresses validity
        api_response = api_instance.check_addresses_validity(chain_id, addresses)
        print("The response of WalletsApi->check_addresses_validity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->check_addresses_validity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
 **addresses** | **str**| A list of wallet addresses, separated by comma. You can specify a maximum of 100 addresses. | 

### Return type

[**List[CheckAddressesValidity200ResponseInner]**](CheckAddressesValidity200ResponseInner.md)

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

# **create_address**
> List[AddressInfo] create_address(wallet_id, create_address_request=create_address_request)

Create addresses in wallet

This operation generates one or more addresses within a specified wallet.  <Note>This operation is applicable to Custodial Wallets and MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.address_info import AddressInfo
from cobo_waas2.models.create_address_request import CreateAddressRequest
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    create_address_request = cobo_waas2.CreateAddressRequest()

    try:
        # Create addresses in wallet
        api_response = api_instance.create_address(wallet_id, create_address_request=create_address_request)
        print("The response of WalletsApi->create_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **create_address_request** | [**CreateAddressRequest**](CreateAddressRequest.md)| The request body to generates addresses within a specified wallet. | [optional] 

### Return type

[**List[AddressInfo]**](AddressInfo.md)

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

# **create_wallet**
> CreatedWalletInfo create_wallet(create_wallet_params=create_wallet_params)

Create wallet

This operation creates a wallet with the provided information.  <Note>This operation is not applicable to Smart Contract Wallets.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_wallet_params import CreateWalletParams
from cobo_waas2.models.created_wallet_info import CreatedWalletInfo
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    create_wallet_params = cobo_waas2.CreateWalletParams()

    try:
        # Create wallet
        api_response = api_instance.create_wallet(create_wallet_params=create_wallet_params)
        print("The response of WalletsApi->create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_wallet_params** | [**CreateWalletParams**](CreateWalletParams.md)| The request body to create a wallet | [optional] 

### Return type

[**CreatedWalletInfo**](CreatedWalletInfo.md)

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

# **delete_wallet_by_id**
> DeleteWalletById201Response delete_wallet_by_id(wallet_id)

Delete wallet

This operation deletes a specified wallet.  <Note>This operation is applicable to Exchange Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_wallet_by_id201_response import DeleteWalletById201Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Delete wallet
        api_response = api_instance.delete_wallet_by_id(wallet_id)
        print("The response of WalletsApi->delete_wallet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->delete_wallet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 

### Return type

[**DeleteWalletById201Response**](DeleteWalletById201Response.md)

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

# **get_chain_by_id**
> ChainInfo get_chain_by_id(chain_id)

Get chain information

This operation retrieves the detailed information about a specified chain. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.chain_info import ChainInfo
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    chain_id = 'ETH'

    try:
        # Get chain information
        api_response = api_instance.get_chain_by_id(chain_id)
        print("The response of WalletsApi->get_chain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_chain_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. | 

### Return type

[**ChainInfo**](ChainInfo.md)

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

# **get_max_transferable_value**
> MaxTransferableValue get_max_transferable_value(wallet_id, token_id, fee_rate, to_address, from_address=from_address)

Get maximum transferable value

This operation retrieves the maximum amount that you can transfer from a wallet or a specified wallet address, along with the corresponding transaction fee.  You must specify `to_address` in your query because it affects the transaction fee.  <Note>This operation is applicable to Custodial Wallets and MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.max_transferable_value import MaxTransferableValue
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    fee_rate = '10'
    to_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE'
    from_address = '2N2xFZtbCFB6Nb3Pj9Sxsx5mX2fxX3yEgkE'

    try:
        # Get maximum transferable value
        api_response = api_instance.get_max_transferable_value(wallet_id, token_id, fee_rate, to_address, from_address=from_address)
        print("The response of WalletsApi->get_max_transferable_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_max_transferable_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
 **fee_rate** | **str**| The fee rate in sats/vByte or gas price in wei. | 
 **to_address** | **str**| The recipient&#39;s address. | 
 **from_address** | **str**| The sender&#39;s address. For EVM addresses in MPC Wallets, this parameter is required. | [optional] 

### Return type

[**MaxTransferableValue**](MaxTransferableValue.md)

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

# **get_token_by_id**
> ExtendedTokenInfo get_token_by_id(token_id)

Get token information

This operation retrieves the detailed information about a specified token. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.extended_token_info import ExtendedTokenInfo
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    token_id = 'ETH_USDT'

    try:
        # Get token information
        api_response = api_instance.get_token_by_id(token_id)
        print("The response of WalletsApi->get_token_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_token_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 

### Return type

[**ExtendedTokenInfo**](ExtendedTokenInfo.md)

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

# **get_wallet_by_id**
> WalletInfo get_wallet_by_id(wallet_id)

Get wallet information

This operation retrieves the detailed information about a specified wallet. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.wallet_info import WalletInfo
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get wallet information
        api_response = api_instance.get_wallet_by_id(wallet_id)
        print("The response of WalletsApi->get_wallet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 

### Return type

[**WalletInfo**](WalletInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful get a wallet info |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_balances_by_token**
> ListAddressBalancesByToken200Response list_address_balances_by_token(wallet_id, token_id, addresses=addresses, limit=limit, before=before, after=after)

List address balances by token

This operation retrieves a list of address balances for a specified token within a wallet.  <Note>This operation is applicable to MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_address_balances_by_token200_response import ListAddressBalancesByToken200Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List address balances by token
        api_response = api_instance.list_address_balances_by_token(wallet_id, token_id, addresses=addresses, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_address_balances_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_address_balances_by_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **addresses** | **str**| A list of wallet addresses, separated by comma. For addresses requiring a memo, append the memo after the address using the &#39;|&#39; separator (e.g., \&quot;address|memo\&quot;). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListAddressBalancesByToken200Response**](ListAddressBalancesByToken200Response.md)

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

# **list_addresses**
> ListAddresses200Response list_addresses(wallet_id, chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)

List wallet addresses

This operation retrieves a list of addresses within a specified wallet. 

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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    chain_ids = 'BTC,ETH'
    addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List wallet addresses
        api_response = api_instance.list_addresses(wallet_id, chain_ids=chain_ids, addresses=addresses, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **addresses** | **str**| A list of wallet addresses, separated by comma. For addresses requiring a memo, append the memo after the address using the &#39;|&#39; separator (e.g., \&quot;address|memo\&quot;). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

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

# **list_enabled_chains**
> ListSupportedChains200Response list_enabled_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, limit=limit, before=before, after=after)

List enabled chains

This operation retrieves all the chains that can be used by your organization.   You can filter the result by wallet type or subtype. If you do not specify a wallet type, this operation returns a combination of chains that can be used by your organization for each wallet type. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_supported_chains200_response import ListSupportedChains200Response
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType()
    wallet_subtype = cobo_waas2.WalletSubtype()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List enabled chains
        api_response = api_instance.list_enabled_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_enabled_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_enabled_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | [**WalletType**](.md)| The wallet type.  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | [optional] 
 **wallet_subtype** | [**WalletSubtype**](.md)| The wallet subtype.  - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets)  - &#x60;Web3&#x60;: Custodial Wallets (Web3 Wallets)  - &#x60;Main&#x60;: Exchange Wallets (Main Account)  - &#x60;Sub&#x60;: Exchange Wallets (Sub Account)  - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets)  - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets)  - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet})  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSupportedChains200Response**](ListSupportedChains200Response.md)

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

# **list_enabled_tokens**
> ListSupportedTokens200Response list_enabled_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)

List enabled tokens

This operation retrieves all the tokens that can be used by your organization.   You can filter the result by wallet type, subtype, and chain IDs. If you do not specify a wallet type, this operation returns a combination of tokens that can be used by your organization for each wallet type. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_supported_tokens200_response import ListSupportedTokens200Response
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType()
    wallet_subtype = cobo_waas2.WalletSubtype()
    chain_ids = 'BTC,ETH'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List enabled tokens
        api_response = api_instance.list_enabled_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_enabled_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_enabled_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | [**WalletType**](.md)| The wallet type.  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | [optional] 
 **wallet_subtype** | [**WalletSubtype**](.md)| The wallet subtype.  - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets)  - &#x60;Web3&#x60;: Custodial Wallets (Web3 Wallets)  - &#x60;Main&#x60;: Exchange Wallets (Main Account)  - &#x60;Sub&#x60;: Exchange Wallets (Sub Account)  - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets)  - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets)  - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet})  | [optional] 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSupportedTokens200Response**](ListSupportedTokens200Response.md)

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

# **list_supported_chains**
> ListSupportedChains200Response list_supported_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)

List supported chains

This operation retrieves all chains supported by a specific wallet type or subtype.   It provides details such as the chain ID, chain symbol, and other relevant information. If you do not specify a wallet type, this operation returns a combination of chains supported by each wallet type. You can filter the result by chain IDs. The chain metadata is publicly available without any permission restrictions.  Cobo Portal currently supports over 80 blockchains and more than 3,000 tokens. In addition to this operation, you can also view the full list of supported chains [here](https://www.cobo.com/chains). We regularly update the list with new additions. If you want to request support for a specific chain or token, please [contact us](https://www.cobo.com/contact). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_supported_chains200_response import ListSupportedChains200Response
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType()
    wallet_subtype = cobo_waas2.WalletSubtype()
    chain_ids = 'BTC,ETH'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List supported chains
        api_response = api_instance.list_supported_chains(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_supported_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_supported_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | [**WalletType**](.md)| The wallet type.  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | [optional] 
 **wallet_subtype** | [**WalletSubtype**](.md)| The wallet subtype.  - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets)  - &#x60;Web3&#x60;: Custodial Wallets (Web3 Wallets)  - &#x60;Main&#x60;: Exchange Wallets (Main Account)  - &#x60;Sub&#x60;: Exchange Wallets (Sub Account)  - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets)  - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets)  - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet})  | [optional] 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSupportedChains200Response**](ListSupportedChains200Response.md)

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

# **list_supported_tokens**
> ListSupportedTokens200Response list_supported_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, token_ids=token_ids, limit=limit, before=before, after=after)

List supported tokens

This operation retrieves all tokens supported by a specific wallet type or subtype.   It provides details such as token ID, token symbol, and other relevant information. If you do not specify a wallet type, this operation returns a combination of tokens supported by each wallet type. You can filter the result by token IDs or chain IDs. The token metadata is publicly available without any permission restrictions.  Cobo Portal currently supports over 80 blockchains and more than 3,000 tokens. In addition to this operation, you can also view the full list of supported tokens [here](https://www.cobo.com/tokens). We regularly update the list with new additions. If you want to request support for a specific chain or token, please [contact us](https://www.cobo.com/contact). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_supported_tokens200_response import ListSupportedTokens200Response
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType()
    wallet_subtype = cobo_waas2.WalletSubtype()
    chain_ids = 'BTC,ETH'
    token_ids = 'ETH_USDT,ETH_USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List supported tokens
        api_response = api_instance.list_supported_tokens(wallet_type=wallet_type, wallet_subtype=wallet_subtype, chain_ids=chain_ids, token_ids=token_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_supported_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_supported_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | [**WalletType**](.md)| The wallet type.  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | [optional] 
 **wallet_subtype** | [**WalletSubtype**](.md)| The wallet subtype.  - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets)  - &#x60;Web3&#x60;: Custodial Wallets (Web3 Wallets)  - &#x60;Main&#x60;: Exchange Wallets (Main Account)  - &#x60;Sub&#x60;: Exchange Wallets (Sub Account)  - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets)  - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets)  - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet})  | [optional] 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSupportedTokens200Response**](ListSupportedTokens200Response.md)

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

# **list_token_balances_for_address**
> ListTokenBalancesForAddress200Response list_token_balances_for_address(wallet_id, address, token_ids=token_ids, limit=limit, before=before, after=after)

List token balances by address

The operation retrieves a list of token balances for a specified address within a wallet.   <Note>This operation is applicable to MPC Wallets and Smart Contract Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_token_balances_for_address200_response import ListTokenBalancesForAddress200Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    token_ids = 'ETH_USDT,ETH_USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List token balances by address
        api_response = api_instance.list_token_balances_for_address(wallet_id, address, token_ids=token_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_token_balances_for_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_token_balances_for_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **address** | **str**| The wallet address. | 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListTokenBalancesForAddress200Response**](ListTokenBalancesForAddress200Response.md)

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

# **list_token_balances_for_wallet**
> ListTokenBalancesForAddress200Response list_token_balances_for_wallet(wallet_id, token_ids=token_ids, limit=limit, before=before, after=after)

List token balances by wallet

The operation retrieves a list of token balances within a specified wallet.  <Note>This operation is not applicable to Exchange Wallets.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_token_balances_for_address200_response import ListTokenBalancesForAddress200Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_ids = 'ETH_USDT,ETH_USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List token balances by wallet
        api_response = api_instance.list_token_balances_for_wallet(wallet_id, token_ids=token_ids, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_token_balances_for_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_token_balances_for_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListTokenBalancesForAddress200Response**](ListTokenBalancesForAddress200Response.md)

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

# **list_utxos**
> ListUtxos200Response list_utxos(wallet_id, token_id, address=address, tx_hash=tx_hash, limit=limit, before=before, after=after)

List UTXOs

The operation retrieves a list of unspent transaction outputs (UTXOs) for a specified wallet and token.  <Note>This operation is applicable to MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_utxos200_response import ListUtxos200Response
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    tx_hash = 'dd7e1cecf6bbde1844ee1815b780711a1e306a718bcd23cd64401b48ef88eb83'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List UTXOs
        api_response = api_instance.list_utxos(wallet_id, token_id, address=address, tx_hash=tx_hash, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_utxos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_utxos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
 **address** | **str**| The wallet address. | [optional] 
 **tx_hash** | **str**|  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListUtxos200Response**](ListUtxos200Response.md)

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

# **list_wallets**
> ListWallets200Response list_wallets(wallet_type=wallet_type, wallet_subtype=wallet_subtype, project_id=project_id, vault_id=vault_id, limit=limit, before=before, after=after)

List all wallets

This operation retrieves the information of all wallets under your organization. You can filter the result by wallet type and subtype. For MPC Wallets, you can also filter by project ID and vault ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_wallets200_response import ListWallets200Response
from cobo_waas2.models.wallet_subtype import WalletSubtype
from cobo_waas2.models.wallet_type import WalletType
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_type = cobo_waas2.WalletType()
    wallet_subtype = cobo_waas2.WalletSubtype()
    project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all wallets
        api_response = api_instance.list_wallets(wallet_type=wallet_type, wallet_subtype=wallet_subtype, project_id=project_id, vault_id=vault_id, limit=limit, before=before, after=after)
        print("The response of WalletsApi->list_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_type** | [**WalletType**](.md)| The wallet type.  - &#x60;Custodial&#x60;: [Custodial Wallets](https://manuals.cobo.com/en/portal/custodial-wallets/introduction)  - &#x60;MPC&#x60;: [MPC Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction)  - &#x60;SmartContract&#x60;: [Smart Contract Wallets](https://manuals.cobo.com/en/portal/smart-contract-wallets/introduction)  - &#x60;Exchange&#x60;: [Exchange Wallets](https://manuals.cobo.com/en/portal/exchange-wallets/introduction)  | [optional] 
 **wallet_subtype** | [**WalletSubtype**](.md)| The wallet subtype.  - &#x60;Asset&#x60;: Custodial Wallets (Asset Wallets)  - &#x60;Web3&#x60;: Custodial Wallets (Web3 Wallets)  - &#x60;Main&#x60;: Exchange Wallets (Main Account)  - &#x60;Sub&#x60;: Exchange Wallets (Sub Account)  - &#x60;Org-Controlled&#x60;: MPC Wallets (Organization-Controlled Wallets)  - &#x60;User-Controlled&#x60;: MPC Wallets (User-Controlled Wallets)  - &#x60;Safe{Wallet}&#x60;: Smart Contract Wallets (Safe{Wallet})  | [optional] 
 **project_id** | **str**| The project ID, which you can retrieve by calling [List all projects](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-projects).  | [optional] 
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-vaults). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListWallets200Response**](ListWallets200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed wallets |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_utxos**
> LockUtxos201Response lock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)

Lock UTXOs

This operation locks the UTXOs with specified transaction hashes. Locked UTXOs cannot be transferred until unlocked.  <Note>This operation is applicable to MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.lock_utxos201_response import LockUtxos201Response
from cobo_waas2.models.lock_utxos_request import LockUtxosRequest
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    lock_utxos_request = cobo_waas2.LockUtxosRequest()

    try:
        # Lock UTXOs
        api_response = api_instance.lock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)
        print("The response of WalletsApi->lock_utxos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->lock_utxos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **lock_utxos_request** | [**LockUtxosRequest**](LockUtxosRequest.md)| The request body of the Lock/Unlock UTXOs operation. | [optional] 

### Return type

[**LockUtxos201Response**](LockUtxos201Response.md)

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

# **refresh_address_balances_by_token**
> RefreshAddressBalancesByToken200Response refresh_address_balances_by_token(wallet_id, token_id, refresh_address_balances_by_token_request=refresh_address_balances_by_token_request)

refresh address balances by token

The operation refresh the balance of the given address list for a specified token within a wallet. The successful return of the request only means that the refresh request has been submitted.  <Note>This operation is applicable to MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.refresh_address_balances_by_token200_response import RefreshAddressBalancesByToken200Response
from cobo_waas2.models.refresh_address_balances_by_token_request import RefreshAddressBalancesByTokenRequest
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    refresh_address_balances_by_token_request = cobo_waas2.RefreshAddressBalancesByTokenRequest()

    try:
        # refresh address balances by token
        api_response = api_instance.refresh_address_balances_by_token(wallet_id, token_id, refresh_address_balances_by_token_request=refresh_address_balances_by_token_request)
        print("The response of WalletsApi->refresh_address_balances_by_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->refresh_address_balances_by_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. | 
 **refresh_address_balances_by_token_request** | [**RefreshAddressBalancesByTokenRequest**](RefreshAddressBalancesByTokenRequest.md)| The request body to refresh the addresses balance by  specified token within a specified wallet | [optional] 

### Return type

[**RefreshAddressBalancesByToken200Response**](RefreshAddressBalancesByToken200Response.md)

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

# **unlock_utxos**
> LockUtxos201Response unlock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)

Unlock UTXOs

This operation unlocks the UTXOs with specified transaction hashes. Locked UTXOs cannot be transferred until unlocked.  <Note>This operation is applicable to MPC Wallets only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.lock_utxos201_response import LockUtxos201Response
from cobo_waas2.models.lock_utxos_request import LockUtxosRequest
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    lock_utxos_request = cobo_waas2.LockUtxosRequest()

    try:
        # Unlock UTXOs
        api_response = api_instance.unlock_utxos(wallet_id, lock_utxos_request=lock_utxos_request)
        print("The response of WalletsApi->unlock_utxos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->unlock_utxos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **lock_utxos_request** | [**LockUtxosRequest**](LockUtxosRequest.md)| The request body of the Lock/Unlock UTXOs operation. | [optional] 

### Return type

[**LockUtxos201Response**](LockUtxos201Response.md)

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

# **update_wallet_by_id**
> WalletInfo update_wallet_by_id(wallet_id, update_wallet_params=update_wallet_params)

Update wallet

This operation updates the information of a specified wallet.  For Exchange Wallets, you can update the API key, API secret, and other information about your exchange accounts with this operation. For other wallet types, you can only update the wallet name. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.update_wallet_params import UpdateWalletParams
from cobo_waas2.models.wallet_info import WalletInfo
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
    api_instance = cobo_waas2.WalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_wallet_params = cobo_waas2.UpdateWalletParams()

    try:
        # Update wallet
        api_response = api_instance.update_wallet_by_id(wallet_id, update_wallet_params=update_wallet_params)
        print("The response of WalletsApi->update_wallet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **update_wallet_params** | [**UpdateWalletParams**](UpdateWalletParams.md)| The request body. | [optional] 

### Return type

[**WalletInfo**](WalletInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated address |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

