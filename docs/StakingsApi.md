# cobo_waas2.StakingsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_babylon_airdrop_registration**](StakingsApi.md#create_babylon_airdrop_registration) | **POST** /stakings/protocols/babylon/airdrops/registrations | Register for Babylon airdrop
[**create_babylon_staking_registration**](StakingsApi.md#create_babylon_staking_registration) | **POST** /stakings/protocols/babylon/stakings/registrations | Register for Babylon Phase-2
[**create_claim_activity**](StakingsApi.md#create_claim_activity) | **POST** /stakings/activities/claim | Create claim activity
[**create_stake_activity**](StakingsApi.md#create_stake_activity) | **POST** /stakings/activities/stake | Create stake activity
[**create_unstake_activity**](StakingsApi.md#create_unstake_activity) | **POST** /stakings/activities/unstake | Create unstake activity
[**create_withdraw_activity**](StakingsApi.md#create_withdraw_activity) | **POST** /stakings/activities/withdraw | Create withdraw activity
[**get_babylon_airdrop_registration_by_id**](StakingsApi.md#get_babylon_airdrop_registration_by_id) | **GET** /stakings/protocols/babylon/airdrops/registrations/{registration_id} | Get Babylon airdrop registration details
[**get_babylon_staking_registration_by_id**](StakingsApi.md#get_babylon_staking_registration_by_id) | **GET** /stakings/protocols/babylon/stakings/registrations/{registration_id} | Get Babylon Phase-2 registration details
[**get_staking_activity_by_id**](StakingsApi.md#get_staking_activity_by_id) | **GET** /stakings/activities/{activity_id} | Get staking activity details
[**get_staking_by_id**](StakingsApi.md#get_staking_by_id) | **GET** /stakings/{staking_id} | Get staking position details
[**get_staking_estimation_fee**](StakingsApi.md#get_staking_estimation_fee) | **POST** /stakings/estimate_fee | Estimate staking fees
[**get_staking_estimation_fee_v2**](StakingsApi.md#get_staking_estimation_fee_v2) | **POST** /stakings/estimate_fee_v2 | Estimate staking fees v2
[**get_staking_pool_by_id**](StakingsApi.md#get_staking_pool_by_id) | **GET** /stakings/pools/{pool_id} | Get staking pool details
[**list_babylon_airdrop_registrations**](StakingsApi.md#list_babylon_airdrop_registrations) | **GET** /stakings/protocols/babylon/airdrops/registrations | List Babylon airdrop registrations
[**list_babylon_eligible_airdrops**](StakingsApi.md#list_babylon_eligible_airdrops) | **GET** /stakings/protocols/babylon/airdrops/eligibles | List wallets eligible for Babylon airdrop
[**list_babylon_eligible_stakings**](StakingsApi.md#list_babylon_eligible_stakings) | **GET** /stakings/protocols/babylon/stakings/eligibles | List staking positions eligible for Babylon Phase-2
[**list_babylon_staking_registrations**](StakingsApi.md#list_babylon_staking_registrations) | **GET** /stakings/protocols/babylon/stakings/registrations | List Babylon Phase-2 registrations
[**list_staking_activities**](StakingsApi.md#list_staking_activities) | **GET** /stakings/activities | List staking activities
[**list_staking_pools**](StakingsApi.md#list_staking_pools) | **GET** /stakings/pools | List staking pools
[**list_stakings**](StakingsApi.md#list_stakings) | **GET** /stakings | List staking positions


# **create_babylon_airdrop_registration**
> CreateBabylonAirdropRegistration201Response create_babylon_airdrop_registration(create_babylon_airdrop_registration_request=create_babylon_airdrop_registration_request)

Register for Babylon airdrop

This operation initiates a Babylon airdrop registration request.   Before calling this operation, please ensure the following: - The Bitcoin (BTC) address is eligible for the Babylon airdrop and has not been registered. You can call the [List wallets eligible for Babylon airdrop](https://www.cobo.com/developers/v2/api-references/stakings/list-wallets-eligible-for-babylon-airdrop) operation to check the registration status. - The Babylon address has enough asset to pay for the registration fee. - The Babylon address must be a Babylon address in an MPC Wallet in your organization.  The system first checks whether the provided address is eligible for the Babylon airdrop. If eligible, it creates a unique registration ID, which can be used to track the status.   The registration is processed asynchronously and may take some time to complete. It is recommended that you regularly call the [Get Babylon airdrop registration details](https://www.cobo.com/developers/v2/api-references/stakings/get-babylon-airdrop-registration-details) operation to check the status and handle registration accordingly.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_babylon_airdrop_registration201_response import CreateBabylonAirdropRegistration201Response
from cobo_waas2.models.create_babylon_airdrop_registration_request import CreateBabylonAirdropRegistrationRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_babylon_airdrop_registration_request = cobo_waas2.CreateBabylonAirdropRegistrationRequest()

    try:
        # Register for Babylon airdrop
        api_response = api_instance.create_babylon_airdrop_registration(create_babylon_airdrop_registration_request=create_babylon_airdrop_registration_request)
        print("The response of StakingsApi->create_babylon_airdrop_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_babylon_airdrop_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_babylon_airdrop_registration_request** | [**CreateBabylonAirdropRegistrationRequest**](CreateBabylonAirdropRegistrationRequest.md)| The request body to register for the Babylon airdrop. | [optional] 

### Return type

[**CreateBabylonAirdropRegistration201Response**](CreateBabylonAirdropRegistration201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Airdrop registration created successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_babylon_staking_registration**
> CreateBabylonStakingRegistration201Response create_babylon_staking_registration(create_babylon_staking_registration_request=create_babylon_staking_registration_request)

Register for Babylon Phase-2

This operation initiates a Babylon Phase-2 registration request.   Before calling this operation, please ensure the following: - The staking position is eligible for the Babylon Phase-2 and has not been registered. You can call the [List staking positions eligible for Babylon Phase-2](https://www.cobo.com/developers/v2/api-references/stakings/list-eligible-staking-positions-for-babylon-phase-2) operation to check the registration status. - The Babylon address has enough asset to pay for the registration fee. - The Babylon address must be a Babylon address in an MPC Wallet in your organization.  The system first checks whether the provided address is eligible for Phase-2. If eligible, it creates a unique registration ID, which can be used to track the status.   The registration is processed asynchronously and may take some time to complete. It is recommended that you regularly call the [Get Babylon Phase-2 registration details](https://www.cobo.com/developers/v2/api-references/stakings/get-babylon-phase-2-registration-details) operation to check the status and handle registration accordingly.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_babylon_staking_registration201_response import CreateBabylonStakingRegistration201Response
from cobo_waas2.models.create_babylon_staking_registration_request import CreateBabylonStakingRegistrationRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_babylon_staking_registration_request = cobo_waas2.CreateBabylonStakingRegistrationRequest()

    try:
        # Register for Babylon Phase-2
        api_response = api_instance.create_babylon_staking_registration(create_babylon_staking_registration_request=create_babylon_staking_registration_request)
        print("The response of StakingsApi->create_babylon_staking_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_babylon_staking_registration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_babylon_staking_registration_request** | [**CreateBabylonStakingRegistrationRequest**](CreateBabylonStakingRegistrationRequest.md)| The request body to transit Babylon BTC staking to phase 2 | [optional] 

### Return type

[**CreateBabylonStakingRegistration201Response**](CreateBabylonStakingRegistration201Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Register Babylon BTC staking for phase 2 successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_claim_activity**
> CreateStakeActivity201Response create_claim_activity(create_claim_activity_request=create_claim_activity_request)

Create claim activity

This operation creates a claim request.  <Note>Currently, only the Ethereum Beacon protocol supports this operation.</Note>  For some protocols, you can use the `fee` property in the request body to specify the maximum fee you are willing to pay. The transaction will fail if the actual fee exceeds the specified maximum fee.  

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.create_claim_activity_request import CreateClaimActivityRequest
from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_claim_activity_request = cobo_waas2.CreateClaimActivityRequest()

    try:
        # Create claim activity
        api_response = api_instance.create_claim_activity(create_claim_activity_request=create_claim_activity_request)
        print("The response of StakingsApi->create_claim_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_claim_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_claim_activity_request** | [**CreateClaimActivityRequest**](CreateClaimActivityRequest.md)| The request body to create a staking request. | [optional] 

### Return type

[**CreateStakeActivity201Response**](CreateStakeActivity201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a staking activity. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stake_activity**
> CreateStakeActivity201Response create_stake_activity(create_stake_activity_request=create_stake_activity_request)

Create stake activity

This operation creates a staking request.  For some protocols, you can use the `fee` property in the request body to specify the maximum fee you are willing to pay. The transaction will fail if the actual fee exceeds the specified maximum fee.   <Note>For the Babylon protocol, you can only select UTXO as the fee model.</Note> 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response
from cobo_waas2.models.create_stake_activity_request import CreateStakeActivityRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_stake_activity_request = cobo_waas2.CreateStakeActivityRequest()

    try:
        # Create stake activity
        api_response = api_instance.create_stake_activity(create_stake_activity_request=create_stake_activity_request)
        print("The response of StakingsApi->create_stake_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_stake_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stake_activity_request** | [**CreateStakeActivityRequest**](CreateStakeActivityRequest.md)| The request body to create a staking request. | [optional] 

### Return type

[**CreateStakeActivity201Response**](CreateStakeActivity201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a staking activity. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_unstake_activity**
> CreateStakeActivity201Response create_unstake_activity(create_unstake_activity_request=create_unstake_activity_request)

Create unstake activity

This operation creates an unstaking request. Your staked tokens will be automatically unlocked once the specified locking period ends. If you want to withdraw your tokens beforehand, you can unstake them with this operation.  For some protocols, you can use the `fee` property in the request body to specify the maximum fee you are willing to pay. The transaction will fail if the actual fee exceeds the specified maximum fee.   <Note>For the Babylon protocol, you can only select UTXO as the fee model.</Note> 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response
from cobo_waas2.models.create_unstake_activity_request import CreateUnstakeActivityRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_unstake_activity_request = cobo_waas2.CreateUnstakeActivityRequest()

    try:
        # Create unstake activity
        api_response = api_instance.create_unstake_activity(create_unstake_activity_request=create_unstake_activity_request)
        print("The response of StakingsApi->create_unstake_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_unstake_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_unstake_activity_request** | [**CreateUnstakeActivityRequest**](CreateUnstakeActivityRequest.md)| The request body to create a unstaking request. | [optional] 

### Return type

[**CreateStakeActivity201Response**](CreateStakeActivity201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a staking activity. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_withdraw_activity**
> CreateStakeActivity201Response create_withdraw_activity(create_withdraw_activity_request=create_withdraw_activity_request)

Create withdraw activity

This operation creates a withdrawal request.   For some protocols, you can use the `fee` property in the request body to specify the maximum fee you are willing to pay. The transaction will fail if the actual fee exceeds the specified maximum fee.   <Note>For the Babylon protocol, you can only select UTXO as the fee model.</Note> 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.create_stake_activity201_response import CreateStakeActivity201Response
from cobo_waas2.models.create_withdraw_activity_request import CreateWithdrawActivityRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    create_withdraw_activity_request = cobo_waas2.CreateWithdrawActivityRequest()

    try:
        # Create withdraw activity
        api_response = api_instance.create_withdraw_activity(create_withdraw_activity_request=create_withdraw_activity_request)
        print("The response of StakingsApi->create_withdraw_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->create_withdraw_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_withdraw_activity_request** | [**CreateWithdrawActivityRequest**](CreateWithdrawActivityRequest.md)| The request body to create a withdraw activity. | [optional] 

### Return type

[**CreateStakeActivity201Response**](CreateStakeActivity201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a staking activity. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_babylon_airdrop_registration_by_id**
> BabylonAirdropRegistration get_babylon_airdrop_registration_by_id(registration_id)

Get Babylon airdrop registration details

This operation returns the details of a specific Babylon airdrop registration, including registration status, Bitcoin (BTC) and Babylon addresses, airdrop amount, and error messages (if any).  Please note that registration is an asynchronous process and may take several minutes to complete. It is recommended to call this operation at regular intervals to track the status.  If the registration request fails, please check the error message and resolve the issues before resubmitting the registration request.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.babylon_airdrop_registration import BabylonAirdropRegistration
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    registration_id = 'registration_id_example'

    try:
        # Get Babylon airdrop registration details
        api_response = api_instance.get_babylon_airdrop_registration_by_id(registration_id)
        print("The response of StakingsApi->get_babylon_airdrop_registration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_babylon_airdrop_registration_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The Babylon airdrop or Babylon Phase-2 registration ID. You can use the [Register for Babylon airdrop](https://www.cobo.com/developers/v2/api-references/stakings/register-for-babylon-airdrop) or the [Register for Babylon Phase-2](https://www.cobo.com/developers/v2/api-references/stakings/register-for-babylon-phase-2) operation to get this information. | 

### Return type

[**BabylonAirdropRegistration**](BabylonAirdropRegistration.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get airdrop registration details successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_babylon_staking_registration_by_id**
> BabylonStakingRegistration get_babylon_staking_registration_by_id(registration_id)

Get Babylon Phase-2 registration details

This operation returns the details of a specific Babylon Phase-2 registration, including registration status, Bitcoin (BTC) and Babylon addresses, staked amount, and error messages (if any).  Please note that registration is an asynchronous process and may take several minutes to complete. It is recommended to call this operation at regular intervals to track the status.  If the registration request fails, please check the error message and resolve the issues before resubmitting the registration request.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.babylon_staking_registration import BabylonStakingRegistration
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    registration_id = 'registration_id_example'

    try:
        # Get Babylon Phase-2 registration details
        api_response = api_instance.get_babylon_staking_registration_by_id(registration_id)
        print("The response of StakingsApi->get_babylon_staking_registration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_babylon_staking_registration_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The Babylon airdrop or Babylon Phase-2 registration ID. You can use the [Register for Babylon airdrop](https://www.cobo.com/developers/v2/api-references/stakings/register-for-babylon-airdrop) or the [Register for Babylon Phase-2](https://www.cobo.com/developers/v2/api-references/stakings/register-for-babylon-phase-2) operation to get this information. | 

### Return type

[**BabylonStakingRegistration**](BabylonStakingRegistration.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get babylon staking registration details successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_activity_by_id**
> Activity get_staking_activity_by_id(activity_id)

Get staking activity details

This operation retrieves the details of a specified staking activity. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.activity import Activity
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    activity_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get staking activity details
        api_response = api_instance.get_staking_activity_by_id(activity_id)
        print("The response of StakingsApi->get_staking_activity_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_staking_activity_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **str**| The activity ID. | 

### Return type

[**Activity**](Activity.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **get_staking_by_id**
> Stakings get_staking_by_id(staking_id)

Get staking position details

This operation retrieves the detailed information about a specified staking position. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.stakings import Stakings
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    staking_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get staking position details
        api_response = api_instance.get_staking_by_id(staking_id)
        print("The response of StakingsApi->get_staking_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_staking_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staking_id** | **str**| The ID of the staking position. You can retrieve a list of staking positions by calling [List staking positions](https://www.cobo.com/developers/v2/api-references/stakings/list-staking-positions). | 

### Return type

[**Stakings**](Stakings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A staking position has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staking_estimation_fee**
> GetStakingEstimationFee201Response get_staking_estimation_fee(get_staking_estimation_fee_request=get_staking_estimation_fee_request)

Estimate staking fees

<Note>This operation is deprecated. Please use the [updated version](https://www.cobo.com/developers/v2/api-references/stakings/estimate-staking-fees-v2) instead.</Note>  This operation calculates the fee required for a staking activity based on factors such as network congestion and transaction complexity.  For some protocols, you can use the `fee.fee_rate` property in the request body to specify the fee rate you are willing to pay.  The `fee.max_fee_amount` property in the request body will be ignored.  <Note>For the Babylon protocol, you can only select UTXO as the fee model.</Note> 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.get_staking_estimation_fee201_response import GetStakingEstimationFee201Response
from cobo_waas2.models.get_staking_estimation_fee_request import GetStakingEstimationFeeRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    get_staking_estimation_fee_request = cobo_waas2.GetStakingEstimationFeeRequest()

    try:
        # Estimate staking fees
        api_response = api_instance.get_staking_estimation_fee(get_staking_estimation_fee_request=get_staking_estimation_fee_request)
        print("The response of StakingsApi->get_staking_estimation_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_staking_estimation_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_staking_estimation_fee_request** | [**GetStakingEstimationFeeRequest**](GetStakingEstimationFeeRequest.md)| The request body to get the estimated fee of a staking activity. | [optional] 

### Return type

[**GetStakingEstimationFee201Response**](GetStakingEstimationFee201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **get_staking_estimation_fee_v2**
> EthStakeEstimatedFee get_staking_estimation_fee_v2(get_staking_estimation_fee_request=get_staking_estimation_fee_request)

Estimate staking fees v2

This operation calculates the fee required for a staking activity based on factors such as network congestion and transaction complexity.  <Note>For the Babylon protocol, you can only select UTXO as the fee model.</Note> 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.eth_stake_estimated_fee import EthStakeEstimatedFee
from cobo_waas2.models.get_staking_estimation_fee_request import GetStakingEstimationFeeRequest
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    get_staking_estimation_fee_request = cobo_waas2.GetStakingEstimationFeeRequest()

    try:
        # Estimate staking fees v2
        api_response = api_instance.get_staking_estimation_fee_v2(get_staking_estimation_fee_request=get_staking_estimation_fee_request)
        print("The response of StakingsApi->get_staking_estimation_fee_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_staking_estimation_fee_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_staking_estimation_fee_request** | [**GetStakingEstimationFeeRequest**](GetStakingEstimationFeeRequest.md)| The request body to get the estimated fee of a staking activity. | [optional] 

### Return type

[**EthStakeEstimatedFee**](EthStakeEstimatedFee.md)

### Authorization

[OAuth2](../README.md#OAuth2)

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

# **get_staking_pool_by_id**
> PoolDetails get_staking_pool_by_id(pool_id)

Get staking pool details

This operation retrieves the detailed information about a specified staking pool. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.pool_details import PoolDetails
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    pool_id = 'babylon_btc'

    try:
        # Get staking pool details
        api_response = api_instance.get_staking_pool_by_id(pool_id)
        print("The response of StakingsApi->get_staking_pool_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->get_staking_pool_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| The ID of the staking pool. A staking pool is a pairing of a staking protocol and a specific type of token. You can call [List staking pools](https://www.cobo.com/developers/v2/api-references/stakings/list-staking-pools) to retrieve a list of staking pools. | 

### Return type

[**PoolDetails**](PoolDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A staking pool has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_babylon_airdrop_registrations**
> ListBabylonAirdropRegistrations200Response list_babylon_airdrop_registrations(status=status, btc_address=btc_address, limit=limit, before=before, after=after)

List Babylon airdrop registrations

This operation lists all Babylon airdrop registration records within your organization. You can filter the results by request status and Bitcoin (BTC) address.  The registration is processed asynchronously and may take some time to complete. It is recommended to implement automatic monitoring and handle the registration on time.  If the registration request fails, please check the error message and resolve the issues before resubmitting the registration request.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_babylon_airdrop_registrations200_response import ListBabylonAirdropRegistrations200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    status = 'Processing'
    btc_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Babylon airdrop registrations
        api_response = api_instance.list_babylon_airdrop_registrations(status=status, btc_address=btc_address, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_babylon_airdrop_registrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_babylon_airdrop_registrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The registration request status. | [optional] 
 **btc_address** | **str**| The Bitcoin (BTC) address used for staking. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListBabylonAirdropRegistrations200Response**](ListBabylonAirdropRegistrations200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of babylon airdrop registrations retrieved successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_babylon_eligible_airdrops**
> ListBabylonEligibleAirdrops200Response list_babylon_eligible_airdrops(status=status, limit=limit, before=before, after=after)

List wallets eligible for Babylon airdrop

This operation lists all wallets that are eligible for the Babylon airdrop. If an eligible wallet's status is `Unregistered`, you can initiate an airdrop registration for it. You can filter the results by airdrop registration status.  You can use this operation to: - Check which wallets are eligible for airdrop registrations - Estimate airdrop amounts before claiming - Monitor available airdrop  As registration is an asynchronous process and might take some time to complete, it is recommended that you regularly call this operation to check wallet eligibility and register eligible wallets on time.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_babylon_eligible_airdrops200_response import ListBabylonEligibleAirdrops200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    status = 'Registered'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List wallets eligible for Babylon airdrop
        api_response = api_instance.list_babylon_eligible_airdrops(status=status, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_babylon_eligible_airdrops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_babylon_eligible_airdrops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The status of Babylon airdrop or Phase-2 registration. Possible values are: - &#x60;Registered&#x60;: Registered for Babylon airdrop or Phase-2. - &#x60;Unregistered&#x60;: Not registered for any Babylon airdrop or Phase-2. - &#x60;Registering&#x60;: The Babylon airdrop or Phase-2 registration is in progress but not yet completed.  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListBabylonEligibleAirdrops200Response**](ListBabylonEligibleAirdrops200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of wallets eligible for Babylon airdrop registration |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_babylon_eligible_stakings**
> ListBabylonEligibleStakings200Response list_babylon_eligible_stakings(status=status, limit=limit, before=before, after=after)

List staking positions eligible for Babylon Phase-2

This operation lists all staking positions that are eligible for Babylon Phase-2. If an eligible staking position's status is `Unregistered`, you can initiate a registration for it. You can filter the results by registration status.  You can use this operation to: - Check which staking positions can be registered - Get staking details before initiating registration - Monitor available positions for registration  As registration is an asynchronous process and might take some time to complete, it is recommended that you regularly call this operation to check staking position eligibility and register eligible positions on time.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_babylon_eligible_stakings200_response import ListBabylonEligibleStakings200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    status = 'Registered'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List staking positions eligible for Babylon Phase-2
        api_response = api_instance.list_babylon_eligible_stakings(status=status, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_babylon_eligible_stakings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_babylon_eligible_stakings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The status of Babylon airdrop or Phase-2 registration. Possible values are: - &#x60;Registered&#x60;: Registered for Babylon airdrop or Phase-2. - &#x60;Unregistered&#x60;: Not registered for any Babylon airdrop or Phase-2. - &#x60;Registering&#x60;: The Babylon airdrop or Phase-2 registration is in progress but not yet completed.  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListBabylonEligibleStakings200Response**](ListBabylonEligibleStakings200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of stakings eligible for Babylon Phase-2 registration |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_babylon_staking_registrations**
> ListBabylonStakingRegistrations200Response list_babylon_staking_registrations(status=status, staking_id=staking_id, limit=limit, before=before, after=after)

List Babylon Phase-2 registrations

This operation lists all Babylon Phase-2 registration records within your organization. You can filter the results by request status and staking position ID.  The registration is processed asynchronously and may take some time to complete. It is recommended to implement automatic monitoring and handle the registration on time.  If the registration request fails, please check the error message and resolve the issues before resubmitting the registration request.  For more information, refer to [Babylon's official doc](https://github.com/babylonlabs-io/babylon/tree/main/docs). 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_babylon_staking_registrations200_response import ListBabylonStakingRegistrations200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    status = 'Processing'
    staking_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Babylon Phase-2 registrations
        api_response = api_instance.list_babylon_staking_registrations(status=status, staking_id=staking_id, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_babylon_staking_registrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_babylon_staking_registrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The registration request status. | [optional] 
 **staking_id** | **str**| The ID of the Phase-1 BTC staking position. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListBabylonStakingRegistrations200Response**](ListBabylonStakingRegistrations200Response.md)

### Authorization

[CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of babylon staking registrations retrieved successfully |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_staking_activities**
> ListStakingActivities200Response list_staking_activities(pool_id=pool_id, staking_id=staking_id, activity_type=activity_type, activity_status=activity_status, min_modified_timestamp=min_modified_timestamp, max_modified_timestamp=max_modified_timestamp, initiator=initiator, request_id=request_id, limit=limit, before=before, after=after)

List staking activities

This operation retrieves a list of staking activities. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.activity_status import ActivityStatus
from cobo_waas2.models.activity_type import ActivityType
from cobo_waas2.models.list_staking_activities200_response import ListStakingActivities200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    pool_id = 'babylon_btc'
    staking_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    activity_type = cobo_waas2.ActivityType()
    activity_status = cobo_waas2.ActivityStatus()
    min_modified_timestamp = 1635744000000
    max_modified_timestamp = 1635744000000
    initiator = 'steve@example.com'
    request_id = 'web_send_by_user_327_1610444045047'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List staking activities
        api_response = api_instance.list_staking_activities(pool_id=pool_id, staking_id=staking_id, activity_type=activity_type, activity_status=activity_status, min_modified_timestamp=min_modified_timestamp, max_modified_timestamp=max_modified_timestamp, initiator=initiator, request_id=request_id, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_staking_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_staking_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| The ID of the staking pool. A staking pool is a pairing of a staking protocol and a specific type of token. You can call [List staking pools](https://www.cobo.com/developers/v2/api-references/stakings/list-staking-pools) to retrieve a list of staking pools. | [optional] 
 **staking_id** | **str**| The ID of the Phase-1 BTC staking position. | [optional] 
 **activity_type** | [**ActivityType**](.md)|  | [optional] 
 **activity_status** | [**ActivityStatus**](.md)|  | [optional] 
 **min_modified_timestamp** | **int**| The start time of the query. All staking activities updated after the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **max_modified_timestamp** | **int**| The end time of the query. All staking activities updated before the specified time will be retrieved. The time is in Unix timestamp format, measured in milliseconds. | [optional] 
 **initiator** | **str**| The activity initiator, which is your API key by default. You can also specify the initiator when creating the activity. | [optional] 
 **request_id** | **str**| The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListStakingActivities200Response**](ListStakingActivities200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of staking activities have been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_staking_pools**
> ListStakingPools200Response list_staking_pools(chain_id=chain_id, token_id=token_id, limit=limit, before=before, after=after)

List staking pools

This operation retrieves a list of staking pools currently supported. 

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.list_staking_pools200_response import ListStakingPools200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    chain_id = 'ETH'
    token_id = 'ETH_USDT'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List staking pools
        api_response = api_instance.list_staking_pools(chain_id=chain_id, token_id=token_id, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_staking_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_staking_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListStakingPools200Response**](ListStakingPools200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of staking pools has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stakings**
> ListStakings200Response list_stakings(pool_id=pool_id, statuses=statuses, wallet_id=wallet_id, token_id=token_id, limit=limit, before=before, after=after)

List staking positions

This operation retrieves a list of staking positions.  

### Example

* OAuth Authentication (OAuth2):

```python
import cobo_waas2
from cobo_waas2.models.list_stakings200_response import ListStakings200Response
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
    api_instance = cobo_waas2.StakingsApi(api_client)
    pool_id = 'babylon_btc'
    statuses = 'Active,StakeInProgress,'
    wallet_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    token_id = 'ETH_USDT'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List staking positions
        api_response = api_instance.list_stakings(pool_id=pool_id, statuses=statuses, wallet_id=wallet_id, token_id=token_id, limit=limit, before=before, after=after)
        print("The response of StakingsApi->list_stakings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingsApi->list_stakings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| The ID of the staking pool. A staking pool is a pairing of a staking protocol and a specific type of token. You can call [List staking pools](https://www.cobo.com/developers/v2/api-references/stakings/list-staking-pools) to retrieve a list of staking pools. | [optional] 
 **statuses** | **str**| The statuses of the staking amounts, separated by comma. Possible values include:  - &#x60;StakeInProgress&#x60;: The staking request is submitted and is waiting to be confirmed by the staking protocol. - &#x60;Active&#x60;: The amount has been staked. - &#x60;Rejected&#x60;: The staking request has been rejected because the signer refuses to sign the transaction. - &#x60;LimitExceeded&#x60;: The total staking cap of the staking protocol has been reached. - &#x60;Invalid&#x60;: The staking request is invalid. This is often due to the failure to broadcast the transaction. - &#x60;UnstakeInProgress&#x60;: The unstaking request is submitted and is waiting to be confirmed by the staking protocol. - &#x60;Withdrawable&#x60;: The tokens have been unstaked and are ready to be withdrawn. - &#x60;WithdrawInProgress&#x60;: The withdrawal request is submitted and is waiting to be confirmed on the chain network. - &#x60;Closed&#x60;: The staking position is closed.  | [optional] 
 **wallet_id** | **str**| The wallet ID. | [optional] 
 **token_id** | **str**| The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListStakings200Response**](ListStakings200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of staking positions has been successfully retrieved. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

