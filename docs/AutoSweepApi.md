# cobo_waas2.AutoSweepApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_sweep_task**](AutoSweepApi.md#create_auto_sweep_task) | **POST** /auto_sweep/tasks | create auto sweep task
[**create_wallet_sweep_to_addresses**](AutoSweepApi.md#create_wallet_sweep_to_addresses) | **POST** /auto_sweep/sweep_to_addresses | create wallet sweep to addresses
[**get_auto_sweep_task_by_id**](AutoSweepApi.md#get_auto_sweep_task_by_id) | **GET** /auto_sweep/tasks/{task_id} | Get auto sweep task information
[**list_auto_sweep_task**](AutoSweepApi.md#list_auto_sweep_task) | **GET** /auto_sweep/tasks | List wallet auto sweep task
[**list_wallet_sweep_to_addresses**](AutoSweepApi.md#list_wallet_sweep_to_addresses) | **GET** /auto_sweep/sweep_to_addresses | List wallet sweep to addresses


# **create_auto_sweep_task**
> AutoSweepTask create_auto_sweep_task(create_auto_sweep_task=create_auto_sweep_task)

create auto sweep task

This operation create a new auto sweep task. 

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
        # create auto sweep task
        api_response = api_instance.create_auto_sweep_task(create_auto_sweep_task=create_auto_sweep_task)
        print("The response of AutoSweepApi->create_auto_sweep_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->create_auto_sweep_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auto_sweep_task** | [**CreateAutoSweepTask**](CreateAutoSweepTask.md)| The request body to generates a new sweep to addresses within a specified wallet. | [optional] 

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
**201** | Successfully create auto sweep task |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet_sweep_to_addresses**
> SweepToAddress create_wallet_sweep_to_addresses(create_sweep_to_address=create_sweep_to_address)

create wallet sweep to addresses

This operation create a new sweep to address for the wallet. The old sweep to address will become invalid. 

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
        # create wallet sweep to addresses
        api_response = api_instance.create_wallet_sweep_to_addresses(create_sweep_to_address=create_sweep_to_address)
        print("The response of AutoSweepApi->create_wallet_sweep_to_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSweepApi->create_wallet_sweep_to_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sweep_to_address** | [**CreateSweepToAddress**](CreateSweepToAddress.md)| The request body to generates a new sweep to addresses within a specified wallet. | [optional] 

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

Get auto sweep task information

This operation retrieves detailed information about a specified auto sweep task. 

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
        # Get auto sweep task information
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
**200** | The information about a auto sweep task. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_sweep_task**
> ListAutoSweepTask200Response list_auto_sweep_task(wallet_id, token_id=token_id, task_ids=task_ids, min_created_timestamp=min_created_timestamp, max_created_timestamp=max_created_timestamp, limit=limit, before=before, after=after, direction=direction)

List wallet auto sweep task

This operation retrieves a list of auto sweep task. 

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
        # List wallet auto sweep task
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
 **task_ids** | **str**| A list of auto sweep task IDs, separated by comma. | [optional] 
 **min_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or after the specified time. | [optional] 
 **max_created_timestamp** | **int**| The time when the transaction was created, in Unix timestamp format, measured in milliseconds. You can use this parameter to filter transactions created on or before the specified time. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 
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
**200** | Successfully listed auto sweep tasks |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallet_sweep_to_addresses**
> ListWalletSweepToAddresses200Response list_wallet_sweep_to_addresses(wallet_id)

List wallet sweep to addresses

This operation retrieves a list of sweep to addresses within your wallet. 

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
        # List wallet sweep to addresses
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
**200** | Successfully listed sweep to addresses |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

