# cobo_waas2.DevelopersApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key_info**](DevelopersApi.md#get_api_key_info) | **GET** /developers/api_key_info | Get API key information


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

