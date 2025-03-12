# cobo_waas2.WalletsSmartContractWalletsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_safe_wallet_delegates**](WalletsSmartContractWalletsApi.md#list_safe_wallet_delegates) | **POST** /wallets/{wallet_id}/smart_contracts/delegates | List Delegates


# **list_safe_wallet_delegates**
> List[CoboSafeDelegate] list_safe_wallet_delegates(wallet_id, safe_wallet_delegates=safe_wallet_delegates)

List Delegates

This operation retrieves all available Delegates of a Safe\\{Wallet\\} for a given transfer or contract call request. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.cobo_safe_delegate import CoboSafeDelegate
from cobo_waas2.models.safe_wallet_delegates import SafeWalletDelegates
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
    api_instance = cobo_waas2.WalletsSmartContractWalletsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    safe_wallet_delegates = cobo_waas2.SafeWalletDelegates()

    try:
        # List Delegates
        api_response = api_instance.list_safe_wallet_delegates(wallet_id, safe_wallet_delegates=safe_wallet_delegates)
        print("The response of WalletsSmartContractWalletsApi->list_safe_wallet_delegates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsSmartContractWalletsApi->list_safe_wallet_delegates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **safe_wallet_delegates** | [**SafeWalletDelegates**](SafeWalletDelegates.md)| The request body to query the Delegates of a Safe{Wallet}. | [optional] 

### Return type

[**List[CoboSafeDelegate]**](CoboSafeDelegate.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Delegates successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

