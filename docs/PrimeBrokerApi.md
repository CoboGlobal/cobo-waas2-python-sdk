# cobo_waas2.PrimeBrokerApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_guard_pubkey**](PrimeBrokerApi.md#change_guard_pubkey) | **PUT** /prime_broker/user/{user_id}/guard_pubkey | change a user guard pubkey
[**create_guard_pubkey**](PrimeBrokerApi.md#create_guard_pubkey) | **POST** /prime_broker/user/{user_id}/guard_pubkey | create a guard pubkey binding
[**create_prime_broker_address**](PrimeBrokerApi.md#create_prime_broker_address) | **POST** /prime_broker/user/{user_id}/addresses | bind addresses to a broker user
[**delete_guard_pubkey**](PrimeBrokerApi.md#delete_guard_pubkey) | **POST** /prime_broker/user/{user_id}/guard_pubkey/delete | delete a user guard pubkey
[**query_approval_statement**](PrimeBrokerApi.md#query_approval_statement) | **GET** /prime_broker/approval_statement/{statement_id} | query a approval statement
[**query_guard_pubkey**](PrimeBrokerApi.md#query_guard_pubkey) | **GET** /prime_broker/user/{user_id}/guard_pubkey | query a user guard pubkey


# **change_guard_pubkey**
> ChangeGuardPubkey200Response change_guard_pubkey(user_id)

change a user guard pubkey

This operation change a user guard pubkey. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.change_guard_pubkey200_response import ChangeGuardPubkey200Response
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    user_id = '168108513539918'

    try:
        # change a user guard pubkey
        api_response = api_instance.change_guard_pubkey(user_id)
        print("The response of PrimeBrokerApi->change_guard_pubkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->change_guard_pubkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id. | 

### Return type

[**ChangeGuardPubkey200Response**](ChangeGuardPubkey200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a guard binding. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_guard_pubkey**
> ChangeGuardPubkey200Response create_guard_pubkey(user_id)

create a guard pubkey binding

This operation create a guard pubkey binding. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.change_guard_pubkey200_response import ChangeGuardPubkey200Response
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    user_id = '168108513539918'

    try:
        # create a guard pubkey binding
        api_response = api_instance.create_guard_pubkey(user_id)
        print("The response of PrimeBrokerApi->create_guard_pubkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->create_guard_pubkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id. | 

### Return type

[**ChangeGuardPubkey200Response**](ChangeGuardPubkey200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a guard binding. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prime_broker_address**
> CreatePrimeBrokerAddress201Response create_prime_broker_address(user_id, create_prime_broker_address_request=create_prime_broker_address_request)

bind addresses to a broker user

This operation bind addresses to a broker user. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_prime_broker_address201_response import CreatePrimeBrokerAddress201Response
from cobo_waas2.models.create_prime_broker_address_request import CreatePrimeBrokerAddressRequest
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    user_id = '168108513539918'
    create_prime_broker_address_request = cobo_waas2.CreatePrimeBrokerAddressRequest()

    try:
        # bind addresses to a broker user
        api_response = api_instance.create_prime_broker_address(user_id, create_prime_broker_address_request=create_prime_broker_address_request)
        print("The response of PrimeBrokerApi->create_prime_broker_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->create_prime_broker_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id. | 
 **create_prime_broker_address_request** | [**CreatePrimeBrokerAddressRequest**](CreatePrimeBrokerAddressRequest.md)| The request body to binding addresses to a broker user. | [optional] 

### Return type

[**CreatePrimeBrokerAddress201Response**](CreatePrimeBrokerAddress201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a address binding. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guard_pubkey**
> DeleteGuardPubkey201Response delete_guard_pubkey(user_id)

delete a user guard pubkey

This operation delete a user guard pubkey. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_guard_pubkey201_response import DeleteGuardPubkey201Response
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    user_id = '168108513539918'

    try:
        # delete a user guard pubkey
        api_response = api_instance.delete_guard_pubkey(user_id)
        print("The response of PrimeBrokerApi->delete_guard_pubkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->delete_guard_pubkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id. | 

### Return type

[**DeleteGuardPubkey201Response**](DeleteGuardPubkey201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a guard binding. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_approval_statement**
> QueryApprovalStatement200Response query_approval_statement(statement_id)

query a approval statement

This operation query a approval statement. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.query_approval_statement200_response import QueryApprovalStatement200Response
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    statement_id = '168108513539918'

    try:
        # query a approval statement
        api_response = api_instance.query_approval_statement(statement_id)
        print("The response of PrimeBrokerApi->query_approval_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->query_approval_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**| approval statement id. | 

### Return type

[**QueryApprovalStatement200Response**](QueryApprovalStatement200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about a approval statement. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_guard_pubkey**
> QueryGuardPubkey200Response query_guard_pubkey(user_id)

query a user guard pubkey

This operation query a user guard pubkey 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.query_guard_pubkey200_response import QueryGuardPubkey200Response
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
    api_instance = cobo_waas2.PrimeBrokerApi(api_client)
    user_id = '168108513539918'

    try:
        # query a user guard pubkey
        api_response = api_instance.query_guard_pubkey(user_id)
        print("The response of PrimeBrokerApi->query_guard_pubkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrimeBrokerApi->query_guard_pubkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user id. | 

### Return type

[**QueryGuardPubkey200Response**](QueryGuardPubkey200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about an user guard pubkey. |  -  |
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

