# cobo_waas2.PaymentApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_exchange_rates**](PaymentApi.md#batch_get_exchange_rates) | **GET** /payments/exchange_rates | Batch get exchange rates
[**cancel_refund_by_id**](PaymentApi.md#cancel_refund_by_id) | **PUT** /payments/refunds/{refund_id}/cancel | Cancel refund order
[**create_counterparty**](PaymentApi.md#create_counterparty) | **POST** /payments/counterparty | Create counterparty
[**create_counterparty_wallet_address**](PaymentApi.md#create_counterparty_wallet_address) | **POST** /payments/counterparty/wallet_address | Create counterparty wallet address
[**create_crypto_address**](PaymentApi.md#create_crypto_address) | **POST** /payments/crypto_addresses | Create crypto address
[**create_destination**](PaymentApi.md#create_destination) | **POST** /payments/destination | Create destination
[**create_destination_bank_account**](PaymentApi.md#create_destination_bank_account) | **POST** /payments/destination/bank_account | Create destination bank account
[**create_destination_wallet_address**](PaymentApi.md#create_destination_wallet_address) | **POST** /payments/destination/wallet_address | Create destination wallet address
[**create_forced_sweep_request**](PaymentApi.md#create_forced_sweep_request) | **POST** /payments/force_sweep_requests | Create forced sweep
[**create_merchant**](PaymentApi.md#create_merchant) | **POST** /payments/merchants | Create merchant
[**create_order_link**](PaymentApi.md#create_order_link) | **POST** /payments/links/orders | Create order link
[**create_payment_order**](PaymentApi.md#create_payment_order) | **POST** /payments/orders | Create pay-in order
[**create_refund**](PaymentApi.md#create_refund) | **POST** /payments/refunds | Create refund order
[**create_refund_link**](PaymentApi.md#create_refund_link) | **POST** /payments/links/refunds | Create refund link
[**create_settlement_request**](PaymentApi.md#create_settlement_request) | **POST** /payments/settlement_requests | Create settlement request
[**delete_counterparty**](PaymentApi.md#delete_counterparty) | **PUT** /payments/counterparty/{counterparty_id}/delete | Delete counterparty
[**delete_counterparty_wallet_address**](PaymentApi.md#delete_counterparty_wallet_address) | **PUT** /payments/counterparty/wallet_address/{wallet_address_id}/delete | Delete counterparty wallet address
[**delete_crypto_address**](PaymentApi.md#delete_crypto_address) | **POST** /payments/crypto_addresses/{crypto_address_id}/delete | Delete crypto address
[**delete_destination**](PaymentApi.md#delete_destination) | **PUT** /payments/destination/{destination_id}/delete | Delete destination
[**delete_destination_bank_account**](PaymentApi.md#delete_destination_bank_account) | **PUT** /payments/destination/bank_account/{bank_account_id}/delete | Delete destination bank account
[**delete_destination_wallet_address**](PaymentApi.md#delete_destination_wallet_address) | **PUT** /payments/destination/wallet_address/{wallet_address_id}/delete | Delete destination wallet address
[**enable_destination_whitelist**](PaymentApi.md#enable_destination_whitelist) | **POST** /payments/destination/enable_whitelist | Enable or disable destination whitelist
[**get_counterparty_detail_by_id**](PaymentApi.md#get_counterparty_detail_by_id) | **GET** /payments/counterparty/{counterparty_id}/detail | Get counterparty information
[**get_destination_bank_account_detail_by_id**](PaymentApi.md#get_destination_bank_account_detail_by_id) | **GET** /payments/destination/bank_account/{bank_account_id}/detail | Get destination bank account information
[**get_destination_detail_by_id**](PaymentApi.md#get_destination_detail_by_id) | **GET** /payments/destination/{destination_id}/detail | Get destination information
[**get_exchange_rate**](PaymentApi.md#get_exchange_rate) | **GET** /payments/exchange_rates/{token_id}/{currency} | Get exchange rate
[**get_payment_order_detail_by_id**](PaymentApi.md#get_payment_order_detail_by_id) | **GET** /payments/orders/{order_id} | Get pay-in order information
[**get_psp_balance**](PaymentApi.md#get_psp_balance) | **GET** /payments/balance/psp | Get developer balance
[**get_refund_detail_by_id**](PaymentApi.md#get_refund_detail_by_id) | **GET** /payments/refunds/{refund_id} | Get refund order information
[**get_refunds**](PaymentApi.md#get_refunds) | **GET** /payments/refunds | List all refund orders
[**get_settlement_by_id**](PaymentApi.md#get_settlement_by_id) | **GET** /payments/settlement_requests/{settlement_request_id} | Get settlement request information
[**get_settlement_info_by_ids**](PaymentApi.md#get_settlement_info_by_ids) | **GET** /payments/settlement_info | Get withdrawable balances
[**get_top_up_address**](PaymentApi.md#get_top_up_address) | **GET** /payments/topup/address | Create/Get top-up address
[**list_bank_accounts**](PaymentApi.md#list_bank_accounts) | **GET** /payments/bank_accounts | List all bank accounts
[**list_counterparties**](PaymentApi.md#list_counterparties) | **GET** /payments/counterparty | List all counterparties
[**list_counterparty_wallet_address**](PaymentApi.md#list_counterparty_wallet_address) | **GET** /payments/counterparty/wallet_address | List counterparty wallet addresses
[**list_crypto_addresses**](PaymentApi.md#list_crypto_addresses) | **GET** /payments/crypto_addresses | List crypto addresses
[**list_destination_bank_accounts**](PaymentApi.md#list_destination_bank_accounts) | **GET** /payments/destination/bank_account | List destination bank accounts
[**list_destination_wallet_addresses**](PaymentApi.md#list_destination_wallet_addresses) | **GET** /payments/destination/wallet_address | List destination wallet addresses
[**list_destinations**](PaymentApi.md#list_destinations) | **GET** /payments/destination | List all destinations
[**list_forced_sweep_requests**](PaymentApi.md#list_forced_sweep_requests) | **GET** /payments/force_sweep_requests | List forced sweeps
[**list_merchant_balances**](PaymentApi.md#list_merchant_balances) | **GET** /payments/balance/merchants | List merchant balances
[**list_merchants**](PaymentApi.md#list_merchants) | **GET** /payments/merchants | List all merchants
[**list_payment_orders**](PaymentApi.md#list_payment_orders) | **GET** /payments/orders | List all pay-in orders
[**list_payment_supported_tokens**](PaymentApi.md#list_payment_supported_tokens) | **GET** /payments/supported_tokens | List all supported tokens
[**list_payment_wallet_balances**](PaymentApi.md#list_payment_wallet_balances) | **GET** /payments/balance/payment_wallets | List payment wallet balances
[**list_settlement_details**](PaymentApi.md#list_settlement_details) | **GET** /payments/settlement_details | List all settlement details
[**list_settlement_requests**](PaymentApi.md#list_settlement_requests) | **GET** /payments/settlement_requests | List all settlement requests
[**list_top_up_payer_accounts**](PaymentApi.md#list_top_up_payer_accounts) | **GET** /payments/topup/payer_accounts | List top-up payer accounts
[**list_top_up_payers**](PaymentApi.md#list_top_up_payers) | **GET** /payments/topup/payers | List payers
[**payment_estimate_fee**](PaymentApi.md#payment_estimate_fee) | **POST** /payments/estimate_fee | Estimate fees
[**query_destination_whitelist_enabled**](PaymentApi.md#query_destination_whitelist_enabled) | **GET** /payments/destination/enable_whitelist | Query destination whitelist enabled status
[**update_bank_account_by_id**](PaymentApi.md#update_bank_account_by_id) | **PUT** /payments/bank_accounts/{bank_account_id} | Update bank account
[**update_counterparty_by_id**](PaymentApi.md#update_counterparty_by_id) | **PUT** /payments/counterparty/{counterparty_id}/update | Update counterparty
[**update_destination_bank_account_by_id**](PaymentApi.md#update_destination_bank_account_by_id) | **PUT** /payments/destination/bank_account/{bank_account_id}/update | Update destination bank account
[**update_destination_by_id**](PaymentApi.md#update_destination_by_id) | **PUT** /payments/destination/{destination_id}/update | Update destination
[**update_merchant_by_id**](PaymentApi.md#update_merchant_by_id) | **PUT** /payments/merchants/{merchant_id} | Update merchant
[**update_payment_order**](PaymentApi.md#update_payment_order) | **PUT** /payments/orders/{order_id} | Update pay-in order
[**update_refund_by_id**](PaymentApi.md#update_refund_by_id) | **PUT** /payments/refunds/{refund_id} | Update refund order
[**update_top_up_address**](PaymentApi.md#update_top_up_address) | **PUT** /payments/topup/address | Update top-up address


# **batch_get_exchange_rates**
> List[ExchangeRate] batch_get_exchange_rates(token_ids, currencies)

Batch get exchange rates

This operation retrieves the current exchange rates between a specified currency and a list of token IDs. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.exchange_rate import ExchangeRate
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_ids = 'ETH_USDT,ETH_USDC,BTC_USDT'
    currencies = 'USD'

    try:
        # Batch get exchange rates
        api_response = api_instance.batch_get_exchange_rates(token_ids, currencies)
        print("The response of PaymentApi->batch_get_exchange_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->batch_get_exchange_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens).  | 
 **currencies** | **str**| List of the fiat currencies, separated by comma. Currently, only &#x60;USD&#x60; is supported.  | 

### Return type

[**List[ExchangeRate]**](ExchangeRate.md)

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

# **cancel_refund_by_id**
> Refund cancel_refund_by_id(refund_id)

Cancel refund order

This operation cancels a specified refund order. You can only cancel refund orders that have not been processed yet. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.refund import Refund
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    refund_id = 'R20250304-M1001-1001'

    try:
        # Cancel refund order
        api_response = api_instance.cancel_refund_by_id(refund_id)
        print("The response of PaymentApi->cancel_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->cancel_refund_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The refund order ID. | 

### Return type

[**Refund**](Refund.md)

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

# **create_counterparty**
> CounterpartyDetail create_counterparty(create_counterparty_request=create_counterparty_request)

Create counterparty

This operation creates a counterparty. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.counterparty_detail import CounterpartyDetail
from cobo_waas2.models.create_counterparty_request import CreateCounterpartyRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_counterparty_request = cobo_waas2.CreateCounterpartyRequest()

    try:
        # Create counterparty
        api_response = api_instance.create_counterparty(create_counterparty_request=create_counterparty_request)
        print("The response of PaymentApi->create_counterparty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_counterparty: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_counterparty_request** | [**CreateCounterpartyRequest**](CreateCounterpartyRequest.md)| The request body to create a counterparty. | [optional] 

### Return type

[**CounterpartyDetail**](CounterpartyDetail.md)

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

# **create_counterparty_wallet_address**
> WalletAddress create_counterparty_wallet_address(create_counterparty_wallet_address_request=create_counterparty_wallet_address_request)

Create counterparty wallet address

This operation creates a counterparty wallet address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_counterparty_wallet_address_request import CreateCounterpartyWalletAddressRequest
from cobo_waas2.models.wallet_address import WalletAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_counterparty_wallet_address_request = cobo_waas2.CreateCounterpartyWalletAddressRequest()

    try:
        # Create counterparty wallet address
        api_response = api_instance.create_counterparty_wallet_address(create_counterparty_wallet_address_request=create_counterparty_wallet_address_request)
        print("The response of PaymentApi->create_counterparty_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_counterparty_wallet_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_counterparty_wallet_address_request** | [**CreateCounterpartyWalletAddressRequest**](CreateCounterpartyWalletAddressRequest.md)| The request body to create a counterparty wallet address. | [optional] 

### Return type

[**WalletAddress**](WalletAddress.md)

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

# **create_crypto_address**
> CryptoAddress create_crypto_address(create_crypto_address_request=create_crypto_address_request)

Create crypto address

This operation registers a crypto address for crypto payouts.  The registered address can later be referenced by its ID when creating settlement requests. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_crypto_address_request import CreateCryptoAddressRequest
from cobo_waas2.models.crypto_address import CryptoAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_crypto_address_request = cobo_waas2.CreateCryptoAddressRequest()

    try:
        # Create crypto address
        api_response = api_instance.create_crypto_address(create_crypto_address_request=create_crypto_address_request)
        print("The response of PaymentApi->create_crypto_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_crypto_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_crypto_address_request** | [**CreateCryptoAddressRequest**](CreateCryptoAddressRequest.md)| The request body to register a crypto address. | [optional] 

### Return type

[**CryptoAddress**](CryptoAddress.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Crypto address created successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_destination**
> DestinationDetail create_destination(create_destination_request=create_destination_request)

Create destination

This operation creates a destination. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_destination_request import CreateDestinationRequest
from cobo_waas2.models.destination_detail import DestinationDetail
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_destination_request = cobo_waas2.CreateDestinationRequest()

    try:
        # Create destination
        api_response = api_instance.create_destination(create_destination_request=create_destination_request)
        print("The response of PaymentApi->create_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_destination_request** | [**CreateDestinationRequest**](CreateDestinationRequest.md)| The request body to create a destination. | [optional] 

### Return type

[**DestinationDetail**](DestinationDetail.md)

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

# **create_destination_bank_account**
> DestinationBankAccount create_destination_bank_account(create_destination_bank_account_request=create_destination_bank_account_request)

Create destination bank account

This operation creates a destination bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_destination_bank_account_request import CreateDestinationBankAccountRequest
from cobo_waas2.models.destination_bank_account import DestinationBankAccount
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_destination_bank_account_request = cobo_waas2.CreateDestinationBankAccountRequest()

    try:
        # Create destination bank account
        api_response = api_instance.create_destination_bank_account(create_destination_bank_account_request=create_destination_bank_account_request)
        print("The response of PaymentApi->create_destination_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_destination_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_destination_bank_account_request** | [**CreateDestinationBankAccountRequest**](CreateDestinationBankAccountRequest.md)| The request body to create a destination bank account. | [optional] 

### Return type

[**DestinationBankAccount**](DestinationBankAccount.md)

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

# **create_destination_wallet_address**
> WalletAddress create_destination_wallet_address(create_destination_wallet_address_request=create_destination_wallet_address_request)

Create destination wallet address

This operation creates a destination wallet address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_destination_wallet_address_request import CreateDestinationWalletAddressRequest
from cobo_waas2.models.wallet_address import WalletAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_destination_wallet_address_request = cobo_waas2.CreateDestinationWalletAddressRequest()

    try:
        # Create destination wallet address
        api_response = api_instance.create_destination_wallet_address(create_destination_wallet_address_request=create_destination_wallet_address_request)
        print("The response of PaymentApi->create_destination_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_destination_wallet_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_destination_wallet_address_request** | [**CreateDestinationWalletAddressRequest**](CreateDestinationWalletAddressRequest.md)| The request body to create a destination wallet address. | [optional] 

### Return type

[**WalletAddress**](WalletAddress.md)

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

# **create_forced_sweep_request**
> ForcedSweep create_forced_sweep_request(forced_sweep_request=forced_sweep_request)

Create forced sweep

<Warning>This operation has been deprecated.</Warning> This operation creates a forced sweep to transfer funds from addresses within a specified wallet to its designated sweep-to address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.forced_sweep import ForcedSweep
from cobo_waas2.models.forced_sweep_request import ForcedSweepRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    forced_sweep_request = cobo_waas2.ForcedSweepRequest()

    try:
        # Create forced sweep
        api_response = api_instance.create_forced_sweep_request(forced_sweep_request=forced_sweep_request)
        print("The response of PaymentApi->create_forced_sweep_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_forced_sweep_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forced_sweep_request** | [**ForcedSweepRequest**](ForcedSweepRequest.md)| The request body for forced sweep. | [optional] 

### Return type

[**ForcedSweep**](ForcedSweep.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Forced sweep created successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_merchant**
> Merchant create_merchant(create_merchant_request=create_merchant_request)

Create merchant

This operation creates a merchant. Upon successful creation, a merchant ID is generated and returned along with the merchant's information. For more information on merchant creation, please refer to [Preparation](https://www.cobo.com/developers/v2/payments/preparation#create-merchant). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_merchant_request import CreateMerchantRequest
from cobo_waas2.models.merchant import Merchant
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_merchant_request = cobo_waas2.CreateMerchantRequest()

    try:
        # Create merchant
        api_response = api_instance.create_merchant(create_merchant_request=create_merchant_request)
        print("The response of PaymentApi->create_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_merchant_request** | [**CreateMerchantRequest**](CreateMerchantRequest.md)| The request body to create a merchant. | [optional] 

### Return type

[**Merchant**](Merchant.md)

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

# **create_order_link**
> Link create_order_link(create_order_link_request=create_order_link_request)

Create order link

This operation generates a payment link for a pay-in order. The link directs users to a hosted payment page where they can complete their payment for the order. You can share the link directly with users or embed the payment page in your website or application using an iframe.  For more details, see [Payment Link](https://www.cobo.com/developers/v2/payments/payment-link). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_order_link_request import CreateOrderLinkRequest
from cobo_waas2.models.link import Link
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_order_link_request = cobo_waas2.CreateOrderLinkRequest()

    try:
        # Create order link
        api_response = api_instance.create_order_link(create_order_link_request=create_order_link_request)
        print("The response of PaymentApi->create_order_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_order_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_link_request** | [**CreateOrderLinkRequest**](CreateOrderLinkRequest.md)| The request body to create a payment link for a pay-in order. | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Link created successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_order**
> Order create_payment_order(create_payment_order_request=create_payment_order_request)

Create pay-in order

This operation creates a pay-in order. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_payment_order_request import CreatePaymentOrderRequest
from cobo_waas2.models.order import Order
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_payment_order_request = cobo_waas2.CreatePaymentOrderRequest()

    try:
        # Create pay-in order
        api_response = api_instance.create_payment_order(create_payment_order_request=create_payment_order_request)
        print("The response of PaymentApi->create_payment_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_payment_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_order_request** | [**CreatePaymentOrderRequest**](CreatePaymentOrderRequest.md)| The request body to create a pay-in order. | [optional] 

### Return type

[**Order**](Order.md)

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

# **create_refund**
> Refund create_refund(create_refund_request=create_refund_request)

Create refund order

This operation creates a refund order to return cryptocurrency to a specified address.   When creating a refund order, you can optionally link it to an existing pay-in order for tracking and reconciliation purposes. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_refund_request import CreateRefundRequest
from cobo_waas2.models.refund import Refund
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_refund_request = cobo_waas2.CreateRefundRequest()

    try:
        # Create refund order
        api_response = api_instance.create_refund(create_refund_request=create_refund_request)
        print("The response of PaymentApi->create_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_refund_request** | [**CreateRefundRequest**](CreateRefundRequest.md)| The request body to create a refund order. | [optional] 

### Return type

[**Refund**](Refund.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Refund transaction created successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund_link**
> Link create_refund_link(create_refund_link_request=create_refund_link_request)

Create refund link

This operation creates a link that points to a Cobo-hosted refund page. The user can submit their desired refund address on the page.  Once the address is submitted, Cobo will automatically create a refund order and initiate the refund process according to your configuration.  For details, see [Create refund link](https://www.cobo.com/developers/v2/payments/create-refund-link). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_refund_link_request import CreateRefundLinkRequest
from cobo_waas2.models.link import Link
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_refund_link_request = cobo_waas2.CreateRefundLinkRequest()

    try:
        # Create refund link
        api_response = api_instance.create_refund_link(create_refund_link_request=create_refund_link_request)
        print("The response of PaymentApi->create_refund_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_refund_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_refund_link_request** | [**CreateRefundLinkRequest**](CreateRefundLinkRequest.md)| The request body to create a refund link. | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Link created successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settlement_request**
> Settlement create_settlement_request(create_settlement_request_request=create_settlement_request_request)

Create settlement request

This operation creates a settlement request to withdraw available balances. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_settlement_request_request import CreateSettlementRequestRequest
from cobo_waas2.models.settlement import Settlement
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    create_settlement_request_request = cobo_waas2.CreateSettlementRequestRequest()

    try:
        # Create settlement request
        api_response = api_instance.create_settlement_request(create_settlement_request_request=create_settlement_request_request)
        print("The response of PaymentApi->create_settlement_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_settlement_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_settlement_request_request** | [**CreateSettlementRequestRequest**](CreateSettlementRequestRequest.md)| The request body to create a settlement request. | [optional] 

### Return type

[**Settlement**](Settlement.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The settlement request was successfully created. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_counterparty**
> DeleteCounterparty200Response delete_counterparty(counterparty_id)

Delete counterparty

This operation deletes a counterparty. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_counterparty200_response import DeleteCounterparty200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    counterparty_id = '5b0ed293-f728-40b4-b1f6-86b88cd51384'

    try:
        # Delete counterparty
        api_response = api_instance.delete_counterparty(counterparty_id)
        print("The response of PaymentApi->delete_counterparty:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_counterparty: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| The counterparty ID. | 

### Return type

[**DeleteCounterparty200Response**](DeleteCounterparty200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_counterparty_wallet_address**
> DeleteCounterpartyWalletAddress200Response delete_counterparty_wallet_address(wallet_address_id)

Delete counterparty wallet address

This operation deletes a counterparty wallet address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_counterparty_wallet_address200_response import DeleteCounterpartyWalletAddress200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    wallet_address_id = '445bac57-7428-4d25-bce1-b3cd017f47a1'

    try:
        # Delete counterparty wallet address
        api_response = api_instance.delete_counterparty_wallet_address(wallet_address_id)
        print("The response of PaymentApi->delete_counterparty_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_counterparty_wallet_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_address_id** | **str**| The wallet address ID. | 

### Return type

[**DeleteCounterpartyWalletAddress200Response**](DeleteCounterpartyWalletAddress200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_crypto_address**
> DeleteCryptoAddress201Response delete_crypto_address(crypto_address_id)

Delete crypto address

This operation unregisters a crypto address from being used for crypto payouts. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_crypto_address201_response import DeleteCryptoAddress201Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    crypto_address_id = 'addr_ethusdt_20250506T123456_ab12cd'

    try:
        # Delete crypto address
        api_response = api_instance.delete_crypto_address(crypto_address_id)
        print("The response of PaymentApi->delete_crypto_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_crypto_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_address_id** | **str**| The crypto address ID. | 

### Return type

[**DeleteCryptoAddress201Response**](DeleteCryptoAddress201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination**
> DeleteDestination200Response delete_destination(destination_id)

Delete destination

This operation deletes a destination. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_destination200_response import DeleteDestination200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    destination_id = '46beeab4-6a8e-476e-bc69-99b89aacbc6f'

    try:
        # Delete destination
        api_response = api_instance.delete_destination(destination_id)
        print("The response of PaymentApi->delete_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The destination ID. | 

### Return type

[**DeleteDestination200Response**](DeleteDestination200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination_bank_account**
> DeleteDestinationBankAccount200Response delete_destination_bank_account(bank_account_id)

Delete destination bank account

This operation deletes a destination bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_destination_bank_account200_response import DeleteDestinationBankAccount200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    bank_account_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Delete destination bank account
        api_response = api_instance.delete_destination_bank_account(bank_account_id)
        print("The response of PaymentApi->delete_destination_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_destination_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**| The bank account ID. | 

### Return type

[**DeleteDestinationBankAccount200Response**](DeleteDestinationBankAccount200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination_wallet_address**
> DeleteDestinationWalletAddress200Response delete_destination_wallet_address(wallet_address_id)

Delete destination wallet address

This operation deletes a destination wallet address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_destination_wallet_address200_response import DeleteDestinationWalletAddress200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    wallet_address_id = '445bac57-7428-4d25-bce1-b3cd017f47a1'

    try:
        # Delete destination wallet address
        api_response = api_instance.delete_destination_wallet_address(wallet_address_id)
        print("The response of PaymentApi->delete_destination_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->delete_destination_wallet_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_address_id** | **str**| The wallet address ID. | 

### Return type

[**DeleteDestinationWalletAddress200Response**](DeleteDestinationWalletAddress200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_destination_whitelist**
> QueryDestinationWhitelistEnabled200Response enable_destination_whitelist(enable_destination_whitelist_request=enable_destination_whitelist_request)

Enable or disable destination whitelist

This operation enables or disables the whitelist for a destination. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.enable_destination_whitelist_request import EnableDestinationWhitelistRequest
from cobo_waas2.models.query_destination_whitelist_enabled200_response import QueryDestinationWhitelistEnabled200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    enable_destination_whitelist_request = cobo_waas2.EnableDestinationWhitelistRequest()

    try:
        # Enable or disable destination whitelist
        api_response = api_instance.enable_destination_whitelist(enable_destination_whitelist_request=enable_destination_whitelist_request)
        print("The response of PaymentApi->enable_destination_whitelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->enable_destination_whitelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_destination_whitelist_request** | [**EnableDestinationWhitelistRequest**](EnableDestinationWhitelistRequest.md)| The request body to enable or disable the destination whitelist. | [optional] 

### Return type

[**QueryDestinationWhitelistEnabled200Response**](QueryDestinationWhitelistEnabled200Response.md)

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

# **get_counterparty_detail_by_id**
> CounterpartyDetail get_counterparty_detail_by_id(counterparty_id)

Get counterparty information

This operation retrieves the detailed information about a specified counterparty. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.counterparty_detail import CounterpartyDetail
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    counterparty_id = '5b0ed293-f728-40b4-b1f6-86b88cd51384'

    try:
        # Get counterparty information
        api_response = api_instance.get_counterparty_detail_by_id(counterparty_id)
        print("The response of PaymentApi->get_counterparty_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_counterparty_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| The counterparty ID. | 

### Return type

[**CounterpartyDetail**](CounterpartyDetail.md)

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

# **get_destination_bank_account_detail_by_id**
> DestinationBankAccountDetail get_destination_bank_account_detail_by_id(bank_account_id)

Get destination bank account information

This operation retrieves the detailed information about a specified destination bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.destination_bank_account_detail import DestinationBankAccountDetail
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    bank_account_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get destination bank account information
        api_response = api_instance.get_destination_bank_account_detail_by_id(bank_account_id)
        print("The response of PaymentApi->get_destination_bank_account_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_destination_bank_account_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**| The bank account ID. | 

### Return type

[**DestinationBankAccountDetail**](DestinationBankAccountDetail.md)

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

# **get_destination_detail_by_id**
> DestinationDetail get_destination_detail_by_id(destination_id)

Get destination information

This operation retrieves the detailed information about a specified destination. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.destination_detail import DestinationDetail
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    destination_id = '46beeab4-6a8e-476e-bc69-99b89aacbc6f'

    try:
        # Get destination information
        api_response = api_instance.get_destination_detail_by_id(destination_id)
        print("The response of PaymentApi->get_destination_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_destination_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The destination ID. | 

### Return type

[**DestinationDetail**](DestinationDetail.md)

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

# **get_exchange_rate**
> GetExchangeRate200Response get_exchange_rate(token_id, currency)

Get exchange rate

This operation retrieves the current exchange rate between a specified currency pair. The exchange rate is updated approximately every 10 minutes.  <Note>This operation returns the exchange rate for reference only. The actual exchange rate may vary due to market fluctuations and other factors.</Note> 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_exchange_rate200_response import GetExchangeRate200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'
    currency = 'USD'

    try:
        # Get exchange rate
        api_response = api_instance.get_exchange_rate(token_id, currency)
        print("The response of PaymentApi->get_exchange_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_exchange_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
 **currency** | **str**| The fiat currency. Currently, only &#x60;USD&#x60; is supported. | [default to &#39;USD&#39;]

### Return type

[**GetExchangeRate200Response**](GetExchangeRate200Response.md)

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

# **get_payment_order_detail_by_id**
> Order get_payment_order_detail_by_id(order_id)

Get pay-in order information

This operation retrieves details of a specific pay-in order. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.order import Order
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    order_id = 'O20250304-M1001-1001'

    try:
        # Get pay-in order information
        api_response = api_instance.get_payment_order_detail_by_id(order_id)
        print("The response of PaymentApi->get_payment_order_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_order_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The pay-in order ID. | 

### Return type

[**Order**](Order.md)

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

# **get_psp_balance**
> PspBalance get_psp_balance(token_id)

Get developer balance

This operation retrieves the balance information for you as the developer. The balance information is grouped by token.  For more information, please refer to [Funds allocation and balances](https://www.cobo.com/developers/v2/payments/amounts-and-balances). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.psp_balance import PspBalance
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'

    try:
        # Get developer balance
        api_response = api_instance.get_psp_balance(token_id)
        print("The response of PaymentApi->get_psp_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_psp_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 

### Return type

[**PspBalance**](PspBalance.md)

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

# **get_refund_detail_by_id**
> Refund get_refund_detail_by_id(refund_id)

Get refund order information

This operation retrieves the detailed information about a specified refund order. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.refund import Refund
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    refund_id = 'R20250304-M1001-1001'

    try:
        # Get refund order information
        api_response = api_instance.get_refund_detail_by_id(refund_id)
        print("The response of PaymentApi->get_refund_detail_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_refund_detail_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The refund order ID. | 

### Return type

[**Refund**](Refund.md)

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

# **get_refunds**
> GetRefunds200Response get_refunds(limit=limit, before=before, after=after, merchant_id=merchant_id, request_id=request_id, statuses=statuses)

List all refund orders

This operation retrieves the information of all refund orders. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_refunds200_response import GetRefunds200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    merchant_id = 'M1001'
    request_id = 'random_request_id'
    statuses = 'Pending,Processing'

    try:
        # List all refund orders
        api_response = api_instance.get_refunds(limit=limit, before=before, after=after, merchant_id=merchant_id, request_id=request_id, statuses=statuses)
        print("The response of PaymentApi->get_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **merchant_id** | **str**| The merchant ID. | [optional] 
 **request_id** | **str**| The request ID. | [optional] 
 **statuses** | **str**| A list of order, refund or settlement statuses. You can refer to the following operations for the possible status values:  - [Get pay-in order information](https://www.cobo.com/developers/v2/api-references/payment/get-pay-in-order-information)  - [Get refund order information](https://www.cobo.com/developers/v2/api-references/payment/get-refund-order-information)  - [List all settlement details](https://www.cobo.com/developers/v2/api-references/payment/list-all-settlement-details)  | [optional] 

### Return type

[**GetRefunds200Response**](GetRefunds200Response.md)

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

# **get_settlement_by_id**
> Settlement get_settlement_by_id(settlement_request_id)

Get settlement request information

This operation retrieves the information of a specific settlement request. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.settlement import Settlement
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    settlement_request_id = 'S20250304-1001'

    try:
        # Get settlement request information
        api_response = api_instance.get_settlement_by_id(settlement_request_id)
        print("The response of PaymentApi->get_settlement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_settlement_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_request_id** | **str**| The settlement request ID. | 

### Return type

[**Settlement**](Settlement.md)

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

# **get_settlement_info_by_ids**
> GetSettlementInfoByIds200Response get_settlement_info_by_ids(merchant_ids=merchant_ids, currency=currency, acquiring_type=acquiring_type)

Get withdrawable balances

<Warning>This operation has been deprecated.</Warning> This operation retrieves the balances of specified merchants or the developer. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.acquiring_type import AcquiringType
from cobo_waas2.models.get_settlement_info_by_ids200_response import GetSettlementInfoByIds200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    merchant_ids = 'M1001,M1002,M1003'
    currency = 'USD'
    acquiring_type = cobo_waas2.AcquiringType()

    try:
        # Get withdrawable balances
        api_response = api_instance.get_settlement_info_by_ids(merchant_ids=merchant_ids, currency=currency, acquiring_type=acquiring_type)
        print("The response of PaymentApi->get_settlement_info_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_settlement_info_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_ids** | **str**| A list of merchant IDs to query. | [optional] 
 **currency** | **str**| The currency for the operation. Currently, only &#x60;USD&#x60; is supported. | [optional] [default to &#39;USD&#39;]
 **acquiring_type** | [**AcquiringType**](.md)|  | [optional] 

### Return type

[**GetSettlementInfoByIds200Response**](GetSettlementInfoByIds200Response.md)

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

# **get_top_up_address**
> TopUpAddress get_top_up_address(token_id, custom_payer_id, merchant_id=merchant_id)

Create/Get top-up address

This operation creates or retrieves a unique top-up address for a payer.   In the request, you need to provide the `custom_payer_id` parameter to identify the payer in your system and link them to the top-up address.  - If no address exists for the payer on the specified chain, a new address will be created and returned. - If an address already exists for the payer on the specified chain, the existing address details will be returned.  You can also provide the `merchant_id` parameter to specify the merchant to which the payer belongs. If not provided, the default merchant will be used. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.top_up_address import TopUpAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'
    custom_payer_id = 'payer_0001'
    merchant_id = 'M1001'

    try:
        # Create/Get top-up address
        api_response = api_instance.get_top_up_address(token_id, custom_payer_id, merchant_id=merchant_id)
        print("The response of PaymentApi->get_top_up_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_top_up_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
 **custom_payer_id** | **str**| A unique identifier to track and identify individual payers in your system. | 
 **merchant_id** | **str**| The merchant ID. | [optional] 

### Return type

[**TopUpAddress**](TopUpAddress.md)

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

# **list_bank_accounts**
> List[BankAccount] list_bank_accounts()

List all bank accounts

This operation retrieves the information of all bank accounts you have registered for payment settlement. Contact our support team at [help@cobo.com](mailto:help@cobo.com) to register a new bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.bank_account import BankAccount
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
    api_instance = cobo_waas2.PaymentApi(api_client)

    try:
        # List all bank accounts
        api_response = api_instance.list_bank_accounts()
        print("The response of PaymentApi->list_bank_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_bank_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BankAccount]**](BankAccount.md)

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

# **list_counterparties**
> ListCounterparties200Response list_counterparties(limit=limit, before=before, after=after, keyword=keyword, counterparty_type=counterparty_type, country=country)

List all counterparties

This operation retrieves the information of all counterparties.   You can filter the results by using a keyword for fuzzy search on counterparty names. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.counterparty_type import CounterpartyType
from cobo_waas2.models.list_counterparties200_response import ListCounterparties200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    keyword = 'keyword'
    counterparty_type = cobo_waas2.CounterpartyType()
    country = 'USA'

    try:
        # List all counterparties
        api_response = api_instance.list_counterparties(limit=limit, before=before, after=after, keyword=keyword, counterparty_type=counterparty_type, country=country)
        print("The response of PaymentApi->list_counterparties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_counterparties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **keyword** | **str**| A search term used for fuzzy matching of merchant names. | [optional] 
 **counterparty_type** | [**CounterpartyType**](.md)| CounterpartyType defines the type of the counterparty: - &#x60;Individual&#x60;: The counterparty is an individual. - &#x60;Organization&#x60;: The counterparty is an organization.  | [optional] 
 **country** | **str**| The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 

### Return type

[**ListCounterparties200Response**](ListCounterparties200Response.md)

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

# **list_counterparty_wallet_address**
> ListCounterpartyWalletAddress200Response list_counterparty_wallet_address(limit=limit, before=before, after=after, counterparty_id=counterparty_id, chain_ids=chain_ids, wallet_address=wallet_address)

List counterparty wallet addresses

This operation retrieves the information of counterparty wallet addresses. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_counterparty_wallet_address200_response import ListCounterpartyWalletAddress200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    counterparty_id = '5b0ed293-f728-40b4-b1f6-86b88cd51384'
    chain_ids = 'BTC,ETH'
    wallet_address = '0x1234567890abcdef...'

    try:
        # List counterparty wallet addresses
        api_response = api_instance.list_counterparty_wallet_address(limit=limit, before=before, after=after, counterparty_id=counterparty_id, chain_ids=chain_ids, wallet_address=wallet_address)
        print("The response of PaymentApi->list_counterparty_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_counterparty_wallet_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **counterparty_id** | **str**| The counterparty ID. | [optional] 
 **chain_ids** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **wallet_address** | **str**| The wallet address. | [optional] 

### Return type

[**ListCounterpartyWalletAddress200Response**](ListCounterpartyWalletAddress200Response.md)

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

# **list_crypto_addresses**
> List[CryptoAddress] list_crypto_addresses(token_id=token_id)

List crypto addresses

This operation retrieves a list of crypto addresses registered for crypto payouts.   Contact our support team at [help@cobo.com](mailto:help@cobo.com) to register a new crypto address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.crypto_address import CryptoAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'

    try:
        # List crypto addresses
        api_response = api_instance.list_crypto_addresses(token_id=token_id)
        print("The response of PaymentApi->list_crypto_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_crypto_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | [optional] 

### Return type

[**List[CryptoAddress]**](CryptoAddress.md)

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

# **list_destination_bank_accounts**
> ListDestinationBankAccounts200Response list_destination_bank_accounts(limit=limit, before=before, after=after, keyword=keyword, destination_id=destination_id, bank_account_status=bank_account_status)

List destination bank accounts

This operation retrieves the information of destination bank accounts. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.bank_account_status import BankAccountStatus
from cobo_waas2.models.list_destination_bank_accounts200_response import ListDestinationBankAccounts200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    keyword = 'keyword'
    destination_id = '46beeab4-6a8e-476e-bc69-99b89aacbc6f'
    bank_account_status = cobo_waas2.BankAccountStatus()

    try:
        # List destination bank accounts
        api_response = api_instance.list_destination_bank_accounts(limit=limit, before=before, after=after, keyword=keyword, destination_id=destination_id, bank_account_status=bank_account_status)
        print("The response of PaymentApi->list_destination_bank_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_destination_bank_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **keyword** | **str**| A search term used for fuzzy matching of merchant names. | [optional] 
 **destination_id** | **str**| The destination ID. | [optional] 
 **bank_account_status** | [**BankAccountStatus**](.md)| BankAccountStatus defines the status of the bank account: - &#x60;Pending&#x60;: The bank account is pending verification by Cobo. - &#x60;Approved&#x60;: The bank account has been approved by Cobo. - &#x60;Rejected&#x60;: The bank account has been rejected by Cobo.  | [optional] 

### Return type

[**ListDestinationBankAccounts200Response**](ListDestinationBankAccounts200Response.md)

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

# **list_destination_wallet_addresses**
> ListDestinationWalletAddresses200Response list_destination_wallet_addresses(limit=limit, before=before, after=after, destination_id=destination_id, chain_ids=chain_ids, wallet_address=wallet_address)

List destination wallet addresses

This operation retrieves the information of destination wallet addresses. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_destination_wallet_addresses200_response import ListDestinationWalletAddresses200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    destination_id = '46beeab4-6a8e-476e-bc69-99b89aacbc6f'
    chain_ids = 'BTC,ETH'
    wallet_address = '0x1234567890abcdef...'

    try:
        # List destination wallet addresses
        api_response = api_instance.list_destination_wallet_addresses(limit=limit, before=before, after=after, destination_id=destination_id, chain_ids=chain_ids, wallet_address=wallet_address)
        print("The response of PaymentApi->list_destination_wallet_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_destination_wallet_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **destination_id** | **str**| The destination ID. | [optional] 
 **chain_ids** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **wallet_address** | **str**| The wallet address. | [optional] 

### Return type

[**ListDestinationWalletAddresses200Response**](ListDestinationWalletAddresses200Response.md)

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

# **list_destinations**
> ListDestinations200Response list_destinations(limit=limit, before=before, after=after, keyword=keyword, destination_type=destination_type, country=country, merchant_ids=merchant_ids)

List all destinations

This operation retrieves the information of all destinations.   You can filter the results by using a keyword for fuzzy search on destination names. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.destination_type import DestinationType
from cobo_waas2.models.list_destinations200_response import ListDestinations200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    keyword = 'keyword'
    destination_type = cobo_waas2.DestinationType()
    country = 'USA'
    merchant_ids = 'M1001,M1002,M1003'

    try:
        # List all destinations
        api_response = api_instance.list_destinations(limit=limit, before=before, after=after, keyword=keyword, destination_type=destination_type, country=country, merchant_ids=merchant_ids)
        print("The response of PaymentApi->list_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_destinations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **keyword** | **str**| A search term used for fuzzy matching of merchant names. | [optional] 
 **destination_type** | [**DestinationType**](.md)| DestinationType defines the type of the destination: - &#x60;Individual&#x60;: The destination is an individual. - &#x60;Organization&#x60;: The destination is an organization.  | [optional] 
 **country** | **str**| The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
 **merchant_ids** | **str**| A list of merchant IDs to query. | [optional] 

### Return type

[**ListDestinations200Response**](ListDestinations200Response.md)

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

# **list_forced_sweep_requests**
> ListForcedSweepRequests200Response list_forced_sweep_requests(limit=limit, before=before, after=after, request_id=request_id)

List forced sweeps

<Warning>This operation has been deprecated.</Warning> This operation retrieves the information of all forced sweeps. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_forced_sweep_requests200_response import ListForcedSweepRequests200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    request_id = 'random_request_id'

    try:
        # List forced sweeps
        api_response = api_instance.list_forced_sweep_requests(limit=limit, before=before, after=after, request_id=request_id)
        print("The response of PaymentApi->list_forced_sweep_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_forced_sweep_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **request_id** | **str**| The request ID. | [optional] 

### Return type

[**ListForcedSweepRequests200Response**](ListForcedSweepRequests200Response.md)

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

# **list_merchant_balances**
> ListMerchantBalances200Response list_merchant_balances(token_id, acquiring_type, merchant_ids=merchant_ids)

List merchant balances

 This operation retrieves the balance information for specified merchants. The balance information is grouped by token and acquiring type. If you do not specify the `merchant_ids` parameter, the balance information for all merchants will be returned.  For more information, please refer to [Funds allocation and balances](https://www.cobo.com/developers/v2/payments/amounts-and-balances). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.acquiring_type import AcquiringType
from cobo_waas2.models.list_merchant_balances200_response import ListMerchantBalances200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'
    acquiring_type = cobo_waas2.AcquiringType()
    merchant_ids = 'M1001,M1002,M1003'

    try:
        # List merchant balances
        api_response = api_instance.list_merchant_balances(token_id, acquiring_type, merchant_ids=merchant_ids)
        print("The response of PaymentApi->list_merchant_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_merchant_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
 **acquiring_type** | [**AcquiringType**](.md)| The payment acquisition type. - &#x60;Order&#x60;: Payers pay by fixed-amount orders. Ideal for specific purchases and one-time transactions. - &#x60;TopUp&#x60;: Account recharge flow where payers deposit funds to their dedicated top-up addresses. Ideal for flexible or usage-based payment models.  | 
 **merchant_ids** | **str**| A list of merchant IDs to query. | [optional] 

### Return type

[**ListMerchantBalances200Response**](ListMerchantBalances200Response.md)

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

# **list_merchants**
> ListMerchants200Response list_merchants(limit=limit, before=before, after=after, keyword=keyword, wallet_id=wallet_id, wallet_setup=wallet_setup)

List all merchants

This operation retrieves the information of all merchants.   You can filter the results by using a keyword for fuzzy search on merchant names or by specifying a wallet ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_merchants200_response import ListMerchants200Response
from cobo_waas2.models.wallet_setup import WalletSetup
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    keyword = 'keyword'
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    wallet_setup = cobo_waas2.WalletSetup()

    try:
        # List all merchants
        api_response = api_instance.list_merchants(limit=limit, before=before, after=after, keyword=keyword, wallet_id=wallet_id, wallet_setup=wallet_setup)
        print("The response of PaymentApi->list_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_merchants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **keyword** | **str**| A search term used for fuzzy matching of merchant names. | [optional] 
 **wallet_id** | **str**| This parameter has been deprecated. | [optional] 
 **wallet_setup** | [**WalletSetup**](.md)| The type of wallet setup for the merchant. Each wallet contains multiple cryptocurrency addresses that serve as the merchant’s receiving addresses.  - &#x60;Shared&#x60;: Multiple merchants share the same wallet. The wallet’s addresses may be used to receive payments for multiple merchants simultaneously. - &#x60;Separate&#x60;: Create a dedicated wallet for the merchant to achieve complete fund isolation. All addresses in this wallet are only used to receive payments for this merchant. - &#x60;Default&#x60;: The default wallet automatically created by the system for the default merchant (the merchant that shares the same name as your organization).  | [optional] 

### Return type

[**ListMerchants200Response**](ListMerchants200Response.md)

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

# **list_payment_orders**
> ListPaymentOrders200Response list_payment_orders(limit=limit, before=before, after=after, merchant_id=merchant_id, psp_order_id=psp_order_id, statuses=statuses)

List all pay-in orders

This operation retrieves the information of all pay-in orders. You can filter the result by merchant ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_payment_orders200_response import ListPaymentOrders200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    merchant_id = 'M1001'
    psp_order_id = 'P20240201001'
    statuses = 'Pending,Processing'

    try:
        # List all pay-in orders
        api_response = api_instance.list_payment_orders(limit=limit, before=before, after=after, merchant_id=merchant_id, psp_order_id=psp_order_id, statuses=statuses)
        print("The response of PaymentApi->list_payment_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_payment_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **merchant_id** | **str**| The merchant ID. | [optional] 
 **psp_order_id** | **str**| A unique reference code assigned by the developer to identify this order in their system. | [optional] 
 **statuses** | **str**| A list of order, refund or settlement statuses. You can refer to the following operations for the possible status values:  - [Get pay-in order information](https://www.cobo.com/developers/v2/api-references/payment/get-pay-in-order-information)  - [Get refund order information](https://www.cobo.com/developers/v2/api-references/payment/get-refund-order-information)  - [List all settlement details](https://www.cobo.com/developers/v2/api-references/payment/list-all-settlement-details)  | [optional] 

### Return type

[**ListPaymentOrders200Response**](ListPaymentOrders200Response.md)

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

# **list_payment_supported_tokens**
> List[SupportedToken] list_payment_supported_tokens()

List all supported tokens

This operation retrieves the information of all supported tokens. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.supported_token import SupportedToken
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
    api_instance = cobo_waas2.PaymentApi(api_client)

    try:
        # List all supported tokens
        api_response = api_instance.list_payment_supported_tokens()
        print("The response of PaymentApi->list_payment_supported_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_payment_supported_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SupportedToken]**](SupportedToken.md)

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

# **list_payment_wallet_balances**
> ListPaymentWalletBalances200Response list_payment_wallet_balances(token_id, wallet_ids=wallet_ids)

List payment wallet balances

<Warning>This operation has been deprecated.</Warning> This operation retrieves the balance information for specified payment wallets. The balance information is grouped by token. If you do not specify the `wallet_ids` parameter, the balance information for all payment wallets will be returned. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_payment_wallet_balances200_response import ListPaymentWalletBalances200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    token_id = 'ETH_USDT'
    wallet_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,f47ac10b-58cc-4372-a567-0e02b2c3d472'

    try:
        # List payment wallet balances
        api_response = api_instance.list_payment_wallet_balances(token_id, wallet_ids=wallet_ids)
        print("The response of PaymentApi->list_payment_wallet_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_payment_wallet_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
 **wallet_ids** | **str**| A list of wallet IDs to query. | [optional] 

### Return type

[**ListPaymentWalletBalances200Response**](ListPaymentWalletBalances200Response.md)

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

# **list_settlement_details**
> ListSettlementDetails200Response list_settlement_details(limit=limit, before=before, after=after, merchant_id=merchant_id, statuses=statuses)

List all settlement details

This operation retrieves the information of all settlement details. You can filter the result by merchant ID or status. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_settlement_details200_response import ListSettlementDetails200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    merchant_id = 'M1001'
    statuses = 'Pending,Processing'

    try:
        # List all settlement details
        api_response = api_instance.list_settlement_details(limit=limit, before=before, after=after, merchant_id=merchant_id, statuses=statuses)
        print("The response of PaymentApi->list_settlement_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_settlement_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **merchant_id** | **str**| The merchant ID. | [optional] 
 **statuses** | **str**| A list of order, refund or settlement statuses. You can refer to the following operations for the possible status values:  - [Get pay-in order information](https://www.cobo.com/developers/v2/api-references/payment/get-pay-in-order-information)  - [Get refund order information](https://www.cobo.com/developers/v2/api-references/payment/get-refund-order-information)  - [List all settlement details](https://www.cobo.com/developers/v2/api-references/payment/list-all-settlement-details)  | [optional] 

### Return type

[**ListSettlementDetails200Response**](ListSettlementDetails200Response.md)

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

# **list_settlement_requests**
> ListSettlementRequests200Response list_settlement_requests(limit=limit, before=before, after=after, request_id=request_id)

List all settlement requests

This operation retrieves the information of all settlement requests. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_settlement_requests200_response import ListSettlementRequests200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    request_id = 'random_request_id'

    try:
        # List all settlement requests
        api_response = api_instance.list_settlement_requests(limit=limit, before=before, after=after, request_id=request_id)
        print("The response of PaymentApi->list_settlement_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_settlement_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **request_id** | **str**| The request ID. | [optional] 

### Return type

[**ListSettlementRequests200Response**](ListSettlementRequests200Response.md)

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

# **list_top_up_payer_accounts**
> ListTopUpPayerAccounts200Response list_top_up_payer_accounts(limit=limit, before=before, after=after, merchant_id=merchant_id, payer_id=payer_id)

List top-up payer accounts

This operation retrieves the accounts of all payers. You can filter the result by merchant ID and payer_id. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_top_up_payer_accounts200_response import ListTopUpPayerAccounts200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    merchant_id = 'M1001'
    payer_id = 'P20250619T0310056d7aa'

    try:
        # List top-up payer accounts
        api_response = api_instance.list_top_up_payer_accounts(limit=limit, before=before, after=after, merchant_id=merchant_id, payer_id=payer_id)
        print("The response of PaymentApi->list_top_up_payer_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_top_up_payer_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **merchant_id** | **str**| The merchant ID. | [optional] 
 **payer_id** | **str**| A unique identifier assigned by Cobo to track and identify individual payers. | [optional] 

### Return type

[**ListTopUpPayerAccounts200Response**](ListTopUpPayerAccounts200Response.md)

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

# **list_top_up_payers**
> ListTopUpPayers200Response list_top_up_payers(limit=limit, before=before, after=after, merchant_id=merchant_id, payer_id=payer_id)

List payers

This operation retrieves the information of all payers under a merchant.   You can filter the result by the payer ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_top_up_payers200_response import ListTopUpPayers200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    merchant_id = 'M1001'
    payer_id = 'P20250619T0310056d7aa'

    try:
        # List payers
        api_response = api_instance.list_top_up_payers(limit=limit, before=before, after=after, merchant_id=merchant_id, payer_id=payer_id)
        print("The response of PaymentApi->list_top_up_payers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_top_up_payers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **merchant_id** | **str**| The merchant ID. | [optional] 
 **payer_id** | **str**| A unique identifier assigned by Cobo to track and identify individual payers. | [optional] 

### Return type

[**ListTopUpPayers200Response**](ListTopUpPayers200Response.md)

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

# **payment_estimate_fee**
> PaymentEstimateFee201Response payment_estimate_fee(payment_estimate_fee_request=payment_estimate_fee_request)

Estimate fees

This operation calculates fees for payment-related operations, including: - **Pay-in**: Fees for accepting payments - **Refunds**: Fees for refunding the payment - **Crypto payouts**: Fees for payouts in crypto - **Fiat off-ramp**: Fees for fiat currency transfers via off-ramp.    The returned fees represent the charges that would apply if the operation were executed immediately. Note that actual fees may vary over time based on your usage volume and applicable fee rates. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.payment_estimate_fee201_response import PaymentEstimateFee201Response
from cobo_waas2.models.payment_estimate_fee_request import PaymentEstimateFeeRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    payment_estimate_fee_request = cobo_waas2.PaymentEstimateFeeRequest()

    try:
        # Estimate fees
        api_response = api_instance.payment_estimate_fee(payment_estimate_fee_request=payment_estimate_fee_request)
        print("The response of PaymentApi->payment_estimate_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_estimate_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_estimate_fee_request** | [**PaymentEstimateFeeRequest**](PaymentEstimateFeeRequest.md)| The request body for fee estimation. | [optional] 

### Return type

[**PaymentEstimateFee201Response**](PaymentEstimateFee201Response.md)

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

# **query_destination_whitelist_enabled**
> QueryDestinationWhitelistEnabled200Response query_destination_whitelist_enabled()

Query destination whitelist enabled status

This operation retrieves the information of whether the destination whitelist is enabled. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.query_destination_whitelist_enabled200_response import QueryDestinationWhitelistEnabled200Response
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
    api_instance = cobo_waas2.PaymentApi(api_client)

    try:
        # Query destination whitelist enabled status
        api_response = api_instance.query_destination_whitelist_enabled()
        print("The response of PaymentApi->query_destination_whitelist_enabled:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->query_destination_whitelist_enabled: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryDestinationWhitelistEnabled200Response**](QueryDestinationWhitelistEnabled200Response.md)

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

# **update_bank_account_by_id**
> BankAccount update_bank_account_by_id(bank_account_id, update_bank_account_by_id_request=update_bank_account_by_id_request)

Update bank account

This operation updates the information of an existing bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.bank_account import BankAccount
from cobo_waas2.models.update_bank_account_by_id_request import UpdateBankAccountByIdRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    bank_account_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_bank_account_by_id_request = cobo_waas2.UpdateBankAccountByIdRequest()

    try:
        # Update bank account
        api_response = api_instance.update_bank_account_by_id(bank_account_id, update_bank_account_by_id_request=update_bank_account_by_id_request)
        print("The response of PaymentApi->update_bank_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_bank_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**| The bank account ID. | 
 **update_bank_account_by_id_request** | [**UpdateBankAccountByIdRequest**](UpdateBankAccountByIdRequest.md)| The request body for updating an existing bank account. | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

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

# **update_counterparty_by_id**
> Counterparty update_counterparty_by_id(counterparty_id, update_counterparty_by_id_request=update_counterparty_by_id_request)

Update counterparty

This operation updates the information of a specified counterparty. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.counterparty import Counterparty
from cobo_waas2.models.update_counterparty_by_id_request import UpdateCounterpartyByIdRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    counterparty_id = '5b0ed293-f728-40b4-b1f6-86b88cd51384'
    update_counterparty_by_id_request = cobo_waas2.UpdateCounterpartyByIdRequest()

    try:
        # Update counterparty
        api_response = api_instance.update_counterparty_by_id(counterparty_id, update_counterparty_by_id_request=update_counterparty_by_id_request)
        print("The response of PaymentApi->update_counterparty_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_counterparty_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| The counterparty ID. | 
 **update_counterparty_by_id_request** | [**UpdateCounterpartyByIdRequest**](UpdateCounterpartyByIdRequest.md)| The request body to update a counterparty. | [optional] 

### Return type

[**Counterparty**](Counterparty.md)

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

# **update_destination_bank_account_by_id**
> DestinationBankAccount update_destination_bank_account_by_id(bank_account_id, update_destination_bank_account=update_destination_bank_account)

Update destination bank account

This operation updates the information of a specified destination bank account. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.destination_bank_account import DestinationBankAccount
from cobo_waas2.models.update_destination_bank_account import UpdateDestinationBankAccount
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    bank_account_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_destination_bank_account = cobo_waas2.UpdateDestinationBankAccount()

    try:
        # Update destination bank account
        api_response = api_instance.update_destination_bank_account_by_id(bank_account_id, update_destination_bank_account=update_destination_bank_account)
        print("The response of PaymentApi->update_destination_bank_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_destination_bank_account_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **str**| The bank account ID. | 
 **update_destination_bank_account** | [**UpdateDestinationBankAccount**](UpdateDestinationBankAccount.md)| The request body to update a destination bank account. | [optional] 

### Return type

[**DestinationBankAccount**](DestinationBankAccount.md)

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

# **update_destination_by_id**
> Destination update_destination_by_id(destination_id, update_destination_by_id_request=update_destination_by_id_request)

Update destination

This operation updates the information of a specified destination. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.destination import Destination
from cobo_waas2.models.update_destination_by_id_request import UpdateDestinationByIdRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    destination_id = '46beeab4-6a8e-476e-bc69-99b89aacbc6f'
    update_destination_by_id_request = cobo_waas2.UpdateDestinationByIdRequest()

    try:
        # Update destination
        api_response = api_instance.update_destination_by_id(destination_id, update_destination_by_id_request=update_destination_by_id_request)
        print("The response of PaymentApi->update_destination_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_destination_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**| The destination ID. | 
 **update_destination_by_id_request** | [**UpdateDestinationByIdRequest**](UpdateDestinationByIdRequest.md)| The request body to create a destination. | [optional] 

### Return type

[**Destination**](Destination.md)

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

# **update_merchant_by_id**
> Merchant update_merchant_by_id(merchant_id, update_merchant_by_id_request=update_merchant_by_id_request)

Update merchant

This operation updates the information of an existing merchant. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.merchant import Merchant
from cobo_waas2.models.update_merchant_by_id_request import UpdateMerchantByIdRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    merchant_id = 'M1001'
    update_merchant_by_id_request = cobo_waas2.UpdateMerchantByIdRequest()

    try:
        # Update merchant
        api_response = api_instance.update_merchant_by_id(merchant_id, update_merchant_by_id_request=update_merchant_by_id_request)
        print("The response of PaymentApi->update_merchant_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_merchant_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The merchant ID. | 
 **update_merchant_by_id_request** | [**UpdateMerchantByIdRequest**](UpdateMerchantByIdRequest.md)| The request body to update a merchant. | [optional] 

### Return type

[**Merchant**](Merchant.md)

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

# **update_payment_order**
> Order update_payment_order(order_id, update_payment_order_request=update_payment_order_request)

Update pay-in order

This operation updates a pay-in order. Use this operation to expire a pay-in order that is no longer needed. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.order import Order
from cobo_waas2.models.update_payment_order_request import UpdatePaymentOrderRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    order_id = 'O20250304-M1001-1001'
    update_payment_order_request = cobo_waas2.UpdatePaymentOrderRequest()

    try:
        # Update pay-in order
        api_response = api_instance.update_payment_order(order_id, update_payment_order_request=update_payment_order_request)
        print("The response of PaymentApi->update_payment_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_payment_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The pay-in order ID. | 
 **update_payment_order_request** | [**UpdatePaymentOrderRequest**](UpdatePaymentOrderRequest.md)| The request body to update a pay-in order. | [optional] 

### Return type

[**Order**](Order.md)

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

# **update_refund_by_id**
> Refund update_refund_by_id(refund_id, update_refund_by_id_request=update_refund_by_id_request)

Update refund order

This operation updates a specified refund order by modifying its recipient address. You can only update the recipient address for refund orders that have not been processed yet. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.refund import Refund
from cobo_waas2.models.update_refund_by_id_request import UpdateRefundByIdRequest
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    refund_id = 'R20250304-M1001-1001'
    update_refund_by_id_request = cobo_waas2.UpdateRefundByIdRequest()

    try:
        # Update refund order
        api_response = api_instance.update_refund_by_id(refund_id, update_refund_by_id_request=update_refund_by_id_request)
        print("The response of PaymentApi->update_refund_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_refund_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The refund order ID. | 
 **update_refund_by_id_request** | [**UpdateRefundByIdRequest**](UpdateRefundByIdRequest.md)| The request body to update a refund order. | [optional] 

### Return type

[**Refund**](Refund.md)

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

# **update_top_up_address**
> TopUpAddress update_top_up_address(update_top_up_address=update_top_up_address)

Update top-up address

This operation updates the dedicated top-up address assigned to a specific payer under a merchant on a specified chain.  <Note>   You can update the top-up address for a given payer a maximum of 10 times. If you exceed this limit, the API request will return an error. </Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.top_up_address import TopUpAddress
from cobo_waas2.models.update_top_up_address import UpdateTopUpAddress
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
    api_instance = cobo_waas2.PaymentApi(api_client)
    update_top_up_address = cobo_waas2.UpdateTopUpAddress()

    try:
        # Update top-up address
        api_response = api_instance.update_top_up_address(update_top_up_address=update_top_up_address)
        print("The response of PaymentApi->update_top_up_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_top_up_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_top_up_address** | [**UpdateTopUpAddress**](UpdateTopUpAddress.md)| The request body to update top-up address. | [optional] 

### Return type

[**TopUpAddress**](TopUpAddress.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Top-up address updated successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

