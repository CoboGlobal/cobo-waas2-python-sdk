# cobo_waas2.TransactionsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_signed_transactions**](TransactionsApi.md#broadcast_signed_transactions) | **POST** /transactions/broadcast | Broadcast signed transactions
[**cancel_transaction_by_id**](TransactionsApi.md#cancel_transaction_by_id) | **POST** /transactions/{transaction_id}/cancel | Cancel transaction
[**check_loop_transfers**](TransactionsApi.md#check_loop_transfers) | **GET** /transactions/check_loop_transfers | Check Cobo Loop transfers
[**create_contract_call_transaction**](TransactionsApi.md#create_contract_call_transaction) | **POST** /transactions/contract_call | Call smart contract
[**create_message_sign_transaction**](TransactionsApi.md#create_message_sign_transaction) | **POST** /transactions/message_sign | Sign message
[**create_transfer_transaction**](TransactionsApi.md#create_transfer_transaction) | **POST** /transactions/transfer | Transfer token
[**drop_transaction_by_id**](TransactionsApi.md#drop_transaction_by_id) | **POST** /transactions/{transaction_id}/drop | Drop transaction
[**estimate_fee**](TransactionsApi.md#estimate_fee) | **POST** /transactions/estimate_fee | Estimate transaction fee
[**get_transaction_approval_detail**](TransactionsApi.md#get_transaction_approval_detail) | **GET** /transactions/{transaction_id}/approval_detail | Get transaction approval details
[**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id) | **GET** /transactions/{transaction_id} | Get transaction information
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List all transactions
[**resend_transaction_by_id**](TransactionsApi.md#resend_transaction_by_id) | **POST** /transactions/{transaction_id}/resend | Resend transaction
[**sign_and_broadcast_transaction_by_id**](TransactionsApi.md#sign_and_broadcast_transaction_by_id) | **POST** /transactions/{transaction_id}/sign_and_broadcast | Sign and broadcast transaction
[**speedup_transaction_by_id**](TransactionsApi.md#speedup_transaction_by_id) | **POST** /transactions/{transaction_id}/speedup | Speed up transaction


# **broadcast_signed_transactions**
> List[BroadcastSignedTransactions201ResponseInner] broadcast_signed_transactions(broadcast_signed_transactions_request=broadcast_signed_transactions_request)

Broadcast signed transactions

<Note>This operation is only applicable to the staking scenarios.</Note> This operation broadcasts a list of signed transactions.   If you set `auto_broadcast` to `false` when [creating a staking activity](https://www.cobo.com/developers/v2/api-references/staking/create-stake-activity), the transaction will not be submitted to the blockchain automatically after being signed. In such cases, you can call this operation to broadcast the transaction to the blockchain.  A transaction can only be broadcast if its status is `Broadcasting`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.broadcast_signed_transactions201_response_inner import BroadcastSignedTransactions201ResponseInner
from cobo_waas2.models.broadcast_signed_transactions_request import BroadcastSignedTransactionsRequest
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    broadcast_signed_transactions_request = cobo_waas2.BroadcastSignedTransactionsRequest()

    try:
        # Broadcast signed transactions
        api_response = api_instance.broadcast_signed_transactions(broadcast_signed_transactions_request=broadcast_signed_transactions_request)
        print("The response of TransactionsApi->broadcast_signed_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->broadcast_signed_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_signed_transactions_request** | [**BroadcastSignedTransactionsRequest**](BroadcastSignedTransactionsRequest.md)| The request body to broadcast a list of signed transactions. | [optional] 

### Return type

[**List[BroadcastSignedTransactions201ResponseInner]**](BroadcastSignedTransactions201ResponseInner.md)

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

# **cancel_transaction_by_id**
> CreateTransferTransaction201Response cancel_transaction_by_id(transaction_id)

Cancel transaction

This operation cancels a specified transaction. Canceling a transaction stops it while it is still pending. For more information, see [Cancel a transaction](https://www.cobo.com/developers/v2/guides/transactions/manage-transactions#cancel-a-transaction).  <Note>This operation only applies to transactions from MPC Wallets and Smart Contract Wallets.</Note>  A transaction can be cancelled if its status is either of the following: - `Submitted` - `PendingScreening` - `PendingAuthorization` - `PendingSignature`  

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Cancel transaction
        api_response = api_instance.cancel_transaction_by_id(transaction_id)
        print("The response of TransactionsApi->cancel_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->cancel_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **check_loop_transfers**
> List[CheckLoopTransfers200ResponseInner] check_loop_transfers(token_id, source_wallet_id, destination_addresses)

Check Cobo Loop transfers

This operation verifies if the transactions from a given source wallet to a list of given destinations can be executed as Cobo Loop transfers.   For more information about Cobo Loop, see [Cobo Loop's product manuals](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.check_loop_transfers200_response_inner import CheckLoopTransfers200ResponseInner
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    token_id = 'ETH_USDT'
    source_wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    destination_addresses = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045,0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'

    try:
        # Check Cobo Loop transfers
        api_response = api_instance.check_loop_transfers(token_id, source_wallet_id, destination_addresses)
        print("The response of TransactionsApi->check_loop_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->check_loop_transfers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
 **source_wallet_id** | **str**| The wallet ID of the transaction source. | 
 **destination_addresses** | **str**| A list of destination addresses, separated by comma. | 

### Return type

[**List[CheckLoopTransfers200ResponseInner]**](CheckLoopTransfers200ResponseInner.md)

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

# **create_contract_call_transaction**
> CreateTransferTransaction201Response create_contract_call_transaction(contract_call_params=contract_call_params)

Call smart contract

This operation creates a transaction to interact with a smart contract on the blockchain.  You need to provide details such as the source address, destination address, and the calldata. You can specify the fee-related properties to limit the transaction fee. A transaction request for tracking is returned upon successful operation.  <Note>Currently, this operation only applies to the transactions from MPC Wallets or Smart Contract Wallets on the blockchains that have a similar architecture to Ethereum.</Note>  <Info>If you initiate a transaction from a Smart Contract Wallet, a relevant transaction will be triggered from the Delegate to the Cobo Safe's address of the Smart Contract Wallet, with a transfer amount of <code>0</code>.</Info> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.contract_call_params import ContractCallParams
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    contract_call_params = cobo_waas2.ContractCallParams()

    try:
        # Call smart contract
        api_response = api_instance.create_contract_call_transaction(contract_call_params=contract_call_params)
        print("The response of TransactionsApi->create_contract_call_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_contract_call_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_call_params** | [**ContractCallParams**](ContractCallParams.md)| The request body for making a contract call. | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **create_message_sign_transaction**
> CreateTransferTransaction201Response create_message_sign_transaction(message_sign_params=message_sign_params)

Sign message

This operation creates a transaction to sign the provided message using cryptographic techniques.  In some scenarios, you want to sign a message for identity authentication or transaction approval. You need to provide details such as the source address, destination address, and the message to be signed. A transaction request for tracking is returned upon successful operation.  You can get the signature result by calling [Get transaction information](https://www.cobo.com/developers/v2/api-references/transactions/get-transaction-information).   <Note>This operation only applies to transactions from MPC Wallets.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.message_sign_params import MessageSignParams
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    message_sign_params = cobo_waas2.MessageSignParams()

    try:
        # Sign message
        api_response = api_instance.create_message_sign_transaction(message_sign_params=message_sign_params)
        print("The response of TransactionsApi->create_message_sign_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_message_sign_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_sign_params** | [**MessageSignParams**](MessageSignParams.md)| The request body to create a message signing transaction | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **create_transfer_transaction**
> CreateTransferTransaction201Response create_transfer_transaction(transfer_params=transfer_params)

Transfer token

The operation transfers your assets from a wallet created on Cobo Portal to another address.  You need to specify details such as the sender address and recipient address, token ID, and the amount to transfer. You can specify the fee-related properties to limit the transaction fee. A transaction request for tracking is returned upon successful operation.  <Note>If you make transfers from Custodial Wallets (Asset Wallets) and Exchange Wallets, do not set the fee-related properties, as they will not take effects.</Note>  <Note>You can transfer tokens to multiple addresses only if you use MPC Wallets as the transaction source. You should use the <code>utxo_outputs</code> property to specify the destination addresses.</Note>  <Info>If you initiate a transaction from a Smart Contract Wallet, a relevant transaction will be triggered from the Delegate to the Cobo Safe's address of the Smart Contract Wallet, with a transfer amount of <code>0</code>.</Info> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.transfer_params import TransferParams
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transfer_params = cobo_waas2.TransferParams()

    try:
        # Transfer token
        api_response = api_instance.create_transfer_transaction(transfer_params=transfer_params)
        print("The response of TransactionsApi->create_transfer_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transfer_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_params** | [**TransferParams**](TransferParams.md)| The request body to create a transfer transaction | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **drop_transaction_by_id**
> CreateTransferTransaction201Response drop_transaction_by_id(transaction_id, transaction_rbf=transaction_rbf)

Drop transaction

This operation drops a specified transaction. Dropping a transaction leverages RBF to replace the original transaction with a version that effectively cancels it. For more details about dropping a transaction, refer to [Drop a transaction](https://www.cobo.com/developers/v2/guides/transactions/manage-transactions#drop-a-transaction).  A transaction can be sped up only if its status is `Broadcasting`.  <Note>This operation only applies to transactions from MPC Wallets and Smart Contract Wallets. It does not apply to transactions on the following chains: VET, TRON, TVET, SOL, and TON.</Note>  You can use the `address` or `included_utxos` properties in the request body to specify the address or UTXOs that will cover the transaction fee. Generally, the transaction fee is paid by the original transaction's source. If that source's balance is insufficient, the specified address or UTXOs can be used to cover the fee. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.transaction_rbf import TransactionRbf
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    transaction_rbf = cobo_waas2.TransactionRbf()

    try:
        # Drop transaction
        api_response = api_instance.drop_transaction_by_id(transaction_id, transaction_rbf=transaction_rbf)
        print("The response of TransactionsApi->drop_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->drop_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 
 **transaction_rbf** | [**TransactionRbf**](TransactionRbf.md)| The request body to drop or to speed up transactions | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **estimate_fee**
> EstimatedFee estimate_fee(estimate_fee_params=estimate_fee_params)

Estimate transaction fee

This operation estimates the transaction fee of a token transfer or a contract call based on the fee model that the chain uses, considering factors such as network congestion and transaction complexity.  You need to specify the transaction information, including the request ID, request type, source address, destination address, token ID (only applicable to token transfers), and chain ID (only applicable to contract calls).  The response can contain different properties based on the transaction fee model used by the chain. For the legacy, EIP-1559, and UTXO fee models, Cobo also supports three different transaction speed levels: slow, recommended, and fast. For more information about estimating transaction fees, refer to [Estimate transaction fee](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.estimate_fee_params import EstimateFeeParams
from cobo_waas2.models.estimated_fee import EstimatedFee
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    estimate_fee_params = cobo_waas2.EstimateFeeParams()

    try:
        # Estimate transaction fee
        api_response = api_instance.estimate_fee(estimate_fee_params=estimate_fee_params)
        print("The response of TransactionsApi->estimate_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->estimate_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_fee_params** | [**EstimateFeeParams**](EstimateFeeParams.md)| The request body to estimate the transaction fee of a token transfer or a contract call. | [optional] 

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
**201** | The request was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_approval_detail**
> TransactionApprovalDetail get_transaction_approval_detail(transaction_id)

Get transaction approval details

This operation retrieves approval detailed information about a specified transaction. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.transaction_approval_detail import TransactionApprovalDetail
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get transaction approval details
        api_response = api_instance.get_transaction_approval_detail(transaction_id)
        print("The response of TransactionsApi->get_transaction_approval_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_approval_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 

### Return type

[**TransactionApprovalDetail**](TransactionApprovalDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about a transaction approval detail. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionDetail get_transaction_by_id(transaction_id)

Get transaction information

This operation retrieves detailed information about a specified transaction, such as the transaction status, source address, destination address, and timestamp. 

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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get transaction information
        api_response = api_instance.get_transaction_by_id(transaction_id)
        print("The response of TransactionsApi->get_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
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

# **list_transactions**
> ListTransactions200Response list_transactions(request_id=request_id, cobo_ids=cobo_ids, transaction_ids=transaction_ids, transaction_hashes=transaction_hashes, types=types, statuses=statuses, wallet_ids=wallet_ids, chain_ids=chain_ids, token_ids=token_ids, asset_ids=asset_ids, vault_id=vault_id, project_id=project_id, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after)

List all transactions

This operation retrieves all the transactions under your organization.  You can filter the results by request ID, Cobo ID, transaction ID, transaction hash, type, status, and timestamps. You can also paginate and sort your query results. 

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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    request_id = 'web_send_by_user_327_1610444045047'
    cobo_ids = '20231213122855000000000000000000,20231213122955000000000000000000'
    transaction_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,557918d2-632a-4fe1-932f-315711f05fe3'
    transaction_hashes = '239861be9a4afe080c359b7fe4a1d035945ec46256b1a0f44d1267c71de8ec28'
    types = 'Deposit,Withdrawal'
    statuses = 'Completed,Failed'
    wallet_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,1ddca562-8434-41c9-8809-d437bad9c868'
    chain_ids = 'BTC,ETH'
    token_ids = 'ETH_USDT,ETH_USDC'
    asset_ids = 'USDT,USDC'
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    min_created_timestamp = 1635744000000
    max_created_timestamp = 1635744000000
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all transactions
        api_response = api_instance.list_transactions(request_id=request_id, cobo_ids=cobo_ids, transaction_ids=transaction_ids, transaction_hashes=transaction_hashes, types=types, statuses=statuses, wallet_ids=wallet_ids, chain_ids=chain_ids, token_ids=token_ids, asset_ids=asset_ids, vault_id=vault_id, project_id=project_id, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after)
        print("The response of TransactionsApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
 **cobo_ids** | **str**| A list of Cobo IDs, separated by comma. A Cobo ID can be used to track a transaction. | [optional] 
 **transaction_ids** | **str**| A list of transaction IDs, separated by comma. | [optional] 
 **transaction_hashes** | **str**| A list of transaction hashes, separated by comma. | [optional] 
 **types** | **str**| A list of transaction types, separated by comma. Possible values include:    - &#x60;Deposit&#x60;: A deposit transaction.   - &#x60;Withdrawal&#x60;: A withdrawal transaction.   - &#x60;ContractCall&#x60;: A transaction that interacts with a smart contract.   - &#x60;MessageSign&#x60;: A transaction that signs a message.    - &#x60;ExternalSafeTx&#x60;: A transaction to a Smart Contract Wallet (Safe{Wallet}) that requires one or multiple signatures to be executed.   - &#x60;Stake&#x60;: A transaction that creates a staking request.   - &#x60;Unstake&#x60;: A transaction that creates a unstaking request.  | [optional] 
 **statuses** | **str**| A list of transaction statuses, separated by comma. Possible values include:    - &#x60;Submitted&#x60;: The transaction is submitted.   - &#x60;PendingScreening&#x60;: The transaction is pending screening by Risk Control.    - &#x60;PendingAuthorization&#x60;: The transaction is pending approvals.   - &#x60;PendingSignature&#x60;: The transaction is pending signature.    - &#x60;Broadcasting&#x60;: The transaction is being broadcast.   - &#x60;Confirming&#x60;: The transaction is waiting for the required number of confirmations.   - &#x60;Completed&#x60;: The transaction is completed.   - &#x60;Failed&#x60;: The transaction failed.   - &#x60;Rejected&#x60;: The transaction is rejected.   - &#x60;Pending&#x60;: The transaction is waiting to be included in the next block of the blockchain.  | [optional] 
 **wallet_ids** | **str**| A list of wallet IDs, separated by comma. | [optional] 
 **chain_ids** | **str**| A list of chain IDs, separated by comma. The chain ID is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **asset_ids** | **str**| (This concept applies to Exchange Wallets only) A list of asset IDs, separated by comma. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-vaults). | [optional] 
 **project_id** | **str**| The project ID, which you can retrieve by calling [List all projects](https://www.cobo.com/developers/v2/api-references/wallets--mpc-wallets/list-all-projects).  | [optional] 
 **min_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or after the specified time. | [optional] 
 **max_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or before the specified time. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

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

# **resend_transaction_by_id**
> CreateTransferTransaction201Response resend_transaction_by_id(transaction_id, transaction_resend=transaction_resend)

Resend transaction

This operation resends a specified transaction. Resending a transaction means retrying a previously failed transaction. For more details about resending a transaction, see [Resend a transaction](https://www.cobo.com/developers/v2/guides/transactions/manage-transactions#resend-a-transaction).  A transaction can be resent if its status is `failed`.  <Note>This operation only applies to transactions from MPC Wallets in the SOL token.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.transaction_resend import TransactionResend
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    transaction_resend = cobo_waas2.TransactionResend()

    try:
        # Resend transaction
        api_response = api_instance.resend_transaction_by_id(transaction_id, transaction_resend=transaction_resend)
        print("The response of TransactionsApi->resend_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->resend_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 
 **transaction_resend** | [**TransactionResend**](TransactionResend.md)| The request body to resend transactions | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **sign_and_broadcast_transaction_by_id**
> CreateTransferTransaction201Response sign_and_broadcast_transaction_by_id(transaction_id)

Sign and broadcast transaction

This operation signs and broadcasts a specified transaction.  To call this operation, the following conditions must be met: - The `transaction_process_type` of the transaction must be set to `BuildOnly` when you call the [Transfer token](https://www.cobo.com/developers/v2/api-references/transactions/transfer-token) or [Call smart contract](https://www.cobo.com/developers/v2/api-references/transactions/call-smart-contract) operation.   - The transaction status must be `Built`. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Sign and broadcast transaction
        api_response = api_instance.sign_and_broadcast_transaction_by_id(transaction_id)
        print("The response of TransactionsApi->sign_and_broadcast_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->sign_and_broadcast_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

# **speedup_transaction_by_id**
> CreateTransferTransaction201Response speedup_transaction_by_id(transaction_id, transaction_rbf=transaction_rbf)

Speed up transaction

This operation accelerates a specified transaction. Speeding up a transaction will trigger a Replace-By-Fee (RBF) transaction which is a new version of the original transaction. For more details about speeding up a transaction, refer to [Speed up a transaction](https://www.cobo.com/developers/v2/guides/transactions/manage-transactions#speed-up-a-transaction).  You can use the `address` or `included_utxos` properties in the request body to specify the address or UTXOs that will cover the transaction fee. Generally, the transaction fee is paid by the original transaction's source. If that source's balance is insufficient, the specified address or UTXOs can be used to cover the fee.  A transaction can be sped up only if its status is `Broadcasting`.  <Note>This operation only applies to transactions from MPC Wallets and Smart Contract Wallets. It does not apply to transactions on the following chains: VET, TRON, TVET, SOL, and TON.</Note>  <Info>If you speed up a transaction from a Smart Contract Wallet, two RBF transactions will be triggered, one for the transaction from the Smart Contract Wallet, and the other for the transaction from the Delegate.</Info> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_transfer_transaction201_response import CreateTransferTransaction201Response
from cobo_waas2.models.transaction_rbf import TransactionRbf
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
    api_instance = cobo_waas2.TransactionsApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    transaction_rbf = cobo_waas2.TransactionRbf()

    try:
        # Speed up transaction
        api_response = api_instance.speedup_transaction_by_id(transaction_id, transaction_rbf=transaction_rbf)
        print("The response of TransactionsApi->speedup_transaction_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->speedup_transaction_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction ID. | 
 **transaction_rbf** | [**TransactionRbf**](TransactionRbf.md)| The request body to drop or to speed up transactions | [optional] 

### Return type

[**CreateTransferTransaction201Response**](CreateTransferTransaction201Response.md)

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

