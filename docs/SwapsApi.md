# cobo_waas2.SwapsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_swap_activity**](SwapsApi.md#create_swap_activity) | **POST** /swaps/swap | Create Swap Activity
[**create_swap_quote**](SwapsApi.md#create_swap_quote) | **POST** /swaps/quote | Create Swap Quote
[**get_swap_activity**](SwapsApi.md#get_swap_activity) | **GET** /swaps/activities/{activity_id} | Get Swap Activity Details
[**get_swap_quote**](SwapsApi.md#get_swap_quote) | **GET** /swaps/quote | Get Current Swap Rate
[**list_enable_token_pairs**](SwapsApi.md#list_enable_token_pairs) | **GET** /swaps/enabled_pairs | List Supported Token Pairs
[**list_swap_activities**](SwapsApi.md#list_swap_activities) | **GET** /swaps/activities | List Swap Activities


# **create_swap_activity**
> SwapActivity create_swap_activity(create_swap_activity_request)

Create Swap Activity

This operation to create a swap activity. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_swap_activity_request import CreateSwapActivityRequest
from cobo_waas2.models.swap_activity import SwapActivity
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

[**SwapActivity**](SwapActivity.md)

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

# **create_swap_quote**
> CreateSwapQuote201Response create_swap_quote(create_swap_quote_request)

Create Swap Quote

This operation retrieves a quote for swapping between two tokens. Either pay_amount or receive_amount must be provided. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_swap_quote201_response import CreateSwapQuote201Response
from cobo_waas2.models.create_swap_quote_request import CreateSwapQuoteRequest
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
    create_swap_quote_request = cobo_waas2.CreateSwapQuoteRequest()

    try:
        # Create Swap Quote
        api_response = api_instance.create_swap_quote(create_swap_quote_request)
        print("The response of SwapsApi->create_swap_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->create_swap_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_swap_quote_request** | [**CreateSwapQuoteRequest**](CreateSwapQuoteRequest.md)| The request body for creating a swap activity. | 

### Return type

[**CreateSwapQuote201Response**](CreateSwapQuote201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The swap quote has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_activity**
> SwapActivity get_swap_activity(activity_id)

Get Swap Activity Details

This operation retrieves the details of a swap activity. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.swap_activity import SwapActivity
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

[**SwapActivity**](SwapActivity.md)

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
 **pay_amount** | **str**| The amount of pay token to swap. | [optional] 
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

# **list_enable_token_pairs**
> ListEnableTokenPairs200Response list_enable_token_pairs(limit=limit, before=before, after=after)

List Supported Token Pairs

This operation retrieves all supported token pairs for swaps in a specified wallet. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_enable_token_pairs200_response import ListEnableTokenPairs200Response
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
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Supported Token Pairs
        api_response = api_instance.list_enable_token_pairs(limit=limit, before=before, after=after)
        print("The response of SwapsApi->list_enable_token_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->list_enable_token_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListEnableTokenPairs200Response**](ListEnableTokenPairs200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The supported token pairs have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_swap_activities**
> ListSwapActivities200Response list_swap_activities(status=status, min_updated_timestamp=min_updated_timestamp, max_updated_timestamp=max_updated_timestamp, initiator=initiator, limit=limit, before=before, after=after, sort_by=sort_by, direction=direction)

List Swap Activities

This operation retrieves a list of swap activities. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_swap_activities200_response import ListSwapActivities200Response
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
    status = 'Success'
    min_updated_timestamp = 1635744000000
    max_updated_timestamp = 1635744000000
    initiator = 'steve@example.com'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'
    sort_by = ''
    direction = ''

    try:
        # List Swap Activities
        api_response = api_instance.list_swap_activities(status=status, min_updated_timestamp=min_updated_timestamp, max_updated_timestamp=max_updated_timestamp, initiator=initiator, limit=limit, before=before, after=after, sort_by=sort_by, direction=direction)
        print("The response of SwapsApi->list_swap_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapsApi->list_swap_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **min_updated_timestamp** | **int**| The start time of the query. All staking activities updated after the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **max_updated_timestamp** | **int**| The end time of the query. All staking activities updated before the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **initiator** | **str**| The activity initiator, which is your API key by default. You can also specify the initiator when creating the activity. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 
 **sort_by** | **str**| The field used for sorting. | [optional] [default to &#39;&#39;]
 **direction** | **str**| The sort direction. Possible values include:   - &#x60;ASC&#x60;: Sort the results in ascending order.   - &#x60;DESC&#x60;: Sort the results in descending order.  | [optional] [default to &#39;&#39;]

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
**200** | A list of staking activities have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

