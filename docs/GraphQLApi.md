# cobo_waas2.GraphQLApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_graphql**](GraphQLApi.md#execute_graphql) | **POST** /graphql | Execute a GraphQL query or mutation


# **execute_graphql**
> GraphQLResponse execute_graphql(graph_ql_request=graph_ql_request)

Execute a GraphQL query or mutation

This endpoint executes a GraphQL query or mutation. The request body must include a valid GraphQL query string. 

### Example

* Api Key Authentication (CoboNonce):
* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):
* Api Key Authentication (CoboSignature):

```python
import cobo_waas2
from cobo_waas2.models.graph_ql_request import GraphQLRequest
from cobo_waas2.models.graph_ql_response import GraphQLResponse
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
    api_instance = cobo_waas2.GraphQLApi(api_client)
    graph_ql_request = cobo_waas2.GraphQLRequest()

    try:
        # Execute a GraphQL query or mutation
        api_response = api_instance.execute_graphql(graph_ql_request=graph_ql_request)
        print("The response of GraphQLApi->execute_graphql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphQLApi->execute_graphql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **graph_ql_request** | [**GraphQLRequest**](GraphQLRequest.md)| The request body to generate addresses within a specified wallet. | [optional] 

### Return type

[**GraphQLResponse**](GraphQLResponse.md)

### Authorization

[CoboNonce](../README.md#CoboNonce), [OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth), [CoboSignature](../README.md#CoboSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A staking activity has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

