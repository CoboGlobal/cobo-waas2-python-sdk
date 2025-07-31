# cobo_waas2.AutoSweepApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_sweep_to_addresses**](AutoSweepApi.md#create_wallet_sweep_to_addresses) | **POST** /auto_sweep/sweep_to_addresses | create wallet sweep to addresses
[**list_wallet_sweep_to_addresses**](AutoSweepApi.md#list_wallet_sweep_to_addresses) | **GET** /auto_sweep/sweep_to_addresses | List wallet sweep to addresses


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

