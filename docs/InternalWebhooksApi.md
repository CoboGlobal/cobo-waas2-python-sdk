# cobo_waas2.InternalWebhooksApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_event**](InternalWebhooksApi.md#create_webhook_event) | **POST** /internal/webhook_event | Create webhook event


# **create_webhook_event**
> CreateWebhookEventInfo create_webhook_event(create_webhook_event_params=create_webhook_event_params)

Create webhook event

This operation creates a webhook event. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_webhook_event_info import CreateWebhookEventInfo
from cobo_waas2.models.create_webhook_event_params import CreateWebhookEventParams
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
    api_instance = cobo_waas2.InternalWebhooksApi(api_client)
    create_webhook_event_params = cobo_waas2.CreateWebhookEventParams()

    try:
        # Create webhook event
        api_response = api_instance.create_webhook_event(create_webhook_event_params=create_webhook_event_params)
        print("The response of InternalWebhooksApi->create_webhook_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWebhooksApi->create_webhook_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_event_params** | [**CreateWebhookEventParams**](CreateWebhookEventParams.md)| The request body to create a webhook event | [optional] 

### Return type

[**CreateWebhookEventInfo**](CreateWebhookEventInfo.md)

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

