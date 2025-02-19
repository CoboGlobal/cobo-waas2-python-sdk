# cobo_waas2.StakingsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_claim_activity**](StakingsApi.md#create_claim_activity) | **POST** /stakings/activities/claim | Create claim activity
[**create_stake_activity**](StakingsApi.md#create_stake_activity) | **POST** /stakings/activities/stake | Create stake activity
[**create_unstake_activity**](StakingsApi.md#create_unstake_activity) | **POST** /stakings/activities/unstake | Create unstake activity
[**create_withdraw_activity**](StakingsApi.md#create_withdraw_activity) | **POST** /stakings/activities/withdraw | Create withdraw activity
[**get_staking_activity_by_id**](StakingsApi.md#get_staking_activity_by_id) | **GET** /stakings/activities/{activity_id} | Get staking activity details
[**get_staking_by_id**](StakingsApi.md#get_staking_by_id) | **GET** /stakings/{staking_id} | Get staking position details
[**get_staking_estimation_fee**](StakingsApi.md#get_staking_estimation_fee) | **POST** /stakings/estimate_fee | Estimate staking fees
[**get_staking_estimation_fee_v2**](StakingsApi.md#get_staking_estimation_fee_v2) | **POST** /stakings/estimate_fee_v2 | Estimate staking fees v2
[**get_staking_pool_by_id**](StakingsApi.md#get_staking_pool_by_id) | **GET** /stakings/pools/{pool_id} | Get staking pool details
[**list_staking_activities**](StakingsApi.md#list_staking_activities) | **GET** /stakings/activities | List staking activities
[**list_staking_pools**](StakingsApi.md#list_staking_pools) | **GET** /stakings/pools | List staking pools
[**list_stakings**](StakingsApi.md#list_stakings) | **GET** /stakings | List staking positions


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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |
**404** | Requested resources not found. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |
**404** | Requested resources not found. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |
**404** | Requested resources not found. |  -  |

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
 **staking_id** | **str**| The position ID. | [optional] 
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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

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
**400** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**401** | Unauthorized. Please provide valid credentials. |  -  |
**403** | Forbidden. You do not have the permission to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

