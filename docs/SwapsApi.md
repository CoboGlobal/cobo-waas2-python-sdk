# cobo_waas2.SwapsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_swap_activity**](SwapsApi.md#create_swap_activity) | **POST** /swaps/swap | Create Swap Activity
[**estimate_swap_fee**](SwapsApi.md#estimate_swap_fee) | **POST** /swaps/estimate_fee | Estimate Swap Fee
[**get_swap_activity**](SwapsApi.md#get_swap_activity) | **GET** /swaps/activities/{activity_id} | Get Swap Activity Details
[**get_swap_quote**](SwapsApi.md#get_swap_quote) | **GET** /swaps/quote | Get Current Swap Rate
[**list_swap_activities**](SwapsApi.md#list_swap_activities) | **GET** /swaps/activities | List Swap Activities
[**list_swap_enabled_tokens**](SwapsApi.md#list_swap_enabled_tokens) | **GET** /swaps/enabled_tokens | List Enabled Tokens


# **create_swap_activity**
> SwapActivityDetail create_swap_activity(create_swap_activity_request)

Create Swap Activity

This operation to create a swap activity. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_swap_activity_request import CreateSwapActivityRequest
from cobo_waas2.models.swap_activity_detail import SwapActivityDetail
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    create_swap_activity_request = cobo_waas2.CreateSwapActivityRequest()

    try:
        # Create Swap Activity
        api_response = api_instance.create_swap_activity(create_swap_activity_request)
        print("The response of SwapsApi->create_swap_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->create_swap_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_swap_activity_request** | [**CreateSwapActivityRequest**](CreateSwapActivityRequest.md)| The request body for creating a swap activity. | 

### Return type

[**SwapActivityDetail**](SwapActivityDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The swap activity details have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_swap_fee**
> EstimatedFee estimate_swap_fee(swap_estimate_fee)

Estimate Swap Fee

This operation to estimate the fee of a swap activity. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.estimated_fee import EstimatedFee
from cobo_waas2.models.swap_estimate_fee import SwapEstimateFee
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    swap_estimate_fee = cobo_waas2.SwapEstimateFee()

    try:
        # Estimate Swap Fee
        api_response = api_instance.estimate_swap_fee(swap_estimate_fee)
        print("The response of SwapsApi->estimate_swap_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->estimate_swap_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swap_estimate_fee** | [**SwapEstimateFee**](SwapEstimateFee.md)| The request body for estimating the fee of a swap activity. | 

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
**201** | Successfully retrieved the estimated fee for swap activity. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_activity**
> SwapActivityDetail get_swap_activity(activity_id)

Get Swap Activity Details

This operation retrieves the details of a swap activity. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.swap_activity_detail import SwapActivityDetail
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    activity_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get Swap Activity Details
        api_response = api_instance.get_swap_activity(activity_id)
        print("The response of SwapsApi->get_swap_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->get_swap_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| The unique id of the activity. | 

### Return type

[**SwapActivityDetail**](SwapActivityDetail.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The swap activity details have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_quote**
> SwapQuote get_swap_quote(wallet_id, pay_token_id, receive_token_id, pay_amount=pay_amount, receive_amount=receive_amount)

Get Current Swap Rate

This operation retrieves the current market exchange rate and estimated amount for swapping between two tokens. Either pay_amount or receive_amount must be provided. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.swap_quote import SwapQuote
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    pay_token_id = 'ETH'
    receive_token_id = 'USDT'
    pay_amount = '1.5'
    receive_amount = '2000'

    try:
        # Get Current Swap Rate
        api_response = api_instance.get_swap_quote(wallet_id, pay_token_id, receive_token_id, pay_amount=pay_amount, receive_amount=receive_amount)
        print("The response of SwapsApi->get_swap_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->get_swap_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID. | 
 **pay_token_id** | **str**| Unique id of the token to pay. | 
 **receive_token_id** | **str**| Unique id of the token to receive. | 
 **pay_amount** | **str**| The amount of pay token. | [optional] 
 **receive_amount** | **str**| The amount of token to receive. | [optional] 

### Return type

[**SwapQuote**](SwapQuote.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The swap quote has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_swap_activities**
> ListSwapActivities200Response list_swap_activities(type=type, status=status, min_updated_timestamp=min_updated_timestamp, max_updated_timestamp=max_updated_timestamp, initiator=initiator, limit=limit, before=before, after=after, sort_by=sort_by, direction=direction)

List Swap Activities

This operation retrieves a list of swap activities. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_swap_activities200_response import ListSwapActivities200Response
from cobo_waas2.models.swap_activity_status import SwapActivityStatus
from cobo_waas2.models.swap_type import SwapType
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    type = cobo_waas2.SwapType()
    status = cobo_waas2.SwapActivityStatus()
    min_updated_timestamp = 1635744000000
    max_updated_timestamp = 1635744000000
    initiator = 'steve@example.com'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    sort_by = 'created_timestamp'
    direction = 'ASC'

    try:
        # List Swap Activities
        api_response = api_instance.list_swap_activities(type=type, status=status, min_updated_timestamp=min_updated_timestamp, max_updated_timestamp=max_updated_timestamp, initiator=initiator, limit=limit, before=before, after=after, sort_by=sort_by, direction=direction)
        print("The response of SwapsApi->list_swap_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->list_swap_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**SwapType**](.md)|  | [optional] 
 **status** | [**SwapActivityStatus**](.md)|  | [optional] 
 **min_updated_timestamp** | **int**| The start time of the query. All staking activities updated after the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **max_updated_timestamp** | **int**| The end time of the query. All staking activities updated before the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **initiator** | **str**| The activity initiator, which is your API key by default. You can also specify the initiator when creating the activity. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 
 **sort_by** | **str**| The field to sort the results by.   Possible values include: - &#x60;created_timestamp&#x60;: Sort by the time when the data was created. - &#x60;updated_timestamp&#x60;: Sort by the time when the data was last updated.  | [optional] 
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListSwapActivities200Response**](ListSwapActivities200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of swap activities have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_swap_enabled_tokens**
> ListSwapEnabledTokens200Response list_swap_enabled_tokens(type=type, asset_id=asset_id, chain_id=chain_id, limit=limit, before=before, after=after)

List Enabled Tokens

This operation retrieves all enabled tokens for swaps.   

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_swap_enabled_tokens200_response import ListSwapEnabledTokens200Response
from cobo_waas2.models.swap_type import SwapType
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
    api_instance = cobo_waas2.SwapsApi(api_client)
    type = cobo_waas2.SwapType()
    asset_id = 'USDT'
    chain_id = 'ETH'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Enabled Tokens
        api_response = api_instance.list_swap_enabled_tokens(type=type, asset_id=asset_id, chain_id=chain_id, limit=limit, before=before, after=after)
        print("The response of SwapsApi->list_swap_enabled_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->list_swap_enabled_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**SwapType**](.md)|  | [optional] 
 **asset_id** | **str**| (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListSwapEnabledTokens200Response**](ListSwapEnabledTokens200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of enabled tokens have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

