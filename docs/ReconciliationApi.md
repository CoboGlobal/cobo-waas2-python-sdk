# cobo_waas2.ReconciliationApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reconciliation_ledger**](ReconciliationApi.md#get_reconciliation_ledger) | **GET** /recon/ledger | Get reconciliation ledger
[**list_reconciliation_statements**](ReconciliationApi.md#list_reconciliation_statements) | **GET** /recon/statements | List reconciliation daily statements


# **get_reconciliation_ledger**
> GetReconciliationLedger200Response get_reconciliation_ledger(transaction_ids)

Get reconciliation ledger

This operation retrieves the post-transaction balance (running balance) for the specified transactions, used for stablecoin deposit and withdrawal reconciliation.  You need to provide the transaction IDs in `transaction_ids`. Each returned entry includes the signed amount and the resulting balance of the address after the transaction, expressed in the token's main unit.  <Note>This operation is available to selected customers only. To request access, please contact Cobo.</Note>  <Note>This operation is applicable to MPC Wallets and Custodial Web3 Wallets only, and covers stablecoins only. To ensure accurate reconciliation results, do not use the contract call and message signing features. Currently, only stablecoins on the Ethereum and TRON chains are supported.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_reconciliation_ledger200_response import GetReconciliationLedger200Response
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
    api_instance = cobo_waas2.ReconciliationApi(api_client)
    transaction_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,557918d2-632a-4fe1-932f-315711f05fe3'

    try:
        # Get reconciliation ledger
        api_response = api_instance.get_reconciliation_ledger(transaction_ids)
        print("The response of ReconciliationApi->get_reconciliation_ledger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationApi->get_reconciliation_ledger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_ids** | **str**| A list of transaction IDs, separated by comma. You can specify 1 to 100 transaction IDs. | 

### Return type

[**GetReconciliationLedger200Response**](GetReconciliationLedger200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reconciliation ledger entries (post-transaction balances). |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reconciliation_statements**
> ListReconciliationStatements200Response list_reconciliation_statements(start_date, end_date, wallet_ids=wallet_ids, token_ids=token_ids, limit=limit, before=before, after=after)

List reconciliation daily statements

This operation retrieves daily reconciliation statements within a date range. Each statement contains the opening balance, total deposits, total withdrawals, and closing balance for a business date, wallet, and token.  You need to specify the date range with `start_date` and `end_date`. You can filter the results by wallets and tokens, and paginate the query results. All amounts are expressed in the token's main unit.  <Note>This operation is available to selected customers only. To request access, please contact Cobo.</Note>  <Note>This operation is applicable to MPC Wallets and Custodial Web3 Wallets only, and covers stablecoins only. To ensure accurate reconciliation results, do not use the contract call and message signing features. Currently, only stablecoins on the Ethereum and TRON chains are supported.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_reconciliation_statements200_response import ListReconciliationStatements200Response
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
    api_instance = cobo_waas2.ReconciliationApi(api_client)
    start_date = '2026-07-01'
    end_date = '2026-07-28'
    wallet_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,1ddca562-8434-41c9-8809-d437bad9c868'
    token_ids = 'ETH_USDT,ETH_USDC'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List reconciliation daily statements
        api_response = api_instance.list_reconciliation_statements(start_date, end_date, wallet_ids=wallet_ids, token_ids=token_ids, limit=limit, before=before, after=after)
        print("The response of ReconciliationApi->list_reconciliation_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationApi->list_reconciliation_statements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| The start date of the reconciliation period (inclusive), in YYYY-MM-DD format (UTC). The range between &#x60;start_date&#x60; and &#x60;end_date&#x60; must not exceed 366 days. | 
 **end_date** | **date**| The end date of the reconciliation period (inclusive), in YYYY-MM-DD format (UTC). The range between &#x60;start_date&#x60; and &#x60;end_date&#x60; must not exceed 366 days. | 
 **wallet_ids** | **str**| A list of wallet IDs, separated by comma. | [optional] 
 **token_ids** | **str**| A list of token IDs, separated by comma. The token ID is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListReconciliationStatements200Response**](ListReconciliationStatements200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The daily reconciliation statements. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

