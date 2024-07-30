# cobo_waas2.WalletsMPCWalletsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_tss_request_by_id**](WalletsMPCWalletsApi.md#cancel_tss_request_by_id) | **POST** /wallets/mpc/vaults/{vault_id}/tss_requests/{tss_request_id}/cancel | Cancel TSS request
[**create_key_share_holder_group**](WalletsMPCWalletsApi.md#create_key_share_holder_group) | **POST** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups | Create key share holder group
[**create_mpc_project**](WalletsMPCWalletsApi.md#create_mpc_project) | **POST** /wallets/mpc/projects | Create project
[**create_mpc_vault**](WalletsMPCWalletsApi.md#create_mpc_vault) | **POST** /wallets/mpc/vaults | Create vault
[**create_tss_request**](WalletsMPCWalletsApi.md#create_tss_request) | **POST** /wallets/mpc/vaults/{vault_id}/tss_requests | Create TSS request
[**delete_key_share_holder_group_by_id**](WalletsMPCWalletsApi.md#delete_key_share_holder_group_by_id) | **POST** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id}/delete | Delete key share holder group
[**get_key_share_holder_group_by_id**](WalletsMPCWalletsApi.md#get_key_share_holder_group_by_id) | **GET** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id} | Get key share holder group information
[**get_mpc_project_by_id**](WalletsMPCWalletsApi.md#get_mpc_project_by_id) | **GET** /wallets/mpc/projects/{project_id} | Get project information
[**get_mpc_vault_by_id**](WalletsMPCWalletsApi.md#get_mpc_vault_by_id) | **GET** /wallets/mpc/vaults/{vault_id} | Get vault information
[**get_tss_request_by_id**](WalletsMPCWalletsApi.md#get_tss_request_by_id) | **GET** /wallets/mpc/vaults/{vault_id}/tss_requests/{tss_request_id} | Get TSS request
[**list_cobo_key_holders**](WalletsMPCWalletsApi.md#list_cobo_key_holders) | **GET** /wallets/mpc/cobo_key_share_holders | List all Cobo key share holders
[**list_key_share_holder_groups**](WalletsMPCWalletsApi.md#list_key_share_holder_groups) | **GET** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups | List all key share holder groups
[**list_mpc_projects**](WalletsMPCWalletsApi.md#list_mpc_projects) | **GET** /wallets/mpc/projects | List all projects
[**list_mpc_vaults**](WalletsMPCWalletsApi.md#list_mpc_vaults) | **GET** /wallets/mpc/vaults | List all vaults
[**list_tss_requests**](WalletsMPCWalletsApi.md#list_tss_requests) | **GET** /wallets/mpc/vaults/{vault_id}/tss_requests | List TSS requests
[**update_key_share_holder_group_by_id**](WalletsMPCWalletsApi.md#update_key_share_holder_group_by_id) | **PUT** /wallets/mpc/vaults/{vault_id}/key_share_holder_groups/{key_share_holder_group_id} | Update key share holder group
[**update_mpc_project_by_id**](WalletsMPCWalletsApi.md#update_mpc_project_by_id) | **PUT** /wallets/mpc/projects/{project_id} | Update project name
[**update_mpc_vault_by_id**](WalletsMPCWalletsApi.md#update_mpc_vault_by_id) | **PUT** /wallets/mpc/vaults/{vault_id} | Update vault name


# **cancel_tss_request_by_id**
> TSSRequest cancel_tss_request_by_id(vault_id, tss_request_id)

Cancel TSS request

This operation cancels a TSS request. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tss_request import TSSRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    tss_request_id = '20240711114129000132315000003970'

    try:
        # Cancel TSS request
        api_response = api_instance.cancel_tss_request_by_id(vault_id, tss_request_id)
        print("The response of WalletsMPCWalletsApi->cancel_tss_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->cancel_tss_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **tss_request_id** | **str**| The TSS request ID, which you can retrieve by calling [List TSS requests](/v2/api-references/wallets--mpc-wallets/list-tss-requests). | 

### Return type

[**TSSRequest**](TSSRequest.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully modified the TSS request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key_share_holder_group**
> KeyShareHolderGroup create_key_share_holder_group(vault_id, create_key_share_holder_group_request=create_key_share_holder_group_request)

Create key share holder group

This operation creates a key share holder group for a specified vault. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_key_share_holder_group_request import CreateKeyShareHolderGroupRequest
from cobo_waas2.models.key_share_holder_group import KeyShareHolderGroup
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    create_key_share_holder_group_request = cobo_waas2.CreateKeyShareHolderGroupRequest()

    try:
        # Create key share holder group
        api_response = api_instance.create_key_share_holder_group(vault_id, create_key_share_holder_group_request=create_key_share_holder_group_request)
        print("The response of WalletsMPCWalletsApi->create_key_share_holder_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->create_key_share_holder_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **create_key_share_holder_group_request** | [**CreateKeyShareHolderGroupRequest**](CreateKeyShareHolderGroupRequest.md)| The request body to create a key share holder group. | [optional] 

### Return type

[**KeyShareHolderGroup**](KeyShareHolderGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | mpc vault successfully created |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpc_project**
> MPCProject create_mpc_project(create_mpc_project_request=create_mpc_project_request)

Create project

This operation creates a project.  <Note>This operation applies to MPC Wallets (User-Controlled Wallets) only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_mpc_project_request import CreateMpcProjectRequest
from cobo_waas2.models.mpc_project import MPCProject
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    create_mpc_project_request = cobo_waas2.CreateMpcProjectRequest()

    try:
        # Create project
        api_response = api_instance.create_mpc_project(create_mpc_project_request=create_mpc_project_request)
        print("The response of WalletsMPCWalletsApi->create_mpc_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->create_mpc_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mpc_project_request** | [**CreateMpcProjectRequest**](CreateMpcProjectRequest.md)| The request body to create a project. | [optional] 

### Return type

[**MPCProject**](MPCProject.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created project. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpc_vault**
> MPCVault create_mpc_vault(create_mpc_vault_request=create_mpc_vault_request)

Create vault

This operation creates a vault. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_mpc_vault_request import CreateMpcVaultRequest
from cobo_waas2.models.mpc_vault import MPCVault
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    create_mpc_vault_request = cobo_waas2.CreateMpcVaultRequest()

    try:
        # Create vault
        api_response = api_instance.create_mpc_vault(create_mpc_vault_request=create_mpc_vault_request)
        print("The response of WalletsMPCWalletsApi->create_mpc_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->create_mpc_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mpc_vault_request** | [**CreateMpcVaultRequest**](CreateMpcVaultRequest.md)| The request body to create a vault. | [optional] 

### Return type

[**MPCVault**](MPCVault.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created the vault. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tss_request**
> TSSRequest create_tss_request(vault_id, create_tss_request_request=create_tss_request_request)

Create TSS request

This operation creates a TSS request under a specified vault. You can use this operation to perform actions such as key generation and recovery. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_tss_request_request import CreateTssRequestRequest
from cobo_waas2.models.tss_request import TSSRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    create_tss_request_request = cobo_waas2.CreateTssRequestRequest()

    try:
        # Create TSS request
        api_response = api_instance.create_tss_request(vault_id, create_tss_request_request=create_tss_request_request)
        print("The response of WalletsMPCWalletsApi->create_tss_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->create_tss_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **create_tss_request_request** | [**CreateTssRequestRequest**](CreateTssRequestRequest.md)| The request body to create a TSS request. | [optional] 

### Return type

[**TSSRequest**](TSSRequest.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | mpc vault successfully created |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_share_holder_group_by_id**
> DeleteKeyShareHolderGroupById201Response delete_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)

Delete key share holder group

This operation deletes a specified key share holder group.

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_key_share_holder_group_by_id201_response import DeleteKeyShareHolderGroupById201Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'

    try:
        # Delete key share holder group
        api_response = api_instance.delete_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)
        print("The response of WalletsMPCWalletsApi->delete_key_share_holder_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->delete_key_share_holder_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **key_share_holder_group_id** | **str**| The key share holder group ID. | 

### Return type

[**DeleteKeyShareHolderGroupById201Response**](DeleteKeyShareHolderGroupById201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully deleted the specified key share holder group. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_share_holder_group_by_id**
> KeyShareHolderGroup get_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)

Get key share holder group information

This operation retrieves detailed information about a specified key share holder group. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.key_share_holder_group import KeyShareHolderGroup
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'

    try:
        # Get key share holder group information
        api_response = api_instance.get_key_share_holder_group_by_id(vault_id, key_share_holder_group_id)
        print("The response of WalletsMPCWalletsApi->get_key_share_holder_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->get_key_share_holder_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **key_share_holder_group_id** | **str**| The key share holder group ID. | 

### Return type

[**KeyShareHolderGroup**](KeyShareHolderGroup.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully get mpc tss group |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpc_project_by_id**
> MPCProject get_mpc_project_by_id(project_id)

Get project information

This operation retrieves detailed information about a project. <Note>This operation applies to MPC Wallets (User-Controlled Wallets) only.</Note> 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.mpc_project import MPCProject
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get project information
        api_response = api_instance.get_mpc_project_by_id(project_id)
        print("The response of WalletsMPCWalletsApi->get_mpc_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->get_mpc_project_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project ID, which you can retrieve by calling [List all projects](/v2/api-references/wallets--mpc-wallets/list-all-projects). | 

### Return type

[**MPCProject**](MPCProject.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed all vaults. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpc_vault_by_id**
> MPCVault get_mpc_vault_by_id(vault_id)

Get vault information

This operation retrieves detailed information about a vault. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.mpc_vault import MPCVault
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get vault information
        api_response = api_instance.get_mpc_vault_by_id(vault_id)
        print("The response of WalletsMPCWalletsApi->get_mpc_vault_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->get_mpc_vault_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 

### Return type

[**MPCVault**](MPCVault.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved vault information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tss_request_by_id**
> TSSRequest get_tss_request_by_id(vault_id, tss_request_id)

Get TSS request

This operation retrieves detailed information about a TSS request. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.tss_request import TSSRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    tss_request_id = '20240711114129000132315000003970'

    try:
        # Get TSS request
        api_response = api_instance.get_tss_request_by_id(vault_id, tss_request_id)
        print("The response of WalletsMPCWalletsApi->get_tss_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->get_tss_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **tss_request_id** | **str**| The TSS request ID, which you can retrieve by calling [List TSS requests](/v2/api-references/wallets--mpc-wallets/list-tss-requests). | 

### Return type

[**TSSRequest**](TSSRequest.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved TSS request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cobo_key_holders**
> List[KeyShareHolder] list_cobo_key_holders()

List all Cobo key share holders

This operation retrieves a list of all Cobo key share holders and their information.   <Note>When using this operation, `type` will only return `Cobo` and will never return `Mobile` or `API`.</Note> 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.key_share_holder import KeyShareHolder
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)

    try:
        # List all Cobo key share holders
        api_response = api_instance.list_cobo_key_holders()
        print("The response of WalletsMPCWalletsApi->list_cobo_key_holders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->list_cobo_key_holders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[KeyShareHolder]**](KeyShareHolder.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed MPC Wallets&#39; key share holder information. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_share_holder_groups**
> ListKeyShareHolderGroups200Response list_key_share_holder_groups(vault_id, key_share_holder_group_type=key_share_holder_group_type, limit=limit, before=before, after=after)

List all key share holder groups

This operation retrieves all key share holder groups under a specified vault. You can filter the result by group type. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.key_share_holder_group_type import KeyShareHolderGroupType
from cobo_waas2.models.list_key_share_holder_groups200_response import ListKeyShareHolderGroups200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    key_share_holder_group_type = cobo_waas2.KeyShareHolderGroupType()
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all key share holder groups
        api_response = api_instance.list_key_share_holder_groups(vault_id, key_share_holder_group_type=key_share_holder_group_type, limit=limit, before=before, after=after)
        print("The response of WalletsMPCWalletsApi->list_key_share_holder_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->list_key_share_holder_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **key_share_holder_group_type** | [**KeyShareHolderGroupType**](.md)| The key share holder group type. Possible values include: - &#x60;MainGroup&#x60;: The [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#main-group).  - &#x60;SigningGroup&#x60;: The [Signing Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#signing-group).  - &#x60;RecoveryGroup&#x60;: The [Recovery Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#recovery-group).  **Note**: If this parameter is left empty, all key share holder group types will be retrieved.  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListKeyShareHolderGroups200Response**](ListKeyShareHolderGroups200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed key share holder groups. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mpc_projects**
> ListMpcProjects200Response list_mpc_projects(limit=limit, before=before, after=after)

List all projects

This operation retrieves a list of all projects.  <Note>This operation applies to MPC Wallets (User-Controlled Wallets) only.</Note> 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_mpc_projects200_response import ListMpcProjects200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all projects
        api_response = api_instance.list_mpc_projects(limit=limit, before=before, after=after)
        print("The response of WalletsMPCWalletsApi->list_mpc_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->list_mpc_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListMpcProjects200Response**](ListMpcProjects200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed all projects. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mpc_vaults**
> ListMpcVaults200Response list_mpc_vaults(vault_type, project_id=project_id, limit=limit, before=before, after=after)

List all vaults

This operation retrieves a list of all vaults. You can filter the result by project ID.  **Notes for query parameters**: 1. `project_id` is required when `vault_type` is set to `User-Controlled`. 2. `project_id` must be left blank when `vault_type` is set to `Org-Controlled`. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_mpc_vaults200_response import ListMpcVaults200Response
from cobo_waas2.models.mpc_vault_type import MPCVaultType
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_type = cobo_waas2.MPCVaultType()
    project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List all vaults
        api_response = api_instance.list_mpc_vaults(vault_type, project_id=project_id, limit=limit, before=before, after=after)
        print("The response of WalletsMPCWalletsApi->list_mpc_vaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->list_mpc_vaults: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_type** | [**MPCVaultType**](.md)| The vault type. Possible values include: - &#x60;Org-Controlled&#x60;: This vault is a collection of [Organization-Controlled Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#organization-controlled-wallets).  - &#x60;User-Controlled&#x60;: This vault is a collection of [User-Controlled Wallets](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#user-controlled-wallets).  | 
 **project_id** | **str**| The project ID, which you can retrieve by calling [List all projects](/v2/api-references/wallets--mpc-wallets/list-all-projects).  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListMpcVaults200Response**](ListMpcVaults200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed all vaults. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tss_requests**
> ListTssRequests200Response list_tss_requests(vault_id, key_share_holder_group_id, limit=limit, before=before, after=after)

List TSS requests

This operation retrieves a list of TSS requests and their details. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_tss_requests200_response import ListTssRequests200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    key_share_holder_group_id = 'a3a45e99-5a12-444f-867a-ffe0ebb1bb30'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List TSS requests
        api_response = api_instance.list_tss_requests(vault_id, key_share_holder_group_id, limit=limit, before=before, after=after)
        print("The response of WalletsMPCWalletsApi->list_tss_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->list_tss_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **key_share_holder_group_id** | **str**| The key share holder group ID of the TSS request, which you can retrieve by calling [List all key share holder groups](/v2/api-references/wallets--mpc-wallets/list-all-key-share-holder-groups). | 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| An object ID that serves as a starting point for retrieving data in reverse chronological order. For example, if you specify &#x60;before&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;, the request will retrieve a list of data objects that end before the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1&#x60;. You can set this parameter to the value of &#x60;pagination.before&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  - If you set &#x60;before&#x60; to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| An object ID that acts as a starting point for retrieving data in chronological order. For example, if you specify &#x60;after&#x60; as &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;, the request will retrieve a list of data objects that start after the object with the object ID &#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;. You can set this parameter to the value of &#x60;pagination.after&#x60; in the response of the previous request.  - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur.  - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListTssRequests200Response**](ListTssRequests200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved TSS request. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_share_holder_group_by_id**
> KeyShareHolderGroup update_key_share_holder_group_by_id(vault_id, key_share_holder_group_id, update_key_share_holder_group_by_id_request=update_key_share_holder_group_by_id_request)

Update key share holder group

This operation updates a specified active [Signing Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups). For example, you can use this operation to upgrade a Signing Group to the [Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.key_share_holder_group import KeyShareHolderGroup
from cobo_waas2.models.update_key_share_holder_group_by_id_request import UpdateKeyShareHolderGroupByIdRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    key_share_holder_group_id = 'e8257ac8-76b8-4d1e-a1f9-eec4cb931dce'
    update_key_share_holder_group_by_id_request = cobo_waas2.UpdateKeyShareHolderGroupByIdRequest()

    try:
        # Update key share holder group
        api_response = api_instance.update_key_share_holder_group_by_id(vault_id, key_share_holder_group_id, update_key_share_holder_group_by_id_request=update_key_share_holder_group_by_id_request)
        print("The response of WalletsMPCWalletsApi->update_key_share_holder_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->update_key_share_holder_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **key_share_holder_group_id** | **str**| The key share holder group ID. | 
 **update_key_share_holder_group_by_id_request** | [**UpdateKeyShareHolderGroupByIdRequest**](UpdateKeyShareHolderGroupByIdRequest.md)|  | [optional] 

### Return type

[**KeyShareHolderGroup**](KeyShareHolderGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully modify mpc tss group |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpc_project_by_id**
> MPCProject update_mpc_project_by_id(project_id, update_mpc_project_by_id_request=update_mpc_project_by_id_request)

Update project name

This operation updates a project's name.  <Note>This operation applies to MPC Wallets (User-Controlled Wallets) only.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.mpc_project import MPCProject
from cobo_waas2.models.update_mpc_project_by_id_request import UpdateMpcProjectByIdRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    project_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_mpc_project_by_id_request = cobo_waas2.UpdateMpcProjectByIdRequest()

    try:
        # Update project name
        api_response = api_instance.update_mpc_project_by_id(project_id, update_mpc_project_by_id_request=update_mpc_project_by_id_request)
        print("The response of WalletsMPCWalletsApi->update_mpc_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->update_mpc_project_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project ID, which you can retrieve by calling [List all projects](/v2/api-references/wallets--mpc-wallets/list-all-projects). | 
 **update_mpc_project_by_id_request** | [**UpdateMpcProjectByIdRequest**](UpdateMpcProjectByIdRequest.md)| The request body to update a project&#39;s name. | [optional] 

### Return type

[**MPCProject**](MPCProject.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully listed all vaults. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpc_vault_by_id**
> MPCVault update_mpc_vault_by_id(vault_id, update_mpc_vault_by_id_request=update_mpc_vault_by_id_request)

Update vault name

This operation updates a vault's name. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.mpc_vault import MPCVault
from cobo_waas2.models.update_mpc_vault_by_id_request import UpdateMpcVaultByIdRequest
from cobo_waas2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dev.cobo.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cobo_waas2.Configuration(
    api_private_key="<YOUR_PRIVATE_KEY>",
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.WalletsMPCWalletsApi(api_client)
    vault_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_mpc_vault_by_id_request = cobo_waas2.UpdateMpcVaultByIdRequest()

    try:
        # Update vault name
        api_response = api_instance.update_mpc_vault_by_id(vault_id, update_mpc_vault_by_id_request=update_mpc_vault_by_id_request)
        print("The response of WalletsMPCWalletsApi->update_mpc_vault_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsMPCWalletsApi->update_mpc_vault_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id** | **str**| The vault ID, which you can retrieve by calling [List all vaults](/v2/api-references/wallets--mpc-wallet/list-all-mpc-vaults). | 
 **update_mpc_vault_by_id_request** | [**UpdateMpcVaultByIdRequest**](UpdateMpcVaultByIdRequest.md)| The request body to update a vault&#39;s name. | [optional] 

### Return type

[**MPCVault**](MPCVault.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully modify mpc vault |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

