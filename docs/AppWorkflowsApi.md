# cobo_waas2.AppWorkflowsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_approval_request**](AppWorkflowsApi.md#create_approval_request) | **POST** /app/workflows/approval_requests | Request workflow approval
[**get_approval_request_by_id**](AppWorkflowsApi.md#get_approval_request_by_id) | **GET** /app/workflows/approval_requests/{approval_id} | Get approval request details
[**list_app_workflows**](AppWorkflowsApi.md#list_app_workflows) | **GET** /app/workflows | List app workflows
[**list_approval_requests**](AppWorkflowsApi.md#list_approval_requests) | **GET** /app/workflows/approval_requests | List approval requests
[**revoke_approval_request**](AppWorkflowsApi.md#revoke_approval_request) | **POST** /app/workflows/approval_requests/{approval_id}/revoke | Revoke approval request


# **create_approval_request**
> CreateApprovalRequest201Response create_approval_request(request_approval=request_approval)

Request workflow approval

This operation triggers a specified workflow and generates a new approval request.  <Note>To use the approval workflow operations, you must use the Cobo OAuth authentication method ([Org Access Token](https://www.cobo.com/developers/v2/apps/org-access-tokens)).</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_approval_request201_response import CreateApprovalRequest201Response
from cobo_waas2.models.request_approval import RequestApproval
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
    api_instance = cobo_waas2.AppWorkflowsApi(api_client)
    request_approval = cobo_waas2.RequestApproval()

    try:
        # Request workflow approval
        api_response = api_instance.create_approval_request(request_approval=request_approval)
        print("The response of AppWorkflowsApi->create_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->create_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_approval** | [**RequestApproval**](RequestApproval.md)| The request body to request workflow approval. | [optional] 

### Return type

[**CreateApprovalRequest201Response**](CreateApprovalRequest201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request workflow approval was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_request_by_id**
> ApprovalRequestDetail get_approval_request_by_id(approval_id)

Get approval request details

This operation retrieves the details of a specific approval request.  <Note>To use the approval workflow operations, you must use the Cobo OAuth authentication method ([Org Access Token](https://www.cobo.com/developers/v2/apps/org-access-tokens)).</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.approval_request_detail import ApprovalRequestDetail
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
    api_instance = cobo_waas2.AppWorkflowsApi(api_client)
    approval_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get approval request details
        api_response = api_instance.get_approval_request_by_id(approval_id)
        print("The response of AppWorkflowsApi->get_approval_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->get_approval_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The system-generated unique ID of the approval request. | 

### Return type

[**ApprovalRequestDetail**](ApprovalRequestDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about an approval request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_workflows**
> List[AppWorkflow] list_app_workflows()

List app workflows

This operation retrieves all approval workflows of an Cobo Portal App. <Note>You need to [configure approval workflow](https://www.cobo.com/developers/v2/apps/configure-workflow) in the app Manifest file first.</Note> <Note>To use the approval workflow operations, you must use the Cobo OAuth authentication method ([Org Access Token](https://www.cobo.com/developers/v2/apps/org-access-tokens)).</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.app_workflow import AppWorkflow
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
    api_instance = cobo_waas2.AppWorkflowsApi(api_client)

    try:
        # List app workflows
        api_response = api_instance.list_app_workflows()
        print("The response of AppWorkflowsApi->list_app_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->list_app_workflows: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppWorkflow]**](AppWorkflow.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of approval workflows successfully retrieved |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approval_requests**
> ListApprovalRequests200Response list_approval_requests(operation_id, limit=limit, before=before, after=after)

List approval requests

This operation retrieves a list of approval requests.  <Note>To use the approval workflow operations, you must use the Cobo OAuth authentication method ([Org Access Token](https://www.cobo.com/developers/v2/apps/org-access-tokens)).</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_approval_requests200_response import ListApprovalRequests200Response
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
    api_instance = cobo_waas2.AppWorkflowsApi(api_client)
    operation_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List approval requests
        api_response = api_instance.list_approval_requests(operation_id, limit=limit, before=before, after=after)
        print("The response of AppWorkflowsApi->list_approval_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->list_approval_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| The unique ID of the approval workflow. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListApprovalRequests200Response**](ListApprovalRequests200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of approval requests have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_approval_request**
> RevokeApprovalRequest201Response revoke_approval_request(approval_id, revoke_approval_request_request=revoke_approval_request_request)

Revoke approval request

This operation revokes a pending approval request.  <Note>To use the approval workflow operations, you must use the Cobo OAuth authentication method ([Org Access Token](https://www.cobo.com/developers/v2/apps/org-access-tokens)).</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.revoke_approval_request201_response import RevokeApprovalRequest201Response
from cobo_waas2.models.revoke_approval_request_request import RevokeApprovalRequestRequest
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
    api_instance = cobo_waas2.AppWorkflowsApi(api_client)
    approval_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    revoke_approval_request_request = cobo_waas2.RevokeApprovalRequestRequest()

    try:
        # Revoke approval request
        api_response = api_instance.revoke_approval_request(approval_id, revoke_approval_request_request=revoke_approval_request_request)
        print("The response of AppWorkflowsApi->revoke_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->revoke_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The system-generated unique ID of the approval request. | 
 **revoke_approval_request_request** | [**RevokeApprovalRequestRequest**](RevokeApprovalRequestRequest.md)| The request body to revoke an approval request. | [optional] 

### Return type

[**RevokeApprovalRequest201Response**](RevokeApprovalRequest201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request workflow approval was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

