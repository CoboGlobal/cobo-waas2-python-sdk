# cobo_waas2.DevelopersWebhooksApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_endpoint**](DevelopersWebhooksApi.md#create_webhook_endpoint) | **POST** /webhooks/endpoints | Register webhook endpoint
[**get_webhook_endpoint_by_id**](DevelopersWebhooksApi.md#get_webhook_endpoint_by_id) | **GET** /webhooks/endpoints/{endpoint_id} | Get webhook endpoint information
[**get_webhook_event_by_id**](DevelopersWebhooksApi.md#get_webhook_event_by_id) | **GET** /webhooks/endpoints/{endpoint_id}/events/{event_id} | Retrieve event information
[**list_webhook_endpoints**](DevelopersWebhooksApi.md#list_webhook_endpoints) | **GET** /webhooks/endpoints | List webhook endpoints
[**list_webhook_event_definitions**](DevelopersWebhooksApi.md#list_webhook_event_definitions) | **GET** /webhooks/events/definitions | Get webhook event types
[**list_webhook_event_logs**](DevelopersWebhooksApi.md#list_webhook_event_logs) | **GET** /webhooks/endpoints/{endpoint_id}/events/{event_id}/logs | List webhook event logs
[**list_webhook_events**](DevelopersWebhooksApi.md#list_webhook_events) | **GET** /webhooks/endpoints/{endpoint_id}/events | List all webhook events
[**retry_webhook_event_by_id**](DevelopersWebhooksApi.md#retry_webhook_event_by_id) | **POST** /webhooks/endpoints/{endpoint_id}/events/{event_id}/retry | Retry event
[**trigger_test_webhook_event**](DevelopersWebhooksApi.md#trigger_test_webhook_event) | **POST** /webhooks/events/trigger | Trigger test event
[**update_webhook_endpoint_by_id**](DevelopersWebhooksApi.md#update_webhook_endpoint_by_id) | **PUT** /webhooks/endpoints/{endpoint_id} | Update webhook endpoint


# **create_webhook_endpoint**
> WebhookEndpoint create_webhook_endpoint(create_webhook_endpoint_request=create_webhook_endpoint_request)

Register webhook endpoint

This operation registers a new webhook endpoint for your organization.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest
from cobo_waas2.models.webhook_endpoint import WebhookEndpoint
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    create_webhook_endpoint_request = cobo_waas2.CreateWebhookEndpointRequest()

    try:
        # Register webhook endpoint
        api_response = api_instance.create_webhook_endpoint(create_webhook_endpoint_request=create_webhook_endpoint_request)
        print("The response of DevelopersWebhooksApi->create_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->create_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_endpoint_request** | [**CreateWebhookEndpointRequest**](CreateWebhookEndpointRequest.md)| The request body to register a webhook endpoint. | [optional] 

### Return type

[**WebhookEndpoint**](WebhookEndpoint.md)

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

# **get_webhook_endpoint_by_id**
> WebhookEndpoint get_webhook_endpoint_by_id(endpoint_id)

Get webhook endpoint information

This operation retrieves the information of a specified webhook endpoint.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.webhook_endpoint import WebhookEndpoint
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get webhook endpoint information
        api_response = api_instance.get_webhook_endpoint_by_id(endpoint_id)
        print("The response of DevelopersWebhooksApi->get_webhook_endpoint_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->get_webhook_endpoint_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 

### Return type

[**WebhookEndpoint**](WebhookEndpoint.md)

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

# **get_webhook_event_by_id**
> WebhookEvent get_webhook_event_by_id(event_id, endpoint_id)

Retrieve event information

This operation retrieves the information of a webhook event by the event ID. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.webhook_event import WebhookEvent
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Retrieve event information
        api_response = api_instance.get_webhook_event_by_id(event_id, endpoint_id)
        print("The response of DevelopersWebhooksApi->get_webhook_event_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->get_webhook_event_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| The event ID. You can obtain a list of event IDs by calling [List all events](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-all-events). | 
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 

### Return type

[**WebhookEvent**](WebhookEvent.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook event information is successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_endpoints**
> ListWebhookEndpoints200Response list_webhook_endpoints(status=status, event_type=event_type, limit=limit, before=before, after=after)

List webhook endpoints

This operation retrieves the information of all webhook endpoints registered under your organization. You can filter the result by endpoint status and the subscribed event type.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_webhook_endpoints200_response import ListWebhookEndpoints200Response
from cobo_waas2.models.webhook_endpoint_status import WebhookEndpointStatus
from cobo_waas2.models.webhook_event_type import WebhookEventType
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    status = cobo_waas2.WebhookEndpointStatus()
    event_type = cobo_waas2.WebhookEventType()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List webhook endpoints
        api_response = api_instance.list_webhook_endpoints(status=status, event_type=event_type, limit=limit, before=before, after=after)
        print("The response of DevelopersWebhooksApi->list_webhook_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->list_webhook_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**WebhookEndpointStatus**](.md)|  | [optional] 
 **event_type** | [**WebhookEventType**](.md)|  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListWebhookEndpoints200Response**](ListWebhookEndpoints200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed of webhook endpoints |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_event_definitions**
> List[ListWebhookEventDefinitions200ResponseInner] list_webhook_event_definitions()

Get webhook event types

This operation retrieves all supported webhook event types.

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_webhook_event_definitions200_response_inner import ListWebhookEventDefinitions200ResponseInner
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)

    try:
        # Get webhook event types
        api_response = api_instance.list_webhook_event_definitions()
        print("The response of DevelopersWebhooksApi->list_webhook_event_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->list_webhook_event_definitions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListWebhookEventDefinitions200ResponseInner]**](ListWebhookEventDefinitions200ResponseInner.md)

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

# **list_webhook_event_logs**
> ListWebhookEventLogs200Response list_webhook_event_logs(event_id, endpoint_id, limit=limit, before=before, after=after)

List webhook event logs

This operation retrieves a list of webhook event logs by event ID. Each retry will generate a separate event log. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_webhook_event_logs200_response import ListWebhookEventLogs200Response
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List webhook event logs
        api_response = api_instance.list_webhook_event_logs(event_id, endpoint_id, limit=limit, before=before, after=after)
        print("The response of DevelopersWebhooksApi->list_webhook_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->list_webhook_event_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| The event ID. You can obtain a list of event IDs by calling [List all events](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-all-events). | 
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListWebhookEventLogs200Response**](ListWebhookEventLogs200Response.md)

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

# **list_webhook_events**
> ListWebhookEvents200Response list_webhook_events(endpoint_id, status=status, type=type, limit=limit, before=before, after=after)

List all webhook events

This operation retrieves a list of webhook events that have occurred within the last 30 days.  <Note>The request will only return webhook events that have occurred to the wallets associated with your current API key. For example, if the current API key is only associated with Custodial Wallets, any webhook events that have occurred to an MPC Wallet will not be retrieved with the current API key.</Note> 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_webhook_events200_response import ListWebhookEvents200Response
from cobo_waas2.models.webhook_event_status import WebhookEventStatus
from cobo_waas2.models.webhook_event_type import WebhookEventType
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    status = cobo_waas2.WebhookEventStatus()
    type = cobo_waas2.WebhookEventType()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all webhook events
        api_response = api_instance.list_webhook_events(endpoint_id, status=status, type=type, limit=limit, before=before, after=after)
        print("The response of DevelopersWebhooksApi->list_webhook_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->list_webhook_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 
 **status** | [**WebhookEventStatus**](.md)|  | [optional] 
 **type** | [**WebhookEventType**](.md)|  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListWebhookEvents200Response**](ListWebhookEvents200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of webhook events has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_webhook_event_by_id**
> RetryWebhookEventById201Response retry_webhook_event_by_id(event_id, endpoint_id)

Retry event

This operation retries delivering a webhook event with the specified event ID. You can only retry delivering a webhook event in the `Retrying` or `Failed` status. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.retry_webhook_event_by_id201_response import RetryWebhookEventById201Response
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    event_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Retry event
        api_response = api_instance.retry_webhook_event_by_id(event_id, endpoint_id)
        print("The response of DevelopersWebhooksApi->retry_webhook_event_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->retry_webhook_event_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| The event ID. You can obtain a list of event IDs by calling [List all events](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-all-events). | 
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 

### Return type

[**RetryWebhookEventById201Response**](RetryWebhookEventById201Response.md)

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

# **trigger_test_webhook_event**
> TriggerTestWebhookEvent201Response trigger_test_webhook_event(trigger_test_webhook_event_request=trigger_test_webhook_event_request)

Trigger test event

This operation tests the functionality of your webhook endpoint by triggering a test webhook event. The test event will be sent to all the endpoints you have registered on Cobo Portal.  You only need to provide the event type. By default, the payload contains dummy data with no impact on your real business transactions or activities. You can optionally provide the `override_data` property to customize the payload. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.trigger_test_webhook_event201_response import TriggerTestWebhookEvent201Response
from cobo_waas2.models.trigger_test_webhook_event_request import TriggerTestWebhookEventRequest
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    trigger_test_webhook_event_request = cobo_waas2.TriggerTestWebhookEventRequest()

    try:
        # Trigger test event
        api_response = api_instance.trigger_test_webhook_event(trigger_test_webhook_event_request=trigger_test_webhook_event_request)
        print("The response of DevelopersWebhooksApi->trigger_test_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->trigger_test_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_test_webhook_event_request** | [**TriggerTestWebhookEventRequest**](TriggerTestWebhookEventRequest.md)| The request body used to trigger a test webhook event.  | [optional] 

### Return type

[**TriggerTestWebhookEvent201Response**](TriggerTestWebhookEvent201Response.md)

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

# **update_webhook_endpoint_by_id**
> WebhookEndpoint update_webhook_endpoint_by_id(endpoint_id, update_webhook_endpoint_by_id_request=update_webhook_endpoint_by_id_request)

Update webhook endpoint

This operation updates the information of a specified webhook endpoint.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.update_webhook_endpoint_by_id_request import UpdateWebhookEndpointByIdRequest
from cobo_waas2.models.webhook_endpoint import WebhookEndpoint
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
    api_instance = cobo_waas2.DevelopersWebhooksApi(api_client)
    endpoint_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_webhook_endpoint_by_id_request = cobo_waas2.UpdateWebhookEndpointByIdRequest()

    try:
        # Update webhook endpoint
        api_response = api_instance.update_webhook_endpoint_by_id(endpoint_id, update_webhook_endpoint_by_id_request=update_webhook_endpoint_by_id_request)
        print("The response of DevelopersWebhooksApi->update_webhook_endpoint_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevelopersWebhooksApi->update_webhook_endpoint_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| The webhook endpoint ID. You can retrieve a list of webhook endpoint IDs by calling [List webhook endpoints](https://www.cobo.com/developers/v2/api-references/developers--webhooks/list-webhook-endpoints). | 
 **update_webhook_endpoint_by_id_request** | [**UpdateWebhookEndpointByIdRequest**](UpdateWebhookEndpointByIdRequest.md)| The request body to update a webhook endpoint. | [optional] 

### Return type

[**WebhookEndpoint**](WebhookEndpoint.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update webhook endpoint successfully. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

