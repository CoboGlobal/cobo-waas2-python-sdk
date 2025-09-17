# cobo_waas2.PaymentApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_refund_by_id**](PaymentApi.md#cancel_refund_by_id) | **PUT** /payments/refunds/{refund_id}/cancel | Cancel refund order
[**create_crypto_address**](PaymentApi.md#create_crypto_address) | **POST** /payments/crypto_addresses | Create crypto address
[**create_forced_sweep_request**](PaymentApi.md#create_forced_sweep_request) | **POST** /payments/force_sweep_requests | Create forced sweep
[**create_merchant**](PaymentApi.md#create_merchant) | **POST** /payments/merchants | Create merchant
[**create_payment_order**](PaymentApi.md#create_payment_order) | **POST** /payments/orders | Create pay-in order
[**create_refund**](PaymentApi.md#create_refund) | **POST** /payments/refunds | Create refund order
[**create_settlement_request**](PaymentApi.md#create_settlement_request) | **POST** /payments/settlement_requests | Create settlement request
[**delete_crypto_address**](PaymentApi.md#delete_crypto_address) | **POST** /payments/crypto_addresses/{crypto_address_id}/delete | Delete crypto address
[**get_exchange_rate**](PaymentApi.md#get_exchange_rate) | **GET** /payments/exchange_rates/{token_id}/{currency} | Get exchange rate
[**get_payer_balance_by_address**](PaymentApi.md#get_payer_balance_by_address) | **GET** /payments/balance/payer/address | Get payer balance
[**get_payment_order_detail_by_id**](PaymentApi.md#get_payment_order_detail_by_id) | **GET** /payments/orders/{order_id} | Get pay-in order information
[**get_psp_balance**](PaymentApi.md#get_psp_balance) | **GET** /payments/balance/psp | Get developer balance
[**get_refund_detail_by_id**](PaymentApi.md#get_refund_detail_by_id) | **GET** /payments/refunds/{refund_id} | Get refund order information
[**get_refunds**](PaymentApi.md#get_refunds) | **GET** /payments/refunds | List all refund orders
[**get_settlement_by_id**](PaymentApi.md#get_settlement_by_id) | **GET** /payments/settlement_requests/{settlement_request_id} | Get settlement request information
[**get_settlement_info_by_ids**](PaymentApi.md#get_settlement_info_by_ids) | **GET** /payments/settlement_info | Get withdrawable balances
[**get_top_up_address**](PaymentApi.md#get_top_up_address) | **GET** /payments/topup/address | Get top-up address
[**list_bank_accounts**](PaymentApi.md#list_bank_accounts) | **GET** /payments/bank_accounts | List all bank accounts
[**list_crypto_addresses**](PaymentApi.md#list_crypto_addresses) | **GET** /payments/crypto_addresses | List crypto addresses
[**list_forced_sweep_requests**](PaymentApi.md#list_forced_sweep_requests) | **GET** /payments/force_sweep_requests | List forced sweeps
[**list_merchant_balances**](PaymentApi.md#list_merchant_balances) | **GET** /payments/balance/merchants | List merchant balances
[**list_merchants**](PaymentApi.md#list_merchants) | **GET** /payments/merchants | List all merchants
[**list_payment_orders**](PaymentApi.md#list_payment_orders) | **GET** /payments/orders | List all pay-in orders
[**list_payment_supported_tokens**](PaymentApi.md#list_payment_supported_tokens) | **GET** /payments/supported_tokens | List all supported tokens
[**list_payment_wallet_balances**](PaymentApi.md#list_payment_wallet_balances) | **GET** /payments/balance/payment_wallets | List payment wallet balances
[**list_settlement_details**](PaymentApi.md#list_settlement_details) | **GET** /payments/settlement_details | List all settlement details
[**list_settlement_requests**](PaymentApi.md#list_settlement_requests) | **GET** /payments/settlement_requests | List all settlement requests
[**list_top_up_payers**](PaymentApi.md#list_top_up_payers) | **GET** /payments/topup/payers | List payers
[**update_merchant_by_id**](PaymentApi.md#update_merchant_by_id) | **PUT** /payments/merchants/{merchant_id} | Update merchant
[**update_payment_order**](PaymentApi.md#update_payment_order) | **PUT** /payments/orders/{order_id} | Update pay-in order
[**update_refund_by_id**](PaymentApi.md#update_refund_by_id) | **PUT** /payments/refunds/{refund_id} | Update refund order
[**update_top_up_address**](PaymentApi.md#update_top_up_address) | **PUT** /payments/topup/address | Update top-up address


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

# **create_crypto_address**
> CryptoAddress create_crypto_address(create_crypto_address_request=create_crypto_address_request)

Create crypto address

This operation registers a crypto address for crypto withdrawal.  The registered address can later be referenced by its ID when creating settlement requests. 

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

# **create_forced_sweep_request**
> ForcedSweep create_forced_sweep_request(forced_sweep_request=forced_sweep_request)

Create forced sweep

This operation creates a forced sweep to transfer funds from addresses within a specified wallet to its designated sweep-to address. 

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

This operation creates a merchant and links it to a specified wallet. Payments to the merchant will be deposited into the linked wallet.  Upon successful creation, a merchant ID is generated and returned along with the merchant's information.  If you are a merchant (directly serving the payer), you only need to create one merchant and do not need to configure the developer fee rate. The developer fee rate only applies to platforms such as payment service providers (PSPs) that charge fees to their downstream merchants. 

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

# **delete_crypto_address**
> DeleteCryptoAddress201Response delete_crypto_address(crypto_address_id)

Delete crypto address

This operation unregisters a crypto address from being used for crypto withdrawals. 

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

# **get_exchange_rate**
> GetExchangeRate200Response get_exchange_rate(token_id, currency)

Get exchange rate

This operation retrieves the current exchange rate between a specified currency pair. 

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

# **get_payer_balance_by_address**
> List[ReceivedAmountPerAddress] get_payer_balance_by_address(merchant_id, payer_id, token_id)

Get payer balance

This operation retrieves the total amount received for a specific payer. The information is grouped by token and receiving address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.received_amount_per_address import ReceivedAmountPerAddress
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
    payer_id = 'P20250619T0310056d7aa'
    token_id = 'ETH_USDT'

    try:
        # Get payer balance
        api_response = api_instance.get_payer_balance_by_address(merchant_id, payer_id, token_id)
        print("The response of PaymentApi->get_payer_balance_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payer_balance_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The merchant ID. | 
 **payer_id** | **str**| Unique payer identifier on the Cobo side, auto-generated by the system. | 
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 

### Return type

[**List[ReceivedAmountPerAddress]**](ReceivedAmountPerAddress.md)

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

This operation retrieves the balance information for you as the developer. The balance information is grouped by token. 

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

This operation retrieves the balances of specified merchants or the developer. 

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
> TopUpAddress get_top_up_address(merchant_id, token_id, custom_payer_id)

Get top-up address

This operation retrieves the information of the dedicated top-up address assigned to a specific payer under a merchant on a specified chain. 

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
    merchant_id = 'M1001'
    token_id = 'ETH_USDT'
    custom_payer_id = 'payer_0001'

    try:
        # Get top-up address
        api_response = api_instance.get_top_up_address(merchant_id, token_id, custom_payer_id)
        print("The response of PaymentApi->get_top_up_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_top_up_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The merchant ID. | 
 **token_id** | **str**| The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. Supported values include:   - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDCOIN&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC2&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
 **custom_payer_id** | **str**| A unique identifier assigned by the developer to track and identify individual payers in their system. | 

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

# **list_crypto_addresses**
> List[CryptoAddress] list_crypto_addresses(token_id=token_id)

List crypto addresses

This operation retrieves a list of crypto addresses registered for crypto withdrawal.   Contact our support team at [help@cobo.com](mailto:help@cobo.com) to register a new crypto address. 

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

# **list_forced_sweep_requests**
> ListForcedSweepRequests200Response list_forced_sweep_requests(limit=limit, before=before, after=after, request_id=request_id)

List forced sweeps

This operation retrieves the information of all forced sweeps. 

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

This operation retrieves the balance information for specified merchants. The balance information is grouped by token and acquiring type. If you do not specify the `merchant_ids` parameter, the balance information for all merchants will be returned. 

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
> ListMerchants200Response list_merchants(limit=limit, before=before, after=after, keyword=keyword, wallet_id=wallet_id)

List all merchants

This operation retrieves the information of all merchants.   You can filter the results by using a keyword for fuzzy search on merchant names or by specifying a wallet ID. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_merchants200_response import ListMerchants200Response
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

    try:
        # List all merchants
        api_response = api_instance.list_merchants(limit=limit, before=before, after=after, keyword=keyword, wallet_id=wallet_id)
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
 **wallet_id** | **str**| The wallet ID. | [optional] 

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

This operation retrieves the balance information for specified payment wallets. The balance information is grouped by token. If you do not specify the `wallet_ids` parameter, the balance information for all payment wallets will be returned. 

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

# **list_top_up_payers**
> ListTopUpPayers200Response list_top_up_payers(merchant_id, limit=limit, before=before, after=after, payer_id=payer_id)

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
    merchant_id = 'M1001'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    payer_id = 'P20250619T0310056d7aa'

    try:
        # List payers
        api_response = api_instance.list_top_up_payers(merchant_id, limit=limit, before=before, after=after, payer_id=payer_id)
        print("The response of PaymentApi->list_top_up_payers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->list_top_up_payers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| The merchant ID. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
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

This operation updates the dedicated top-up address assigned to a specific payer under a merchant on a specified chain. 

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

