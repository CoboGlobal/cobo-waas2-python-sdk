# cobo_waas2.InternalFeeEngineApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_commission_fee**](InternalFeeEngineApi.md#get_commission_fee) | **GET** /internal/commission_fee | Get commission fee


# **get_commission_fee**
> List[CommissionFeeDetail] get_commission_fee(request_id, business_type_id=business_type_id, amount=amount, chain_id=chain_id, token_id=token_id, wallet_id=wallet_id, wallet_type=wallet_type, request_type=request_type, strategy_context=strategy_context)

Get commission fee

This operation retrieves commission fee. 

### Example

* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.commission_fee_detail import CommissionFeeDetail
from cobo_waas2.models.transaction_request_type_params import TransactionRequestTypeParams
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
    api_instance = cobo_waas2.InternalFeeEngineApi(api_client)
    request_id = 'request_id_example'
    business_type_id = 56
    amount = 56
    chain_id = 'chain_id_example'
    token_id = 'token_id_example'
    wallet_id = 'wallet_id_example'
    wallet_type = 56
    request_type = cobo_waas2.TransactionRequestTypeParams()
    strategy_context = None

    try:
        # Get commission fee
        api_response = api_instance.get_commission_fee(request_id, business_type_id=business_type_id, amount=amount, chain_id=chain_id, token_id=token_id, wallet_id=wallet_id, wallet_type=wallet_type, request_type=request_type, strategy_context=strategy_context)
        print("The response of InternalFeeEngineApi->get_commission_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalFeeEngineApi->get_commission_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Unique request identifier | 
 **business_type_id** | **int**|  | [optional] 
 **amount** | **int**| Transaction amount in smallest unit | [optional] 
 **chain_id** | **str**| Blockchain chain ID | [optional] 
 **token_id** | **str**| Token ID | [optional] 
 **wallet_id** | **str**| Wallet ID | [optional] 
 **wallet_type** | **int**| Wallet type | [optional] 
 **request_type** | [**TransactionRequestTypeParams**](.md)|  | [optional] 
 **strategy_context** | [**Dict[str, object]**](object.md)| Strategy context parameters.  | [optional] 

### Return type

[**List[CommissionFeeDetail]**](CommissionFeeDetail.md)

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

