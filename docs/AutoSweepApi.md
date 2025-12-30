# cobo_waas2.AutoSweepApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_sweep_task**](AutoSweepApi.md#create_auto_sweep_task) | **POST** /auto_sweep/tasks | Create auto-sweep task
[**create_wallet_sweep_to_addresses**](AutoSweepApi.md#create_wallet_sweep_to_addresses) | **POST** /auto_sweep/sweep_to_addresses | Create sweep-to address
[**get_auto_sweep_task_by_id**](AutoSweepApi.md#get_auto_sweep_task_by_id) | **GET** /auto_sweep/tasks/{task_id} | Get auto-sweep task details
[**list_auto_sweep_task**](AutoSweepApi.md#list_auto_sweep_task) | **GET** /auto_sweep/tasks | List auto-sweep tasks
[**list_wallet_sweep_to_addresses**](AutoSweepApi.md#list_wallet_sweep_to_addresses) | **GET** /auto_sweep/sweep_to_addresses | List sweep-to addresses


# **create_auto_sweep_task**
> AutoSweepTask create_auto_sweep_task(create_auto_sweep_task=create_auto_sweep_task)

Create auto-sweep task

This operation creates an auto-sweep task for the specified wallet and token. The task triggers transactions to sweep the full balance of the specified token to the configured sweep-to address. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.auto_sweep_task import AutoSweepTask
from cobo_waas2.models.create_auto_sweep_task import CreateAutoSweepTask
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
    api_instance = cobo_waas2.AutoSweepApi(api_client)
    create_auto_sweep_task = cobo_waas2.CreateAutoSweepTask()

    try:
        # Create auto-sweep task
        api_response = api_instance.create_auto_sweep_task(create_auto_sweep_task=create_auto_sweep_task)
        print("The response of AutoSweepApi->create_auto_sweep_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->create_auto_sweep_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auto_sweep_task** | [**CreateAutoSweepTask**](CreateAutoSweepTask.md)| The request body to create an auto-sweep task. | [optional] 

### Return type

[**AutoSweepTask**](AutoSweepTask.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created auto-sweep task. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_sweep_to_addresses**
> SweepToAddress create_wallet_sweep_to_addresses(create_sweep_to_address=create_sweep_to_address)

Create sweep-to address

This operation creates a new sweep-to address for the specified wallet. The previously sweep-to address for the same token becomes invalid once the new one is created.  Use this operation to change the sweep-to address when your setup changes, you switch networks, or the current address is compromised or tainted by suspicious funds. You can withdraw any remaining balances from the old sweep-to addresses to the new address or another designated destination.  <Note>Sweep-to addresses are only applicable to MPC Wallets and Custodial Wallets (Web3 Wallets) with the auto-sweep feature enabled.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_sweep_to_address import CreateSweepToAddress
from cobo_waas2.models.sweep_to_address import SweepToAddress
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
    api_instance = cobo_waas2.AutoSweepApi(api_client)
    create_sweep_to_address = cobo_waas2.CreateSweepToAddress()

    try:
        # Create sweep-to address
        api_response = api_instance.create_wallet_sweep_to_addresses(create_sweep_to_address=create_sweep_to_address)
        print("The response of AutoSweepApi->create_wallet_sweep_to_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->create_wallet_sweep_to_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sweep_to_address** | [**CreateSweepToAddress**](CreateSweepToAddress.md)| The request body to generates a new sweep-to address within a specified wallet. | [optional] 

### Return type

[**SweepToAddress**](SweepToAddress.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully create sweep to addresses |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_sweep_task_by_id**
> AutoSweepTask get_auto_sweep_task_by_id(task_id)

Get auto-sweep task details

This operation retrieves detailed information about a specified auto-sweep task. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.auto_sweep_task import AutoSweepTask
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
    api_instance = cobo_waas2.AutoSweepApi(api_client)
    task_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get auto-sweep task details
        api_response = api_instance.get_auto_sweep_task_by_id(task_id)
        print("The response of AutoSweepApi->get_auto_sweep_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->get_auto_sweep_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The auto sweep task ID. | 

### Return type

[**AutoSweepTask**](AutoSweepTask.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about a auto-sweep task. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_sweep_task**
> ListAutoSweepTask200Response list_auto_sweep_task(wallet_id, token_id=token_id, task_ids=task_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)

List auto-sweep tasks

This operation retrieves a list of auto-sweep tasks for the specified wallet. You can filter the results by token ID, task IDs, or a created-time range. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_auto_sweep_task200_response import ListAutoSweepTask200Response
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
    api_instance = cobo_waas2.AutoSweepApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    task_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,1ddca562-8434-41c9-8809-d437bad9c868'
    min_created_timestamp = 1635744000000
    max_created_timestamp = 1635744000000
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    direction = 'ASC'

    try:
        # List auto-sweep tasks
        api_response = api_instance.list_auto_sweep_task(wallet_id, token_id=token_id, task_ids=task_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)
        print("The response of AutoSweepApi->list_auto_sweep_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->list_auto_sweep_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **task_ids** | **str**| A list of auto-sweep task IDs, separated by comma. | [optional] 
 **min_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or after the specified time.  If not provided, the default value is 90 days before the current time. This default value is subject to change.  | [optional] 
 **max_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or before the specified time.  If not provided, the default value is the current time. This default value is subject to change.  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListAutoSweepTask200Response**](ListAutoSweepTask200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved auto-sweep tasks |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallet_sweep_to_addresses**
> ListWalletSweepToAddresses200Response list_wallet_sweep_to_addresses(wallet_id)

List sweep-to addresses

This operation retrieves a list of sweep-to addresses within your wallet.  <Note>Sweep-to addresses are only applicable to MPC Wallets and Custodial Wallets (Web3 Wallets) with the auto-sweep feature enabled.</Note>  <Info>For EVM-compatible chains (such as Ethereum and BNB Smart Chain), the same address is used across chains. As a result, when listing sweep-to addresses, only one address entry (shown under Ethereum) is returned for all EVM-compatible chains. Separate entries are not returned for each individual EVM chain.</Info> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_wallet_sweep_to_addresses200_response import ListWalletSweepToAddresses200Response
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
    api_instance = cobo_waas2.AutoSweepApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # List sweep-to addresses
        api_response = api_instance.list_wallet_sweep_to_addresses(wallet_id)
        print("The response of AutoSweepApi->list_wallet_sweep_to_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->list_wallet_sweep_to_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 

### Return type

[**ListWalletSweepToAddresses200Response**](ListWalletSweepToAddresses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved sweep-to addresses |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

