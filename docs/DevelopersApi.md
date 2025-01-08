# cobo_waas2.DevelopersApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key_info**](DevelopersApi.md#get_api_key_info) | **GET** /developers/api_key_info | Get API key information
[**list_callback_messages**](DevelopersApi.md#list_callback_messages) | **GET** /developers/callback_messages | List all callback messages
[**retry_callback_message**](DevelopersApi.md#retry_callback_message) | **POST** /developers/callback_messages/{message_id}/retry | Retry callback message


# **get_api_key_info**
> GetApiKeyInfo200Response get_api_key_info()

Get API key information

This operation retrieves the details of the API key that you are using.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_api_key_info200_response import GetApiKeyInfo200Response
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
    api_instance = cobo_waas2.DevelopersApi(api_client)

    try:
        # Get API key information
        api_response = api_instance.get_api_key_info()
        print("The response of DevelopersApi->get_api_key_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersApi->get_api_key_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetApiKeyInfo200Response**](GetApiKeyInfo200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API key information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_callback_messages**
> ListCallbackMessages200Response list_callback_messages(callback_message_ids=callback_message_ids, request_ids=request_ids, transaction_ids=transaction_ids, wallet_ids=wallet_ids, status=status, limit=limit, before=before, after=after)

List all callback messages

This operation retrieves all the callback messages in your organization.  For more details about how to respond to callback messages, refer to [Callback messages](/v2/guides/webhooks-callbacks/set-up-endpoint#callback-messages). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_callback_messages200_response import ListCallbackMessages200Response
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
    api_instance = cobo_waas2.DevelopersApi(api_client)
    callback_message_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,f47ac10b-58cc-4372-a567-0e02b2c3d479'
    request_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,f47ac10b-58cc-4372-a567-0e02b2c3d479'
    transaction_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,f47ac10b-58cc-4372-a567-0e02b2c3d479'
    wallet_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,f47ac10b-58cc-4372-a567-0e02b2c3d479'
    status = 'Approved'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all callback messages
        api_response = api_instance.list_callback_messages(callback_message_ids=callback_message_ids, request_ids=request_ids, transaction_ids=transaction_ids, wallet_ids=wallet_ids, status=status, limit=limit, before=before, after=after)
        print("The response of DevelopersApi->list_callback_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersApi->list_callback_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_message_ids** | **str**| A list of callback message IDs, separated by commas. | [optional] 
 **request_ids** | **str**| A list of request IDs, separated by commas. The request ID is provided by you and must be unique within your organization. | [optional] 
 **transaction_ids** | **str**| A list of transaction IDs, separated by commas. | [optional] 
 **wallet_ids** | **str**| A list of wallet IDs, separated by commas. | [optional] 
 **status** | **str**| The callback message status. Possible values include &#x60;Approved&#x60;, &#x60;Denied&#x60;, and &#x60;Failed&#x60;. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListCallbackMessages200Response**](ListCallbackMessages200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about callback messages. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_callback_message**
> RetryCallbackMessage201Response retry_callback_message(message_id)

Retry callback message

This operation resends a callback message that failed previously.  If your callback endpoint doesn't respond as expected, the WaaS service will retry sending the callback message up to 30 times. After that, the callback message status will be `Failed`. Use this operation to resend the message. For more details, refer to [Webhooks and Callbacks](/v2/guides/webhooks-callbacks/set-up-endpoint#callback-messages). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.retry_callback_message201_response import RetryCallbackMessage201Response
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
    api_instance = cobo_waas2.DevelopersApi(api_client)
    message_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Retry callback message
        api_response = api_instance.retry_callback_message(message_id)
        print("The response of DevelopersApi->retry_callback_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersApi->retry_callback_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| The callback message ID. | 

### Return type

[**RetryCallbackMessage201Response**](RetryCallbackMessage201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

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

