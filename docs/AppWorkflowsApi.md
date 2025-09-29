# cobo_waas2.AppWorkflowsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_approval_request**](AppWorkflowsApi.md#create_approval_request) | **POST** /app/workflows/approval_requests | Request app workflow approval
[**get_approval_request_by_id**](AppWorkflowsApi.md#get_approval_request_by_id) | **GET** /app/workflows/approval_requests/{approval_id} | Get app workflow approval request by approval id
[**list_app_workflows**](AppWorkflowsApi.md#list_app_workflows) | **GET** /app/workflows | list app workflows
[**list_approval_requests**](AppWorkflowsApi.md#list_approval_requests) | **GET** /app/workflows/approval_requests | List app workflow approval requests by operation_id
[**revoke_approval_request**](AppWorkflowsApi.md#revoke_approval_request) | **POST** /app/workflows/approval_requests/{approval_id}/revoke | Revoke an app workflow approval request by request initiator.


# **create_approval_request**
> CreateApprovalRequest201Response create_approval_request(request_approval=request_approval)

Request app workflow approval

This operation is request approval from app workflow with idempotency checks. 

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
        # Request app workflow approval
        api_response = api_instance.create_approval_request(request_approval=request_approval)
        print("The response of AppWorkflowsApi->create_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->create_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_approval** | [**RequestApproval**](RequestApproval.md)| The request body to app workflow approval. | [optional] 

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

Get app workflow approval request by approval id

This operation is retrieves approval request from app workflow. 

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
        # Get app workflow approval request by approval id
        api_response = api_instance.get_approval_request_by_id(approval_id)
        print("The response of AppWorkflowsApi->get_approval_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->get_approval_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The approval ID that is used to track a workflow approval request. | 

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
**200** | The information about an app workflow approval. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_workflows**
> List[AppWorkflow] list_app_workflows()

list app workflows

This operation is list app workflows of app. 

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
        # list app workflows
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
**200** | A list of app workflows have been successfully configured. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approval_requests**
> ListApprovalRequests200Response list_approval_requests(operation_id, limit=limit, before=before, after=after)

List app workflow approval requests by operation_id

This operation is retrieves list approval requests from app workflow. 

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
        # List app workflow approval requests by operation_id
        api_response = api_instance.list_approval_requests(operation_id, limit=limit, before=before, after=after)
        print("The response of AppWorkflowsApi->list_approval_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->list_approval_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| The operation ID that is used to track a workflow. The operation ID is provided by you and must be unique within your app. | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

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
**200** | A list of approval request have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_approval_request**
> RevokeApprovalRequest201Response revoke_approval_request(approval_id, revoke_approval_request_request=revoke_approval_request_request)

Revoke an app workflow approval request by request initiator.

This operation is revoke approval request from app workflow. 

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
        # Revoke an app workflow approval request by request initiator.
        api_response = api_instance.revoke_approval_request(approval_id, revoke_approval_request_request=revoke_approval_request_request)
        print("The response of AppWorkflowsApi->revoke_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppWorkflowsApi->revoke_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The approval ID that is used to track a workflow approval request. | 
 **revoke_approval_request_request** | [**RevokeApprovalRequestRequest**](RevokeApprovalRequestRequest.md)| The revoke request body to app workflow approval. | [optional] 

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

