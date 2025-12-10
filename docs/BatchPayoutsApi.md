# cobo_waas2.BatchPayoutsApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_batch_payout**](BatchPayoutsApi.md#cancel_batch_payout) | **POST** /batch_payouts/payouts/{payout_id}/cancel | Cancel batch payout
[**create_batch_payout**](BatchPayoutsApi.md#create_batch_payout) | **POST** /batch_payouts/payouts | Create batch payout
[**drop_batch_payout**](BatchPayoutsApi.md#drop_batch_payout) | **POST** /batch_payouts/payouts/{payout_id}/drop | Drop batch payout
[**estimate_batch_payout_fee**](BatchPayoutsApi.md#estimate_batch_payout_fee) | **POST** /batch_payouts/estimate_fee | Estimate batch payout fee
[**get_batch_payout**](BatchPayoutsApi.md#get_batch_payout) | **GET** /batch_payouts/payouts/{payout_id} | Get batch payout
[**list_batch_payouts**](BatchPayoutsApi.md#list_batch_payouts) | **GET** /batch_payouts/payouts | List batch payouts
[**revoke_batch_payout**](BatchPayoutsApi.md#revoke_batch_payout) | **POST** /batch_payouts/payouts/{payout_id}/revoke | Revoke batch payout
[**speed_up_batch_payout**](BatchPayoutsApi.md#speed_up_batch_payout) | **POST** /batch_payouts/payouts/{payout_id}/speedup | Speed up batch payout


# **cancel_batch_payout**
> PayoutDetail cancel_batch_payout(payout_id, cancel_payout_body=cancel_payout_body)

Cancel batch payout

This operation cancels a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.cancel_payout_body import CancelPayoutBody
from cobo_waas2.models.payout_detail import PayoutDetail
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    payout_id = 'e3986401-4aec-480a-973d-e775a4518413'
    cancel_payout_body = cobo_waas2.CancelPayoutBody()

    try:
        # Cancel batch payout
        api_response = api_instance.cancel_batch_payout(payout_id, cancel_payout_body=cancel_payout_body)
        print("The response of BatchPayoutsApi->cancel_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->cancel_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The payout ID. | 
 **cancel_payout_body** | [**CancelPayoutBody**](CancelPayoutBody.md)| The request body to cancel a batch payout. | [optional] 

### Return type

[**PayoutDetail**](PayoutDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **create_batch_payout**
> CreateBatchPayout201Response create_batch_payout(create_batch_payout_request=create_batch_payout_request)

Create batch payout

This operation creates a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_batch_payout201_response import CreateBatchPayout201Response
from cobo_waas2.models.create_batch_payout_request import CreateBatchPayoutRequest
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    create_batch_payout_request = cobo_waas2.CreateBatchPayoutRequest()

    try:
        # Create batch payout
        api_response = api_instance.create_batch_payout(create_batch_payout_request=create_batch_payout_request)
        print("The response of BatchPayoutsApi->create_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->create_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_batch_payout_request** | [**CreateBatchPayoutRequest**](CreateBatchPayoutRequest.md)| The request body to create a batch payout. | [optional] 

### Return type

[**CreateBatchPayout201Response**](CreateBatchPayout201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Infos of a newly initiated payout. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_batch_payout**
> PayoutDetail drop_batch_payout(payout_id, payout_rbf_body=payout_rbf_body)

Drop batch payout

This operation drops a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.payout_detail import PayoutDetail
from cobo_waas2.models.payout_rbf_body import PayoutRbfBody
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    payout_id = 'e3986401-4aec-480a-973d-e775a4518413'
    payout_rbf_body = cobo_waas2.PayoutRbfBody()

    try:
        # Drop batch payout
        api_response = api_instance.drop_batch_payout(payout_id, payout_rbf_body=payout_rbf_body)
        print("The response of BatchPayoutsApi->drop_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->drop_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The payout ID. | 
 **payout_rbf_body** | [**PayoutRbfBody**](PayoutRbfBody.md)| The request body to speed up or drop a batch payout. | [optional] 

### Return type

[**PayoutDetail**](PayoutDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **estimate_batch_payout_fee**
> List[PayoutEstimatedFee] estimate_batch_payout_fee(estimate_batch_payout_fee_request=estimate_batch_payout_fee_request)

Estimate batch payout fee

This operation estimates the fee of a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.estimate_batch_payout_fee_request import EstimateBatchPayoutFeeRequest
from cobo_waas2.models.payout_estimated_fee import PayoutEstimatedFee
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    estimate_batch_payout_fee_request = cobo_waas2.EstimateBatchPayoutFeeRequest()

    try:
        # Estimate batch payout fee
        api_response = api_instance.estimate_batch_payout_fee(estimate_batch_payout_fee_request=estimate_batch_payout_fee_request)
        print("The response of BatchPayoutsApi->estimate_batch_payout_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->estimate_batch_payout_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_batch_payout_fee_request** | [**EstimateBatchPayoutFeeRequest**](EstimateBatchPayoutFeeRequest.md)| The request body to estimate the fee of a batch payout. | [optional] 

### Return type

[**List[PayoutEstimatedFee]**](PayoutEstimatedFee.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **get_batch_payout**
> PayoutDetail get_batch_payout(payout_id)

Get batch payout

This operation retrieves details of a specific batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.payout_detail import PayoutDetail
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    payout_id = 'e3986401-4aec-480a-973d-e775a4518413'

    try:
        # Get batch payout
        api_response = api_instance.get_batch_payout(payout_id)
        print("The response of BatchPayoutsApi->get_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->get_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The payout ID. | 

### Return type

[**PayoutDetail**](PayoutDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **list_batch_payouts**
> ListBatchPayouts200Response list_batch_payouts(limit=limit, before=before, after=after)

List batch payouts

This operation retrieves the information of all batch payouts. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_batch_payouts200_response import ListBatchPayouts200Response
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List batch payouts
        api_response = api_instance.list_batch_payouts(limit=limit, before=before, after=after)
        print("The response of BatchPayoutsApi->list_batch_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->list_batch_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListBatchPayouts200Response**](ListBatchPayouts200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **revoke_batch_payout**
> PayoutDetail revoke_batch_payout(payout_id)

Revoke batch payout

This operation revokes a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.payout_detail import PayoutDetail
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    payout_id = 'e3986401-4aec-480a-973d-e775a4518413'

    try:
        # Revoke batch payout
        api_response = api_instance.revoke_batch_payout(payout_id)
        print("The response of BatchPayoutsApi->revoke_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->revoke_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The payout ID. | 

### Return type

[**PayoutDetail**](PayoutDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

# **speed_up_batch_payout**
> PayoutDetail speed_up_batch_payout(payout_id, payout_rbf_body=payout_rbf_body)

Speed up batch payout

This operation speeds up a batch payout. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.payout_detail import PayoutDetail
from cobo_waas2.models.payout_rbf_body import PayoutRbfBody
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
    api_instance = cobo_waas2.BatchPayoutsApi(api_client)
    payout_id = 'e3986401-4aec-480a-973d-e775a4518413'
    payout_rbf_body = cobo_waas2.PayoutRbfBody()

    try:
        # Speed up batch payout
        api_response = api_instance.speed_up_batch_payout(payout_id, payout_rbf_body=payout_rbf_body)
        print("The response of BatchPayoutsApi->speed_up_batch_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchPayoutsApi->speed_up_batch_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The payout ID. | 
 **payout_rbf_body** | [**PayoutRbfBody**](PayoutRbfBody.md)| The request body to speed up or drop a batch payout. | [optional] 

### Return type

[**PayoutDetail**](PayoutDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

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

