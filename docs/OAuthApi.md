# cobo_waas2.OAuthApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](OAuthApi.md#get_token) | **GET** /oauth/token | Get Org Access Token
[**refresh_token**](OAuthApi.md#refresh_token) | **POST** /oauth/token | Refresh Org Access Token


# **get_token**
> GetToken200Response get_token(client_id, org_id, grant_type)

Get Org Access Token

<Note>This operation is only applicable to Cobo Portal App developers. To call this operation, you need to use the Cobo OAuth authentication method that requires an app key.</Note> This operation allows Cobo Portal Apps to get an Org Access Token and a Refresh Token with a specified client ID, organization ID, and grant type.   Access tokens allow the app to signal to the WaaS service that it has received permission to access specific resources of the app user's [organization](https://manuals.cobo.com/en/portal/organization/introduction). Once the app has been granted permission by the organization's admin, it can use this operation to obtain both an Org Access Token and a Refresh Token.  For security purposes, Org Access Tokens expire after a certain period. Once they expire, the app needs to call [Refresh token](/v2/api-references/oauth/refresh-org-access-token) to get a new Org Access Token and a new Refresh Token.  

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.get_token200_response import GetToken200Response
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
    api_instance = cobo_waas2.OAuthApi(api_client)
    client_id = 'pvSwS8iFrfK0oZrB0ugG54XPDOLEv0Ij'
    org_id = 'e3986401-4aec-480a-973d-e775a4518413'
    grant_type = 'org_implicit'

    try:
        # Get Org Access Token
        api_response = api_instance.get_token(client_id, org_id, grant_type)
        print("The response of OAuthApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID, a unique identifier to distinguish Cobo Portal Apps. You can get the client ID by retrieving the manifest file after publishing the app. | 
 **org_id** | **str**| Organization ID, a unique identifier to distinguish different organizations. You can get the organization ID from the callback message sent to the URL that was configured in the manifest file. | 
 **grant_type** | **str**| The OAuth grant type. Set the value as &#x60;org_implicit&#x60;. | 

### Return type

[**GetToken200Response**](GetToken200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. |  -  |
**4XX** | Unauthorized. Please provide valid credentials. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> RefreshToken201Response refresh_token(refresh_token_request)

Refresh Org Access Token

<Note>This operation is only applicable to Cobo Portal Apps developers. To call this operation, you need to use the Cobo OAuth authentication method that requires an app key.</Note> This operation allows Cobo Portal Apps to obtain a new Org Access Token with a specified client ID, grant type and a Refresh Token.   For security purposes, Org Access Tokens expire after a certain period. Once they expire, the app needs to call this operation to get a new Org Access Token and a new Refresh Token.  

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.refresh_token201_response import RefreshToken201Response
from cobo_waas2.models.refresh_token_request import RefreshTokenRequest
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
    api_instance = cobo_waas2.OAuthApi(api_client)
    refresh_token_request = cobo_waas2.RefreshTokenRequest()

    try:
        # Refresh Org Access Token
        api_response = api_instance.refresh_token(refresh_token_request)
        print("The response of OAuthApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)| The request body for refreshing an Org Access Token. | 

### Return type

[**RefreshToken201Response**](RefreshToken201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request was successful. |  -  |
**4XX** | Unauthorized. Please provide valid credentials. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

