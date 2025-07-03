# cobo_waas2.OrganizationsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_info**](OrganizationsApi.md#get_org_info) | **GET** /organizations/info | Get organization information


# **get_org_info**
> OrgInfo get_org_info()

Get organization information

This operation retrieves the detailed information about the organization associated with the current API key. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.org_info import OrgInfo
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
    api_instance = cobo_waas2.OrganizationsApi(api_client)

    try:
        # Get organization information
        api_response = api_instance.get_org_info()
        print("The response of OrganizationsApi->get_org_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_org_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgInfo**](OrgInfo.md)

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

